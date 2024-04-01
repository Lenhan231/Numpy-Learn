import numpy as np

np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
np2 = np1.reshape(2, int(len(np1)/2))

# Reshape and then print the items in np2
for x in np2:
    print(x[1]) # Get the 1 index in each x in np2

np3 = np1.reshape(2, 3, 2)
# Reshape in to 3-D
print(np3)
for x in np3:
    print(x[1][1]) # Print 1.1 in each items

# Use np.nditer()
for x in np.nditer(np3): # This shit pull out all the items of the array
    print(x)
