import pandas as pd
import numpy as np

Name = np.array(['John', 'Mary', 'Sarah'])
Age = np.array([25, 32, 28])
# Create a dictionary
data = {'Name': Name, 'Age': Age}
# Display the dictionary in DataFrame
df = pd.DataFrame(data) 

print(df)