;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname fibfac) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))

;; Team Doorstuck :: Eric Guo, Andy Lin
;; SoftDev pd2
;; K27 -- Basic functions in JavaScript
;; 2022-02-04
(define fib (lambda (n)
              (if (= n 0)
                  0
                  (if (<= n 2)
                      1
                      (+ (fib(- n 1)) (fib(- n 2)))
                      )
                  )
              )
  )

(define factorial(lambda (x)
                  (if(= x 0)
                     1
                     (* (factorial(- x 1)) x)
                     )
                  )
  )

(fib 0)
(fib 1)
(fib 2)
(fib 3)
(fib 4)
(fib 5)
(fib 6)
(fib 7)
(fib 8)
(fib 9)
(fib 10)
"------------------------------------------------"
(factorial 0)
(factorial 1)
(factorial 2)
(factorial 3)
(factorial 4)
(factorial 5)
(factorial 6)
(factorial 7)
(factorial 8)
(factorial 9)
(factorial 10)