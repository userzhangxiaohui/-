var url = 'http://www.cnblogs.com/qiyeboy/';
var page = require('webpage').create();
page.onResourceRequested = function(request) {
    console.log('request ' + JSON.stringify(request, undefined, 4));
};
page.onResourceReceived = function(response) {
    console.log('receive ' + JSON.stringify(response, undefined,4));
};
page.open(url);
phantom.exit();