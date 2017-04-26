## Deep Belief Network

It is a stack of RBMs where hidden layer of one RBM act as input layer for another.Except the first and final layer each layer serves double role hidden layer and visible layer.Each layer communicate with the previous and subsequent layer but not within itself.Like RBMs, DBN too only accepts binary input.
They were the first general-purpose Deep Learning Architecture although CNNs are much older but only used for Vision tasks.They are primarily used for classification, clustering and data generation.Stack of RBMs or DBN would always outperform primitive RBM with only 2 layers.

![img](https://i.stack.imgur.com/1bCQl.png)

Structurally DBN looks similar to MLP but the training process is entirly different.Being Generative Model DBNs are used for generating and recognizing images (Hinton, Osindero & Teh 2006, Ranzato et. al. 2007, Bengio et.al., 2007), video sequences (Sutskever and Hinton, 2007), and motion-capture data (Taylor et. al. 2007).

### Why DBN?

DBN were developed as an alternative to Back propagation since it can lead to local minima.DBN solve the problem by incorporating an extra step called pre-training which leads to solution near to the global minima's solution and then we do the usual back propagation to reach global minima.

### Resources
* [Easy Math](www.scholarpedia.org/article/Deep_belief_networks)

