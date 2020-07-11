import pandas as pd
import sys
from readargs import read_args
from readdata import covid_info_data, pop_data, covid_rate_data
from printdata import print_covid_info, print_covid_rate
from graphdata import graph_covid_rate

# Start the program having loaded up parameters into argdict
def run_covid19(argdict):
    if argdict != {}:
        if argdict["operation"] == "info":
            covid19_info(argdict)
        elif argdict["operation"] == "rate":
            covid19_rate(argdict)
        else:
            print("Invalid operation: ", argdict["operation"])

# Get and print COVID-19 info for country, province and date.
def covid19_info(argdict):
    if (argdict["countries"] != [] and argdict["fdate"] != ""):

        # Get covid info as a Panda dataframe
        df = covid_info_data(argdict["countries"][0], argdict["province"], argdict["fdate"])
        
        # Print data if dataframe not empty
        if not df.empty:
            # Get and print country population size for 2018 (latest year data available)
            pop_sz = pop_data(argdict["countries"][0], 2018)
            
            # Print selected covid data
            print_covid_info(df, pop_sz)
        else:
            print("Invalid or missing argument")
    else:
        print("Invald country or date")

# Compare COVID-19 death rates between different countries and between from and to dates.
def covid19_rate(argdict):
    if (argdict["countries"] != [] and argdict["fdate"] != "" and argdict["fdate"] != ""):   
        
        # Get covid country rates as an array of panda dataframes
        country_data = covid_rate_data(argdict["countries"], argdict["fdate"], argdict["tdate"])

        # Print data if dataframe not empty
        if country_data != []:
            # Create a graph or print the data
            if argdict["graph"] == True:
                graph_covid_rate(country_data, argdict["rate"], argdict["measure"])
            else:
                print_covid_rate(country_data, argdict["measure"])
        else:
            print("Invalid or missing argument")
    else:
        print("Invald country or date")

############################
# Main program starts here #
############################
if __name__ == "__main__":

    # Read command line args and take action depending on the 'operation' 
    # entry of the returned dictionary.
    argdict = read_args(sys.argv)
    run_covid19(argdict)