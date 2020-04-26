# Code for analysing COVID-19 country data available from this data source:
# https://datahub.io/docs/about
# COVID-19 is specifically available here:
# https://datahub.io/core/covid-19

import pandas as pd
import sys

# Format and print the dataframe
def print_covid_data(df):
    if df.empty:
        print("Invalid or missing argument")
    else:    
        print("Date: ", df.values[0][0])
        print("Country: ", df.values[0][1])
        # If no province specified cell will be null
        if pd.isnull(df.values[0][2]):
            print("Province: No province") 
        else:
            print("Province: ", df.values[0][2])
        print("Confirmed: ", "{:,}".format(int(df.values[0][5])))
        print("Recovered: ", "{:,}".format(int(df.values[0][6])))
        print("Deaths: ", "{:,}".format(int(df.values[0][7])))

# Print help
def print_help():
    print("Parameters -c <country> -p <province> -d <date>")
    print("country: String containing valid country name")
    print("province: String containing valid province name")
    print("date: String containing date in form yyyy-mm-dd")

# Read command line arguments
def read_args():
    date = "NaN"
    country = "NaN"
    province = "NaN"
    numargs = len(sys.argv)
    index = 1
    
    if numargs == 1:
        print_help()
    elif sys.argv[index] == '-h':
        print_help()
    else:
        while index < numargs:
            try:
                arg = sys.argv[index]
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

# Return population of country for year
def population_size(country, year):
    try:
        # Read dataset as a panda dataframe
        pop_df = pd.read_csv('population.csv')
    
        # Get data for particular country
        df1 = pop_df[pop_df["Country Name"] == country]
        df2 = df1[df1["Year"] == year]
        return df2['Value'].values[0]
    except:
        return 0

#####################
# Program starts here
#####################

# Read command line args 
args = read_args()

if (args[0] != "NaN") and (args[2] != "NaN"):
    # Read dataset as a panda dataframe
    df1 = pd.read_csv('covid19.csv')

    # Get subset of data for specified country/region
    df2 = df1[df1["Country/Region"] == args[0]]

    # Get subset of data for specified date
    df3 = df2[df2["Date"] == args[2]]

    # Get subset of data for specified province (including if none specified)
    if args[1] == "NaN":
        df4 = df3[df3['Province/State'].str.contains(args[1], na=True)]
    else:
        df4 = df3[df3['Province/State'].str.contains(args[1], na=False)]

    # Print selected covid data from last subset
    print_covid_data(df4)
    
    # Get and print country population size for 2018 (latest year data available)
    pop_sz = population_size(args[0], 2018)
    if pop_sz > 0:
        print("Population: ", "{:,}".format(pop_sz))
else:
    print("Missing argument")