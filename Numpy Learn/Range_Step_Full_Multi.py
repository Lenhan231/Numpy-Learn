import numpy as np # inport library

np1 = np.array([[0, 3], [3, 5]]) #Inital array
print(np1.shape) #2D matrix 2x2

#using range in array
np2 = np.array([range(10)])
print(np2)

#Step
np3 = np.array([range(0, 10 ,2)])
print(np3)

#zeros
np4 = np.zeros(10)
print(np4)

# Multidimensional zeros
np5 = np.zeros((2, 10))
print(np5)

#full
np6 = np.full((2, 10), 0.)
print(np6)


