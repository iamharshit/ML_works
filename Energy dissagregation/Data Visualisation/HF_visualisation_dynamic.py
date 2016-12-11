'''
Generating Dynamic Heatmap for HF dataset
'''
import matplotlib.pyplot as plt
import numpy as np
import time

# create the figure
fig = plt.figure()
ax = fig.add_subplot(111)

intensity = np.genfromtxt('output_1.1.csv', delimiter=',').T

#TimeTicksHF
timestamp = np.genfromtxt('TimeTicksHF.csv', delimiter=',',dtype=np.int)


plt.show(block=False)
#initial, final = 0, intensity.shape[0]/10
initial, final = 51834-500, 51834-500 + 200
#print initial, final
print intensity.shape[0]

#while final<=intensity.shape[0]:
while final<=52143+500:
	time.sleep(0.2)
	print 'intial= '+str(initial), '  final= '+str(final),' timestamp= ',timestamp[initial]
	if(timestamp[initial] >= 1334355690 and timestamp[initial] <= 1334356020):
		print '========= Washing Machine ========'

	ax.imshow(intensity[initial: final], aspect='auto')
	print intensity[initial: final]
    
	fig.canvas.draw()

	initial += 50
	final += 50