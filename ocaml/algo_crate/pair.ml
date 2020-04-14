open Type_class

module type EQ_Pair (X : EQ) (Y : EQ) : (EQ with type t = X.t * Y.t)
module type ORD_Pair (X : ORD) (Y : ORD) : (ORD with type t = X.t * Y.t)
