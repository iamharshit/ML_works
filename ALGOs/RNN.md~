## Recurrent Neural Network

Although RNNs are best suited for sequential data but they could also be used for other purposes

### Why RNN?

RNN are used to model sequential data(i.e where the current datapoint has some dependence on the previous data point eg.if our dataset is day's temperature vs day's wether condition then a day's weather also have some dependence on the weather of day before).Tradiontal neural network has no feature/layer to account for the same but in recurrent neural network we have an additional hidden layer which incorporated that.

## Application
These are used in applications that deal with sequential data.Those includes:

* Word prediction: A word in a sentence depend upon its neighboring words to match the same context, we use a RNN to model that.
* Music Composition: New word depends upon previous word too, they kinda shares the same melody.

We have variants of RNNs to solve much complex problem.Those include Recursive Neural Network, Recursive Neural Tensor Network, Hopfield network, Echo State Network.

RNNs are easier to implement then they sounds because Tensorflow provides in-built methods for RNN implementation.

## Problem

The RNN need to store all the states it had trained upto at some time point which can be much computationally expensive both in terms of space and time.Also the gradient keep on reducing during backpropagation phase ultimately vanishing hence we are unable to modify the weight for great-great grandparents, officially the problem is called "Vanishing gradient problem".
To solve the above problem we have come up with LSTM(Long short term memory model).

## LSTM

By maintaining a more constant error, they allow recurrent nets to continue to learn over many time steps (over 1000).
The model is inspired from the computer architecture.The LSTM units are composed of 4 main elements: Information Cell(Responsible for holding data), the 3 logistic gates decides the flow of data inside LSTM, the Write gate(responsible for writing data into the information cell), the Read gate(reads information from the information cell and sends that data to RNN), the Keep gate(deletes useless data from the information cell).

Previous  --> LSTM --> Current 

The write gate is responsible for writing new data into the information cell.The read data is responsible for sending the data from LSTM back to the recurrent network.

Overall all three gate allows the data to freely flow inside and outside of the information cell.

## References

* [LSTM explained](https://deeplearning4j.org/lstm.html)

