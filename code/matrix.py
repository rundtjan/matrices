import numpy as np
from memory_profiler import profile
import matplotlib.pyplot as plt

@profile
def func():
   #Creating the matrixes with random sampling
   A = np.random.uniform(0.00000001,1,(pow(10,6),pow(10,3)))
   B = np.random.uniform(0.00000001,1,(pow(10,3),pow(10,6)))
   C = np.random.uniform(0.00000001,1,(pow(10,6),1))

   #Matrix multiplications
   BC = np.matmul(B, C)
   D = np.matmul(A, BC)

   #Taking a random sample from matrix A to show the distribution
   rng = np.random.default_rng()
   sample = rng.choice(A, pow(10,5), replace=False)
   flat = sample.flatten()

   #Plotting the CDF for the sample from A
   x = np.sort(flat)
   y = 1. * np.arange(len(x)) / (len(x) - 1)
   plt.plot(x, y)
   plt.savefig('cdf.png')

if __name__ == '__main__':
   func()
