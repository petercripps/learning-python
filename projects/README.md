## Projects
### covid19
Prints various country specific data on the COVID-19 pandemic using data from: https://datahub.io/docs/about.

The contents of covid19.csv can be found here: https://datahub.io/core/covid-19#resource-time-series-19-covid-combined. Look for 'time-series-19-covid-combined'.

population.csv that can be found here: https://datahub.io/core/population.

In each case download the data (as CSV) into the files as named into a folder and set the path to the folder in the variable path. This variable is defined at the top of covid19.py. There is also a basic UI for entering data that way. Just use appwindow.py.

General usage:<br> 
covid19.py info | rate [options]<br>

'info' shows general COVID-19 data for a given country.<br> 

Options are:<br>
-c <country> (required):    String containing valid country name e.g. 'United Kingdom'<br>
-p <province> (optional):   String containing valid province name e.g. 'Bermuda'<br>
-d <date> (required):       String containing date in form yyyy-mm-dd e.g. '2020-03-31'<br>

'rate' shows death rate increase/decrease per day between a date range<br>

Options are:<br> 
-c <country> (required):    String containing valid country name e.g. 'United Kingdom'<br>
-p <province> (optional):   String containing valid province name e.g. 'Bermuda'<br>
-f <date> (required):       String containing from date in form yyyy-mm-dd e.g. '2020-03-31'<br>
-t <date> (required):       String containing to date in form yyyy-mm-dd e.g. '2020-03-31'<br>
-g (optional):              Draws a graph of the data<br>
-r (optional): absolute | hundred | million specifies how death rate is calculated, absolute number, per hundred thousand or per million<br>

If no parameters are provided the program will look for a file called 'covid19.yaml' and will read data from that.
An example of this file is:<br>

  countries:<br>
    - United Kingdom<br>
    - Spain<br>
    - Italy<br>
  operation: rate<br>
  date: "2020-03-01"<br>
  fdate: "2020-02-01"<br>
  tdate: "2020-05-09"<br>
  province: ""<br>
  graph: False<br>
  rate: absolute<br>

operation must be one of: info | rate<br>
rate must be one of absolute | hundred | million<br>

### population
Prints population by year (in the range 1960 to 2018).<br>

General usage:<br>
population.py [options]<br>

Options are:<br>
-c <country> (required): String containing valid country name e.g. 'United Kingdom'<br>
-f <year> (required): Integer containing from year in form yyyy e.g. 1960<br>
-t <year> (required): Integer containing to date in form yyyy e.g. 2020<br>