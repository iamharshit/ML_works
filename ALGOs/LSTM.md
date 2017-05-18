### LSTM

LSTMs are used to model long term sequential data.Like RNNs they have a repeating module just with a different structure.

The core idea of LSTM is memory cell which acts like bucket to store all the information till now and pass only the relevant information to the hidden node.


The gates states(calculated through sigmoid functions) describe how much of each component be passed through.

### Meaning of "Long Short Term Meomory"
Here Short memory refers the memory that a memory cell stores in each datapoint i.e information stored in a sequence and Long term memory refers to memory stored stored across different datapoints. From the long term training of weights an LSTM learns that what it needs to forget and what it needs to remember in short term.

### When LSTM wants to forget

When the LSTM identifies a new subject it forgets the old one.How much of the memory need to be kept from m(t-1) to m(t) is decided by using the values of current input state [x(t)] and the last hidden state [h(t-1)] 

### When LSTM want to store new information

We want add information about the new subject.
We use the new input state [x(t)] and the last hidden state  [h(t-1)] to know by how much the cell state be updated
We apply the tanH function to current input node{x(t)} and the last hidden node state{h(t-1)} as the contribution of the new state to memory cell.

### what we need to output 

In the above sentence output refers to tensors flowing from memory cell to hidden node.The hidden node then is used to calculate the final output.
To decide which parts of the cell state we are going to output we use the the current input node{x(t)} and the last hidden node state{h(t-1)}.

### Glossory

THe full repeating module is called an LSTM, it is composed of input, hidden, output and memory nodes or neurons, the memory neuron is also called just 'cell' sometimes. 'State' usually denotes the value of memory cell.

### Implementing LSTM in tensorflow

Tensorflow have inbuilt implemtation of the RNN model-basic one, LSTM and GRU.We just need to pass in the size of the memory cell during the RNN initialisation.The hidden value should not be much large to avoid overfitting and neither too small to avoid underfitting.Moreover the sequence in each of the data points should be a list.All these are entries are concatenated to form a list.

Hence each datapoint is generally a list of lists.



