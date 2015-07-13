//This is based on code found <a
//        href="http://cnx.org/contents/85310cba-5bbc-4f1d-b437-778a1aef9d02@2/Turtle_graphics_with_the_HTML5"> here. </a>

"use strict";


var turtle = {
    x: 0,
    y: 0,
    angleInRadians: 0,
    penDown: true,
    strokeStyle: "black",
    lineWidth: 3
};

document.addEventListener("DOMContentLoaded", function () {
    //<canvas id="canvas" width="800" height="600"></canvas>

    var canvas = document.createElement('canvas');
    canvas.setAttribute("width", window.innerWidth);
    canvas.setAttribute("height", window.innerHeight);

    turtle.x = window.innerWidth / 2;
    turtle.y = window.innerHeight / 2;

    turtle.penDown = true;

    turtle.strokeStyle = "black";
    turtle.lineWidth = 3;
    turtle.left(180);

    document.body.appendChild(canvas)
    if (canvas && canvas.getContext) { // does the browser support 'canvas'?
        turtle.ct = canvas.getContext("2d"); // get drawing context
    } else {
        alert('You need a browser which supports the HTML5 canvas!');
    }
});


turtle.logPenStatus = function () {
    console.log('x=' + this.x + "; y=" + this.y + '; angle = ' + this.angle() + '; penDown = ' + this.penDown);
};


turtle.forward = function (length) {
    var lastX = this.x,
        lastY = this.y;
    this.x += length * Math.sin(this.angleInRadians);
    this.y += length * Math.cos(this.angleInRadians);
    if (this.ct) {
        if (this.penDown) {
            this.logPenStatus();
            this.ct.beginPath();
            this.ct.lineWidth = this.lineWidth;
            this.ct.strokeStyle = this.strokeStyle;
            this.ct.moveTo(lastX, lastY);
            this.ct.lineTo(this.x, this.y);
            this.ct.stroke();
        }
    } else {
        this.ct.moveTo(this.x, this.y);
    }
    return this;
};

turtle.backward = function (length) {
    this.forward(-length);
    return this;
};

turtle.left = function (angleInDegrees) {
    this.angleInRadians += angleInDegrees * Math.PI / 180.0;
    return this;
};

turtle.right = function (angleInDegrees) {
    this.left(-angleInDegrees);
    return this;
};


turtle.angle = function () {
    return this.angleInRadians * 180.0 / Math.PI;
};

turtle.drawTurtle = function () {
    turtle.left(150);
    turtle.forward(12);
    turtle.backward(12);
    turtle.right(150);
    turtle.right(150);
    turtle.forward(12);
    turtle.backward(12);
    turtle.left(150);
};

turtle.repeat = function (fn, count, angle) {
    var i;
    for (i = 1; i <= count; i++) {
        console.log(i);
        fn();
        turtle.left(angle);
    }
};