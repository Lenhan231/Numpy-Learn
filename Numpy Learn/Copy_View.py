import numpy as np
np1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# view() function will syn after the alter happen
np2 = np1.view()
# copy() function will not syn anything 
np2 = np1.copy()

