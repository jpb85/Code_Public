fun maxmin [] = raise Fail "maxmin: empty list"
 | maxmin [x] = (x,x) (* a pair *)
 | maxmin (x::xs) = 
     let val (max,min) = maxmin xs in
         if x < min then (max,x)
         else if x > max then (x,min)
         else (max,min)
     end;