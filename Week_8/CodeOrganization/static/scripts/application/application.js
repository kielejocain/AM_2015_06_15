var MY_STORE = {};
MY_STORE.application = function () {
    var self = this;

    function drawProducts() {
        console.log(MY_STORE.application.models.products);
        MY_STORE.application.views.product_list.draw(
            MY_STORE.application.models.products,
            MY_STORE.application.options.product_list
        )
    }

    function loadData(url, callBackFunctionName, modelName) {
        var xhr = new XMLHttpRequest();
        xhr.open("get", url);
        xhr.onload = function (e) {
            var data = JSON.parse(e.target.responseText);
            MY_STORE.application.models[modelName] = data;
            callBackFunctionName();
        };
        xhr.send();

    }

    function init(options) {
        this.options = options;
        this.loadData("api/products.js", drawProducts, "products");
    }

    return {
        views: [],
        models: [],
        loadData: loadData,
        init: init,
        options: this.options
    }
}();

