import pandas as pd
import pickle

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)

# Save the DataFrame to a pickle file
with open('data.pkl', 'wb') as f:
    pickle.dump(df, f)

# Load the DataFrame from the pickle file
with open('data.pkl', 'rb') as f:
    loaded_df = pickle.load(f)

# Display the loaded DataFrame
print("Loaded DataFrame from pickle file:")
print(loaded_df)
