import pandas as pd

# Define the path to your CSV file
file_path = r'C:\Users\rf\Desktop\dataflow\dataflow_system\dataflow_system\data\Amount data.csv'

# Create an empty DataFrame with the same columns
columns = ['current_time','name','Description','Amount']

empty_df = pd.DataFrame(columns=columns)

# Save the empty DataFrame to the CSV file (this will clear the file)
empty_df.to_csv(file_path, index=False)

print(f"Data has been removed from {file_path}.")