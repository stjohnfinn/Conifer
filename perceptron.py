import random
import sys
import np

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
  
  def train(self):

    for i in range(self.epochs):
      total_errors = 0

      print(f"Currently predicting y = {round(self.w, 2)}x + {round(self.b, 2)}")

      for idx in range(self.size):
        # make a prediction
        y_prime = self.w * self.X[idx] + self.b
        # update based on accuracy
        if y_prime != self.y[idx]:

          # self.w = self.w + (self.y[idx] - y_prime) * self.X[idx] * self.learning_rate
          # self.b = self.w + (self.y[idx] - y_prime) * self.learning_rate

          a = self.y[idx] - y_prime
          b = a * self.X[idx]
          c = b * self.learning_rate
          print(f'a {a}')
          print(f'b {b}')
          print(f'c {c}')
          self.w = self.w + c
          print('-----------')

          print(f"self.w                {round(self.w, 1)}              {type(self.w)}")
          print(f"self.y[idx]           {round(self.y[idx], 1)}         {type(self.y[idx])}")
          print(f"y_prime               {round(y_prime, 1)}             {type(y_prime)}")
          print(f"self.X[idx]           {round(self.X[idx], 1)}         {type(self.X[idx])}")
          print(f"self.learning_rate    {round(self.learning_rate, 1)}  {type(self.learning_rate)}")
          # sys.exit(1)

          total_errors += 1

      # if total accuracy is {threshold} or higher, break
      num_correct = self.size - total_errors
      accuracy = num_correct / self.size
      print(f"Achieved {round(accuracy, 2)} accuracy!")
      if (accuracy >= self.threshold):
        print(f"Stopping training. This is higher than set threshold of {threshold}.")
        break