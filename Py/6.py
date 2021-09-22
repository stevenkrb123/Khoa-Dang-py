import numpy as np 
a = np.arange(1,100)
x = a[(a % 3 == 0) | (a % 5 == 0)]
print (x[:100])
print (sum(x))
