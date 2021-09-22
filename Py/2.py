import numpy as np
A = np.array([[1, 2, 3], [4, 5, 6]])
result = np.all((A == 0))

if result:
    print('Your array has 0')
else:
    print('Your array does not have 0')