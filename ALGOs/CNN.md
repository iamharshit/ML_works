# Convolutional Neural Network

CNN are inspired from the visual cortex found in some animals.

Basically a Feature Extractor.
These are currently the most famous Neural Net architecture/model because of its impressive applications.
In one line a CNN extract features from an input image.
How CNNs are used to used to extract features ?
CNNs uses special type of network structure.The network contains multiple copies of the same neuron and all neurin share same weights, bias and activation function.
Feature Engineering is the process of extracting useful features from the input data and feed it into the predictive model.CNN are an alternative to Feature Enginnering.
Feature learning algorithm learns which features are useful for distinguishiing between different classes.
The extracted features can be used for classification or regression.
The next CNN layers then combine these features to increase the complexity of the image.Like combining nose, eyes, lips, ears to form a whole human face.
The final layers of CNNs use these generated features for the task at hand.

## Convolving

Think of a convolution as a way of mixing two functions by multiplying them.The first function is the input image being analyzed, and the second(mobile) function is known as the kernel/filter, because it picks up a signal or feature in the image.
![Visualisation](http://cs.stanford.edu/people/karpathy/convnetjs/demo/mnist.html)

Many filters over a single image, each one picking up a different signal.Initial filters(horizontal line filter, vertical line filter, diagonal line filter) detect edges in the image.

A 3X3 convolve kernel move across the whole image to form our convolve matrix.Kernel maps a region of the input matrix on to an element of the output matrix.

* Deciding upon Kerel
	1) For edge detection: Edge is a region/line where the color change.Hence we would get peak only at edges.
		[[0, 0, 0],
		 [1,-1,0],
       [0 ,0,0]]

	2) For image bluring: This kernel would erase the pattern that a deep Neural Net would need, hence is not useful for our purposes.
		[[1/9, 1/9, 1/9],
		 [1/9, 1/9, 1/9],
		 [1/9, 1/9, 1/9]]

Note: Various Kernals for different purposes are mentioned [here](https://en.wikipedia.org/wiki/Kernel_(image_processing)) and live demo can be seen [here](http://setosa.io/ev/image-kernels/).

Convnet processes images as Tensors(multi-dimensional array).The tensors are generally 4D array as shown below.

![img](https://deeplearning4j.org/img/3d_matrix.png)

The width and height of an image are easily understood. The depth is necessary because of how colors are encoded. Red-Green-Blue (RGB) encoding, for example, produces an image three layers deep. Each layer is called a “channel”, and through convolution it produces a stack of feature maps (explained below), which exist in the fourth dimension.

In layman terms...
So convolutional networks perform a sort of search. Picture a small magnifying glass sliding left to right across a larger image, and recommencing at the left once it reaches the end of one pass (like typewriters do). That moving window is capable recognizing only one thing, say, a short vertical line.A convolutional net runs many, many searches over a single image – horizontal lines, diagonal ones, as many as there are visual elements to be sought.Each time a match is found, the location of each vertical line match is recorded, a bit like birdwatchers leave pins in a map to mark where they last saw a great blue heron.

Padding padds the layers with the specified pad size so that information is not lost in subsequent layer during convolution.Stride specifies the step size by which the kernel moves.Higher the stride lesser computation would be required.

After a convolutional layer, input is passed through a nonlinear transform such as tanh or rectified linear unit, which will squash input values into a range between -1 and 1.Generally ReLU is used in CNNs.Note: Activation function are applied to both a simple neuron layer, convolving layer and   downsampling layer.

### How Convolving works?
Unlike humans Convnet percieve image as group of pixels.So a convolutional network receives a normal color image as a rectangular box whose width and height are measured by the number of pixels along those dimensions, and whose depth is three layers deep, one for each letter in RGB. Those depth layers are referred to as channels.

Rather than focus on one pixel at a time, a convolutional net takes in square patches of pixels and passes them through a filter(or kernel). That filter is also a square matrix smaller than the image itself, and equal in size to the patch.

We are going to take the dot product of the filter with this patch of the image channel. If the two matrices have high values in the same positions, the dot product’s output will be high. If they don’t, it will be low. In this way, a single value – the output of the dot product – can tell us whether the pixel pattern in the underlying image matches the pixel pattern expressed by our filter.Eg if the filter represents a horizontal line then it will output high value of dot product if the patch too contains a horizontal line.
Now, because there can be many different features in an image which we want to extract there are many filters used.This creates a stack of layers on the convolved side, each layer output of some filters.Thats the reason convolved image have higher breadth.
One of the problem which the input image and the convolved image is that they are of high dimensions(which costs higher computation time), hence we use an additional layer to reduce the dimensionality called "Max Pooling" or "Downsampling" layer.Also the maxpooling make the value as position unspecific,which makes better for us to identify if the feature is slightly shifted.
![](https://deeplearning4j.org/img/maxpool.png)
Although it leads to loss of information but still we need it unless we have GPUs.
ReLU Layer:
We use ReLU for normalisation purposes, i.e it changes a negative value to 0.

Fully Connected Layer:
This is the final layer

## Appications

CNNs are primarily used for image processing(image classification,clustering by similarity,object recognition) but can also be used for Recommender System, Speech Recognition and signal processing.It has such a wide range of applications because CNN can be applied on any 2D/3D/... data and we can extract the features.

We will use CNN for object recognition where we use CNN to extract elements of an image.Object Recognition is one of main reason why the world kind of likes Machine Learning domain.In object recognition it can identify faces,individuals, street signs, plants etc.
CNN could also learn to play vedio games by analysing pixels of certain frame and next frame and then adjusting its actions accordingly.It would revolutionising if CNNs could learn certain tasks such as cooking by simply watching the youtube vedios.

## Training of Object Recogniser
We try to mimic the human brain

* Form a representation of the visual world.
* Extract the primitive fartures, combine those to detect parts of the objects and then recombine parts to form object itself. 
* Report the appropriate category.

Overall, We use alternating convolution layer(for feature detection) and Maxpolling(for dimensionality reduction).In the last, before the output layer there is a fully connected layer.

As more and more information is lost, the patterns processed by the convolutional net become more abstract and grow more distant from visual patterns we recognize as humans.This is also one of the reasons why people find working of convnet non-intuative.

1[convnet network](https://www.researchgate.net/profile/Xiaoou_Tang/publication/263237688/figure/fig1/AS:296553458749440@1447715262034/Figure-1-The-ConvNet-structure-for-DeepID2-extraction.png)

# References 

* [Became Pro in CNNs](https://cs231n.github.io/)
* [How Convent works? Shown with math](https://www.youtube.com/watch?v=FmpDIaiMIeA)


## MNIST training why minibatches??
Batch gradient descent isn't used generally because its computationaly expensive.Hence we uses minibatches(of size 50) generally to train.
Case-1) We use Neural Net's Multi-layer perceptron model for training.
Case-2) Then we use CNN to train our model.
 
We get an accuracy of 
Some of the techniques to increase our prediction is DropConnect, multi-column deep nets, augmented pattern classification and dropout.






