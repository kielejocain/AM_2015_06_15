//Requires: request.js
(function () {
    var self = this;
    self.views = {};
    self.models = {};


    function handleData(data) {
        self.models = data;
        updateViews();

    }

    function buttonClick(e) {
        console.log("button_click");
        console.log(e)
    }

    function addEventListeners() {
        var button_list = document.getElementsByTagName("button");
        for (var i = 0; i < button_list.length; i++) {
            button_list[i].addEventListener("click", buttonClick)
        }
    }

    function updateViews() {
        for (var index in self.views) {
            var view = self.views[index];
            view.draw();
        }
        addEventListeners();
    }

    function init() {
        var r = new Request("/api/v1/all/get/", handleData);
        r.send();
        views.Lists = new Lists();
        views.Songs = new Songs();
        views.All = new All();
    }

    document.addEventListener("DOMContentLoaded", init);

    function Lists() {

        var element = document.getElementById("lists");

        element.addEventListener("change", function (e) {
            self.views.Songs.draw(e.target.value);
            addEventListeners();
            console.log(e.target.value);
        });

        function draw() {
            objectListIntoSelectOptions(self.views.Lists.element, self.models.lists, "name", "id");
        }

        return {
            element: element,
            draw: draw
        }
    }


    function Songs() {

        var element = document.getElementById("songs");

        function draw(list_id) {
            if (list_id != undefined) {
                objectListIntoTemplateItems(element, self.models.lists[list_id].songs);
            }
        }

        return {
            element: element,
            draw: draw
        }
    }

    function All() {
        var element = document.getElementById("all");

        function draw() {
            objectListIntoTemplateItems(element, self.models.all);
            var selects = element.getElementsByClassName("list-to-add");
            for (var s = 0; s < selects.length; s++) {
                var select = selects[s];
                objectListIntoSelectOptions(select, self.models.lists, "name", "id");
            }
            var buttons = element.getElementsByClassName("list-to-add");
            for (var b = 0; b < buttons.length; b++) {
                var button = buttons[b];
                button.addEventListener("click", function (e) {
                    console.log(e.target.parentElement)
                });
            }
        }

        return {
            element: element,
            draw: draw
        }
    }
}());