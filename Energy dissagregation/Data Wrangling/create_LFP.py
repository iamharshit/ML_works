import numpy as np
import time
import csv

y1 = np.genfromtxt('LF2V.csv', delimiter=',',dtype=str)
y2 = np.genfromtxt('LF2I.csv', delimiter=',',dtype=str)
timestamp = np.genfromtxt('TimeTicks1.csv', delimiter=',',dtype=np.int)

#base = np.array([169.306647511, 2.88084968399e-05, 0.59951967656, 3.05860023276e-05, 0.797017596535, 5.15186842957e-05])

#finding the absolute values
print '----started---------'
for i in range(y.shape[0]):
    for j in range(y.shape[1]):
		#y[i][j] = np.angle(complex(y[i][j].replace('i', 'j')), deg=True )
        y1[i][j] = round(np.absolute(complex(y1[i][j].replace('i', 'j')) * complex(y2[i][j].replace('i', 'j')) ),2)
    if (i%100000 == 0):
        print '1 lakh rows completed'

y = np.array(y, dtype=np.float32)

#save 2D numpy array as csv file
np.savetxt("LF2P_new.csv", y, delimiter=",")

print '----completed---------'