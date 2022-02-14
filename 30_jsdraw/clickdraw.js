//retrieve node in DOM via ID
var c = document.getElementById("slate")

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
    bToggler.innerText = mode;
}

let drawRect = (e) => {
    var mouseX = e.offsetX;
    var mouseY = e.offsetY;
    console.log("mouseclick registered at ", mouseX, mouseY);
    ctx.fillStyle="red";
    ctx.fillRect(mouseX,mouseY,50,75);
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
    ctx.clearRect(0, 0, c.offsetWidth, c.offsetHeight);
}

c.addEventListener("click", draw);
var bToggler = document.getElementById("buttonToggle") ;
bToggler.addEventListener("click", toggleMode) ;
let clearB = document.getElementById("buttonClear")
clearB.addEventListener("click", wipeCanvas)
bToggler.innerText = mode;