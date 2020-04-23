# Code for analysing various COVID-19 data available from this data source:
# https://datahub.io/docs/about
# COVID-19 is specifically available here:
# https://datahub.io/core/covid-19

import pandas as pd

filename = 'covid19.csv'
date = "2020-04-22"
country = "United Kingdom"
province = "NaN"

# Read dataset as a panda dataframe
ds = pd.read_csv(filename)
df1 = pd.DataFrame(ds)

# Get data for particular date
df2 = df1[df1['Date'].str.contains(date)]

# Get data for particular country
df3 = df2[df2['Country/Region'].str.contains(country)]

# Get data for particular province
df4 = df3[df3['Province/State'].str.contains(province, na=False)]

print (df4)