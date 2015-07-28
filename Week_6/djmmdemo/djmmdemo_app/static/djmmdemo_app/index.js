//Requires: request.js
(function () {
    var self = this;
    self.views = {};
    self.models = {};


    function handleData(data) {
        self.models = data;
        updateViews();
    }

    function updateViews() {
        for (var index in self.views) {
            var view = self.views[index];
            view.draw();
        }
    }

    function init() {
        var r = new Request("/api/v1/all/get/", handleData);
        r.send();
        views.lists = new lists();
        views.songs = new songs();
        views.all = new all();
    }

    document.addEventListener("DOMContentLoaded", init);


    function lists() {
        var element = document.getElementById("lists");
        element.addEventListener("change", function (e) {
            self.views.songs.draw(e.target.value);
            console.log(e.target.value);
        });
        function draw() {
            objectListIntoSelectOptions(
                self.views.lists.element,
                self.models.lists,
                "name"
            );
        }

        return {
            element: element,
            draw: draw
        }
    }


    function songs() {
        var element = document.getElementById("songs");
        element.addEventListener("click", function (e) {
            console.log(e.target.value);
        });
        function draw(list_id) {
            if(list_id != undefined){
                objectListIntoTemplateItems(element,  self.models.lists[list_id].songs);
            }
        }
        return {
            element: element,
            draw: draw
        }
    }
    function all() {
        var element = document.getElementById("all");
        element.addEventListener("click", function (e) {
            console.log(e.target.value);
        });
        function draw() {
            objectListIntoTemplateItems(element,  self.models.all);
        }
        return {
            element: element,
            draw: draw
        }
    }

}());