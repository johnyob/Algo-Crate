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

module RedBlackTree (Ord : ORD) : (RED_BLACK_TREE with type k = Ord.t) = struct
  
  type color = Red | Black | BB
  type 'a t = Empty 
            | Empty_BB
            | Vertex of {
              k : 'a;
              c : color; 
              l : 'a t;
              r : 'a t
            }
  
  let empty = Empty
  let is_empty t = (t = Empty)
  
  let traverse step f acc t = 
    let rec inner t acc = match t with
      | Empty -> acc
      | Vertex {k;l;r} -> step (f k) (inner l) (inner r) acc
    in inner t acc
  
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

  let balance t = match t with
    | Vertex {k=y; c=Black; l=Vertex {k=x; c=Red; l=a; r=Vertex {k=z; c=Red; l=b; r=c}}; r=d}
    | Vertex {k=x; c=Black; l=a; r=Vertex {k=y; c=Red; l=Vertex {k=z; c=Red; l=b; r=c}; r=d}}
    | Vertex {k=x; c=Black; l=a; r=Vertex {k=z; c=Red; l=b; r=Vertex {k=z; c=Red; l=c; r=d}}}
    | Vertex {k=y; c=Black; l=Vertex {k=z; c=Red; l=Vertex {k=x; c=Red; l=a; r=b}; r=c}; r=d}
      -> Vertex {k=z; c=Red; l=Vertex {k=x; c=Black; l=a; r=b}; r=Vertex {k=y; c=Black; l=c; r=d}}
    
    | Vertex {k=x; c=BB; l=Vertex {k=y; c=Red; l=a; r=Vertex {k=z; c=Red; l=b; r=c}}; r=d}
    | Vertex {k=y; c=BB; l=a; r=Vertex {k=x; c=Red; l=Vertex {k=z; c=Red; l=b; r=c}; r=d}}
      -> Vertex {k=z; c=Black; l=Vertex {k=y; c=Black; l=a; r=b}; r=Vertex {k=x; c=Black; l=c; r=d}}
    
    | _ -> t

  let insert t k = 
    let rec ins t = match t with
      | Empty -> Vertex {k=k; c=Red; l=Empty; r=Empty}
      | Vertex n when Ord.lt k n.k -> balance (Vertex {n with l=ins n.l}) 
      | Vertex n when Ord.gt k n.k -> balance (Vertex {n with r=ins n.r})
      | _ -> t
    and make_black t = match t with
      | Empty -> Empty
      | Vertex n -> Vertex {n with c=Black} 
    in make_black (ins t)


  let rotate t = match t with
    (*Case i*)
    | Vertex {k=y; c=Red; l=Vertex {k=x; c=BB; l=a; r=b}; r=Vertex {k=z; c=Black; l=c; r=d}} 
      -> balance (Vertex {k=z; c=Black; l=Vertex {k=y; c=Red; l=Vertex {k=x; c=Black; l=a; r=b}; r=c}; r=d})
    | Vertex {k=y; c=Red; l=Vertex {k=x; c=Black; l=a; r=b}; r=Vertex {k=z; c=BB; l=c; r=d}} 
      -> balance (Vertex {k=x; c=Black; l=a; r=Vertex {k=y; c=Red; l=b; r=Vertex {k=z; c=Black; l=c; r=d}}})
    
    (*Case ii*)
    | Vertex {k=y; c=Black; l=Vertex {k=x; c=BB; l=a; r=b}; r=Vertex {k=z; c=Black; l=c; r=d}} 
      -> balance (Vertex {k=z; c=BB; l=Vertex {k=y; c=Red; l=Vertex {k=x; c=Black; l=a; r=b}; r=c}; r=d})
    | Vertex {k=y; c=Black; l=Vertex {k=x; c=Black; l=a; r=b}; r=Vertex {k=z; c=BB; l=c; r=d}} 
      -> balance (Vertex {k=x; c=BB; l=a; r=Vertex {k=y; c=Red; l=b; r=Vertex {k=z; c=Black; l=c; r=d}}})

    (*Case iii*)
    | Vertex {k=y; c=Black; l=Vertex {k=x; c=BB; l=a; r=b}; r=Vertex {k=z; c=Red; l=Vertex {k=w; c=Black; l=c; r=d}; r=e}}
      -> Vertex {k=z; c=Black; l=balance $ Vertex {k=w; c=Black; l=Vertex {k=y; c=Red; l=Vertex {k=x; c=Black; l=a; r=b}; r=c}; r=d}; r=e}
    | Vertex {k=y; c=Black; l=Vertex {k=x; c=Red; l=a; r=Vertex {k=w; c=Black; l=b; r=c}}; r=Vertex {k=z; c=BB; ld; r=e}}
      -> Vertex {k=x; c=Black; l=a; r=balance $ Vertex {k=w; c=Blackl; l=b; r=Vertex {k=y; c=Red; l=c; r=Vertex {k=z; c=Black; l=d; r=e}}}}
  

  let rec delete t k = 
    let rec del t = match t with
      | Empty -> Empty
      
      (*Case i: Vertex t has no children and is red. delete red -> bh doesn't change*)
      | Vertex {k=x; c=Red; l=Empty; r=Empty} when Ord.eq k y -> Empty
      | Vertex {k=x; c=Red; l=Empty; r=Empty} -> t
      
      (*Case i: Vertex t has no children and is black. delete black -> bh decreases, use BB vertex*)
      | Vertex {k=x; c=Black; l=Empty; r=Empty} when Ord.eq k y -> Empty_BB
      | Vertex {k=x; c=Black; l=Empty; r=Empty} -> t
      
      (*Case ii: Vertex t has a single child*)
      | Vertex {k=x; c=Black; l=Vertex {k=y; c=Red; l=Empty; r=Empty}; r=Empty} when Ord.eq k x -> Vertex {k=y; c=Black; l=Empty; r=Empty} 
      | Vertex {k=x; c=Black; l=Vertex {k=y; c=Red; l=Empty; r=Empty}; r=Empty} as n when Ord.lt k x -> Vertex {n with l=del n.l}  
      | Vertex {k=x; c=Black; l=Vertex {k=y; c=Red; l=Empty; r=Empty}; r=Empty} (*when Ord.gt k x*) -> t 
      
      | Vertex {k=x; c=Black; l=Empty; r=Vertex {k=y; c=Red; l=Empty; r=Empty}} when Ord.eq k x -> Vertex {k=y; c=Black; l=Empty; r=Empty} 
      | Vertex {k=x; c=Black; l=Empty; r=Vertex {k=y; c=Red; l=Empty; r=Empty}} as n when Ord.lt k x -> t  
      | Vertex {k=x; c=Black; l=Empty; r=Vertex {k=y; c=Red; l=Empty; r=Empty}} (*when Ord.gt k x*) -> Vertex {n with r=del n.r}
      

      (*Case R->B and B->B cannot exist for single child*)

      (*Case iii: Vertex t has two children. Requires rotations to bubble DB to root*)
      | Vertex n when Ord.lt k n.k -> rotate $ Vertex {n with l=del n.l}
      | Vertex n when Ord.gt k n.k -> rotate $ Vertex {n with r=del n.r}
      | Vertex n -> 
        let Vertex {k=k'} = min n.r in
        let r' = delete n.r k' 
        in rotate $ Vertex {k=k'; c=n.c; l=n.l; r=r'}
    and make_black t = match t with
      | Empty -> Empty
      | Empty_BB -> Empty
      | Vertex n -> Vertex {n with c=Black} 
    in make_black (del t)


end

