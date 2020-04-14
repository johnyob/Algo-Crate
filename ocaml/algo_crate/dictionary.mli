open Type_class

module type DICTIONARY = sig
  type k
  type 'v t
  exception Not_found

  val empty : 'v t
  val is_empty : 'v t -> bool
  

  val insert : 'v t -> k -> 'v -> 'v t
  val delete : 'v t -> k -> 'v t

  val search : 'v t -> k -> 'v
  val search_opt : 'v t -> k -> 'v option

end

module ListDictionary (Eq : EQ) : (DICTIONARY with type k = Eq.t)
module TreeDictionary (Ord : ORD) : (DICTIONARY with type k = Ord.t)