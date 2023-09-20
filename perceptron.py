import random

class Perceptron1d:
  def __init__(self, X, y, learning_rate, epochs):
    self.size = len(X)
    self.X = X
    self.y = y
    self.w = random.random()
    print(f'initializing W as {self.w}.')
    self.b = random.random()
    print(f'initializing B as {self.b}.')
  
  def train(self):
    total_errors = 0

    for idx in range(self.size):
      # make a prediction
      y_prime = self.w * self.X[idx] + self.b
      # update based on accuracy
      if y_prime != y[idx]:
        self.w = self.w + (self.y[idx] - y_prime) * self.X[idx]
        self.b = self.w + (self.y[idx] - y_prime)
        errors += 1