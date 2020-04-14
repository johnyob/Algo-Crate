type 'a t
exception Empty

val empty : 'a t
val is_empty : 'a t -> bool 

val push : 'a t -> 'a -> 'a t
val pop  : 'a t -> 'a t

val peek : 'a t -> 'a
val peek_opt : 'a t -> 'a option