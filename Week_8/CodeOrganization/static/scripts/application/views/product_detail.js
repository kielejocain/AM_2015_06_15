MY_STORE.application.views.product_detail = function () {
    function draw(item, container) {
        container.innerHTML = "";
        var element = document.createElement("div");
        element.setAttribute("data-id", item.id);

        var name = document.createElement("h1");
        name.classList.add("name");
        name.innerHTML = product.name;
        element.appendChild(name);

        var description = document.createElement("div");
        description.classList.add("description");
        description.innerHTML = product.description;
        element.appendChild(description);

        container.appendChild(element);

    }
};
