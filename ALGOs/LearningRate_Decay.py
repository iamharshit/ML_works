#1.
class LR_LinearDecay():
   '''
   Function : -Learning rate decay linearly(a constant factor) after each epoch
              -Eg. LR= 5, 5.8, 5.6, 5.4, ........  
   '''
   def __init__(self, min_lr=1e-5, max_lr=1e-2, epochs=None):
        super().__init__()
        
        self.min_lr           = min_lr
        self.max_lr           = max_lr
        self.total_iterations = epochs
        
   def get_lr(self, epoch_i):
        '''Return the updated learning rate.'''
        self.iteration = epoch_i
        x              = self.iteration / self.total_iterations 

        return self.max_lr - (self.max_lr-self.min_lr) * x





#2.
class LR_StepDecay():
   '''
   Function : -Learning rate decay stepwise(a varing factor) after every few epochs
              - Eg. LR= 5, 5, 5, 2.5, 2.5, 2.5, 1.25, 1.25, 1.25, ...... 
   '''
   def __init__(self, max_lr=1e-2, step_size=3, decay_factor=2):
        super().__init__()
        
        self.max_lr           = max_lr
        self.step_size        = step_size   # meaning: update happens after every `step_size` iterations 
        self.decay_factor     = decay_factor
        
   def get_lr(self, epoch_i):
        '''Return the updated learning rate.'''
        self.iteration  = epoch_i
        x               = self.iteration / self.step_size
        
        return self.max_lr / (self.decay_factor ** int(x) )





#3.
class LR_ExponentialDecay():
   '''
   Function : Learning rate decay exponentially( exp(k*t) ) after each epoch
   '''
   def __init__(self, max_lr=1e-2, decay_factor=0.1):
        super().__init__()
        
        self.max_lr           = max_lr
        self.decay_factor     = decay_factor
        
   def get_lr(self, epoch_i):
        '''Return the updated learning rate.'''
        return self.max_lr / math.exp(self.decay_factor*epoch_i ) 





#4.
class LR_Cyclical():
    '''
    Function - This implements 2 techniques: 1.Linear annealing(to better converge at minima)
                                             2.Learning rate linear restart(to escape local minima)
    '''
    def __init__(self, min_lr=1e-5, max_lr=1e-2, step_size=10, mode='triangular', gamma=1., scale_fn=None, scale_mode='cycle'):
        super(CyclicLR, self).__init__()
        import math

        self.min_lr     = min_lr
        self.max_lr     = max_lr
        self.step_size  = step_size
        self.mode       = mode
        
        if scale_fn == None:
            if(self.mode == 'triangular'):
                self.scale_fn     = lambda x: 1.
            elif(self.mode == 'triangular2'):
                self.scale_fn     = lambda x: 1/(2.**(x-1))
            elif(self.mode == 'exp_range'):
                self.scale_fn     = lambda x: gamma**(x)
        else:
            self.scale_fn         = scale_fn
        
    def get_lr(self, epoch_i):
        cycle = math.floor(1 + epoch_i/(2*self.step_size))
        x     = math.abs  (epoch_i/self.step_size - 2*cycle + 1)
        
        return self.base_lr + (self.max_lr-self.min_lr) * (1-x) * self.scale_fn(cycle)

		



#5.
class LR_StochasticGradientDescentWithWarmRestarts():
    '''
    Function - This implements 2 techniques: 1.Cosine annealing(to better converge at minima)
                                             2.Learning rate sharp restart(to escape local minima)
    '''
    def __init__(self, min_lr, max_lr, epoch_steps=10):

		self.min_lr              = min_lr
		self.max_lr              = max_lr

		self.epoch_steps         = epoch_steps         # restarts after every `epoch_steps` no. of epochs

		self.batch_since_restart = 0
        
    def get_lr(self, epoch_i):
		'''Calculate the learning rate.'''
		self.batch_since_restart   = epoch_i % epoch_steps
		fraction_to_restart        = self.batch_since_restart / (epoch_steps)
		
		return self.min_lr + 0.5 * (self.max_lr - self.min_lr) * (1 + np.cos(fraction_to_restart * np.pi))







'''
Example.

>> epoch_n = 50
>> lr = LR_LinearDecay(epochs = epoch_n)
>> for epoch_i in range(1,epoch_n+1):
        learning_rate = lr.get_lr(epoch_i = epoch_i )   
'''
