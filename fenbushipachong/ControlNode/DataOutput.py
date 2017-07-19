# -*- coding: utf-8 -*-

import codecs
import time

class DataOutput(object):
    
    def __init__(self):
        self.filepath = r'C:\Users\zhang\Desktop\python\Learn\spiders\fenbushipachong\baike_%s.html' \
                        %(time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime()) )
        self.output_head(self.filepath)
        self.datas = []

    def store_data(self, data):

        if data is None:
            return
        self.datas.append(data)
        if len(self.datas) > 0:
            self.output_html(self.filepath)

    def output_head(self, path):
        '''
        写入html头
        '''
        fout = codecs.open(path, 'w', encoding='utf-8')
        fout.write("<html>")
        fout.write("<head>")
        #根据窗口大小自动调整列宽，自动换行
        fout.write("<style>table { \
                    table-layout:fixed; word-break: break-all; \
                    word-wrap: break-word; } \
                    </style>")
        fout.write("</head>")
        fout.write("<body>")
        fout.write("<table>")
        fout.close()

    def output_html(self, path):
        '''
        将数据写入HTML中
        '''
        fout=codecs.open(path,'a',encoding='utf-8')
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>"%data['url'])
            fout.write("<td>%s</td>"%data['title'])
            fout.write("<td>%s</td>"%data['summary'])
            fout.write("</tr>")
            self.datas.remove(data)
        fout.close()
    
    def output_end(self, path):
        '''
        数据写入后，写入HTML关闭标签
        '''
        fout=codecs.open(path,'a',encoding='utf-8')
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")
        fout.close()
