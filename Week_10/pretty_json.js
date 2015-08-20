function prettyJson(inputObject) {
    var json = JSON.stringify(inputObject);

    var output = "";
    var indent = 0;
    for (var i = 0; i < json.length; i++) {
        var c = json[i];
        var prev = json[i - 1];
        var next = json[i + 1];
        var spacesPerTab = 5;
        var prefix = "";

        if (c == '}') {
            indent--;
        }

        if (
            '}'.indexOf(c) != -1 ||
            (
                '"'.indexOf(c) != -1 &&
                ':'.indexOf(prev) == -1 &&
                ':,}'.indexOf(next) == -1
            )
        ) {
            prefix = "<br>";
            for (var t = 0; t < (indent * spacesPerTab); t++) {
                prefix += "&nbsp;";
            }
        }

        if (c == '{') {
            indent++;
        }

        output += prefix + c;
    }
    return output;
}