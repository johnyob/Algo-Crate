let ( <.> ) f g = fun x -> f (g x)
let ( $ ) f x = f x