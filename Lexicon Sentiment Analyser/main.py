import pandas as pd
import os
from KaggleWord2VecUtility import KaggleWord2VecUtility 

if __name__=='__main__':
	# Reading training and testing data
	data = pd.read_csv(os.path.join(os.path.dirname(__file__),'data','labeledTrainData.tsv'), header=0, delimiter='\t', quoting=3 )
	train_data = data[:data.shape[0]/2]
	test_data = data[data.shape[0]/2:]
	
	# Removing stop words
	clean_train_data = []
	for i in range(0, len(train_data['review']) ):
		clean_train_data.append(' '.join(KaggleWord2VecUtility.review_to_wordlist(train_data['review'][i],True) ))
	clean_test_data = []
	for i in range(0, len(test_data['review']) ):
		clean_test_data.append(' '.join(KaggleWord2VecUtility.review_to_wordlist(test_data['review'][data.shape[0]/2+i],	True) ))
	
	# Reading Lexicons
	df = pd.read_csv('data/AFINN-111.txt', delimiter='\t')
	lexicon_dict = dict(zip(df['WORD'],df['SENTIMENT'] ))

	correct_ness = 0
	for para,label in zip(clean_test_data,test_data['sentiment']):
		sentiment_sum = 0		
		for word in para.split(' '):
			sentiment_sum +=lexicon_dict.get(word,0)
		prediction = int(sentiment_sum>0)
			
		correct_ness += int(prediction==label)
	
	print 100.0*correct_ness/test_data.shape[0] #70% accuracy 
	
	print '\a'
