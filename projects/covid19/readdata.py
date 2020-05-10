import pandas as pd

# Defines absolute or relative path to where datasets are found.
path = "/Users/petercripps/Code/Python/Learning/datasets/"
coviddata = "covid19.csv"
popdata = "population.csv"

# Use this dictionary for differences between population dataset (key) and covid dataset (value)
# Name in population dataset is the one that must be used in argument list
alternatives = {"United States": "US",
                "Syrian Arab Republic": "Syria"}

# Return COVID-19 info for country, province and date.
def covid_info_data(country, province, date):
    df4 = pd.DataFrame()
    if (country != "") and (date != ""):
        try:
            # Read dataset as a panda dataframe
            df1 = pd.read_csv(path + coviddata)

            # Check if country has an alternate name for this dataset
            if country in alternatives:
                country = alternatives[country]

            # Get subset of data for specified country/region
            df2 = df1[df1["Country/Region"] == country]

            # Get subset of data for specified date
            df3 = df2[df2["Date"] == date]

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

# Return population of country for year (or 0 if none found).
def pop_data(country, year):
    try:
        # Read dataset as a panda dataframe
        pop_df = pd.read_csv(path + popdata)
    
        # Get data for particular country
        df1 = pop_df[pop_df["Country Name"] == country]
        df2 = df1[df1["Year"] == year]
        return df2['Value'].values[0]
    except FileNotFoundError:
        print("Invalid file or path")
        return 0

# Return COVID-19 rate data for country, province and fdate/tdate.
def covid_rate_data(country, province, fdate, tdate):
    df4 = pd.DataFrame()
    if (country != "") and (fdate != "") and (tdate != ""):
        try:
            # Read dataset as a panda dataframe
            df1 = pd.read_csv(path + coviddata)

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
    return df4