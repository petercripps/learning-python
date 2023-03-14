# Use pandas library to play around with basic data formatting and simple analysis
# Must install pandas using
# 'pip install pandas'
# https://pandas.pydata.org/docs/index.html 

import pandas

# Create a pandas dataframe with test data. Create column names then print the dataframe
df1 = pandas.DataFrame([["Smith","0897",60000.00],["Jones","0208",50350.00],
    ["Timpson","0233",75000.00],["Jackson","0972",67250.00],
    ["O'Neil","0143",65000.25],["Thompson","0822",57550.00],
    ["Beveridge","0935",75000.00],["Davies","0002",107250.00],
    ["Shah","0555",85000.00],["O'Rourke","0112",30250.00], 
    ["Wilks","0073",90000.50],["Hendrix","0031",65150.75]],
    columns=["Surname","ID","Salary"])

# Set these to 'True' to get info

if False:
    print(df1)

# Print first 3 rows
if False:
    print(df1.head(3))

# Print datatypes
if False:
    print(df1.dtypes)

# What's the datatype of df1 and df1.Salary?
if False:
    print("Type is: ",type(df1))
    print("Type is: ",type(df1.Salary))

# Provide a full summary of stats
if False:
    print(df1.describe(include="all"))

# Simple analysis of Salary
if True:
    print("Sum salary: ", df1.Salary.sum())
    print("Mean salary: ", df1.Salary.mean())
    print("Max salary: ", df1.Salary.max())
    print("Min salary: ", df1.Salary.min())
    print("Median salary: ", df1.Salary.median())

# Select a single column 'Salary' and print each entry
if False:
    print(type(df1['Salary']))
    for entry in df1['Salary']:
        print(entry)

# Iterate over column headers
# For more ways of iterating see: https://pythonbasics.org/pandas-iterate-dataframe/
if False:
    for column_name in df1:
        print(type(column_name))
        print(column_name)
        print('------\n')  

# Iterate over rows using iterrows()
if False:
    for row_index, row in df1.iterrows():
        print(type(row))
        print(row_index, row, sep='\n')

# Iterate over rows using iterrows()
if False:
    for row in df1.itertuples():
        print(row)