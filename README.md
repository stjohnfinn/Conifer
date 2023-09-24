# Conifer

A perceptron implemented in Python.

## High level perceptron overview

Created in 1958, based on the way signals propogate through neuron chains.

Now that neural networks are commonplace, it's easiest to explain Perceptrons as a 
single-layer neural network. There is one set of weights and one set of biases. The entire
thing is just a dot product and a matrix addition (in the multidimensional case
obviously). The result of those operations are run through an activation function to
produce a prediction. With one layer, there is no backpropogation involved, so updating
the weights is also very simple. Keep in mind this is also only a linear classification
model. There is one output, so generally it encodes two states (1 or 0). The threshold
for positive and negative classes is arbitrary (I'm using the sigmoid function, so 
greater than 0.5 is positive), which leads me to believe you could, in the same way,
define N thresholds and classify N+1 classes. Is this accurate? I believe it is. The 
boundaries would still be linear, but it would work.

The main parts of this code:

1. load data
    1. for the 1d perceptron, I'm generating it myself because it's trivial
    1. for the Xd perceptron, I'm probably going to use a dataset I find online
    1. transform or format the data to a usable form
1. create network
    1. feed hyperparameters and stuff
    1. initialize weights and biases
        1. this should be random initialization
1. given data, train
    1. for each epoch,
        1. for each datapoint,
            1. make a prediction
            1. if prediction is incorrect
                1. update weights
1. after training, test
    1. for all test data
    1. make a prediction
    1. tally 

## Data

### 1-Dimensional

For the one-dimensional perceptron, this is just generating random real numbers and 
setting a 1-dimensional threshold (a point)

### N-Dimensional

I found a dataset of nearest-earth objects (NEOs) from some NASA API on Kaggle. It's a binary
classification task obviously. 

[Link ⤴](https://www.kaggle.com/datasets/sameepvani/nasa-nearest-earth-objects)
