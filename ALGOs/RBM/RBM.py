import numpy as np

class RBM:
	def __init__(self, n_visible, n_hidden, learning_rate=0.1):
		self.n_visible = n_visible
		self.n_hidden = n_hidden
		self.learning_rate = learning_rate	

		#Random Initialisation of weights for synapse#1
		self.weights = 0.1*np.random.randn(n_visible, n_hidden)
		
		#Weights for Bias inserted in the first row and first column
		self.weights = np.insert(self.weights, 0, 0, axis=0)
		self.weights = np.insert(self.weights, 0, 0, axis=1)

	def train(self, data, max_iterations=100):
		n_examples = data.shape[0]
		
		#first column filled with 1 as a Bias unit
		data = np.insert(data, 0, 1, axis=1)
				
		#Training iterations
		for _ in range(max_iterations):
			#Forward Propagation phase
			hidden_abs_value = np.dot(data, self.weights)
			hidden_probs = self.logistic(hidden_abs_value)
			hidden_state = hidden_probs > np.random.rand(n_examples, self.n_hidden+1)
			
			pos_associations = np.dot(data.T, hidden_probs)			

			#Reconstruction phase		
			visible_abs_value = np.dot(hidden_state, self.weights.T)
			visible_probs = self.logistic(visible_abs_value)
			visible_probs[:,0] = 1 #Bias Unit
			
			neg_hidden_abs_value = np.dot(visible_probs, self.weights)
			neg_hidden_probs = self.logistic(neg_hidden_abs_value)

			neg_associations = np.dot(visible_probs.T, neg_hidden_probs)

			#Update Weigths using Gradient Descend
			self.weights += self.learning_rate*(pos_associations-neg_associations)/n_examples 
			
			#error = np.sum((data-visible_probs)**2)
		#	print "Iteration %s: Error is %s"%(_,error)

	def run_visible(self, data):
		'''
		Accepts input data at the visible layer and 
		Returns a matrix representing the state of hidden layer. 
		'''
		n_examples = data.shape[0]
		
		hidden_states = np.ones((n_examples, self.n_hidden+1))
		
		#Bias Unit
		data = np.insert(data, 0, 1, axis=1)
		
		hidden_abs_value = np.dot(data, self.weights)
		hidden_probs = self.logistic(hidden_abs_value)
		hidden_states[:,:] = hidden_probs > np.random.rand(n_examples, self.n_hidden+1)
		
		hidden_states = hidden_states[:,1:]
		return hidden_states

	def run_hidden(self, data):
		'''
		Accepts a matrix with rows consisting of the hidden units ans
		Returns a matrix representing the state of the visible layer 
		'''
		n_examples = data.shape[0]
		
		#Bias Unit
		data = np.insert(data, 0, 1, axis=1)

		visible_abs_value = np.dot(data, self.weight.T)
		visible_prob = self.logistic(visible_abs_value)
		visible_state[:,:] = visible_prob > np.random.rand(num_examples, self.num_visible + 1)

		#Removing the Bias column
		visible_state = visible_state[:,1:]
		return visible_state 	

	def logistic(self, x):
		return 1.0/(1+np.exp(-x))

if __name__=='__main__':
	
	#example
	r = RBM(n_visible = 5, n_hidden = 3)
  	training_data = np.array([[1,1,1,0,1],[1,0,1,0,1],[0,1,1,1,0], [0,0,1,0,1]])
  	r.train(training_data, max_iterations = 5000)
  	print r.weights
	#analyse the weight distribution to identify latent features

