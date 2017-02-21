import theano
import theano.tensor as T
from helper import activations 
from helper import misc,updates
from scipy.stats import gaussian_kde
from matplotlib import pyplot as plt
from matplotlib.pyplot import *
'''
from foxhound import activations
from foxhound import updates
'''
from helper import inits

from helper.theano_utils import floatX, sharedX

#defining parameters
sz=2048
nh=2048
leaky_rectify = activations.leaky_rectify()
rectify = activations.Rectify()
tanh = activations.Tanh()
sigmoid = activations.Sigmoid()
bce = T.nnet.binary_crossentropy
batch_size = 128
init_fn = misc.Normal(scale=0.02)

#returns the probability of X to be choosed if gaussian distribution followed	
def gaussian_probability(X, u=0., s=1.):
	return (1./(s*np.sqrt(2*np.pi)))*np.exp(-(((X - u)**2)/(2*s**2)))

def scale_and_shift(X, g, b):
	return X*g + b

#defining Generator(G) network as multilayer perceptron
def G(X, w1, g1, b1, w2, g2, b2, w3):
	h1 = leaky_rectify(scale_and_shift(T.dot(X,w1), g1, b1))
	h2 = leaky_rectify(scale_and_shift(T.dot(h1,w2), g2, b2))
	y = T.dot(h2, w3)
	return y

#defining Discriminator(D) network as multilayer perceptron
def D(X, w1, g1, b1, w2, g2, b2, w3):
	h1 = leaky_rectify(scale_and_shift(T.dot(X,w1), g1, b1))	
	h2 = tanh(scale_and_shift(T.dot(h1,w2), g2, b2))
	y = sigmoid(T.dot(h2,w3))
	return y

#initialise parameters for G and D
g_w1 = init_fn((1, nh))
g_g1 = inits.Normal(1., 0.02)(nh)
g_b1 = inits.Normal(0., 0.02)(nh)
g_w2 = init_fn((nh, nh))
g_g2 = inits.Normal(1., 0.02)(nh)
g_b2 = inits.Normal(0., 0.02)(nh)
g_w3 = init_fn((nh, 1))
#ggy = inits.Constant(1.)(1)
#gby = inits.Normal(0., 0.02)(1)
d_w1 = init_fn((1, nh))
d_g1 = inits.Normal(1., 0.02)(nh)
d_b1 = inits.Normal(0., 0.02)(nh)
d_w2 = init_fn((nh, nh))
d_g2 = inits.Normal(1., 0.02)(nh)
d_b2 = inits.Normal(0., 0.02)(nh)
d_w3 = init_fn((nh, 1))
#dgy = inits.Normal(1., 0.02)(1)
#dby = inits.Normal(0., 0.02)(1)

#defining input 
Z = T.matrix()
X = T.matrix()

#building generator, "gen" stores the output of generator layer
gen = G(Z, g_w1, g_g1, g_b1, g_w2, g_g2, g_b2, g_w3 )

#getting the probability for real ang generated data
prob_real = D(X, d_w1, d_g1, d_b1, d_w2, d_g2, d_b2, d_w3)
prob_gen  = D(gen, d_w1, d_g1, d_b1, d_w2, d_g2, d_b2, d_w3)

#cost calculation for G and D
g_cost = T.nnet.binary_crossentropy(prob_gen, T.ones(prob_gen.shape)).mean()
d_real_cost = T.nnet.binary_crossentropy(prob_real, T.ones(prob_gen.shape)).mean()
d_gen_cost = T.nnet.binary_crossentropy(prob_gen, T.zeros(prob_gen.shape)).mean()
d_cost = d_real_cost + d_gen_cost

#all costs summarized in one list
cost = [g_cost, d_cost, d_real_cost, d_gen_cost]

#using Adam optimizer
learning_rate= 0.001
g_updater = updates.Adam(lr=sharedX(learning_rate) )
d_updater = updates.Adam(lr=sharedX(learning_rate) )

g_update = g_updater([g_w1, g_g1, g_b1, g_w2, g_g2, g_b2, g_w3 ], g_cost)
d_update = d_updater([d_w1, d_g1, d_b1, d_w2, d_g2, d_b2, d_w3 ], d_cost)

#interconversion between variable and function
train_g = theano.function([X, Z], cost, updates=g_update)
train_d = theano.function([X, Z], cost, updates=d_update)
_gen = theano.function([Z], gen)
_score = theano.function([X], prob_real)

# visualising G and D
def visualise(i):
	fig = plt.figure()
	
	#generatiing distribution	
	x = np.linspace(-5, 5, 500).astype('float32')
	z = np.linspace(-1, 1, 500).astype('float32')
	y_true = gaussian_probability(x)	
	kde = gaussian_kde(_gen(z.reshape(-1,1)).flatten())
	y_gen = kde(x)
	preal = _score(x.reshape(-1, 1)).flatten()	

	#plotting distribution
	plt.clf()
	plt.plot(x, y_true, '--', lw=2)
	plt.plot(x, y_gen, lw=2)
	plt.plot(x, preal, lw=2)

	plt.xlim([-5.,5.])
	plt.ylim([0.,1.])
	plt.ylabel('Probability--> ')
	plt.xlabel('X --> ')
	plt.legend(['Training Data', 'Generated Data', 'Discriminator'])
	plt.title('GAN learn Gaussian distibution | Generation: '+str(i))
	
	#fig.canvas.draw()
	#plt.show()
	#show()
	plt.savefig("fig"+str(i)+".png")

#Training G and N for 50 generations
for i in range(100):
	x = np.random.normal(1, 1, size=(batch_size, 1)).astype('float32')
	y = np.random.uniform(-1, 1, size=(batch_size, 1)).astype('float32')	
	if i%5==0:	
		train_g(x, y)
		print "Generation = ",str(i)		
		visualise(i)
	else:
		train_d(x, y)
