# Code for analysing COVID-19 country data available from this data source:
# https://datahub.io/docs/about
# COVID-19 is specifically available here:
# https://datahub.io/core/covid-19

import pandas as pd
import sys

filename = 'covid19.csv'

# Format and print the dataframe
def format_print_df(df):
    if df.empty:
        print("Invalid or missing argument")
    else:    
        print("Date: ", df.values[0][0])
        print("Country: ", df.values[0][1])
        # If no province specified cell will be null
        if pd.isnull(df.values[0][2]):
            print("No province") 
        else:
            print("Province: ", df.values[0][2])
        print("Confirmed: ", df.values[0][5])
        print("Recovered: ", df.values[0][6])
        print("Deaths: ", df.values[0][7])

# Read command line arguments
def read_args():
    date = "NaN"
    country = "NaN"
    province = "NaN"
    numargs = len(sys.argv)
    index = 1
    while index < numargs:
        try:
            arg = str(sys.argv[index])
            if arg == '-c':
                country = str(sys.argv[index+1])
            elif arg == '-p':
                province = str(sys.argv[index+1])
            elif arg == '-d':
                date = str(sys.argv[index+1])
            else:
                print("Invalid argument: ", arg)
        except IndexError:
            print("Invalid number of arguments")
        except:
            print("Input error")
        index = index + 2
    return [country, province, date]

# Read command line args
args = read_args()

# Read dataset as a panda dataframe
ds = pd.read_csv(filename)
df1 = pd.DataFrame(ds)

# Get data for particular date
df2 = df1[df1['Date'].str.contains(args[2])]

# Get data for particular country
df3 = df2[df2['Country/Region'].str.contains(args[0])]

# Get data for particular province (including if none specified)
if args[1] == "NaN":
    df4 = df3[df3['Province/State'].str.contains(args[1], na=True)]
else:
    df4 = df3[df3['Province/State'].str.contains(args[1], na=False)]

# Print selected data
format_print_df(df4)