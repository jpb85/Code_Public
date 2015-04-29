; extra credit
;

(define (range L)
(let ((start car(L)) (step (car(cdr(L)))) (end (car(cdr(cdr(L))))) )
if(start>step)
	'()
else cond(start) range(start+step step end)
