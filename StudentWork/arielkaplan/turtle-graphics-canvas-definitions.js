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

turtle.triangle = function (length) {
    for (var i = 1; i <= 3; i++) {
        turtle.forward(length);
        turtle.left(120);
    }
};

turtle.circle = function (diameter) {
    var radius = (diameter / 2);
    var draw = 0;

    // to fill in the gaps
    if (diameter < 200) {
        draw = 1;
    } else if (diameter < 500) {
        draw = 2;
    } else {
        draw = 3;
    }

    for (var i = 1; i <= 360; i++) {
        turtle.penDown = false;
        turtle.forward(radius);
        turtle.penDown = true;
        turtle.left(90);
        turtle.forward(draw);
        turtle.backward(draw * 2);
        turtle.forward(draw);
        turtle.right(90);
        turtle.penDown = false;
        turtle.backward(radius);
        turtle.left(1);
        turtle.penDown = true;
    }
};

turtle.multiple = function (shape_function, size, how_many) {
    for (var i = 0; i < how_many; i++) {
        shape_function(size);
        turtle.forward(size);
    }
};

turtle.seed = function (diameter) {
    radius = (diameter / 2);
    //turtle.circle(diameter);
    for (var i = 0; i < 6; i++) {
        turtle.circle(diameter);
        turtle.penDown = false;
        turtle.forward(radius);
        turtle.left(60);
        turtle.penDown = true;
    }
};

turtle.flower = function (diameter) {
    for (var i = 0; i < 6; i++) {
        turtle.seed(diameter);
        turtle.penDown = false;
        turtle.right(60);
        turtle.penDown = true;
    }
};