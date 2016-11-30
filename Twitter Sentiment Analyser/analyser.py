import tweepy
from textblob import TextBlob
from sys import argv
import urllib2
import json

query = argv[1]

def twitter_sentiment_analyser():
	consumer_key='<your-consumer-key>'
        consumer_secret='<your-consumer-secret>'
        access_token='<your-access-token>'
        access_token_secret='<your-access-token-secret>'        

	auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
	auth.set_access_token(access_token,access_token_secret)
	api=tweepy.API(auth)

	tweets = api.search(query)

	polarity = []
	for tweet in tweets:
		analysis = TextBlob(tweet.text)
		polarity.append(analysis.sentiment.polarity)

	if 1.0*sum(polarity)/len(polarity)>0:
		print 'People have overall POSITIVE views on '+query+' on Twitter.'
	else:
		print 'People have overall NEGATIVE views on '+query+' on Twitter.'

'''		
def facebook_sentiment_analyser():
   	access_token = ''

   	url = 'https://graph.facebook.com/search?access_token=' + access_token + 'q=' + query + '&type=post'
   	req = urllib2.Request(url)
   	response = urllib2.urlopen(req)
   	while response.getcode()!=200:
   		response = urllib2.urlopen(req)

   	data = json.loads(response.read())

   	polarity = []
   	for i in range(10):
   		post = data['data'][i]['message']
		analysis = TextBlob(post)
		polarity.append(analysis.sentiment.polarity)
	if 1.0*sum(polarity)/len(polarity)>0:
		print 'People have POSITIVE view on +'+query+' on Facebook.'
	else:
		print 'People have NEGATIVE view on +'+query+' on Facebook.'
   		
   		
'''

twitter_sentiment_analyser()
