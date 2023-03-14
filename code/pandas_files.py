# Read and write various files using pandas.
# https://pandas.pydata.org/docs/index.html

import pandas
import json

# Read a CSV file into a pandas dataframe and print it out.
df1 = pandas.read_csv("employee-data.csv")
print(df1)

# Read an Excel file into a pandas dataframe and print it out.
df2 = pandas.read_excel("employee-data.xlsx")
print(df2)

# Build a JSON schema as a dictionary from the dataframe and print it out
dict = df2.to_dict()
print(dict)

# Convert JSON schema to a string and write it to a JSON file.
json_str = json.dumps(dict)
f = open("employee-data.json", "w")
f.write(json_str)
f.close()

# Open and read the JSON file just created and print it out.
f = open("employee-data.json", "r")
content = f.read()
print(content)

# Read a JSON file into a pandas dataframe and print it out.
df3 = pandas.read_json("employee-data.json")
print(df3)