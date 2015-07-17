turtle.drawArrow = function () {
    turtle.forward(50);
    turtle.left(150);
    turtle.forward(7);
    turtle.backward(7);
    turtle.right(150);
    turtle.right(150);
    turtle.forward(7);
    turtle.backward(7);
    turtle.left(150);
};


turtle.hexagon = function (length) {
    var i;
    for (i = 1; i <= 6; i++) {
        turtle.forward(length);
        turtle.left(60);

    }
};


turtle.drawStar = function () {
    var i;
    for (i = 0; i < 18; i++) {
        turtle.left(100);
        turtle.forward(80);
    }
};

turtle.square = function (length) {
    var i;
    for (i = 1; i <= 4; i++) {
        turtle.forward(length);
        turtle.left(90);

    }
};



