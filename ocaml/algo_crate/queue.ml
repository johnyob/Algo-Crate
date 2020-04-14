type 'a t = 'a list * 'a list
exception Empty

let empty = ([], [])
let is_empty q = (q = empty)

let norm q = match q with
  | ([], ys) -> (List.rev ys, [])
  | q -> q
  
let enqueue (xs, ys) y = norm (xs, y :: ys)
let dequeue q = match q with
  | (x :: xs, ys) -> norm (xs, ys)
  | _ -> raise Empty

let peek q = match q with
  | (x :: _, _) -> x
  | _ -> raise Emtpy
let peek_opt q = match q with
  | (x :: _, _) -> Some x
  | _ -> None
