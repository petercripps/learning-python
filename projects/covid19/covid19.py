import pandas as pd
import sys
from readargs import read_args
from readdata import covid_info_data, pop_data, covid_rate_data
from printdata import print_covid_info, print_covid_rate
from graphdata import graph_covid_rate

# Get and print COVID-19 info for country, province and date.
def covid19_info(args):
    if (args["countries"] != [] and args["date"] != ""):

        # Get covid info as a Panda dataframe
        df = covid_info_data(args["countries"][0], args["province"], args["date"])
        
        # Print data if dataframe not empty
        if not df.empty:
            # Get and print country population size for 2018 (latest year data available)
            pop_sz = pop_data(args["countries"][0], 2018)
            
            # Print selected covid data
            print_covid_info(df, pop_sz)
        else:
            print("Invalid or missing argument")
    else:
        print("Invald country or date")

# Compare COVID-19 death rates between different countries and between from and to dates.
def covid19_rate(args):
    if (args["countries"] != [] and args["fdate"] != "" and args["fdate"] != ""):   
        
        # Get covid country rates as an array of panda dataframes
        country_data = covid_rate_data(args["countries"], args["fdate"], args["tdate"])

        # Print data if dataframe not empty
        if country_data != []:
            # Create a graph or print the data
            if args["graph"] == True:
                graph_covid_rate(country_data, args["rate"], args["measure"])
            else:
                print_covid_rate(country_data, args["measure"])
        else:
            print("Invalid or missing argument")
    else:
        print("Invald country or date")

############################
# Main program starts here #
############################

# Read command line args and take action depending on the 'operation' 
# entry of the returned dictionary.
args = read_args(sys.argv)
if args != {}:
    if args["operation"] == "info":
        covid19_info(args)
    elif args["operation"] == "rate":
        covid19_rate(args)
    else:
        print("Invalid operation")