from math import sqrt

class Fibonacci_r:          # Slow
    def __init__(self, n):
        self.n = n
    def run(self):
        if self.n == 1 or self.n == 2:
          return 1
        return Fibonacci_r(self.n - 1).run() + Fibonacci_r(self.n - 2).run()

class Fibonacci_loop:       # Fast
    def __init__(self, n):
        self.n = n
    def run(self):
        a, b = 1, 1
        for i in range(self.n - 1):
            a, b = b, a + b
        return a

class Fibonacci_sqrt:       # Fastest
    def __init__(self, n):
        self.n = n
    def run(self):
        return ((1 + sqrt(5))** self.n - (1 - sqrt(5))** self.n) / (2 ** self.n * sqrt(5))

def get_classes():
    li = [Fibonacci_loop, Fibonacci_sqrt, Fibonacci_r]
    return li

for i in range (0, 3):
    print (int(get_classes()[i](30).run()), '\n')
