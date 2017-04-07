## Machine Generated Music

The songs in the dataset are converted to text and each word is represented in vector form, this vector are then grouped together as the corresponding label(Happiness, Anger etc) mentioned in the Datset.The user inputs the set of emotion which he wants in his music which are then mapped to the word vectors of the model generated from the dataset, the output are the set of cords that best represent those emotions.

Here we use RBM as our generative model.We create a sample from our input using [Gibbs sampling algorithm](https://www.quora.com/In-laymans-terms-how-does-Gibbs-Sampling-work).The project is currently under the working phase.

### Inspiration
This is inspired from the state of the art Deepmind paper on Wavnet(know best for Music Generation and Text to Speech). The model uses Parametric Audio generation(ALL information required to generate music are stored in model parameters) over Concatenative Audio generation(combination of static audio fragments). The output music of very good instead it was just computionally expensive(90 min training on GPU).It basically uses CNN for music generation.

### References
* [DeepMind's Wavnet explained](https://deepmind.com/blog/wavenet-generative-model-raw-audio/)
* [Generating Music using RNN](http://www.hexahedria.com/2015/08/03/composing-music-with-recurrent-neural-networks/)

