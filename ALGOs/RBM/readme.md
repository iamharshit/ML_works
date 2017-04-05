## RBM 

Restricted Boltzmann Machine or RBM are primarily used for Latent Feature extraction from the given input dataset which is done by analysing weight distribution on each hidden node for each input.
It is a graphical model for binary random variables.It is a very shallow network and contains only 2 layers the visible and the hidden layer.It acts like a bipartite graph since each node in the visible layer is connected to each node in the hidden layer. The term "restricted" comes because the nodes in the same layer are not allowed to be connected.Based on a complete bipartite graph separating hidden and observed variables, it is the binary analog to the factor analysis model.
For simple feed-forward movements, the RBM nodes function as an autoencoder.

* Forward Propagation Phase
![RBM NNet img](https://deeplearning4j.org/img/multiple_inputs_RBM.png)

* Reconstruction Phase
![Reconstrustion img](https://deeplearning4j.org/img/reconstruction_RBM.png)

### References
* [Nice Example on application of RBM](http://blog.echen.me/2011/07/18/introduction-to-restricted-boltzmann-machines/)
* [RBM Basics and Training](https://deeplearning4j.org/restrictedboltzmannmachine)



