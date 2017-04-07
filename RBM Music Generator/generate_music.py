import numpy as np #scintific computing
import pandas as pd #DA library
import tensorflow as tf #ML lib
import tqdm #Progress bar
import helper
import glob
from tensorflow.python.ops import control_flow_ops	
import msgpack

#Loading Datset
def get_songs(path):
    files = glob.glob('{}/*.mid*'.format(path))
    songs = []
    for f in tqdm.tqdm(files):
        try:
            song = np.array(helper	.midiToNoteStateMatrix(f))
            if np.array(song).shape[0] > 50:
                songs.append(song)
        except Exception as e:
            raise e           
    return songs

songs = get_songs('Dataset') #These songs have already been converted from midi to msgpack
print "{} songs processed".format(len(songs))

#Defining HyperParameters
note_low = helper.lowerBound
note_high = helper.upperBound
note_range = note_high - note_low

n_timestamps = 15
n_visible = 2*note_range*n_timestamps	#since the size of the song is 2*note_range*timestamps_in_song
n_hidden = 20

n_epochs = 200
#No of training examples that we are going to send at a time
batch_size = 50
lr = tf.constant(0.1, tf.float32)

inputt = tf.placeholder(tf.float32, [None, n_visible], name="inputt")
weight = tf.Variable(tf.random_normal([], 0.1), name="weight")
bias_hidden = tf.Variable(tf.zeros([1, n_hidden], tf.float32, name="bias_hidden"))
bias_visible = tf.Variable(tf.zeros([1, n_visible], tf.float32, name="bias_visible"))

def gibbs_sample(k=1):
 	 #Runs a k-step gibbs chain to sample from the probability distribution of the RBM 
    def gibbs_step(count, k, xk):
        #Runs a single gibbs step. The visible values are initialized to xk
        hk = sample(tf.sigmoid(tf.matmul(xk, weight) + bias_hidden)) #Propagate the visible values to sample the hidden values
        xk = sample(tf.sigmoid(tf.matmul(hk, tf.transpose(weight)) + bias_visible)) #Propagate the hidden values to sample the visible values
        return count+1, k, xk

    #Run gibbs steps for k iterations
    ct = tf.constant(0) #counter
    [_, _, inputt_sample] = control_flow_ops.while_loop(lambda count, num_iter, *args: count < num_iter,gibbs_step, [ct, tf.constant(k), inputt])
    #This is not strictly necessary in this implementation, but if you want to adapt this code to use one of TensorFlow's
    #optimizers, you need this in order to stop tensorflow from propagating gradients back through the gibbs step
    inputt_sample = tf.stop_gradient(inputt_sample) 
    return inputt_sample

def sample(probVec):
	'''
	Accepts a vector of probablities and
	Returns it in 0 and 1 form vector
	'''
	return tf.floor(probVec + tf.random_uniform(tf.shape(probVec),0,1))

#Get sample of inputt using gibbs sampling
inputt_sample = gibbs_sample()
#Sample of hidden nodes starting from generated inputt sample
h_sample = sample(tf.sigmoid(tf.matmul(inputt_sample,weight)+bias_hidden))
#Sample of hidden nodes starting from original inputt
h_original = sample(tf.sigmoid(tf.matmul(inputt,weight)+bias_hidden))

#Update weights ans bias Based upon inputt
size_bt = tf.cast(tf.shape(inputt)[0], tf.float32)
W_adder  = tf.mul(lr/size_bt, tf.sub(tf.matmul(tf.transpose(inputt), h_original), tf.matmul(tf.transpose(inputt_sample), h_sample)))
bv_adder = tf.mul(lr/size_bt, tf.reduce_sum(tf.sub(inputt, inputt_sample), 0, True))
bh_adder = tf.mul(lr/size_bt, tf.reduce_sum(tf.sub(h_original, h_sample), 0, True))
#When we do sess.run(updt), TensorFlow will run all 3 update steps
updt = [weight.assign_add(W_adder), bias_visible.assign_add(bv_adder), bias_hiddem.assign_add(bh_adder)]

with tf.Session() as sess:
	#Initialising all variables
	sess.run(tf.global_variables_initializer())
		
	#Training
	for epoch in tqdm.tqdm(range(n_epochs)):
		#for each epoch we go through entire dataset
		for song in songs:
			#Converting to numpy array and reshaping it to = n_examples * (2*note_range*timestamps_in_song)
			song = np.array(song)
			song = song[:np.floor(song.shape[0]/n_timesteps)*n_timesteps]
			song = np.reshape(song, [song.shape[0]/n_timesteps, song.shape[1]*n_timesteps])
			
			#training RBM on batch_size examples
			for i in range(1, len(song), batch_size):
				x_batch = song[i:i+batch_size]
				sess.run(updt, feed_dict={inputt: x_batch}) 
	#Now the model is trained hence
	#Generate Music
	sample = gibbs_sample().eval(session=sess, feed_dict={x: np.zeros((10, n_visible))})
	for i in range(sample.shape[0]):
		if not any(sample[i,:]):
			continue
		  
			#Saving the generated music
			S = np.reshape(sample[i,:], (n_timesteps, 2*note_range))
			helper.noteStateMatrixToMidi(S, "generated_chord_{}".format(i))

