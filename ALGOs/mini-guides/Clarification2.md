These FAQ are basically on overfitting, activation functions, optimizers


==================================Overfitting========================
## When do we say the model is overfit?
If we plot the training and testing accuracy in a plot, we see that first it converges then diverges, overfitting start from the point when the traing and testing accuracy starts to diverge.
Hence different model can overfit at different values of training accuracy.


## Do we ever need overfitting ?
Yes, ideally we should first try to overfit to 100% on our training data to know that our model has sufficient complexity to memorize our data - if it overfits we can conclude that if our model can memorize it can also generalise over the data since that requires comparitivly less accuracy


## Is 100% Overfitting always possible?
Yes, provided your model have sufficient complexity for the given data(no matter if its correct or not), it is always possible to do 100% overfitting.
 


==================================Activation Function=================
## Overview
Activation functions are a way of modelling thresolding as observed in our brain.Activation function mainly does 2 roles- Firing behavior- i.e fire the neuron if data is greater then a certain value(used for classification problem) , Non-Linearity - introduce non-linearity in the overall function(generally used for regression problem).
There are 4 commonly used activation functions- 1.sigmoid, 2.softmax, 3.tanh, 4.relu, written in the order of preference level.


## Sigmoid vs Tanh
Sigmoid suffers from the problem of non-zero centered output and vanishing gradient but tanh suffers from the problem of vanishing gradient only.Hence tanh is preferred over sigmoid.Hence in industry also tanh function is preffered over sigmoid for classification purposes.


## Why non-zero centered output is a problem ?
Generally normalised data(i.e mean is 0) is given as input to a neuron or activation function, it changes the inherent distribution of the data. Thus, each following layer has to learn a new distribution each time. So, preserving the data distribution helps in converging faster.


## Tanh vs RelU
RelU doesn't suffers from the problem of vanishing gradient. But unlike Tanh, Relu doesn’t provide zero-centred output.


## Why instead of calculating the direct probability the softmax function calculates the probability of the value(y)'s exponent?




## Roles of activation function?
sigmoid and tanh are used generally for classification purpose because there outputs are bounded, Relu is used for regression purposes because its output range from 0 to +infinity.
Sometimes tanh is used for regression also by rescaling its output.


## Why don't we use e^x as an activation function although it have firing behaviour?
Because e^x function doesn't have the firing behaviour unlike the usual activation function like other activation functions - sigmoid, Tanh,Relu. Moreover, it may also explode the values.


## Why don't we use sin(x) as an activation function although it have firing behaviour?
Because the cortical neurons never invert the sign of the incoming signal


ReLU


## Why RelU have a slope of exact 0 or near to zero and not any other value for x<0 ?
ReLU is more biologically plausible than standard sigmoidal functions, as it is rare to have cortical neurons in their maximum saturation regime.


## Can RelU be used to model functions like x^2?
Although at first glance it looks like that relu can really model curvy functions because its curve has a sharp tip and not curveness but if we use multiple ReLU function in combination then it can approximatly model curves like x^2.
![img]


## Advantages of ReLU
1. Overcomes vanishing gradient problem
2. No saturation regime
3. Near approximation of softplus(ln(1 + e^x)) 
4. Computationally efficient
## Disadvantages of ReLU
1. Neurons initialized with <0 value die out
2. Not zero-centred (adding a shift bias to the data distribution)


Leaky ReLU


f(x) =| x for x>0
        | 0.01x for x<0


* Solves the problem of vanishing gradient for -ve half
* Though, didn’t add much to the accuracy




Parametrized ReLU


f(x) =| x for x>0
        | ax for x<0


a = hyperparameter, dimensionality same as the number of channels
        Updated during backprop
* Though, becomes ReLU if a diminishes to 0


Exponential Linear Unit(ELU)


f(x) =| x for x>0
        | a(e^x - 1) for x<0


* Approximately zero-centred
* Saturates to a  negative value with smaller arguments


Bounded ReLU


f(x) =| x for a>x>0
        | 0.01x for x<0
        | a for x>a




* To cater to systems which allow a limited range of values, eg - embedding systems
* Idea is that as long as the output boundary is large enough to alleviate the vanishing grad. Problem, but at the same time small enough to avoid the numerical instability problem.






## Good References for activation functions


1. http://www.cs.toronto.edu/~fritz/absps/reluICML.pdf
2. https://www.semanticscholar.org/paper/Rectifier-Nonlinearities-Improve-Neural-Network-Ac-Maas-Hannun/367f2c63a6f6a10b3b64b8729d601e69337ee3cc
3. ReLU - http://proceedings.mlr.press/v15/glorot11a/glorot11a.pdf
4. PReLU - https://arxiv.org/abs/1502.01852
5. ELU - https://arxiv.org/abs/1511.07289
6. Bounded activation - http://www.sciencedirect.com/science/article/pii/S0925231216308797




============================Optimizers=============================


Basic Notations used - 
        P - set of parameters
        J(P) - cost function
        n - learning rate
        d - del operator


1. Gradient Descent
* Computes the gradient wrt P for the entire dataset
* Just 1 update
* Not possible if the memory can’t fit the entire dataset
        P = P - n*d(J(P))


      2. Stochastic Gradient Descent
* Performs parameter update for each training dataset
* Computationally inefficient
* Slower convergence
        P = P - n*d(J(P: xi, yi))


      3. Mini-batch GD
* Performs update for every mini-batch of training examples
* Leads to stable convergence
* Makes full use of the memory
* Makes use of the highly optimized matrix operations
        P = P - n*d(J(P; xi:xi+n, yi:yi+n))


      Challenges of GD - 
* Choosing a good learning rate
* Difficulty at saddle points


      To overcome the saddle point problem -
      # Momentum
* To overcome the problem of navigating through ravines(surface curves more steeply in one direction as compared to another)
* Momentum helps accelerate SGD in the relevant direction and dampens oscillations in ravines
V(t)t = yv(t-1) + n*d(J(P))        y = 0.9
P = P - V(t) 
* To decrease updates in dimensions where gradient changes direction and increase where direction is constant
* Disadv - might overshoot minimum
