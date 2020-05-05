# Code for analysing COVID-19 country data available from this data source:
# https://datahub.io/docs/about
# COVID-19 is specifically available here:
# https://datahub.io/core/covid-19
# This program analyses death rates over a range of dates giving daily increase/decrease.

import pandas as pd
import sys

# Defines absolute or relative path to where datasets are found.
path = "/Users/petercripps/Code/Python/Learning/datasets/"
# Set this to True to print out debug info.
debug = False

# Read command line arguments.
def read_args(args):
    # argdict will contain the required arguments
    argdict = {"country": "", "province": "", "fdate": "", "tdate": ""}
    
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
            elif args[i] == '-f':
                argdict["fdate"] = args[i + 1]
                i += 1
            elif args[i] == '-t':
                argdict["tdate"] = args[i + 1]
                i += 1    
            else:
                print("Unknown argument", args[i])
            i += 1    
    except IndexError:
        print("Invalid or missing argument")
    if debug:
        print(argdict)
    return argdict

# Print help.
def print_help():
    print("Usage: covidrates.py -c <country> -p <province> -f <date> -t <date>")
    print("Where:")
    print("-c <country> (required): String containing valid country name e.g. 'United Kingdom'")
    print("-p <province> (optional): String containing valid province name e.g. 'Bermuda'")
    print("-f <date> (required): String containing from date in form yyyy-mm-dd e.g. '2020-03-31'")
    print("-t <date> (required): String containing to date in form yyyy-mm-dd e.g. '2020-03-31'")

# Return COVID-19 data for country, province and fdate/tdate.
def covid_data(country, province, fdate, tdate):
    df4 = pd.DataFrame()
    if (country != "") and (fdate != "") and (tdate != ""):
        try:
            # Read dataset as a panda dataframe
            df1 = pd.read_csv(path + 'covid19.csv')

            # Get subset of data for specified country/region
            df2 = df1[df1["Country/Region"] == country]

            # Get subset of data for specified province. If none specified but there
            # are provinces the current dataframe will contain all with the first one being 
            # country and province as 'NaN'. In that case just select country otherwise select
            # province as well.
            if province == "":
                df3 = df2[df2["Province/State"].isnull()]
            else:
                df3 = df2[df2["Province/State"] == province]
            
            # Get subset of data for date range
            df4 = df3.loc[(df3["Date"] >= fdate) & (df3["Date"] <= tdate)]
        except FileNotFoundError:
            print("Invalid file or path")
    else:
        print("Invalid or missing argument")
    # Return selected covid data from last subset
    if debug:
        print(df4)
    return df4

# Format and print the dataframe for death rate.
def print_covid_data(df):
    if df.empty:
        print("Invalid or missing argument")
    else:
        try: 
            print("Country: ", df.values[0][1])
            
            # If no province specified cell will be null
            if pd.isnull(df.values[0][2]):
                print("Province: No province") 
            else:
                print("Province: ", df.values[0][2])

            # Print date, number of deaths on that day and rate increase/decrease over previous day
            # Rate is calculated by dividing current day by previous deaths
            # pdeaths is previous days deaths to allow rate calculation
            pdeaths = 0
            first = True
            for deaths, date in zip(df['Deaths'], df['Date']):
                if first:
                    # First time through just record previous days deaths, nothing to print for rate
                    pdeaths = deaths
                    first = False
                    print(f"Date: {date}, Deaths: {deaths}")
                else:
                    # All subsequent times through calcualte death rate increase/decrease over previous day
                    if pdeaths == 0:
                        rate = 0
                    else:
                        rate = deaths/pdeaths
                    print(f"Date: {date}, Deaths: {deaths}, Rate {round(rate, 3)}")
                    pdeaths = deaths
        except ValueError:
            print("Inappropriate argument value")
        except:
            print("An error occured")

#######################
# Program starts here #
#######################

# Read command line args. 
args = read_args(sys.argv)
if debug:
    print(args)
if (args["country"] != "" and args["fdate"] != "" and args["tdate"] != ""):

    # Get covid dataframe
    df = covid_data(args["country"],args["province"],args["fdate"],args["tdate"])

    # Print data if dataframe not empty
    if not df.empty:
        if debug:
            print(df)
        
        # Print covid data
        print_covid_data(df)
    else:
        print("Invalid or missing argument")
else:
        print("Invalid or missing argument")