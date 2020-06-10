import pandas as pd
from readdata import pop_data

# Calculate the change in number being measured from the previous day for each day in the provided
# Pandas dataframe. Return is an array as where each entry is an array as follows:
# [0] = Date
# [1] = num (actual)
# [2] = num (change)
def calc_rates(df, measure):
    rates = []
    prev_num = 0
    first = True
    for num, date in zip(df[measure], df['Date']):
        if first:
            # First time through no change to record
            prev_num = num
            first = False
            rates.append([date, num, 0])
        else:
            # All subsequent times through calculate death rate increase/decrease over previous day
            change = num - prev_num
            rates.append([date, num, change])
            prev_num = num
    return rates

# Calculate the proportional rate for an amount e.g. amount per 100,000 or amount per million of
# population.
def calc_proportional_rate(amount, country, rate):
    divisor = 1
    pop_sz = pop_data(country, 2018)
    if pop_sz > 0:
        if rate == 'hundred':
            divisor = pop_sz/100000
        elif rate == 'million':
            divisor = pop_sz/1000000
        else:
            print("Invalid rate: ", rate)
        return round(amount/divisor, 2)
    else:
        return 0

##########################
# Test program starts here
##########################
if __name__ == "__main__":
    # execute only if run as a script
    print("Testing...")
    if False:
        print(calc_proportional_rate(500, "United Kingdom", "hundred"))