## News Summarizer
Summarizes the Big News Column from a Newspaper to just a sentence.It is just an extension of Standard LSTM Text Summarizer

### Overview
Here we used the "Global Vector" algorithm for quantifying words(word embedding) over standard "word2vec" algorithm because GloVe is faster.We use Seq2Seq neural architecture comprised of Encoder RNN and Decoder RNN.We use "Attention" mechanism  for outputing each word in the decoder i.e for each output word it computes weight for each input word which represents how much attention should be paid to that word.It helps RNN to focus on the most relevant feature when generating new Text.

### Dataset Download
* GloVe Dataset can be downloaded from [here](https://nlp.stanford.edu/projects/glove/) and put it inside the folder named "data". 
* News dataset can be downloaded from [here](http://research.signalmedia.co/newsir16/signal-dataset.html) and put it inside the folder named "data".

### Status 
The project is not completed yet and is currently under the working phase.
