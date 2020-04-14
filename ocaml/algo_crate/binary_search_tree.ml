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


module BinarySearchTree (Ord : ORD) : (BINARY_SEARCH_TREE with type k = Ord.t) = 
struct
  include Binary_tree
  
  type k = Ord.t
  exception Not_found

  let rec min t = match t with
    | Empty -> raise Not_found
    | Vertex {l=Empty} -> t
    | Vertex {l} -> min l

  let rec max t = match t with
    | Empty -> raise Not_found
    | Vertex {r=Empty} -> t
    | Vertex {r} -> max r
  
  let rec insert t k = match t with
    | Empty -> Vertex {k = k; l = Empty; r = Empty;}
    | Vertex n when Ord.lt k n.k -> Vertex {n with l = insert n.l k}
    | Vertex n when Ord.gt k n.k -> Vertex {n with r = insert n.r k} 
    | _ -> t

  let rec delete t k = match t with
    | Empty -> Empty
    | Vertex n when Ord.lt k n.k -> Vertex {n with l = delete n.l k}
    | Vertex n when Ord.gt k n.k -> Vertex {n with r = delete n.r k} 
    | _ -> match t with
      | Vertex {l=Empty; r=Empty} -> Empty
      | Vertex {l=Empty; r} -> r
      | Vertex {l; r=Empty} -> l
      | Vertex {l; r} -> 
        let Vertex {k=k'} = min r in
        let r' = delete r k' 
        in Vertex {k=k'; l=l; r=r'}

  let rec search t k = match t with
    | Empty -> raise Not_found
    | Vertex {k=k'; l} when Ord.lt k k' -> search l k
    | Vertex {k=k'; r} when Ord.gt k k' -> search r k
    | _ -> t

  let rec search_opt t k = match t with
    | Empty -> None
    | Vertex {k=k'; l} when Ord.lt k k' -> search l k
    | Vertex {k=k'; r} when Ord.gt k k' -> search r k
    | _ -> Some t
  
end