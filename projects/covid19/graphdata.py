import pandas as pd
from datetime import datetime as dt
from bokeh.plotting import figure, output_file, show
from bokeh.models import DatetimeTickFormatter
from calcdata import calc_proportional_rate, calc_rates

# See https://docs.bokeh.org/en/latest/docs/reference/colors.html for colors    
line_colors = ["darkblue","darkcyan","darkgoldenrod","darkgray","darkgreen","darkgrey","darkkhaki","darkmagenta","darkolivegreen","darkorange",
    "darkorchid","darkred","darksalmon","darkseagreen","darkslateblue","darkslategray","darkslategrey","darkturquoise","darkviolet","deeppink",
    "deepskyblue","dodgerblue","firebrick","forestgreen","fuchsia","gold","goldenrod","gray","green","honeydew","hotpink","indianred","indigo"]  

# Create a line graph of COVID-19 rates for each country specified between the given dates.
# Up to 15 countries can be plotted (but only constrained by number of line colours)
# Parameters: 
# country_data : list
#   An array of covid19 Pandas dataframes, one for each country.
# rate : str 
#   Defines how rate should be calculated: 'absolute', 'hundred', 'million' or 'change'
# measure : str
#   Defines what number is being measured: 'Confirmed', 'Recovered' or 'Deaths'
# Returns:
# None

def graph_covid_rate(country_data, rate, measure):
    x = []
    multi_y = []
    countries = []
    rate_str = ""
    
    try:
        # First get dates which will be x-axis
        for date in country_data[0]['Date']: 
            date_obj = dt.strptime(date, "%Y-%m-%d")
            x.append(date_obj)
        
        # Print a status message
        print("Working...")
        # Get each country rate number for multi y-axes
        for df in country_data:
            countries.append(df.values[0][1])
            
            # Print a status message
            print(" ", df.values[0][1])
            y = []  
            if rate == 'change':
                change = calc_rates(df, measure)
                for i in change:
                    y.append(i[2])
            else:
                for num in df[measure]:
                    if rate == 'hundred' or rate == 'million':
                        prop_num = calc_proportional_rate(num, df.values[0][1],rate)
                        y.append(prop_num)
                    elif rate == 'absolute':    
                        y.append(num)
                    else:
                        print(__file__, "Invalid rate: ", rate)     
            multi_y.append(y)

        # output to static HTML file
        output_file("lines.html")

        # create a new plot with a title and axis labels
        if rate == 'hundred':
            rate_str = "per hundred thousand"
        elif rate == 'million': 
            rate_str = "per million"
        elif rate == 'change': 
            rate_str = "change over previous day"    
        p = figure(title="COVID-19 "+measure+" "+rate_str, plot_width=1200, plot_height=800, x_axis_label='Date', y_axis_label=measure, x_axis_type='datetime')

        # add a line renderer with legend and line thickness
        i = 0
        for y, country in zip(multi_y, countries):
            if i < len(line_colors):
                p.line(x, y, legend_label=country, line_width=4, line_color=line_colors[i])
                i += 1
            else:
                print(f"Cannot plot more than {len(line_colors)} line colors")
        p.xaxis.major_label_orientation = 3/4
        # p.add_layout(legend, 'right')
        # https://stackoverflow.com/questions/26254619/position-of-the-legend-in-a-bokeh-plot

        # show the results
        show(p)
        # Print a status message
        print("Complete")
    except IndexError: 
        print(__file__, "Error building graph")

##########################
# Test program starts here
##########################
if __name__ == "__main__":
    # execute only if run as a script
    print("Testing...")
    if False:
        df = pd.read_csv("covid19test.csv")
        graph_covid_rate([df], "hundred","Deaths")
