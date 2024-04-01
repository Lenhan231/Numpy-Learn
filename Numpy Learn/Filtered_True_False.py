import numpy as np

np1 = np.array([1, 2, 3, 4])
x = [True, True, False, False]
print(np1[x])

# This shit will return the True filtered in the array
filtered = []
for thing in np1:
    if thing % 2 == 0:
        filtered.append(True)
    else:
        filtered.append(False)
print(np1[filtered])

# Breaf
filtered = np1 % 2 == 0
print(np1[filtered])