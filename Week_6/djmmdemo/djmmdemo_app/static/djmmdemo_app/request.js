var Request = function (url, callback) {
    var self = this;
    self.url = url;
    self.callback = callback;

    self.handleResponse = function (event) {
        if (4 == event.target.readyState) {
            self.callback.call(self.callback, JSON.parse(event.target.responseText))
        }
    };

    self.xhr = new XMLHttpRequest();
    self.xhr.open("GET", url);
    self.xhr.onreadystatechange = self.handleResponse;
    var send=function(){
        self.xhr.send();
    };
    return {
        send: send
    }
};