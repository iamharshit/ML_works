import matplotlib.pyplot as plt
import numpy as np
import time
import csv
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#opening csv file into a numpy array
X = np.genfromtxt('LF1P_new.csv', delimiter=',',dtype=np.float_)
'''
#for combine training 
X1 = np.genfromtxt('LF1P_new.csv', delimiter=',',dtype=np.float_)
X2 = np.genfromtxt('LF2P_new.csv', delimiter=',',dtype=np.float_)
X = np.array(zip(X2.ravel(),X2.ravel()), dtype=('f8,f8')).reshape(X2.shape)
'''

taggedinfo = np.genfromtxt('TaggingInfo.csv', delimiter=',',dtype=np.float_)
y = np.array([0]*518945)

timeticks = np.genfromtxt('TimeTicks1.csv', delimiter=',',dtype=np.float_)

#fitting the KNN classifier
initial=0
for i in range(taggedinfo.shape[0]):
	k=0
	while initial<518944:
		if timeticks[initial]>=taggedinfo[i][2] and timeticks[initial]<=taggedinfo[i][3]:
			y[initial] = i+1
		if timeticks[initial]>taggedinfo[i][3]:
				break
		initial+=1

clf =  KNeighborsClassifier(n_neighbors=3)	
clf.fit(X[:518940],y[:518940])

#predicting the predicted result and the actual result
print X[331546].reshape(1,-1)
print clf.predict(X[331200].reshape(1,-1)) ,y[331200]
print clf.predict(X[333978].reshape(1,-1)) ,y[333978]
print clf.predict(X[334589].reshape(1,-1)) ,y[334589]
print clf.predict(X[336741].reshape(1,-1)) ,y[336741]
print clf.predict(X[339935].reshape(1,-1)) ,y[339935]
print clf.predict(X[340345].reshape(1,-1)) ,y[340345]
print clf.predict(X[344440].reshape(1,-1)) ,y[344440]

#getting the accuracy
lower = 218000
upper = 219000
y_pred = np.array([0]*518940)

for i in range(lower,upper):
	y_pred[i] = clf.predict(X[i].reshape(1,-1))

print accuracy_score(y_pred[lower:upper], y[lower:upper])