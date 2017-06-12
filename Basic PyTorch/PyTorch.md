## Overview
PyTorch does imperative programming i.e the code is compiled/executed at the time of function declaration unlike symblic programming where the code is graph of operations/functions is built first and then the execution happens.Imperative program are flexible in terms of graph structure/architecture since it can be changed in the middle during compilation also.

Hence in PyTorch we can make dynamic graphs, this isn't possible in tensorflow since we define the computation graph first and then executed it i.e its structure cannot be changed during execution(those are called Static graph- since graph cannot be changed during run time) since it follows imperative programming.In short we have more degree of freedom with PyTorch.

