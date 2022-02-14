//retrieve node in DOM via ID
//var c =

//instantiate a CanvasRenderingContext2D object
let ctx = c.getContext("2d");

//init global state var
let mode = "rect";

//var toggleMode = function(e) {
let toggleMode = (e) => {
    console.log("toggle...");
    if(mode=="rect") {
        mode="circ";
    } else {
        mode="rect";
    }
}

let drawRect = (e) => {
    var mouseX = e.clientX-e.offsetX;
    var mouseY = e.clientY-e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    beginPath();
    fillstyle="red";
    fillrect(mouseX,mouseY,50,75);
    console.log(e);
}

//var drawCircle = function(e) {
let drawCircle = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
}

//var draw = function(e) {
let draw = (e) => {
    if(mode=="rect"){
        drawRect(e);
    } else {
        drawCircle(e);
    }
}

//var wipeCanvas = function() {
var wipeCanvas = () => {

}

c.addEventListener("click", draw);
// var bToggler = document. ;
// bToggler. ;
// let clearB = ;
// clearB. ;