from datetime import datetime as dt
from bokeh.plotting import figure, output_file, show
from bokeh.models import DatetimeTickFormatter

def graph_covid_rate(df):
    x = []
    y = []
    country = df.values[0][1]
    for deaths, date in zip(df['Deaths'], df['Date']):
        y.append(deaths) 
        date_obj = dt.strptime(date, "%Y-%m-%d")
        x.append(date_obj)

    # output to static HTML file
    output_file("lines.html")

    # create a new plot with a title and axis labels
    p = figure(title="COVID-19 Deaths for "+country, x_axis_label='Date', y_axis_label='Deaths', x_axis_type='datetime')

    # add a line renderer with legend and line thickness
    p.line(x, y, legend_label="COVID-19 Deaths for "+country, line_width=3, line_color="green")
    p.xaxis.major_label_orientation = 3/4

    # show the results
    show(p)