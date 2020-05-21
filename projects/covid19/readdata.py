import pandas as pd
import numpy as np

# Defines absolute or relative path to where datasets are found.
path = "/Users/petercripps/Code/Python/Learning/datasets/"
coviddata = "covid19.csv"
popdata = "population.csv"

# Use this dictionary for differences between population dataset
# Name in covid dataset is the one that must be used in argument list
alternatives = {"US": "United States",
                "Syria": "Syrian Arab Republic"}
# If a country is in this list then it has no data at the country level, only
# for each of its provinces. Country level data must be derived therefore
no_country_data = ["Australia", "China"]

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
                df_temp = pd.DataFrame([[date, country,np.NaN,0,0,df3.Confirmed.sum(),df3.Recovered.sum(),df3.Deaths.sum()]], columns=list(df3))
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
            print("Invalid file or path")
    # Return selected covid data from last subset
    return df4

# Return COVID-19 rate data for multiple countries and a from date to date.
# Returns an array of pandas dataframes, one for each country.
def covid_rate_data(countries, fdate, tdate):
    df4 = pd.DataFrame()
    country_data = []
    if (countries != []) and (fdate != "") and (tdate != ""):
        try:
            # Read dataset as a panda dataframe
            df1 = pd.read_csv(path + coviddata)
            for country in countries:
                
                # Get subset of data for specified country/region
                df2 = df1[df1["Country/Region"] == country]
                
                # Ignore provinces.
                df3 = df2[df2["Province/State"].isnull()]
                if df3.empty:
                    print(f"Country level data not available for {country}")
                else:
                    # Get subset of data for date range
                    df4 = df3.loc[(df3["Date"] >= fdate) & (df3["Date"] <= tdate)]
                    country_data.append(df4)
        except FileNotFoundError:
            print("Invalid file or path")
    else:
        print("Invalid or missing argument")
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
        print("Invalid file or path")
        return 0

##########################
# Test program starts here
##########################
if __name__ == "__main__":
    # execute only if run as a script
    print("Testing...")
    country1 = "China"
    country2 = "Germany"
    date1 = "2020-05-10"
    date2 = "2020-05-14"
    
    if False:
        print(covid_info_data(country1, "", date1))
    if False:
        print(covid_rate_data([country1], date1, date2))
    if False:
        print(pop_data(country1, 2018))