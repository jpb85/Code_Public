

(define (range start step end)
  (if (> start end)
      '()
      (cons start
            (range (+ start step) step end))))