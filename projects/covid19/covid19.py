# Code for analysing COVID-19 country data available from this data source:
# https://datahub.io/docs/about
# COVID-19 is specifically available here:
# https://datahub.io/core/covid-19
# Population data is specifically available here:
# https://datahub.io/core/population

import pandas as pd
import sys

# Defines absolute or relative path to where datasets are found.
path = "../../../datasets/"
debug = False

# Use this dictionary for difference between population dataset (key) and covid dataset (value)
# Name in population dataset is the one that must be used in argument list
alternatives = {"United States": "US",
                "Syrian Arab Republic": "Syria"}

# Format and print the dataframe and population data.
def print_covid_data(df, pop_sz):
    if df.empty:
        print("Invalid or missing argument")
    else:
        try:    
            print("Date: ", df.values[0][0])
            print("Country: ", df.values[0][1])
            
            # If no province specified cell will be null
            if pd.isnull(df.values[0][2]):
                print("Province: No province") 
            else:
                print("Province: ", df.values[0][2])
            confirmed = int(df.values[0][5])
            deaths = int(df.values[0][7])
            print("Confirmed: ", "{:,}".format(confirmed))
            print("Recovered: ", "{:,}".format(int(df.values[0][6])))
            print("Deaths: ", "{:,}".format(deaths))
            if pop_sz > 0:
                print("Population: ", "{:,}".format(pop_sz))
                divisor = pop_sz/100000
                print("Confirmed/100,000:", round(df.values[0][5]/divisor, 2))
                print("Deaths/100,000:", round(df.values[0][7]/divisor, 2))
                print("Percent Deaths/Confirmed:", round((deaths/confirmed)*100, 2))
            else:
                print("Population: Unknown")
        except ValueError:
            print("Inappropriate argument value")
        except:
            print("Invalid or missing argument")

# Print help.
def print_help():
    print("Usage: covid19.py -c <country> -p <province> -d <date>")
    print("Where:")
    print("-c <country> (required): String containing valid country name e.g. 'United Kingdom'")
    print("-p <province> (optional): String containing valid province name e.g. 'Bermuda'")
    print("-d <date> (required): String containing date in form yyyy-mm-dd e.g. '2020-03-31'")

# Read command line arguments.
def read_args(args):
    argdict = {"country": "", "province": "", "date": ""}
    
    # If no arguments return empty dict
    if len(args) == 1:
        print("No arguments provided, try using '-h'")
        return argdict
    
    # If first argument is -h print help and return empty dict
    if args[1] == '-h':
        print_help()
        return argdict
    
    # Read arguments
    try:
        i = 1
        while i < len(args):    
            if args[i] == '-c':
                argdict["country"] = args[i + 1]
                i += 1
            elif args[i] == '-p':
                argdict["province"] = args[i + 1]
                i += 1   
            elif args[i] == '-d':
                argdict["date"] = args[i + 1]
                i += 1
            else:
                print("Unknown argument", args[i])
            i += 1    
    except IndexError:
        print("Invalid or missing argument")
    return argdict

# Return COVID-19 data for country, province and date.
def covid_data(country, province, date):
    df4 = pd.DataFrame()
    if (country != "") and (date != ""):
        
        # Read dataset as a panda dataframe
        df1 = pd.read_csv(path + 'covid19.csv')

        # Get subset of data for specified country/region
        if country in alternatives:
            country = alternatives[country]

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
def pop_size(country, year):
    try:
        # Read dataset as a panda dataframe
        pop_df = pd.read_csv(path + 'population.csv')
    
        # Get data for particular country
        df1 = pop_df[pop_df["Country Name"] == country]
        df2 = df1[df1["Year"] == year]
        return df2['Value'].values[0]
    except:
        return 0

#######################
# Program starts here #
#######################

# Read command line args. 
args = read_args(sys.argv)
if debug:
    print(args)
if (args["country"] != "" and args["date"] != ""):

    # Get covid dataframe
    df = covid_data(args["country"],args["province"],args["date"])

    # Print data if dataframe not empty
    if not df.empty:
        if debug:
            print(df)
        # Get and print country population size for 2018 (latest year data available)
        pop_sz = pop_size(args["country"], 2018)
        
        # Print selected covid data
        print_covid_data(df, pop_sz)
    else:
        print("Invalid or missing argument")