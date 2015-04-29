; tail

(define (factorial n)
  (fold-right * 1 (iota n 1)))
(define (two-to-the n)
  (fold-right * 1 (make-list n 2)))