import psutil
import time
import numpy as np

cpu_use = []
mem_use = []

#Measuring the cpu and memory-utilization every hundreth of a second for 90 seconds
for i in range(9000):
   cpu_use.append(psutil.cpu_percent())
   mem_use.append(psutil.virtual_memory().percent)
   time.sleep(0.01)

#Converting into numpy-arrays and using numpy-saving function to create plot in different file (see plot.ipynb)
cpu = np.asarray(cpu_use)
mem = np.asarray(mem_use)
with open('result.npy', 'wb') as f:
   np.save(f, cpu)
   np.save(f, mem)
