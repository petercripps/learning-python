## Projects
### covid19
Prints various country specific data on the COVID-19 pandemic using data from: https://datahub.io/docs/about.

covid19.csv is [this file](https://pkgstore.datahub.io/core/covid-19/time-series-19-covid-combined_csv/data/4377c9f681df7cf9393745df53ed3bc6/time-series-19-covid-combined_csv.csv) that can be found here: https://datahub.io/core/covid-19. 

population.csv is [this file](https://pkgstore.datahub.io/core/population/population_csv/data/e23cbc93dc1e8b8814ed62d73fc36c33/population_csv.csv) that can be found here: https://datahub.io/core/population.

In each case download the data (as CSV) into the files as named into a folder and set the path to the folder in the variable `path`. This variable is defined at the top of covid19.py.

Usage is as follows:

`covid19.py -c <country> -p <province> -d <date>`

Where:
- `-c country` (required): String containing valid country name e.g. 'United Kingdom'
- `-p province` (optional): String containing valid province name e.g. 'Bermuda'
- `-d date` (required): String containing date in form yyyy-mm-dd e.g. '2020-03-31'

### population
Prints population by year (in the range 1960 to 2018).

Usage is as follows:

`population.py -c <country> -f <date> -t <date>`

Where:
- `-c <country>` (required): String containing valid country name e.g. 'United Kingdom'
- `-f <year>` (required): Integer containing from year in form yyyy e.g. 1960
- `-t <year>` (required): Integer containing to date in form yyyy e.g. 2020

### covidrates
Analyses death rates over a range of dates giving daily increase/decrease.

Usage is as follows:

`covidrates.py -c <country> -p <province> -f <date> -t <date>`

Where:
- `-c <country>` (required): String containing valid country name e.g. 'United Kingdom'
- `-p <province>` (optional): String containing valid province name e.g. 'Bermuda'
- `-f <date>` (required): String containing from date in form yyyy-mm-dd e.g. '2020-03-31'
`-t <date>` (required): String containing to date in form yyyy-mm-dd e.g. '2020-04-30'
