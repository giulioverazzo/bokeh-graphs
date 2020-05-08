from os.path import dirname, join
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, Div
from bokeh.plotting import figure

from .helpers import read_csv, get_min_max, get_datetime_string

def setup():
  # Set up data
  filename = join(dirname(__file__), 'data', '202001.temp.csv')
  csv_list = read_csv(filename)

  csv_line = csv_list[0]
  x = [csv_line['temp_2m'], csv_line['temp_5m'], csv_line['temp_10m'], csv_line['temp_33m']]
  y = [2,5,10,33]
  source = ColumnDataSource(data=dict(x=x, y=y))

  x_min, x_max = get_min_max(csv_list)

  TOOLTIPS = [
    ("Temperature:", "$x °C"),
    ("Height:", "$y m")
  ]

  # Set up plot
  plot = figure(plot_height=700, plot_width=700, title="Vertical profiles",
                tools="crosshair,pan,reset,save,wheel_zoom",
                x_axis_label='Temperature [°C ]', 
                y_axis_label='Height [m]',
                tooltips=TOOLTIPS,
                x_range=[-25, 1],
                y_range=[0, 36])

  plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)
  plot.circle('x', 'y', source=source, size=8)

  # Set up widgets
  offset = Slider(title="Move the slider to change the time", value=0, start=0, end=len(csv_list) - 1, step=1, show_value=False, tooltips=False)
  html_text = get_datetime_string(csv_line)
  par = Div(text=html_text, width=200, height=100)

  # TODO: add text with date

  def update_data(attrname, old, new):
    # Generate the new curve   
    csv_line = csv_list[new]
    x = [csv_line['temp_2m'], csv_line['temp_5m'], csv_line['temp_10m'], csv_line['temp_33m']]
    par.text = get_datetime_string(csv_line)
    source.data = dict(x=x, y=y)
  
  offset.on_change('value', update_data)

  # Set up layouts and add to document
  inputs = column(offset, par)

  curdoc().add_root(row(inputs, plot, width=800))
  curdoc().title = "Profili verticali"

#def main():
#  filename = join(dirname(__file__), 'data', '202001.temp.csv')
#  read_csv(filename, setup)

# call main function
setup()