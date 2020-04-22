# Use pandas library to play around with basic data formatting and simple analysis
# Must install pandas using
# 'pip install pandas'
# https://pandas.pydata.org/docs/index.html 

import pandas

# Create a pandas dataframe with test data. Create column names then then print it
df1 = pandas.DataFrame([["Smith","0897",60000],["Jones","0208",50350],
    ["Timpson","0233",75000],["Jackson","0972",67250], 
    ["Wilks","0073",90000],["Hendrix","031",65150]],
    columns=["Surname","ID","Salary"])
print(df1)

# What's the datatype of df1 and df1.Salary?
print("Type is: ",type(df1))
print("Type is: ",type(df1.Salary))

# Simple analysis of Salary
print("Mean salary: ", df1.Salary.mean())
print("Max salary: ", df1.Salary.max())
print("Min salary: ", df1.Salary.min())
print("Median salary: ", df1.Salary.median())