import tensorflow as tf
import numpy as np
import datasetload

#Specifying Hyperparameters
mnist_dimension = 28
n_layer1 = mnist_dimension * mnist_dimension
n_hidden = 400

#Creating Nodes for input data and corrupted data
X = tf.placeholder("float", [None, n_layer1], name='X')
mask = tf.placeholder("float", [None, n_layer1], name='X')

#Creating Nodes for hidden layer
W_init_max = 4 * np.sqrt(6. / (n_layer1 + n_hidden))
W_init = tf.random_uniform(shape=[n_layer1, n_hidden], minval=-W_init_max, maxval=W_init_max)

W1 = tf.Variable(W_init, name='W1')
b1 = tf.Variable(tf.zeros([n_hidden]), name='b1')

W2 = tf.transpose(W1)  # tied weights between encoder and decoder
b2 = tf.Variable(tf.zeros([n_layer1]), name='b2')

#Building Model
def model(X, mask, W1, b1, W2, b2):
	X_corrupt = mask*X;

	Y = tf.nn.sigmoid(tf.matmul(X_corrupt,W1) + b1)
	Z = tf.nn.sigmoid(tf.matmul(Y,W2) + b2)
	
	return Z

#output
Z = model(X, mask, W1, b1, W2, b2)

#Specifying cost function
cost = tf.reduce_sum(tf.pow(X-Z,2))
train_op = tf.train.GradientDescentOptimizer(0.02).minimize(cost)

#Load Mnist Dataset
trX, trY, teX, teY = datasetload.load_mnist() 

#Starting actual training
#The error minimises with each iteration hence the generated image becames better 
with tf.Session() as sess:
	tf.initialize_all_variables().run()

	for i in range(100):
		#training for each epoch	 
		for start,end in zip(range(0,len(trX),128), range(128,len(trX),128)):
			input_ = trX[start:end]
			mask_ = np.random.binomial(1, 1-corrution_level, input_shape)
			sess.run(train_op, feed_dict={X:input_, mask:mask_})
