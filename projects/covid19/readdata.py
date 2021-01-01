import pandas as pd
import numpy as np
import datetime as dt
import csv

# Define absolute path to where datasets are found.
path = "/Users/petercripps/Code/Python/Learning/datasets/"

# Define filenames. Covid data is a CSV file of the form:
# Date,Country/Region,Province/State,Confirmed,Recovered,Deaths.
coviddata = "covid19.csv"

# Population data is a CSV file of the form:
# Country Name,Country Code,Year,Value
popdata = "population.csv"

# Use this dictionary for differences between population dataset
# and covid dataset. Name in covid dataset is the one that must be passed in
# as an argument to this program and is the 'key' in this dictionary.
alternatives = {"US": "United States",
                "Czechia": "Czech Republic",
                "Burma": "Myanmar",
                "Slovakia": "Slovak Republic",
                "Syria": "Syrian Arab Republic",
                "Russia": "Russian Federation"}

# If a country is in this list then it has no data at the country level, only
# for each of its provinces. Country level data must be derived therefore
no_country_data = ["Australia", "China", "Canada"]

# Return COVID-19 info for country, province and date.
def covid_info_data(country, province, date):
    df4 = pd.DataFrame()
    if (country != "") and (date != ""):
        try:
            # Read dataset as a panda dataframe
            df1 = pd.read_csv(path + coviddata)

            # Get subset of data for specified country/region
            df2 = df1[df1["Country/Region"] == country]

            # Get subset of data for specified date
            df3 = df2[df2["Date"] == date]

            if country in no_country_data:
            # Create a new dataframe by summing the key data from each of the provinces of this country.
            # Other fields can be set to 0 or NaN
                df_temp = pd.DataFrame([[date, country,np.NaN,df3.Confirmed.sum(),df3.Recovered.sum(),df3.Deaths.sum()]], columns=list(df3))
                df3 = pd.concat([df_temp, df3])
                 
            # Get subset of data for specified province. If none specified but there
            # are provinces the current dataframe will contain all with the first one being 
            # country and province as 'NaN'. In that case just select country otherwise select
            # province as well.
            if province == "":
                df4 = df3[df3["Province/State"].isnull()]
            else:
                df4 = df3[df3["Province/State"] == province]
        except FileNotFoundError:
            print(__file__, "Invalid file or path")
    # Return selected covid data from last subset
    return df4

# Return COVID-19 rate data for multiple countries between 'fdate' and 'tdate'.
# Returns an array of pandas dataframes, one for each country.
def covid_rate_data(countries, fdate, tdate):
    country_data = []
    if (countries != []) and (fdate != "") and (tdate != ""):
        try:
            # Read dataset as a pandas data frame
            df_all = pd.read_csv(path + coviddata)
            for country in countries:
                
                # Get subset of data for specified country/region
                df_country = df_all[df_all["Country/Region"] == country]

                # Get subset of data for date range
                df_date = df_country.loc[(df_country["Date"] >= fdate) & (df_country["Date"] <= tdate)]

                if country in no_country_data:
                    # Country data is split across all provinces. Create a new data frame by summing the 
                    # key data from each of the provinces of this country for every date between fdate and tdate. 
                    # Other fields can be set to 0 or NaN. Note we start at tdate and go backwards in order to get
                    # data frames in ascending order.
                    date = tdate
                    df_final = pd.DataFrame()
                    while date != fdate: 
                        # Get all provinces for first date
                        df_one_date = df_date.loc[(df_date["Date"] == date)]
                        # Sum the data from each province into a new temp data frame
                        df_temp = pd.DataFrame([[date, country,np.NaN,df_one_date.Confirmed.sum(),df_one_date.Recovered.sum(),df_one_date.Deaths.sum()]],columns=list(df_all))
                        df_final = pd.concat([df_temp, df_final])
                        date = inc_date(date,-1)
                    # Get last entry
                    df_one_date = df_date.loc[(df_date["Date"] == date) ]
                    df_temp = pd.DataFrame([[date, country,np.NaN,df_one_date.Confirmed.sum(),df_one_date.Recovered.sum(),df_one_date.Deaths.sum()]],columns=list(df_all))
                    df_final = pd.concat([df_temp, df_final])
                    country_data.append(df_final)
                else:
                    # Ignore provinces.
                    df_final = df_date[df_date["Province/State"].isnull()]
                    
                    if df_final.empty:
                        print(f"Country level data not available for {country}")
                    else:
                        country_data.append(df_final)
        except FileNotFoundError:
            print(__file__, "Invalid file or path")
    else:
        print(__file__, "Invalid or missing argument")
    return country_data

# Return population of country for year (or 0 if none found).
def pop_data(country, year):
    # Check if country has an alternate name for this dataset
    if country in alternatives:
        country = alternatives[country]
    try:
        # Read dataset as a panda dataframe
        pop_df = pd.read_csv(path + popdata)
    
        # Get data for particular country
        df1 = pop_df[pop_df["Country Name"] == country]
        df2 = df1[df1["Year"] == year]
        return df2['Value'].values[0]
    except IndexError:
        print(f"Invalid country {country} or year {year}")
        return 0
    except FileNotFoundError:
        print(__file__, "Invalid file or path")
        return 0

# Takes a date as a string, increments it by amt and returns new date (as a string)
# Format assumed is '%Y-%m-%d'
def inc_date(date, amt):
    date_time_obj = dt.datetime.strptime(date, '%Y-%m-%d') 
    date_time_obj += dt.timedelta(days=amt)
    return date_time_obj.strftime('%Y-%m-%d')

# Read list of countries
def country_data():
    countries = []
    with open('countries.txt', mode ='r') as file: 
        lines = file.readlines()
        for line in lines:
            countries.append(line.strip())
    return countries

##########################
# Test program starts here
##########################
if __name__ == "__main__":
    # execute only if run as a script
    print("Testing...")
    country1 = "China"
    country2 = "United Kingdom"
    date1 = "2020-12-23"
    date2 = "2020-12-25"
    
    if False:
        print(covid_info_data(country2, "", date1))
    if False:
        print(covid_rate_data([country1, country2], date1, date2))
    if False:
        print(pop_data(country1, 2018))
    if False:
        print(inc_date("2020-05-29",1))
    if False:
        print(country_data())