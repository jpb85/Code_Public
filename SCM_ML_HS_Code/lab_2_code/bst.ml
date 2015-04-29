datatype btree =
  Empty |
  Node of int * btree * btree;


   fun bstInsert (x, Empty) = Node(x, Empty, Empty)
   |   bstInsert (x, Node(y, left, right) ) =
          if x<y then Node(y, bstInsert(x,left), right)
          else Node(y, left, bstInsert(x, right) );


   fun inBst (x, Empty) = false
   |   inBst (x, Node(y, left, right) ) =
          if x=y then true
          else if x<y then inBst(x, left)
          else inBst(x, right);






































exception Empty_btree;


      fun root (Empty ) = raise Empty_btree
      |   root (Node(x, right,left)) = x;


      fun left(Empty) = raise Empty_btree
      |   left(Node(x, left, right)) = left;


      fun right(Empty) = raise Empty_btree
      |   right(Node(x,left,right)) = right;



   fun first(t:btree) =
       if left(t)=Empty then root(t)
		else first(left(t));
