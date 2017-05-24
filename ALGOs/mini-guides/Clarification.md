
Discussions over some of the questions where i myself have faced doubts.

### Why weight initialisation using autoencoder is better favorable over random weight initialisation?
Ans. Although with weight initialisation using autoencoder we doesn't have full gaurantee that those weight would definatly be in neighbourhood of global minima because the curve of autoencoder need not be similar to that of our neural net then why the optimised weights of autoencoder be near or equal to the optimised weights of our neural net.But doesn't kinda sounds doing better that chosing something randomly would be bad over chosing something with some strategy.

It should be noted that weight initialisation using autoencoder doesn't affect the accuracy of neural net greatly, it just gives a jump of 2% to 3%.

### What if the probability difference is quite low while training the neural net for a classification problem Eg. highest probability  is  0.2229 followed by 0.2228?
Ans. Although here also we can directly the highest probability value but the confidence level would be low due to such a small difference.

From that we can infer that our neural net is not trained goodly, it may be suffering from one of the following problem - Data Insufficiency, Bad Network Architecture, Bad tuning of hyperparameters, or may be the test set is very much different from training set. 

Hence we need to iterate through each of the probable issues mentioned above and solve attempt to solve the problem. 

## When you get bad accuracy over the test set

* Adjust the hyperparameters like learning rate-make it lower.
* Increase the dataset if possible.
* Go for Transfer Learning i.e using an existing network to train our NNet.

## They say translational invariance is achieved by using same weights for each patch but since then those new valuse are updated at different positions, doesn't that matter since then in the fully connected step the value may be multiplied by different weights ? 


## What is better batch training a NNet or feeding all the datapoints at once?
Ans. In one line - People say that batch wise training is less preffered over feeding all the datapoints at once because but...

It matters the sequence in which we feed in the batches.

## How to choose the best learning rate?
Ans. My answer- learning rate should be variable - it should be a function of gradient - High at high gradient values and lower at low gradient values for better learning. 

## Normalisation across features for single datapoint is important or normalisation across different datapoints for single feature is important ?
Ans. Normalisation across features for single datapoint
The total no. of training iterations increases ...

## Why weights can not be initialised to 0 for NNet with more then or equal 2 layers ?
Ans.If you set weights for all the layers to 0 -> output of layer would be 0  -> during backpropagation gradient of the second last layer would be 0 since the xi value is made 0 for that NNet which is used up during gradient calculation -> overall for second last layer and behind the weight would never update from 0 and always be 0 -> which surly isn't desirable.

It is preferred to initialise weights with uniform distribution so that no number is likly to occur more then once.

## Why weights cannot be initialised with the same number ? 


## How updation happens in tensorflow ?
Ans. Batch-wise updation happens in tensorflow

## Why vanishing gradient problem doesn't arises in deep feed forward net or in deep CNN?






















