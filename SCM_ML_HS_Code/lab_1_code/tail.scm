; tail

(define (factorial n)
  (fold * 1 (iota n 1)))
(define (two-to-the n)
  (fold * 1 (make-list n 2)))