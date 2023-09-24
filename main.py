#!/usr/bin/env python

import random
import numpy as np

from perceptron import *

#
# Generate Extremely Basic Data
#

DATA_dir = 'data'
DATA_size = 5
DATA_input_label = 'input'
DATA_output_label = 'output'

# returns an entire row as a string
def create_data_point():
  x = random.uniform(0, 100)

  # decision boundary: data is 1d, so decision boundary must split a 1d object (a line)
  # this means it's really just a point
  # let's go with   x == 22
  y = 0 if x < 22 else 1

  return f"{x}, {y}"

with open(f'{DATA_dir}/basic_data.csv', 'w+') as data_file:
  # header
  data_file.write(f'{DATA_input_label},{DATA_output_label}\n')

  # generate data according to create_data_point
  for i in range(DATA_size):
    line = create_data_point() + '\n'
    data_file.write(line)

print('Generated data!')

data = np.loadtxt(f'{DATA_dir}/basic_data.csv', delimiter=',', skiprows=1)

print('Loaded data!')

X = data[:,0]
y = data[:,1]

# show proportion of classes
positive_samples = 0
for label in y:
  if label == 1:
    positive_samples += 1
print(f'Data is {positive_samples/len(y)} positive and {(len(y)-positive_samples)/len(y)} negative.')

# create perceptron

learning_rate = 0.001
epochs = 1
threshold = 0.80

net = Perceptron1d(X=X, y=y, learning_rate=learning_rate, epochs=epochs, threshold=threshold)

net.train()