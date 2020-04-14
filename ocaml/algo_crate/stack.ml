type 'a t = 'a list
exception Empty

let empty = [] 
let is_empty xs = (xs = empty)

let push xs x = x :: xs
let pop xs = match xs with
  | _ :: xs -> xs
  | _ -> raise Empty

let peek xs = match xs with
  | x :: _ -> x
  | _ -> raise Empty
let peek_opt xs = match xs with
  | x :: _ -> Some x
  | _ -> None
