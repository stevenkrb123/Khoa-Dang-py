import numpy as np
sammpleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(sammpleArray)
min = np.amin(sammpleArray,1)
print(min)
max = np.amax(sammpleArray,0)
print(max)