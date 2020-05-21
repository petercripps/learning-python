import pandas as pd
from calcdata import calc_death_rates

# Format and print the dataframe and population data.
def print_covid_info(df, pop_sz):
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
            print("An error occurred")

# Format and print the dataframe for death rate for a single country.
def print_covid_country_rate(df):
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

            # Print date, number of deaths on that day and change over previous day
            death_rates = calc_death_rates(df)
            for death_rate in death_rates:
                print("Date:", death_rate[0], "Deaths: ", "{:,}".format(int(death_rate[1])), "Change: ", "{:,}".format(int(death_rate[2])))
        except ValueError:
            print("Inappropriate argument value")
        except:
            print("An error occured")

# Format and print the dataframe for death rate for multipe countries.
def print_covid_rate(country_data, rate):
    if country_data != []:
        for df in country_data:
            print_covid_country_rate(df)