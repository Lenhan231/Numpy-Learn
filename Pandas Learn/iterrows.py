import pandas as pd

# Create a Pandas DataFrame 
data = {'Name': ['John', 'Mary', 'Sarah'], 
        'Age': [25, 32, 28]}
df = pd.DataFrame(data) 

# Sequences - Iterate through the DataFrame rows
for index, row in df.iterrows():
    print(row['Name'], row['Age'])

# Pickling - Serialize the DataFrame
import pickle
pickle.dump(df, open('data.pkl', 'wb')) 
df3 = pickle.load(open('data.pkl', 'rb'))