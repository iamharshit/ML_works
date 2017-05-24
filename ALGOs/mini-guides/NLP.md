## Why word to numbers?

Just like a computer, a neural network can't understand words. It only sees a series of numbers. Feeding a neural network these series of numbers would require it to learn the english vocabulary. This requires more data than we have. Instead, let's turn the words into something easer for a neural network to learn from.

Just like ASCII encodes a character as a number, you can encode a word as a number. For example, the text "my bat is the best bat" could be changed to [1, 2, 3, 4, 5, 2]. Each word has been converted to a number where the number assigned to a word is arbitrary.

It's only required that each number corresponds to a single word and vice versa. This is known as a one to one function

## Bag of Words

A way of converting sentence to numbers.Here the number represent frequency of the word used.
A bag of words is usually represented as a dictionary. The key is the word and the value is the number of times a word appears in the text. For example, the sentence "the fox jumps over the lazy dog" would become:
{'the': 2, 'jumps': 1, 'lazy': 1, 'over': 1, 'fox': 1, 'dog': 1}

The model losses the information- the ordering of words in the sentence.

Simple Implementation:
```
from collections import Counter

def bag_of_words(text):
    # TODO: Implement bag of words
    bag = Counter()
    for word in text.split(' '):
        bag[word]+=1
    return bag

test_text = 'the quick brown fox jumps over the lazy dog'

print(bag_of_words(test_text))


```
