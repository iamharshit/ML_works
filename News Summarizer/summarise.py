import keras #for ML
from keras.models import Sequential
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from	collections import Counter #for tokenisation
import cPickle as pickle #for Data Processing

#Loading Data
with open('data/%s.pkl'%'vocabulary-embedding', 'rb') as fp:
	headings, descriptions, keywords = pickle.load(fp)

#Tokenizing text
def tokenize_text(para):
	count, tokens = Counter(word for line in para for word in line.split())
	return tokens, count

vocab, vocab_count = tokenize_text(headings + descriptions)

#Generating Word Embedding with GloVe
glovefile = 'data/glove.6B.100d.txt'
f = open(gloveFile,'r')
model = {}
for line in f:
    splitLine = line.split()
    word = splitLine[0]
    embedding = [float(val) for val in splitLine[1:]]
    model[word] = embedding
word_embeddings = model

#Building 3 stacked LSTM RNN model
def build_model(embedding):
	model = Sequential()
	model.add(Embedding(weights=[embedding], name='embedding_1'))
	for i in range(3):
		lstm = LSTM()
		model.add(lstm)
		model.add(Dropout(p_dense, name='droupout))
	model.add(Dense())
	model.add(Activation('softmax',name='activation'))
	return model

#Building Encoder RNN and Initialising it
encoder = build_model(word_embeddings)
encoder.compile(loss='categorical_crossentropy', optimizer='rmsprop')
encoder.save_weights('embedding.pkl', overwrite=True)

#Building Decoder RNN and Initialising it
with open('embedding.pkl','rb') as fp:
	embeddings = pickle.load(fp)
decoder = build_model(embeddings)
 












