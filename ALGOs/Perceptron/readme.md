# Perceptron
 
A perceptron can be single layer or multiple layer.

## Single Layer Perceptron

![NNet of SL perceptron](http://computing.dcu.ie/~humphrys/Notes/Neural/Bitmaps/sum.jpg)

Single layer perceptron is just the weighted sum of the inputs and if the weighted sum is greater then threshold 't' output is 1 otherwise 0.It consistes of just 2 layers input and output layer.Using perceptron we can simple write logic gates such as "AND", "OR", "NOT".

![single layer perceptron](http://computing.dcu.ie/~humphrys/Notes/Neural/Bitmaps/rule.gif)

Graphically if we see a perceptron model just draws a line for w1I1 + w2I2 = t on the I1 vs I2 axis and check the position of specified (i1,i2) relative to the line.

![img](http://computing.dcu.ie/~humphrys/Notes/Neural/Bitmaps/or.linear.jpg)

Although i have explicitly defined weights but we need not define the weights, instead they are automatically learned by showing it the correct answer.So basically we start with drawing a random line. Some point is on the wrong side. So we shift the line. Some other point is now on the wrong side. So we shift the line again. And so on. Until the line separates the points correctly.
It can only works for linearly seprable data, infact we can classify data with any no. of classes as long as it is linearly seprable.

Example:

![prob](http://computing.dcu.ie/~humphrys/Notes/Neural/Bitmaps/furniture.space.jpg)

![sol](http://computing.dcu.ie/~humphrys/Notes/Neural/Bitmaps/furniture.net.jpg)

For not non-linearly seprable data we use multilayer perceptron.


## Multi-Layer Perceptron

It has atleast one hidden layer other then input & output layer and is used for non-linear data classification.Using multi-layer perceptron we can implement non-linearly seprable logic gates eg.XOR.In general a layer 2 neural net can classify area formed by any no. of lines. 

![img](http://computing.dcu.ie/~humphrys/Notes/Neural/Bitmaps/multi.neural.1.jpg)

### History of evolution of perceptron
The perceptron model is inspired from the human brain.
Perceptrons were the most earliest NNet developed.Although people knew they need multi-layer perceptron for non-linear classification but it came into picture much later because learning algorithm for multi-layers were not known then.Only after the advent of back-propagation algorithm we started using multi-layer perceptron model.
