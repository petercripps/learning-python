import pandas as pd
import sys
from readargs import read_args
from printdata import print_covid_info, print_covid_rate
from readdata import covid_info_data, pop_data, covid_rate_data
from graphdata import graph_covid_rate

# Get and print COVID-19 info for country, province and date.
def covid19_info(args):
    if (args["country"] != "" and args["date"] != ""):

        # Get covid info as a Panda dataframe
        df = covid_info_data(args["country"],args["province"],args["date"])

        # Print data if dataframe not empty
        if not df.empty:
            # Get and print country population size for 2018 (latest year data available)
            pop_sz = pop_data(args["country"], 2018)
            
            # Print selected covid data
            print_covid_info(df, pop_sz)
        else:
            print("Invalid or missing argument")
    else:
        print("Invald country or date")

# Get and print COVID-19 rate for country, province and fdate/tdate.
def covid19_rate(args):
    if (args["country"] != "" and args["fdate"] != "" and args["fdate"] != ""):
            
        # Get covid rate as a Panda dataframe
        df = covid_rate_data(args["country"],args["province"],args["fdate"], args["tdate"])

        # Print data if dataframe not empty
        if not df.empty:
            # Print selected covid data
            print_covid_rate(df)
            if args["graph"] == True:
                graph_covid_rate(df)
        else:
            print("Invalid or missing argument")
    else:
        print("Invald country or date")

def covid19_compare(args):
    print("Not currently implemented")

############################
# Main program starts here #
############################

# Read command line args and take action depending on the 'operation' 
# entry of the returned dictionary.
args = read_args(sys.argv)
if args["operation"] == "info":
    covid19_info(args)
elif args["operation"] == "rate":
    covid19_rate(args)
elif args["operation"] == "compare":
    covid19_compare(args)
else:
     print("Invalid operation")
