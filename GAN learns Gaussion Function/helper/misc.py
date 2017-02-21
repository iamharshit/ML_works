import numpy as np
from time import time
from sklearn.externals import joblib

import theano
import theano.tensor as T
from theano_utils import sharedX, floatX, intX
from rng import np_rng

class Normal(object):
    def __init__(self, loc=0., scale=0.05):
        self.scale = scale
        self.loc = loc

    def __call__(self, shape, name=None):
        return sharedX(np_rng.normal(loc=self.loc, scale=self.scale, size=shape), name=name)

class Constant(object):

    def __init__(self, c=0.):
        self.c = c

    def __call__(self, shape):
		  return sharedX(np.ones(shape) * self.c)
