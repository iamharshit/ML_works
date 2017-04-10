import numpy as np
import os

word2vec = {}

def load_vectors():
	dir_ = 'vectors' 
	for file_ in os.listdir(dir_): 
		temp_word2vec = {}		

		with open(dir_+'/'+file_) as f:
			if file_ == 'vectors0.txt':
				#skip the first line
				next(f)
			for line in f:
				line_list = line.replace('\r','').replace('\n','').split(' ')
				word = line_list[0]
				vector = np.array([float(i) for i in line_list[1:] if len(i)>1])
				#word2vec dict not used for faster insertion						
				temp_word2vec[word] = vector

		#update the original vector
		word2vec.update(temp_word2vec)

def get_odd(words):
	#getting vectors for each word
	vector_list = []
	for word in words:
		#the unknown word is the ans
		if word not in word2vec:
			return word
		#normalising the vectors
		vector_list.append(word2vec[word]/np.linalg.norm(word2vec[word]))
	
	#computing mean and normalising it
	mean = np.array(vector_list).mean(axis=0)
	mean = mean/np.linalg.norm(mean)

	#computing distances and returning the farthest dist
	#np.linalg.norm() return single value for whole vector
	dist_from_mean = [np.linalg.norm(v-mean) for v in vector_list]
	return words[np.argmax(dist_from_mean)]

#load the word2vec model in dictionary
print 'Loading word2vec....'
load_vectors()
while(1):
	words = raw_input('>>>Enter words: ').lower().split(' ')
	print 'Odd word: '+get_odd(words)
	print ''

