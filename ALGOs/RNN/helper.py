import math
import random

# 1D dot
def dot(a, b):
	ans = [ a[i]*b[i] for i in range(len(a)) ]
	return [sum(ans)]

# 2D random array
def dot_2D(a, b):
	matrix = []
	for i in range(len(a)):
		row = []
		for j in range(len(b[0])):
			element = sum( [a[i][k]*b[k][j] for k in range(len(a[0]))] )
			row.append(element)
		matrix.append(row)	
	
	return matrix
	
	
def tanh_(x):
	return math.tanh(x)
	
	
def tanh_2D(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			matrix[i][j] = tanh_(matrix[i][j])
			
	return matrix
	

def tanh(matrix):
	return [tanh_(x) for x in matrix]
	

# 2D random array
def random_2D(n_rows, n_cols):
	ans = []
	for i in range(n_rows):
		ans.append([ random.random() for j in range(n_cols) ])
	
	return ans

# 1D random array
# Here n_cols = 1
def random_(n_rows, n_cols):
	return [ random.random() for j in range(n_rows) ]
	

def add(a,b,c):
	ans = [a[i]+b[i]+c[i] for i in range(len(a))]
	return ans

