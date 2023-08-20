; 4.1
(define (factorial x) 
    (cond ((= x 1) x)
            (else (* x (factorial (- x 1))))
    )
)

; 4.2
(define (fib n)
        (cond ((= n 0) 0)
            ((= n 1) 1)
            (else (+ (fib (- n 1)) (fib (- n 2))))
        )
)

scm> (fib 0)
0
scm> (fib 1)
1
scm> (fib 10)
55

; 5.1
(define (my-append a b)
    (cond ((null? (cdr a)) (cons (car a) b))
        (else (cons (car a) (my-append (cdr a) b)))
    )
)
scm> (my-append '(1 2 3) '(2 3 4))
(1 2 3 2 3 4)

;5.2
(define s '(5 4 (1 2) 3 7))
(car (cdr (cdr (cdr s)))) ;3

;5.3
(define (duplicate lst)
    (define a (car lst))
    (cond ((null? (cdr lst)) (cons (car lst) (cons (car lst) '())))
        (else (cons (car lst) (cons (car lst) (duplicate (cdr lst)))))
    )
)

;5.4
(define (insert element lst index)
    (cond ((= index 0) (cons element lst))
        (else (cons (car lst) (insert element (cdr lst) (- index 1))))
    )
)