## Projects
### covid19
Prints various country specif data on the COVI-19 pandemic using data from: https://datahub.io/docs/about.

covid19.csv is [this file](https://pkgstore.datahub.io/core/covid-19/time-series-19-covid-combined_csv/data/4377c9f681df7cf9393745df53ed3bc6/time-series-19-covid-combined_csv.csv) that can be found here: https://datahub.io/core/covid-19. 

population.csv is [this file](https://pkgstore.datahub.io/core/population/population_csv/data/e23cbc93dc1e8b8814ed62d73fc36c33/population_csv.csv) that can be found here: https://datahub.io/core/population.

In each case download tha data (as CSV) into the files as named into a folder and set the path to the folder in the variable `path`.

Usage is as follows:

`covid19.py -c <country> -p <province> -d <date>")'

Where:
<country> (required): String containing valid country name e.g. 'United Kingdom')
<province> (optional): String containing valid province name e.g. 'Bermuda')
<date> (required): String containing date in form yyyy-mm-dd e.g. '2020-03-31')
