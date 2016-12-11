'''
Generating Static Heatmap with 1000 range on y axis
'''
import numpy as np
import numpy.random
import matplotlib.pyplot as plt
import csv
import pandas as pd


chunksize = 1000
print '....started.....'

x=0
i=52500
for chunk in pd.read_csv('HF_transpose.csv', chunksize=chunksize):
	print 'At '+str(x)+' th row'
	if x>=i:
		pass
	else:
		x+=1000
		continue

	intensity = chunk.as_matrix()

	x = np.arange(1, 4095+1, 1)
	y = np.arange(x+1.066, x+(intensity.shape[0]+1)*1.066, 1.066)
	#print x.shape
	#print y.shape
	
	plt.xlim(1, 4096)
	plt.ylim(x+1, x+int((intensity.shape[0]+1)*1.066) )
	
	plt.pcolormesh(x, y, intensity)
	plt.colorbar()
	plt.show()
	#i+=chunksize
	break

print '....completed....'