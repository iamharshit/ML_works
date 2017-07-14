# MiniTensorflow

Nodes basically performs matematical functions such as Linear Combination and Activation function using input from the previous nodes. In case of LinearCombinator Node i.e X*W+b both the weights and bias are stored as seprate nodes with input node X in the previous layer.

Here the network can have 3 types of nodes simple node-that just stores a value and processing node- LinearCombinator node and Activator node.Hence here we need to know the position of simple,linear combinator and activator node in the previous layer so that we can accordingly process it.

NOTE: In actual Neural Nets the Linear combination operation is performed on the edges itself and the node just apply the activation function.

The input node can store just one value or a list/vector or matrix (in general a tensor).

# Steps

1. Define the nodes of the graph(i.e graph architecture and its operations).
2. Using the dataset feed in the values to train the Neural Net.

Each node stores 3 values: the address of inbound_nodes(so that it can use its values for calculation of current value), value of current node(so that the nodes of next layer can use it), outbound_nodes(so that from current node we can go to the next node).
