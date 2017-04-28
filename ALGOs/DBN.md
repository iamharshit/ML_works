## Deep Belief Network

It is a stack of RBMs(<i>for begineers becaz actually thats Deep Boltzmann Network</i>) where hidden layer of one RBM act as input layer for another.Except the first and final layer each layer serves double role hidden layer and visible layer.Each layer communicate with the previous and subsequent layer but not within itself.Like RBMs, DBN too only accepts binary input.

They were the first general-purpose Deep Learning Architecture although CNNs are much older but only used for Vision tasks.They are primarily used for classification, clustering and data generation.Stack of RBMs or DBN would always outperform primitive RBM with only 2 layers.

![img](https://agollp.files.wordpress.com/2013/12/dbm.jpg)	

Structurally DBN looks similar to MLP but the training process is entirly different.Being Generative Model DBNs are used for generating and recognizing images, video sequences and motion-capture data.
Specifically only the the top 2 layers forms an RBM with undirected interations and other layer with directed edges forms Sigmoid Belief Network.

### Why DBN for "Classification/Supervised Learning" when we had Traditional Neural Net?

DBN were developed as an alternative to random initialisation of parameters since it can lead to local minima.DBN solve the problem by incorporating an extra step called pre-training which leads to solution near to the global minima's solution and then we do the usual back propagation to reach global minima.

### Why DBN for "Feature Extraction" when we had RBM?

RBM suffers from vanishing gradient problem which is incorporated in RBM. Moreover DBN(stack of RBMs) outperforms single RBM generally.	

### Training of DBN

The DBN's training process is same for both objectives i.e using DBN for pretraining and using DBN as feature extractor.During training the DBN learns to probablistically reconstruct the input from the hidden layer.The layer if analysed acts as feature detectors for input.After this training the weights learned can be used in a supervised training of the same data.

### Resources
* [Easy Math](https://scholarpedia.org/article/Deep_belief_networks)

