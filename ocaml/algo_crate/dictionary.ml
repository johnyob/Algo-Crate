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

module ListDictionary (Eq : EQ) : (DICTIONARY with type k = Eq.t) = 
struct
  type k = Eq.t 
  type 'v t = (k * 'v) list
  exception Not_found

  let empty = []
  let is_empty d = (d = empty)

  let insert d k v = (k, v) :: d
  let rec delete d k = match d with
    | [] -> []
    | (k', v) :: d when Eq.eq k k' -> d
    | (k', v) :: d -> (k', v) :: delete d k

  let rec search d k = match d with
    | [] -> raise Not_found
    | (k', v) :: d when Eq.eq k k' -> v
    | (k', v) :: d -> search d k

  let rec search_opt d k = match d with
    | [] -> None
    | (k', v) :: d when Eq.eq k k' -> Some v
    | (k', v) :: d -> search d k

end

module TreeDictionary (Ord : ORD) : (DICTIONARY with type k = Ord.t) = 
struct
  (*required RB trees*)
end

