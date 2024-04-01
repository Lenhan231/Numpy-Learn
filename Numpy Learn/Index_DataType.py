import numpy as np

np1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

x = np.where(np1 == 3) # return index and data type

print(x) # print the tuple 
print(x[0]) # print the index
# if there is another item that like 3 then
# Print will return 2 index in lieu of 1
print(np1[x[0]])
# This will return the data

x = np.where(np1%2 == 0)
print(x)
print(np1[x[0]])
