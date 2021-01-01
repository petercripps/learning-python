import pandas as pd
from calcdata import calc_rates

# Format and print the dataframe and population data. The dataframe is formatted as follows:
# df.values[0][0]) == "Date"
# df.values[0][1]) == "Country"
# df.values[0][2]) == "Province"
# df.values[0][3]) == "Confirmed"
# df.values[0][4]) == "Recovered"
# df.values[0][5]) == "Deaths"
def print_covid_info(df, pop_sz):
    if df.empty:
        print(__file__, "Invalid or missing argument")
    else:
        try:    
            print("Date: ", df.values[0][0])
            print("Country: ", df.values[0][1])
            
            # If no province specified cell will be null
            if pd.isnull(df.values[0][2]):
                print("Province: No province") 
            else:
                print("Province: ", df.values[0][2])
            confirmed = int(df.values[0][3])
            deaths = int(df.values[0][5])
            print("Confirmed: ", "{:,}".format(confirmed))
            print("Recovered: ", "{:,}".format(int(df.values[0][4])))
            print("Deaths: ", "{:,}".format(deaths))
            if pop_sz > 0:
                print("Population: ", "{:,}".format(pop_sz))
                divisor = pop_sz/100000
                print("Confirmed/100,000:", round(df.values[0][3]/divisor, 2))
                print("Deaths/100,000:", round(df.values[0][5]/divisor, 2))
                print("Percent Deaths/Confirmed:", round((deaths/confirmed)*100, 2))
            else:
                print("Population: Unknown")
        except ValueError:
            print(__file__, "Inappropriate argument value")
        except:
            print(__file__, "An error occurred")

# Format and print the dataframe for number being measured for a single country.
def print_covid_country_rate(df, measure):
    if df.empty:
        print(__file__, "Invalid or missing argument")
    else:
        try: 
            print("Country:", df.values[0][1])
            
            # If no province specified cell will be null
            if pd.isnull(df.values[0][2]):
                print("Province: No province") 
            else:
                print("Province:", df.values[0][2])

            # Print date, number being measured on that day and change over previous day
            rates = calc_rates(df, measure)
            for rate in rates:
                print("Date", rate[0], measure, "{:,}".format(int(rate[1])), "Change", "{:,}".format(int(rate[2])))
        except ValueError:
            print(__file__, "Inappropriate argument value")
        except:
            print(__file__, "An error occured")

# Format and print the dataframe for death rate for multipe countries.
def print_covid_rate(country_data, measure):
    if country_data != []:
        for df in country_data:
            print_covid_country_rate(df, measure)