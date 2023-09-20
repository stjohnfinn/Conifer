#!/usr/bin/env python

import random
import numpy as np
import ./perceptron.py

#
# Generate Extremely Basic Data
#

DATA_dir = 'data'
DATA_size = 10_000
DATA_input_label = 'input'
DATA_output_label = 'output'

# returns an entire row as a string
def create_data_point():
  x = random.randint(0, 10_000)
  y = 1 if x % 2 == 0 else 0
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

X = data[:,0]
y = data[:,1]

print('Loaded data!')

# create perceptron

learning_rate = 0.01
epochs = 100

net = Perceptron1d(X=X, y=y, learning_rate=learning_rate, epochs=epochs)