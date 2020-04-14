module type EQ = sig
  type t

  val eq : t -> t -> bool
  val ne : t -> t -> bool
end

module type ORD = sig
  include EQ

  type ordering = LT | GT | EQ
  val compare : t -> t -> ordering
  
  val lt : t -> t -> bool
  val gt : t -> t -> bool
  val lte : t -> t -> bool
  val gte : t -> t -> bool

  val min : t -> t -> t
  val max : t -> t -> t
end

