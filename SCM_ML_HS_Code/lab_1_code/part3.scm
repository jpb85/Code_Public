; extra credit

(define (range L)
(let (
	(start (car L)) 
	(step (car (cdr L)))
 	(end (car (cdr (cdr L)))) 
	)
(if 
	(> start end)
	'()
	(cons start (range (list (+ start step) step end)))
)
)
)

(define (seq f L)
	(map f (range L))
) 
