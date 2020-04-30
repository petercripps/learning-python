# Code for analysing population data available from this data source:
# https://datahub.io/docs/about
# Population data is specifically available here:
# https://datahub.io/core/population
# See https://plotly.com/dash/ for creating dashboards

import pandas as pd
import sys

# Defines absolute or relative path to where datasets are found.
path = "../../../datasets/"

# Print help.
def print_help():
    print("Usage: population.py -c <country> -f <date> -t <date>")
    print("Where:")
    print("-c <country> (required): String containing valid country name e.g. 'United Kingdom'")
    print("-f <year> (required): Integer containing from year in form yyyy e.g. 1960")
    print("-t <year> (required): Integer containing to date in form yyyy e.g. 2020")

# Read command line arguments.
def read_args():
    fyear = 0
    tyear = 0
    country = ""
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
                elif arg == '-f':
                    fyear = sys.argv[index+1]
                elif arg == '-t':
                    tyear = sys.argv[index+1]
                else:
                    print("Invalid argument: ", arg)
            except IndexError:
                print("Invalid number of arguments")
            except:
                print("Input error")
            index = index + 2       
    return [country, int(fyear), int(tyear)]

# Return population of country between specified years.
def pop_data(country, fyear, tyear):
    pop_df = pd.DataFrame()

    if (fyear < 1960 or fyear > 2018) or (tyear < 1960 or tyear > 2018):
        print("From date or to date is out of range (1960 - 2018)")
    else:
        try:
            # Read dataset as a panda dataframe
            df1 = pd.read_csv(path + 'population.csv')
                
            # Get data for particular country
            df2 = df1[df1["Country Name"] == country]

            # Get data for date range
            pop_df = df2.loc[(df2['Year'] >= fyear) & (df2['Year'] <= tyear)]
        except FileNotFoundError:
            print("Invalid file")
        except:
            print("Index error")
    return pop_df

# Print population data for country
def print_pop_data(df, country):
    if df.empty:
        print("Missing or invalid argument(s)")
    else: 
        print("Data for:", country)
        for year, value in zip(df['Year'], df['Value']):
            print("Year:", year, ", Population:", "{:,}".format(value))

#####################
# Program starts here
#####################

# Read command line args 
args = read_args()
if args:

    # Get population dataframe
    df = pop_data(args[0],args[1],args[2])

    # Print data if dataframe not empty
    if not df.empty:
        
        # Print selected population data
        print_pop_data(df, args[0])
    else:
        print("Missing or invalid argument(s)")