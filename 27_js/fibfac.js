// Team Doorstuck :: Eric Guo, Andy Lin
// SoftDev pd2
// K27 -- Basic functions in JavaScript
// 2022-02-04
// --------------------------------------------------


// as a duo...
// pair programming style,
// implement a fact and fib fxn


let fib = (n) => {
    if(n == 0) {
        return 0;
    } else if(n <= 2) {
        return 1;
    } else {
        return fib(n - 1) + fib(n - 2);
    }
}

let factorial = (n) => {
    if (n == 0) {
        return 1;
    } else {
        return factorial(n - 1) * n;
    }
}

let gcd = (a, b) => {
    gcdNum;
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
    }
}

let y = factorial(5);
console.log(y);
console.log(gcdNum(20,40))
