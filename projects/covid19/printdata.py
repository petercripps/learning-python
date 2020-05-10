import pandas as pd

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
            print("Unknown error occurred")

# Format and print the dataframe for death rate.
def print_covid_rate(df):
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
            # Change is calculated by subtracting current day from previous days deaths
            # pdeaths is previous days deaths to allow change calculation
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
                        change = 0
                    else:
                        change = deaths - pdeaths
                    print("Date: ",date, "Deaths: ", "{:,}".format(int(deaths)), "Change: ", "{:,}".format(int(change)))
                    pdeaths = deaths
        except ValueError:
            print("Inappropriate argument value")
        except:
            print("An error occured")