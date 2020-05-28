from datetime import datetime as dt
from bokeh.plotting import figure, output_file, show
from bokeh.models import DatetimeTickFormatter
from calcdata import calc_proportional_death_rate

# Create a line graph of COVID-19 death rates for each country specified between the given dates.
# Rate can be specified as an absolute or as per 100,000 or per 1,000,000
def graph_covid_rate(country_data, rate):
    x = []
    multi_y = []
    countries = []
    rate_str = ""
    line_colors = ["pink", "purple", "blue", "green", "orange", "red", "brown","plum", "peachpuff", "black", "turquoise", "darkgray", "darkseagreen", "lavendar", "yellow"]
    
    try:
        # First get dates which will be x-axis
        for date in country_data[0]['Date']: 
            date_obj = dt.strptime(date, "%Y-%m-%d")
            x.append(date_obj)

        # Get each country death rate for multi y-axes
        for df in country_data:
            countries.append(df.values[0][1])
            y = []
            for deaths in df['Deaths']:
                if rate == 'hundred' or rate == 'million':
                    prop_deaths = calc_proportional_death_rate(deaths, df.values[0][1],rate)
                    y.append(prop_deaths)
                else:    
                    y.append(deaths) 
            multi_y.append(y)

        # output to static HTML file
        output_file("lines.html")

        # create a new plot with a title and axis labels
        if rate == 'hundred':
            rate_str = "per hundred thousand"
        elif rate == 'million': 
            rate_str = "per million"
        p = figure(title="COVID-19 Deaths "+rate_str,plot_width=1200, plot_height=800, x_axis_label='Date', y_axis_label='Deaths', x_axis_type='datetime')

        # add a line renderer with legend and line thickness
        i = 0
        for y, country in zip(multi_y, countries):
            if i < len(line_colors):
                p.line(x, y, legend_label=country, line_width=2, line_color=line_colors[i])
                i += 1
            else:
                print(f"Cannot plot more than {len(line_colors)} line colors")
        p.xaxis.major_label_orientation = 3/4
        # p.add_layout(legend, 'right')
        # https://stackoverflow.com/questions/26254619/position-of-the-legend-in-a-bokeh-plot

        # show the results
        show(p)
    except IndexError: 
        print("Error building graph")
