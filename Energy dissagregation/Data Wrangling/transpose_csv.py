'''
#Time consuming method
import csv

#with open('HF_new.csv', 'wb') as fnew:
with open('HF_transpose.csv', 'wb') as fnew:
	writer = csv.writer(fnew)
	for i in range(81001):
		with open('HF.csv') as f:
			l=[]
			reader = csv.reader(f)
			for row in reader:
				l.append(row[i])
			writer.writerow(l)

'''
import pandas as pd
import csv
import numpy as np


#Tranposing each chunk and Saving it
chunksize = 500
iteration = 0
l = ['HF_1.csv','HF_2.csv','HF_3.csv','HF_4.csv','HF_5.csv','HF_6.csv','HF_7.csv','HF_8.csv','HF_9.csv']
print '....started.....'

for chunk in pd.read_csv('HF.csv', chunksize=chunksize):
	name = l[iteration]
	fd = open(name, 'w')	
	f = csv.writer(fd,delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

	np.savetxt(name, chunk.as_matrix().T, delimiter=",",  fmt='%i')
	#chunk.as_matrix().tofile(name, sep=',', format='%d')
	#chunk.as_matrix().savez(name)

	print iteration
	iteration+=1
	fd.close()

#========================================================================================
#Joining all the files
fw = open('HF_transpose.csv','a')
writer = csv.writer(fw, delimiter=',', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')

fr1 = open('HF_1.csv','rb')
reader1 = csv.reader(fr1, delimiter=',')
fr2 = open('HF_2.csv','rb')
reader2 = csv.reader(fr2, delimiter=',')
fr3 = open('HF_3.csv','r')
reader3 = csv.reader(fr3, delimiter=',')
fr4 = open('HF_4.csv','r')
reader4 = csv.reader(fr4, delimiter=',')
fr5 = open('HF_5.csv','r')
reader5 = csv.reader(fr5, delimiter=',')
fr6 = open('HF_6.csv','r')
reader6 = csv.reader(fr6, delimiter=',')
fr7 = open('HF_7.csv','r')
reader7 = csv.reader(fr7, delimiter=',')
fr8 = open('HF_8.csv','r')
reader8 = csv.reader(fr8, delimiter=',')
fr9 = open('HF_9.csv','r')
reader9 = csv.reader(fr9, delimiter=',')

for row1 in reader1:
	for row2 in reader2:
		for row3 in reader3:
			for row4 in reader4:
				for row5 in reader5:
					for row6 in reader6:
						for row7 in reader7:
							for row8 in reader8:
								for row9 in reader9:
									print row1,row2,row3,row4,row5,row6,row7,row8,row9
									writer.writerow(row1+row2+row3+row4+row5+row6+row7+row8+row9)
									break
								break
							break
						break
					break
				break
			break
		break

fw.close()
print '...completed....'