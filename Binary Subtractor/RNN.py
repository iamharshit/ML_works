import numpy as np 
import copy

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_derivative(x):
    return x*(1-x)

# defining constants
binary_dim = 8
input_dim = 2
hidden_dim = 16
output_dim = 1
alpha = 0.1

num_max = pow(2,binary_dim)
int2binary = np.unpackbits(np.array([range(num_max)], dtype=np.uint8).T, axis=1)

# initialising synapses
np.random.seed(1)
synapses_0 = 2*np.random.random((input_dim, hidden_dim))-1
synapses_1 = 2*np.random.random((hidden_dim, output_dim))-1
synapses_h = 2*np.random.random((hidden_dim, hidden_dim))-1

synapses_0_update = np.zeros_like(synapses_0)
synapses_1_update = np.zeros_like(synapses_1)
synapses_h_update = np.zeros_like(synapses_h)

# training
for j in range(10000):
    num1_int = np.random.randint(num_max/2,num_max)
    num1 = int2binary[num1_int]

    num2_int = np.random.randint(0,num_max/2)
    num2 = int2binary[num2_int]

    ans_int = num1_int - num2_int
    ans = int2binary[ans_int]

    d = np.zeros_like(ans)

    layer_1_values = list()
    layer_1_values.append(np.zeros(hidden_dim))

    layer_2_deltas = list()

    overallError = 0

    # front propagation for all the bits
    for position in range(8):
        X = np.array([[num1[binary_dim-1-position], num2[binary_dim-1-position]]])
        Y = np.array([[ans[binary_dim-1-position] ]]).T

        layer_1 = sigmoid(np.dot(X,synapses_0) + np.dot(layer_1_values[-1],synapses_h))
        layer_2 = sigmoid(np.dot(layer_1,synapses_1))

        layer_2_error = Y - layer_2
        overallError += np.abs(layer_2_error[0])
        layer_2_deltas.append((layer_2_error)*sigmoid_derivative(layer_2))

        layer_1_values.append(copy.deepcopy(layer_1))

        d[8-position-1] = np.round(layer_2[0][0])

    # back propagation
    new_layer_1_delta = np.zeros(hidden_dim)
    for position in range(8):
        X = np.array([[num1[position], num2[position] ]])
        layer_1 = layer_1_values[-position-1]
        prev_layer_1 = layer_1_values[-position-2]

        layer_2_delta = layer_2_deltas[-position-1]
        layer_1_delta = (np.dot(new_layer_1_delta, synapses_h.T) + np.dot(layer_2_delta, synapses_1.T))*sigmoid_derivative(layer_1)

        synapses_1_update += np.atleast_2d(layer_1).T.dot(layer_2_delta)
        synapses_h_update += np.atleast_2d(prev_layer_1).T.dot(layer_1_delta)
        synapses_0_update += X.T.dot(layer_1_delta)

        new_layer_1_delta = layer_1_delta
    

    synapses_0 += synapses_0_update * alpha    
    synapses_1 += synapses_1_update * alpha
    synapses_h += synapses_h_update * alpha

    synapses_0_update *= 0
    synapses_1_update *= 0
    synapses_h_update *= 0
    
    # performance analysis
    if(j%1000 == 0):
        print 'Error= '+str(overallError)
        output = 0
        for index,x in enumerate(reversed(d)):
            output += x*pow(2,index)
        print str(num1_int) + ' - ' + str(num2_int) + ' = ' + str(output)
        print '------------------'        
input()