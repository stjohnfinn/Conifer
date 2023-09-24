import random
import sys
import numpy as np

class Perceptron1d:
  def __init__(self, X, y, learning_rate, epochs, threshold):
    self.size = len(X)
    self.epochs = epochs
    self.learning_rate = learning_rate
    self.threshold = threshold
    self.X = X
    self.y = y
    self.w = random.random()
    print(f'initializing W as {self.w}.')
    self.b = random.random()
    print(f'initializing B as {self.b}.')

  def _sigmoid(self, x):
    return 1 / (1 + np.exp(-x))
  
  def train(self):

    for i in range(self.epochs):
      total_errors = 0

      for idx in range(self.size):
        print(f'predicting: y = {round(self.w, 4)} * x + {round(self.b, 4)}')
        # make a prediction
        raw_activation = self.w * self.X[idx] + self.b
        # put this through sigmoid function
        print(raw_activation)
        y_prime = 1 if self._sigmoid(raw_activation) > 0.5 else 0
        print(y_prime)

        # update based on accuracy
        if y_prime != self.y[idx]:

          self.w = self.w + (self.y[idx] - y_prime) * self.X[idx] * self.learning_rate
          self.b = self.w + (self.y[idx] - y_prime) * self.learning_rate

          total_errors += 1

      # if total accuracy is {threshold} or higher, break
      num_correct = self.size - total_errors
      accuracy = num_correct / self.size
      if i % 10 == 0: print(f"Achieved {round(accuracy, 2)} accuracy!")
      if (accuracy >= self.threshold):
        print(f"Achieved {round(accuracy, 2)} accuracy!")
        print(f"Stopping training. This is higher than set threshold of {self.threshold}.")
        break



class PerceptronNd:
  def __init__():
    