function objectListIntoSelectOptions(select, objectList, displayField, valueField) {
    select.innerHTML="";
    for (var index in objectList) {
        var item = objectList[index];
        var option = document.createElement("option");
        option.value = item[valueField];
        option.innerHTML = item[displayField];
        select.appendChild(option);
    }
}


function objectListIntoTemplateItems(parentElement, objectList) {
    //Assumes a child element with the class template exists
    // and class names match key/property names
    var template_list = parentElement.getElementsByClassName("template");
    if(template_list.length < 1){
        console.log("no template defined in parent element");
        return;
    }
    var template = template_list[0];
    parentElement.innerHTML="";
    parentElement.appendChild(template);

    for (var index in objectList) {
        var item = objectList[index];
        var element = template.cloneNode(true);
        for (var key in item) {
            var value = item[key];
            var subElementList = element.getElementsByClassName(key);
            for (se in subElementList) {
                var subElement = subElementList[se];
                if (value != undefined && subElement != undefined) {
                    subElement.innerHTML = value;
                    subElement.value = value;
                }
            }
        }
        element.classList.remove("template");
        parentElement.appendChild(element);
    }
}