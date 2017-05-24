## NNet 
An artifically inspired technique that learn to identify patterns in the data.

## Activation function - Does Categorisation

The idea with Activation functions is they incorporate the idea of binary output i.e 1(OR yes) and 0(OR no), hence these are usually used in classification problems.It pushes the output towards 0 and 1.

Why not use the direct step function instead of continous activation function ?

Although here the direct step function suits best for the job but then it creates a problem during backpropagation since the step function is non-differentiable.Instead we can also incorporate the idea of discrete/direct step function with continous step function by pushing the value to 0 if its less then 0.5 and to 1 if greater then 0.5 and simultaneously incorporate the idea of backpropagation.

Generally we use the sigmoid function as the activator.
Additional advantage - Calculating derivative with sigmoid is quite direct.

## Why not sigmoid?

The maximum value sigmoid derivative can take is 0.25 hence the error shrinks by atleast 75%, this often leads to vanishing gradient which isn't desirable.

Also sigmoid is generally used for binary classification.

## Alternative:ReLU

We use ReLU as activation function, its derivative at max is 1 hence it leads to faster training.It is pre-implemented in tensorflow as `tf.nn.relu()`.

## When Softmax?

Softmax function are used when there are many classes.It's the perfect function to use as the output activation for a network predicting multiple classes.`tf.nn.softmax()` implements the softmax function for you. It takes in logits and returns softmax activations.

## Softmax vs Sigmoid 

The only real difference between this and a normal sigmoid is that the softmax normalizes the outputs so that they sum to one. In both cases you can put in a vector and get out a vector where the outputs are a vector of the same size, but all the values are squashed between 0 and 1. You would use a sigmoid with one output unit for binary classification. But if you’re doing multinomial classification, you’d want to use multiple output units (one for each class) and the softmax activation on the output.

The softmax can be used for any number of classes.It's also used for hundreds and thousands of classes, for example in object recognition problems where there are hundreds of different possible objects.

## Cross Entropy

It is used generally  when the output is expressed in one-hot encoding.What's cool about using one-hot encoding for the label vector is that y​j​​ is 0 except for the one true class. Then, all terms in that sum except for where y​j​​=1 are zero and the cross entropy is simply D=−ln​y​^​​ for the true label.
It can be easily computed in tensorflow as: `-tf.reduce_sum(one_hot*tf.log(softmax))` or `tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logits, labels=y))`.

NOTE: Unlike SSE, Cross-Entropy is non-symmetrical.

## Weight init

Choosing weights from a normal distribution prevents any one weight from overwhelming other weights. We'll use the `tf.truncated_normal()` function to generate random numbers from a normal distribution.Moreover, we randomize the values so that the model is not stuck at the same place we run our code.
Since the weights are already helping prevent the model from getting stuck, you don't need to randomize the bias.Hence we can initialise the bias using `tf.zeros(n_labels)`

## One Hot encoding 

A way of representing the label in mathematical manner.Can be done in scikit-learn
```
import numpy as np
from sklearn import preprocessing

# Example labels
labels = np.array([1,5,3,2,1,4,2,1,3])

# Create the encoder
lb = preprocessing.LabelBinarizer()

# Here the encoder finds the classes and assigns one-hot vectors 
lb.fit(labels)

# And finally, trans1form the labels into one-hot encoded vectors
lb.transform(labels)
```

## Why hidden layer?

Adding a hidden layer to a network allows it to model more complex functions. Also, using a non-linear activation function on the hidden layer lets it model non-linear functions.

## Numerical Optimisation

We model ML as a Numerical Optimisation Problem where our aim is to optimise(here minimise) the Loss function.There are various optimisation methods with GradientDescent one of them.Hence deciding the loss function directly affects the NNet's performance.

## Gradient Descent vs Stochastic Gradient Descent

Computing exact gradient is computionaly expensive hence we compute gradient estimate for Gradient Descent.Although this estimate is quite bad but computing it for many steps ultimately leads to optimisation.
In SGD instead of running in the direction of minima we run in random direction, those steps in aggregate takes us to the global minima.

## Adagrad

Modification of SGD which implicitly does momentum and learning rate decay.

## Minibatching

Mini-batching is a technique for training on subsets of the dataset instead of all the data at one time. This provides the ability to train a model, even if a computer lacks the memory to store the entire dataset.

Mini-batching is computationally inefficient, since you can't calculate the loss simultaneously across all samples. However, this 
is a small price to pay in order to be able to run the model at all.

## Epoch

An epoch is a single forward and backward pass of the whole dataset. This is used to increase the accuracy of the model without requiring more data.

## Learning rate 

Ideally Learning rate should be large in the initial steps but should be small as we reach the global minima.Hence its value is kept variable in practise with its value continously decreasing over time.This technique is called as learning rate decay.

## Numerical Stability 

Its python behavior that when a large number is added to a small number it introduces a small error in it.We want the value of our loss function to neither get too big or too small.

This can be obtained if the each input has mean 0 and different inputs have equal variance.For a well prepared input set the optimizer takes less number of iterations to reach the minima.Eg) Normalising pixel values(which have range 0 to 255) = (input - 128)/128.THe technique is called as Normalised Input.

## Weight Initialisation

Weight Initialisation is an important step since it determines that the final optimised point is global minima or local minima.GenerallyWe initialse the weights with values the follow normal distribution, have mean of 0 and have small std deviation(so that the decision is more uncertain).

## Why Measuring Performance is Important?

Every Classifier we build tries to memorize the training set, it is our job to reduce the memorisation and increase its generalisation.

## Validation Set 

Used to tune the hyperparameters by hit & trial method.

## Artificial NNet vs Natural NNet

Natural NNet exists in real although Artificial NNet is just a concept that is simulated on computer.Natural NNet uses electrical signals, whereas Artificial NNet uses value as signals.
Despite all theses disilariter in some cases eg.chess - the Artificial NNet outperforms Natural NNet.

## Why RNN and CNN works over feed forward?

Because our data have some structure that it need not learn from scratch. By using RNN or CNNs architecture in our Neural Net it is seeing from our eyes.

Data we feed in Neural Net in CNN:
* Translational Invariance - It doesn't matter if the image of cat occurs in which part of the frame.The meaning of a word is independent of where the word is occuring.
			   - In CNN weights are shared across different kernels while in RNN weights are shared across a sequence.
* Filters: Classify Local Patterns

## CNN specialities

It isn't hard coded to learn specific characteristics in a patch instead the CNN learns on its own.

## Why hidden to hidden connections are needed in an RNN?


