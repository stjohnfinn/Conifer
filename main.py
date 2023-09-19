#!/usr/bin/env python

import random

#
# Generate Extremely Basic Data   
#

DATA_dir = 'data'
DATA_size = 10_000

# returns an entire row as a string
def create_data_point():
  x = random.randint(0, 10_000)
  y = 1 if x % 2 == 0 else 0
  return f"{x}, {y}"

with open(f'{DATA_dir}/basic_data.csv', 'w+') as data_file:
  # header
  data_file.write('x,y\n')

  # generate data according to create_data_point
  for i in range(DATA_size):
    line = create_data_point() + '\n'
    data_file.write(line)

print('Generated data!')