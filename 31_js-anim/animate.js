// Doorstuck - Eric Guo and Andy Lin
// Softdev pd2
// K31 -- canvas based JS animation
// 2022-02-15t

// model for HTML5 canvas-based animation

// SKEELTON


//access canvas and buttons via DOM
let c = document.getElementById("playground");// GET CANVAS
let dotButton = document.getElementById("buttonCircle"); // GET DOT BUTTON
let stopButton = document.getElementById("buttonStop");// GET STOP BUTTON

//prepare to interact with canvas in 2D
let ctx = c.getContext("2d");

//set fill color to team color
ctx.fillStyle = "light blue";

let requestID;  //init global let for use with animation frames


//let clear = function(e) {
let clear = (e) => {
  console.log("clear invoked...");
  ctx.clearRect(0, 0, c.offsetWidth, c.offsetHeight);;
};

let radius = 0;
let growing = true;

//let drawDot = function() {
let drawDot = () => {
  console.log("drawDot invoked...")

  clear(c);
  window.cancelAnimationFrame(requestID);
  if (growing) {
    radius += 1;
  } else {
    radius -= 1;
  }
  ctx.beginPath();
  ctx.arc(c.offsetHeight / 2, c.offsetWidth / 2, radius, 0, 360);
  ctx.fillStyle = "orange"
  ctx.fill();
  console.log(requestID);
  requestID = window.requestAnimationFrame(drawDot);
  if (radius >= c.offsetHeight / 2) {
    growing = false
  } else if (radius <= 0){
    growing = true
  }

  /*
    ...to
    Wipe the canvas,
    Repaint the circle,

    ...and somewhere (where/when is the right time?)
    Update requestID to propagate the animation.
    You will need
    window.cancelAnimationFrame()
    window.requestAnimationFrame()

   */
};


//let stopIt = function() {
let stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );
  window.cancelAnimationFrame(requestID);
};


dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );