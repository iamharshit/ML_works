'''
* Simple 2D Matrix Factorization/Matrix Decomposition done by using Gradient descent.  
* Here it is used to find the missing values in the original matrix
* Reason: Numpy isn't used here - so as to make the code independent of any dependencies
'''

class MatrixDecomposition:
    def __init__(self, lr=0.0002, k=2, steps=5000, beta=0.02, garbage=0):
        self.lr    = lr
        self.k     = k
        self.steps = steps
        self.beta = beta
        self.garbage = garbage

    def transpose(self, matrix):
        return zip(*matrix)


    # Total Error = (Actual-Predicted) + Regularisation error
    def get_error(self, R_actual, P, Q):
        error = 0
        for i in range(len(P)):
            for j in range(len(Q[0])):
                actual = R[i][j]
                if actual!=self.garbage:
                    pred = 0
                    for k in range(self.k):
                        pred += P[i][k]*Q[k][j]
                        error += (self.beta/2) *(pow(P[i][k],2) + pow(Q[k][j],2))
                    error += pow(actual - pred, 2)

        return error


    def update_coeffiecients(self, R_actual, R_pred, P, Q):
        for i in range(len(P)):
            for j in range(len(Q[0])):
                if R_actual[i][j] != self.garbage:
                    eij = R_actual[i][j]-R_pred[i][j]
                    for k in range(self.k):
                        P[i][k] -= self.lr*( 2*eij*(-Q[k][j]) + self.beta*P[i][k] )
                        Q[k][j] -= self.lr*( 2*eij*(-P[i][k]) + self.beta*Q[k][j] ) 
        return P,Q


    def column(self, matrix, index):
        return [matrix[i][index] for i in range(len(matrix))]
    

    def prod_2D(self, P, Q):
        R_pred = []
        for _ in range(len(P)):
            R_pred.append( [0]*len(Q[0]) )
        for i in range(len(P)):
                for j in range(len(Q[0] )):
                    R_pred[i][j] = sum([P[i][k_]*Q[k_][j] for k_ in range(self.k)])
        return R_pred


    def random_matrix(self, n_row, n_col):
        import random
        ans = []
        for i in range(n_row):
            ans.append([random.random() for j in range(n_col)])
        return ans

    # Main Function
    def decompose(self, R_actual):
        P = self.random_matrix(len(R_actual), self.k           )
        Q = self.random_matrix(self.k,        len(R_actual[0]) )

        R_pred = self.prod_2D(P, Q)
        threshold = 0.01
        error = self.get_error(R_actual, P, Q); 
        steps=0
        while abs(error)>threshold and steps<self.steps:
            P,Q = self.update_coeffiecients(R_actual, R_pred, P, Q)
            R_pred = self.prod_2D(P, Q)         
            error = self.get_error(R_actual, P, Q);
            steps+=1
        return R_pred

    
G = 0 #garbage value

R = [[5, 3, G, 1],
     [4, G, G, 1],
     [1, 1, G, 5],
     [1, G, G, 4],
     [G, 1, 5, 4]
    ]

R_pred = MatrixDecomposition(garbage=G).decompose(R)

print R_pred
'''
Output:
[[5,   2.9, 4.7, 0.9],
 [3.9, 2.3, 3.8, 0.9],
 [1,   0.8, 4.9, 4.9],
 [0.9, 0.7, 4,   3.9],
 [1.9, 1.3, 4.9, 4  ]
]

'''
