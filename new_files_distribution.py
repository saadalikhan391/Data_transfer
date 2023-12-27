import pandas as pd

# Input CSV file
input_file_path = 'D:/data_transfer/countries_name.csv'

# Read data from the input CSV file
input_df = pd.read_csv(input_file_path)

# Split the data into chunks, each containing 20 rows
chunk_size = 20
data_chunks = [input_df.iloc[i:i+chunk_size] for i in range(0, len(input_df), chunk_size)]

# Output directory for new Excel files
output_directory = 'D:/data_transfer/New_folder/'

# Create and write Excel files with 20 rows each
for i, chunk in enumerate(data_chunks, start=1):
    output_file_path = f'{output_directory}new_file_{i}.xlsx'
    chunk.to_excel(output_file_path, index=False)
    print(f"File {i} created with {len(chunk)} rows: {output_file_path}")

print("Data distribution completed.")
