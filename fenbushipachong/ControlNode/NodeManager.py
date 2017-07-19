# -*- coding: utf-8 -*-

from multiprocessing import Queue, Process
from multiprocessing.managers import BaseManager
import time
from DataOutput import DataOutput
from UrlManager import UrlManager

class NodeManager(object):

    def start_Manager(self, url_q, result_q):
        '''
        创建一个分布式管理器
        url_q: url队列
        resuilt_q: 结果队列
        '''
        #注册两个队列,在网络中暴露
        BaseManager.register('get_task_queue', callable=lambda: url_q)
        BaseManager.register('get_result_queue', callable=lambda:result_q)
        #绑定端口8001， 设置验证口令‘baike’。
        authkey = 'abc'.encode('utf-8')
        manager = BaseManager(address=('', 8001), authkey=authkey)
        return manager

    def url_manager_proc(self, url_q, conn_q, root_url):
        url_manager = UrlManager()
        url_manager.add_new_url(root_url)
        while True:
            while(url_manager.has_new_url()):
                new_url = url_manager.get_new_url()
                #将获取的new_url发给工作节点
                url_q.put(new_url)
                print('old_url = ' + str(url_manager.old_url_size()))
                if(url_manager.old_url_size() > 2000):
                    url_q.put('end')
                    url_manager.save_progress('new_urls.txt', url_manager.new_urls)
                    url_manager.save_progress('old_urls.txt', url_manager.old_urls)
                    return
            try:
                if not conn_q.empty():
                    urls = conn_q.get()
                    url_manager.add_new_url(urls)
            except BaseException:
                time.sleep(0.1)
    
    def result_solve_proc(self, result_q, conn_q, store_q):
        while True:
            try:
                if not result_q.empty():
                    content = result_q.get(True)
                    if content['new_urls'] == 'end':
                        store_q.put('end')
                        return
                    conn_q.put(content['new_urls'])
                    store_q.put(content['data'])
                else:
                    time.sleep(0.1)
            except BaseException:
                time.sleep(0.1)

    def store_proc(self, store_q):
        output = DataOutput()
        while True:
            if not store_q.empty():
                data = store_q.get()
                if data=='end':
                    print('存储进程接受通知然后结束!')
                    output.output_end(output.filepath)
                    return
                output.store_data(data)
            else:
                time.sleep(0.1)
                

if __name__ == '__main__':
    #初始化4个队列
    url_q = Queue()
    result_q = Queue()
    store_q = Queue()
    conn_q = Queue()
    #创建分布式管理器
    node = NodeManager()
    manager = node.start_Manager(url_q, result_q)
    #创建URL管理进程、数据提取和数据存储进程
    url_manager_proc = Process(target=node.url_manager_proc, args=(url_q, conn_q,
                                'http://baike.baidu.com/view/284853.htm',))
    result_solve_proc = Process(target=node.result_solve_proc, args=(result_q,conn_q,store_q,))
    store_proc = Process(target=node.store_proc, args=(store_q,))
    #启动3个进程和分布式管理器
    url_manager_proc.start()
    result_solve_proc.start()
    store_proc.start()
    manager.get_server().serve_forever()