import tweepy
from textblob import TextBlob
from sys import argv
import urllib2
import json

query = 'Narendra Modi'

def twitter_sentiment_analyser():
	consumer_key = 'WVXJlr2qElRUOpDv467v6U5Il'
	consumer_secret = 'b52Jv3G7Dzqdtxa92QhnB55ffV1m4VBDzk9vFfxzwjxNW9bLwa'
	access_token = '463718527-Dr4R2wSBKWgBIqYcjMETlzw21Zj28Ix4maw6gCUe'
	access_token_secret = '6QZopWCLd63qfR4GAjcD3IGT2Df2ut4s5CtAGo8EllLMI'

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
   	access_token = 'EAACEdEose0cBALgrzi8itRLrTUwuaEwRRckMqskMTuso5swLWA5LxT2i839toK7DwOEiK243XhJP82wVA2QIbscWzxAHJTwDMS80hr3ezwmY21Q31mhXH8H5DeLaoPgqrokaZC7FYEm0ZA15mTL6TZAzQQ2mB9nOu5D6V8xOAZDZD'

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
