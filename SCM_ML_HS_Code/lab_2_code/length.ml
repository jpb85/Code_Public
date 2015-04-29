fun len1 [] sofar = sofar
 | len1 (x::xs) sofar = len1 xs (sofar+1);

fun len lis = len1 lis 0;