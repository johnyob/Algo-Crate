open TypeClass
open Util

module EQ_Bool : EQ with type t = bool = struct
  type t = bool

  let eq = Pervasives.( = )
  let ne x y = not (eq x y)
end
