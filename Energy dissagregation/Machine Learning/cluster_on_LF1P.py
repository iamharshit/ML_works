import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
import csv

#converting dataset into numpy array
X = np.genfromtxt('LF1P.csv', delimiter=',',dtype=np.float_)

#Estimating Bandwidth and fiting the clusterer on the dataset
bandwidth = estimate_bandwidth(X[:518940], n_samples=10000)

cltr = MeanShift(bandwidth=bandwidth, bin_seeding=True)
cltr.fit(X[:518940])

labels = cltr.labels_

#Printing unique lables and Getting frequency of each label
labels_unique = np.unique(labels)
print 'Total unique labels = ',labels_unique	

t = [0]*len(labels_unique)
for i in labels:
	t[i]+=1

for i in range(len(t)):
	print 'label=',i,'  frequency=',t[i]

#Putting all the labels in csv file so that it is easier for visualisation
net = []
i=0
while i<len(labels):
	temp = labels[i:i+20]
	net.append(temp)
	i+=20

with open('cluster_result.csv','w') as f:
	writer = csv.writer(f, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
	for row in net:
		writer.writerow(row)
