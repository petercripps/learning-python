# Code for analysing COVID-19 country data available from this data source:
# https://datahub.io/docs/about
# COVID-19 is specifically available here:
# https://datahub.io/core/covid-19

import pandas as pd
import sys

# Defines absolute or relative path to where datasets are found.
path = "../../../datasets/"

# Format and print the dataframe.
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

# Print help.
def print_help():
    print("Usage: covid19.py -c <country> -p <province> -d <date>")
    print("Where:")
    print("<country> (required): String containing valid country name e.g. 'United Kingdom'")
    print("<province> (optional): String containing valid province name e.g. 'Bermuda'")
    print("<date> (required): String containing date in form yyyy-mm-dd e.g. '2020-03-31'")

# Read command line arguments.
def read_args():
    date = ""
    country = ""
    province = ""
    numargs = len(sys.argv)
    index = 1
    
    if numargs == 1:
        # No arguments so print help
        print_help()
        return []
    elif sys.argv[index] == '-h':
        print_help()
        return []
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

# Return COVID-19 data for country, province and date.
def covid_data(country, province, date):
    df4 = pd.DataFrame()
    if (country != "") and (date != ""):
        
        # Read dataset as a panda dataframe
        df1 = pd.read_csv(path + 'covid19.csv')

        # Get subset of data for specified country/region
        df2 = df1[df1["Country/Region"] == country]

        # Get subset of data for specified date
        df3 = df2[df2["Date"] == date]

        # Get subset of data for specified province. If none specified and there
        # are provinces dataframe will contain all with first one being country
        # and province as 'NaN'
        if province == "":
            df4 = df3[df3['Province/State'].str.contains(province, na=True)]
        else:
            df4 = df3[df3['Province/State'].str.contains(province, na=False)]

    # Return selected covid data from last subset
    return df4

# Return population of country for year.
def population_size(country, year):
    try:
        # Read dataset as a panda dataframe
        pop_df = pd.read_csv(path + 'population.csv')
    
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
if args:

    # Get covid dataframe
    df = covid_data(args[0],args[1],args[2])

    # Print data if dataframe not empty
    if not df.empty:

        # Print selected covid data from last subset
        print_covid_data(df)

        # Get and print country population size for 2018 (latest year data available)
        pop_sz = population_size(args[0], 2018)
        if pop_sz > 0:
            print("Population: ", "{:,}".format(pop_sz))
    else:
        print("Missing or invalid argument(s)")