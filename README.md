# Data_transfer
automation of data transfer


To automate the transfer of data from one Excel file to another in Windows using Python, you can use the pandas library for data manipulation and the openpyxl library for working with Excel files. Here's a simple example:

Install Required Libraries:
If you haven't installed pandas and openpyxl yet, you can install them using the following commands:

pip install pandas
pip install openpyxl

Write Python Script:
Create a Python script that reads data from one Excel file and writes it to another. Adjust the file paths and column names according to your specific Excel files.

Replace 'path/to/input_file.xlsx' and 'path/to/output_file.xlsx' with the actual paths of your input and output Excel files. You can also perform any necessary data processing within the script before writing to the output file.

Run the Script:
Save the script with a .py extension (e.g., excel_transfer.py) and run it using a Python interpreter.


If your Excel files have multiple sheets or if you need to perform more complex data manipulations, you can explore additional features provided by the pandas and openpyxl libraries.


data_transfer_excel:
this file transfer all data to given output path

new_file_distribution:
chunk define row number you want to distribute 
this file create files and divide data equally other files 
