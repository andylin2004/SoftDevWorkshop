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
let dvdButton = document.getElementById("buttonDvd");// GET DVD BUTTON

var dvdLogo = new Image();
dvdLogo.src = "logo_dvd.jpg";

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
var changeX = 1;
var changeY = 1;
var posX = Math.random() * c.offsetWidth;
var posY = Math.random() * c.offsetHeight;

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

var drawDVD = () => {
  console.log("nooooooo")

  if (requestID) {
    cancelAnimationFrame(requestID);
  }

  if (posX <= 1 || posX >= 500-75) {
    changeX *= -1;
  }
  if (posY <= 1 || posY >= 500-50) {
    changeY *= -1;
  }

  posX += changeX;
  posY += changeY;

  clear(ctx);
  ctx.drawImage(dvdLogo, posX, posY, 75, 50);

  requestID = requestAnimationFrame(drawDVD)

}

//let stopIt = function() {
let stopIt = () => {
  console.log("stopIt invoked...")
  console.log( requestID );
  window.cancelAnimationFrame(requestID);
};


dotButton.addEventListener( "click", drawDot );
stopButton.addEventListener( "click",  stopIt );
dvdButton.addEventListener( "click",  drawDVD );