## MNIST Autoencoder
Generating Novel yet similar image to the trained dataset(which is MNIST here).

![img](https://blog.keras.io/img/ae/autoencoder_schema.jpg)

### Overview of Autoencoders
For generation of much novel and unsimilar images one could go for variational autoencoder.
An autoenoder basically compromises of Encoder and Decoder Networks.Encoder reduces the dimensionality of the input layer(like a file compressor) and decoder(decompresses the data then). Hence auoencoder are quite popularly used in "Data Compression" domain.Compared to standard Image Compression algorithms like "jpeg", autoencoder doesn't provide any significant advantage. 

Even Tech Giant Google uses autoencoder for image compression so now the image can be handled easily by google's web crawler, here the autoencoder does "Dimensionalty Reduction" and works better then its predecessor the "PCA" for the same.They are also used in one class classification tasks.Autoencoder are used for denoising of input data to get more pure data as output.
Here were are using only 2 layer autoencoder because we get the desirable output with least computation power and complexity.One could also use Stacked Autoencoder for much better results. 
Since Autoencoder construct the output same as the input,it needs to know which feature are the most important ones eventually acting as a Feature Extractor. 

### Basic Usage

* Download the standard MNIST dataset and place it in "dataset" directory.
* Run main.py

