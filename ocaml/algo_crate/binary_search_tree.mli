open Type_class

module type BINARY_SEARCH_TREE = sig
  include Binary_tree

  type k
  exception Not_found

  val min : k t -> k t
  val max : k t -> k t

  val insert : k t -> k -> k t
  val delete : k t -> k -> k t

  val search : k t -> k -> k t
  val search_opt : k t -> k -> (k t) option

end

module BinarySearchTree (Ord : ORD) : (BINARY_SEARCH_TREE with type k = Ord.t)