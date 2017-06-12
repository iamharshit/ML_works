# Computer Understands Relation
Given 2 related words A,B and a new word C the model extracts the relation between A & B and predicts a word that satisfy the similar relation with C i.e `A:B::C:D`.It uses the word2vec embeddings trained on Wikipedia text corpus for training purposes.

These are formally called as Word Analogies. 

![img](http://colah.github.io/posts/2014-07-NLP-RNNs-Representations/img/Mikolov-GenderVecs.png)

It basically uses the following formulae:

```
		V("woman")−V("man") ≃ V("aunt")−V("uncle")
```

where V represents the vector representation of the respective word.

### Basic Usage
* Download the word2vec training dataset from [here](https://drive.google.com/open?id=0B4EnoW35ElayalNSNU1OQWp4WVE) and should be saved in directory named `vectors`.
* Run `predict_relation.py` file.
* Note: The standard format `A:B::C: ` be followed for input purposes and position of `D` be left blank.

![img](/Computer%20Understands%20Relation/screenshot.png)

