import numpy as np
import tensorflow as tf
from random import shuffle

bit_length = input('Enter the Binary sequence length: ')

# Construct training data
print 'Contructing dataset....'
train_input = [('{0:0'+str(bit_length)+'b}').format(i) for i in range(2**(bit_length/2+1) )]
shuffle(train_input)
num_examples = 100
train_input = train_input[:num_examples]
train_input = [map(lambda x: [int(x)], i) for i in train_input] #Converting into tensorflow acceptable format

train_output = []
for x in train_input:
	cnt = 0
	for y in x:
		if y[0]==1: cnt+=1
		else: pass
	temp = [0]*(bit_length+1)
	temp[cnt]=1
	train_output.append(np.array(temp))

# Building Model
print 'Building Model....'
data = tf.placeholder(tf.float32, [None, bit_length, 1])
target = tf.placeholder(tf.float32,[None, bit_length+1])

lstm = tf.contrib.rnn.LSTMCell(24) # 24 is the hidden_state size
val,_ = tf.nn.dynamic_rnn(lstm, data, dtype=tf.float32) # memory cell state is not useful, size of val is batch_size*sequence_sixe(=20)*24

val = tf.transpose(val, [1,0,2])
val = tf.gather(val, val.shape[0]-1) # we need the value of only the last hidden state  

weights = tf.Variable(tf.random_normal( [24,int(target.shape[1])] )) # tf.Variable(np.random.normal([24,int(target.shape[1]) ] ), tf.float32)
bias = tf.Variable(tf.random_normal([int(target.shape[1])] )) # tf.Variable(np.random.normal( [int(target.shape[1])] ), tf.float32)

prediction = tf.nn.softmax(tf.matmul(val,weights)+ bias)
loss = -tf.reduce_sum(target*tf.log(prediction))

optimizer = tf.train.AdamOptimizer()
minimize = optimizer.minimize(loss)

# Start Session
print 'Start training.....'
sess = tf.Session()
sess.run(tf.global_variables_initializer())

num_epochs = 100
batch_size = 10
num_batches= num_examples/batch_size
for e in range(num_epochs):
	start=0
	for b in range(num_batches):
		inp = train_input[start:start+batch_size]
		out = train_output[start:start+batch_size]
		start += batch_size
	
		sess.run(minimize, {data:inp, target:out})
# Prediction
for _ in range(5):
	inp = raw_input('Enter a Binary number of Length '+str(bit_length)+' : ')
	inp = [ map(lambda x: [int(x)],inp) ]
	ans_array = sess.run(prediction, {data: inp})[0]
	print 'Predicted length: '+str( sess.run( tf.argmax(ans_array) ) )
	print ''





