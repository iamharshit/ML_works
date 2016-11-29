import os
import pandas as pd
from KaggleWord2VecUtility import KaggleWord2VecUtility # for removing stopwords
from sklearn .feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sys import argv
import requests
from bs4 import BeautifulSoup

if __name__=='__main__':

	# ----------------Rotten Tomatoes Scrapper------------
	movie_name = argv[1].lower()
	r=requests.get('https://www.rottentomatoes.com/m/'+movie_name+'/reviews')
	soup=BeautifulSoup(r.content,'html.parser')
	reviews = soup.find_all("div", { "class" : "the_review" })
	if not reviews:
		print 'Please Check the Movie Name "'+ +'"movie_name'
		exit(1)
	
	
	# ----------------Sentiment Analyser------------------
	# Reading the training and test data
	train_data = pd.read_csv(os.path.join(os.path.dirname(__file__),'data','labeledTrainData.tsv'), header=0, delimiter='\t', quoting=3 )
	test_data = pd.read_csv(os.path.join(os.path.dirname(__file__),'data','testData.tsv'), header=0, delimiter='\t', quoting=3 )
	
	# Cleaning train_data 	 
	# nltk.download() # if you havenot downloaded the nltk corpus
	clean_train_data = []
	for i in range(0, len(train_data['review']) ):
		clean_train_data.append(' '.join(KaggleWord2VecUtility.review_to_wordlist(train_data['review'][i],True) ))
	
	# Creating bag of words
	vectorizer = CountVectorizer(analyzer='word', tokenizer=None, preprocessor=None, stop_words=None, max_features=5000)
	
	# word vs freauency
	train_data_features = vectorizer.fit_transform(clean_train_data)
	train_data_features = train_data_features.toarray()
	
	# Training Random Forest Classifier	
	clf = RandomForestClassifier()
	clf = clf.fit(train_data_features, train_data['sentiment'])

	'''
	# calculating accuracy over test_data
	clean_test_data = []
	for i in range(0, len(test_data['review']) ):
		clean_test_data.append(' '.join(KaggleWord2VecUtility.review_to_wordlist(test_data['review'][i],True) ))
 	test_data_features = vectorizer.transform(clean_test_data).toarray()
 	prediction = clf.predict(test_data_features)
 	acc = clf.score(prediction, test_data['sentiment'])
 	print acc
	''' 	

 	# ----------------Prediction-------------------
	score = 0 
	for review in reviews:
		prediction = clf.predict(review.get_text())
		if prediction:
			score+=1
		else:
			score-=1
	if score>0:
		print 'The Movie has got a GOOD review overall.'
	else:
		print 'The Movie has got a BAD review overall.'
