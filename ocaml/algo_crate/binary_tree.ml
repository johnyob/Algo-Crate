type 'a t = Empty
          | Vertex of {
            k : 'a;
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
