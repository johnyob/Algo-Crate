open Type_class
open Util

module EQ_Int : (EQ with type t = int) = 
struct
  type t = int

  let eq = Pervasives.( = )
  let ne = not <.> eq
end

module ORD_Int : ORD  = struct
  include EQ_Int

  let compare x y = match Pervasives.compare x y with
    | n when n = 0 -> EQ
    | n when n < 0 -> LT
    | n when n > 0 -> GT

  let lt = Pervasives.( < )
  let gt = Pervasives.( > )

  let lte = Pervasives.( <= ) 
  let gte = Pervasives.( >= )

  let min = Pervasives.min
  let max = Pervasives.max
end