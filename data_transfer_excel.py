import pandas as pd

# Input CSV file
input_file_path = 'D:/data_transfer/countries_name.csv'

# Output Excel file
output_file_path = 'D:/data_transfer/new_file.xlsx'

# Read data from the input CSV file
input_df = pd.read_csv(input_file_path)

# Do any necessary data processing or manipulation here
# For example, you can filter rows, rename columns, etc.

# Clean the data by removing characters not allowed in Excel
# input_df = input_df.applymap(lambda x: ''.join([i if ord(i) < 128 else '' for i in str(x)]))
input_df = input_df.apply(lambda x: x.map(lambda i: ''.join([j if ord(j) < 128 else '' for j in str(i)])))

# Write the processed data to the output Excel file
input_df.to_excel(output_file_path, index=False)

print("Data transfer completed.")