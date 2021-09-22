import numpy as np
sampleArray = np.array([[34,43,73],[82,22,12],[53,94,66]])
print(sampleArray)

row = sampleArray[sampleArray[1,:].argsort()]
print(row)

column = sampleArray[sampleArray[:,1].argsort()]
print(column)