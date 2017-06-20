# Identify Me Out
Figure out the odd word in the list by finding the fartest distance in word2vec embedding.It uses the word2vec embeddings trained on Wikipedia text corpus.We compute the mean of vectors of the given set of words and find out the fartest point as the odd one out.

### Basic Usage
* Download the word2vec training dataset from [here](https://drive.google.com/open?id=0B4EnoW35ElayalNSNU1OQWp4WVE) and should be saved in directory named `vectors`.
* Run `identify_odd.py` file.

### Demo
![img](/Identify%20Me%20Out/screenshot.png)

### About Word2Vec 

Vector Representation of words, basically converting word to a set of numbers so that it is computer readable.

<b>Overview:</b>
Converts text to numerical format called vectors so that deep NNets can understand it.It basically makes Natural Language computer readable.
It is a 2 layer Neural net with input as text corpus and output is each word has a vector associated with N fetures.
<i>Just as a painting which is a combinations of oil represent a 3-D object, similarly a cobination of numbers(each representing some feature) called as a whole a vector represents a word.</i>
It groups similar words together.Based on neighbouring words in past occurences of a word, word2vec can identify meaning of that word and its associations with other words.It is used identifies pattern among words.

<b> Training of word2vec: </b>
We need a way to allot weights to a word along each feature that can be done by training the model by CBOW(predicting word from context) or Skip-gram(predicting context from word).In each training iteration based on prediction the weights along each features are updated.

<b> The Magic: </b>
Word2vec algorithm has never been taught a single rule of English syntax. It knows nothing about the world, and is unassociated with any rules-based symbolic logic or knowledge graph. And yet it learns more, in a flexible and automated fashion, than most knowledge graphs will learn after a years of human labor. It comes to the Google News documents as a blank slate, and by the end of training, it can compute complex analogies that mean something to humans.

### References

* [Nice visualisation of word2vec](http://projector.tensorflow.org/)

### GloVe

Construct Co-occurance matrix --> Factorize that matrix to get (word*feature) matrix

### Comparison

Both Word2Vec and GloVe does the same things, the main difference is how they are built.Word2Vec is built by predicting the word or contex from the given word(more specifically the word vector) whereas GloVe is built from word-word co-occrance matrix(i.e frequency of 2 words occuring together).

GloVe was developed because Word2Vec fails to capture some of the information of a word in its vector representation specifically saying it fails to capture Linear Substructures present in each word.

It is showed that GloVe outperformed Word2Vec in standard test of word analogies.
