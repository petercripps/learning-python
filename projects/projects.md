## Projects
### covid19
Prints various country specific data on the COVID-19 pandemic using data from: https://datahub.io/docs/about.

covid19.csv that can be found here: https://datahub.io/core/covid-19. 

population.csv that can be found here: https://datahub.io/core/population.

In each case download the data (as CSV) into the files as named into a folder and set the path to the folder in the variable `path`. This variable is defined at the top of covid19.py.

General usage: 
`covid19.py info | rate | compare [options]`

`info` shows general COVID-19 data for a given country. 
Options are: 
`-c <country>` (required):    String containing valid country name e.g. 'United Kingdom'
`-p <province>` (optional):   String containing valid province name e.g. 'Bermuda'
`-d <date>` (required):       String containing date in form yyyy-mm-dd e.g. '2020-03-31'

`rate` shows death rate increase/decrease per day between a date range
Options are: 
`-c <country>` (required):    String containing valid country name e.g. 'United Kingdom'
`-p <province>` (optional):   String containing valid province name e.g. 'Bermuda'
`-f <date>` (required):       String containing from date in form yyyy-mm-dd e.g. '2020-03-31'
`-t <date>` (required):       String containing to date in form yyyy-mm-dd e.g. '2020-03-31'
`-g (optional)`               Draws a graph of the data

`compare` not currently implemented.

### population
Prints population by year (in the range 1960 to 2018).

Usage is as follows:

`population.py [options]`

Options are:
- `-c <country>` (required): String containing valid country name e.g. 'United Kingdom'
- `-f <year>` (required): Integer containing from year in form yyyy e.g. 1960
- `-t <year>` (required): Integer containing to date in form yyyy e.g. 2020