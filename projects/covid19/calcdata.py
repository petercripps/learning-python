import pandas as pd
from readdata import pop_data

def calc_death_rates(df):
    death_rates = []
    pdeaths = 0
    first = True
    for deaths, date in zip(df['Deaths'], df['Date']):
        if first:
            # First time through no change to record
            pdeaths = deaths
            first = False
            death_rates.append([date, deaths, 0])
        else:
            # All subsequent times through calculate death rate increase/decrease over previous day
            change = deaths - pdeaths
            death_rates.append([date, deaths, change])
            pdeaths = deaths
    return death_rates

# Calculate the proportional death rate i.e. deaths per 100,000 of population for
# total number of deaths in a country.
def calc_proportional_death_rate(deaths, country, rate):
    pop_sz = pop_data(country, 2018)
    if pop_sz > 0:
        if rate == 'hundred':
            divisor = pop_sz/100000
        else:
            divisor = pop_sz/1000000
        return round(deaths/divisor, 2)
    else:
        return 0