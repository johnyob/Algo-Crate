module type RED_BLACK_TREE = sig
  type 'a t
  type color

  val empty : 'a t
  val is_empty : 'a t -> bool
  
  val traverse : ('b -> ('c -> 'c) -> ('c -> 'c) -> 'c -> 'c) -> ('a -> 'b) -> 'c -> 'a t -> 'c
  
  type k
  exception Not_found

  val min : k t -> k t
  val max : k t -> k t

  val insert : k t -> k -> k t
  val delete : k t -> k -> k t

  val search : k t -> k -> k t
  val search_opt : k t -> k -> (k t) option

end

module RedBlackTree (Ord : ORD) : (RED_BLACK_TREE with type k = Ord.t)