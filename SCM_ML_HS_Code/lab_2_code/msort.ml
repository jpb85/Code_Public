open List;

fun merge [] ys = ys
 |  merge xs [] = xs
 |  merge (x::xs) (y::ys) =
      if x <= y then x :: merge xs (y::ys)
      else  y :: merge (x::xs) ys;

fun msort [] = []
 |  msort [x] = [x]
 |  msort lis =
       let val n = (length lis) div 2;
           val fsthalf = take(lis,n);
           val sndhalf = drop(lis,n);
           val lis1 = msort fsthalf;
           val lis2 = msort sndhalf;
       in
         merge lis1 lis2
       end;