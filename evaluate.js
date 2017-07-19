var url = 'http://www.cnblogs.com/qiyeboy/';
var page = require('webpage').create();
page.open(url, function(status) {
    var title = page.evaluate(function() {
        return document.title;
    });
    console.log(title);
    phantom.exit();
});