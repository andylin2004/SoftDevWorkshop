/*
   your PPTASK:
   
   Test drive each bit of code in this file,
    and insert comments galore, indicating anything
     you discover,
    	have questions about,
    		or otherwise deem notable.
    		
    		Write with your future self or teammates in mind.
    		
    		If you find yourself falling out of flow mode, consult 
    		other teams
    		MDN

   A few comments have been pre-filled for you...
   
   (delete this block comment once you are done)
*/

// Team Doorstuck :: Eric Guo, Andy Lin
// SoftDev pd2
// K28 -- Getting more comfortable with the dev console and the DOM
// 2022-02-08
// --------------------------------------------------


//send diagnostic output to console
//(Ctrl-Shift-K in Firefox to reveal console)
console.log("AYO");

let i = "hello";
let j = 20;


//assign an anonymous fxn to a let
let f = function(x) {
  let j=30;
  return j+x;
};


//instantiate an object
let o = { 'name' : 'Thluffy',
          age : 15,
          items : [10, 20, 30, 40],
          morestuff : {a : 1, b : 'ayo'},
          func : function(x) {
            return x+30;
          }
};

//seems like document is already ready to be used at the start, as a global let
let addItem = function(text) {
  let list = document.getElementById("thelist");
  let newitem = document.createElement("li");
  newitem.innerHTML = text;
  list.appendChild(newitem); // ooh oop but the objects are html elements! smells like beautifulsoup but better
};


let removeItem = function(n) {
  let listitems = document.getElementsByTagName('li');
  listitems[n].remove(); // more oop things, this time removing things
};

let red = function() {
  let items = document.getElementsByTagName("li");
  for(let i = 0; i < items.length; i++) {
    items[i].classList.add('red'); // makes html elements not red yet red
  }
};

let stripe = function() {
  let items = document.getElementsByTagName("li");
  for(let i = 0; i < items.length; i++) {
    if (i%2==0){
      items[i].classList.add('red');
    } else {
      items[i].classList.add('blue'); //same as before, but alts between red and blue unless color already assigned
    }
  }
};

let fib = (n) => {
  let left = 0, right = 1;
  if (n == 0) {
    return left;
  }
  for (let i = 1; i < n; i++){
    let newRight = left + right;
    left = right;
    right = newRight;
  }
  return right
}

let factorial = (n) => {
  let total = 1;
  while (n > 1) {
    total *= n;
    n--;
  }
  return total;
}

let gcd = (a, b) => {
  let gcdNum;
  if (a > b) {
      for (i = 2; i <= b; i++){
          if (a % i == 0 && b % i == 0) {
              gcdNum = i
          }
      }
      return gcdNum
  } else if (a == b) {
      return a;
  } else {
      for (i = 2; i <= a; i++){
          if (a % i == 0 && b % i == 0) {
              gcdNum = i
          }
      }
      return gcdNum;
  }
}

addItem(gcd(40, 60).toString())
addItem(factorial(69).toString())
addItem(fib(69).toString())