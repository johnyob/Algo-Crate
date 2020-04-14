type 'a t

val empty : 'a t
val is_empty : 'a t -> bool

val traverse : ('b -> ('c -> 'c) -> ('c -> 'c) -> 'c -> 'c) -> ('a -> 'b) -> 'c -> 'a t -> 'c