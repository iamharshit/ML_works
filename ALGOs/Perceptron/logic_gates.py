#The input to the gate can only be 0 or 1
'''
Single Layer Perceptrons
'''
def AND_perceptron(x1,x2):
	w1, w2, t = 1, 1, 2
	return w1*x1 + w2*x2 >=t

def OR_perceptron(x1,x2):
	w1, w2, t = 1, 1, 1
	return w1*x1 + w2*x2 >=t

def AND_perceptron(x1):
	w1, t = -1, 0
	return w1*x1 >=t


'''
Multi Layer Perceptrons
'''
def XOR_perceptron(x1,x2):
	w1, w2, t = 1, 1, 0.5
	h_1_1 = (w1*x1 + w2*x2 >=t)		#layer:1 node:1

	w1, w2, t = -1, -1, -1.5
	h_1_2 = (w1*x1 + w2*x2 >=t)		#layer:1 node:2
	
	w1, w2, t = 1, 1, 1.5
	return w1*h_1_1 + w2*h_1_2 >=t  #layer:2 or output layer

print XOR_perceptron(0,0)
print XOR_perceptron(0,1)
print XOR_perceptron(1,0)
print XOR_perceptron(1,1)