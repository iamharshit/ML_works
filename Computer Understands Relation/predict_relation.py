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

def predict_next(words):
	for word in words:
		#the unknown word is the ans
		if word not in word2vec:
			return "Sorry, Unable to understand '"+word+"'"

	#vector of the predicted word
	predicted_vec = word2vec[words[2]]/np.linalg.norm(word2vec[words[2]]) - ( word2vec[words[0]]/np.linalg.norm(word2vec[words[0]]) - word2vec[words[1]]/np.linalg.norm(word2vec[words[1]]) )
	dist_from_predicted_vec = [np.linalg.norm( vec/np.linalg.norm(vec)-predicted_vec ) for vec in word2vec.values()]

 	#sometimes it gives the input word as ans because of low distances 
	ans = word2vec.keys()[np.argmin(dist_from_predicted_vec)]
	while ans in words:
		dist_from_predicted_vec[np.argmin(dist_from_predicted_vec)]=dist_from_predicted_vec[np.argmax(dist_from_predicted_vec)]
		ans = word2vec.keys()[np.argmin(dist_from_predicted_vec)]

	return 'Answer: '+ans
																																																												 

#load the word2vec model in dictionary
print 'Loading word2vec....'
load_vectors()
while(1):
	words = raw_input('>>>Enter words: ').lower().split('::')
	words = words[0].split(':')+[words[1][:-1]]
	print predict_next(words)
	print ''

