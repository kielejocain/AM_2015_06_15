MY_STORE.application.views.product_list = function () {
    function draw(product_list, container) {
        container.innerHTML = "";

        for (var i = 0; i < product_list.length; i++) {
            var item = product_list[i];
            var element = document.createElement("div");
            element.setAttribute("data-id", item.id);

            var name = document.createElement("h1");
            name.classList.add("name");
            name.innerHTML = item.name;
            element.appendChild(name);

            container.appendChild(element);
        }
    }

    return {
        draw: draw
    }
}();
