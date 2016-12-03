import tweepy
from textblob import TextBlob
import csv
from keras.models import Sequential
from keras.layers import Dense, LSTM

#inserting API keys
consumer_key = ' '
consumer_secret = ' '
access_token = ' '
access_token_secret = ' '
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#doing sentiment analysis
tweets = api.search('Apple')
threshold = 0
pos_sentiment = 0 
neg_sentiment = 0 
for tweet in tweets:
	analysis = TextBlob(tweet.text)
	if analysis.sentiment.polarity>=threshold:
		pos_sentiment += 1
	else:
		neg_sentiment += 1
if(pos_sentiment>neg_sentiment):
	print 'Overall Positive'
else:
	print 'Overall Negative'

#reading data
dates = []
prices = []
with open('aapl.csv', 'r') as f:
	csv_f = csv.reader(f)
	f.next()
	for row in csv_f:
		dates.append(int(row[0].split('-')[0]) )
		prices.append(float(row[1]))

trainX = dates[:0.8*len(dates)]
trainY = prices[:0.8*len(prices)]
testX = dates[0.8*len(dates):]
testY = prices[0.8*len(prices):] 

#fitting model
model = Sequential()
mmodel.add(Dense(32,input_dim=1,init='uniform',activation='relu'))
model.add(Dense(16,init='uniform',activation='relu'))    
model.add(Dense(1,init='uniform',activation='relu'))
model.compile(loss='mean_squared_error',optimizer='adam',metrics=['accuracy'])
model.fit(TrainX,TrainY,nb_epoch=100,batch_size=3,verbose=1)

#prediction
print model.predict([23]) #23 december
