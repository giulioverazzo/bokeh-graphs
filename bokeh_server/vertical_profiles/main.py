from os.path import dirname, join
from bokeh.io import curdoc
from bokeh.layouts import column, row
from bokeh.models import ColumnDataSource, Slider, TextInput
from bokeh.plotting import figure

from .helpers import read_csv, get_min_max

def setup():
  # Set up data
  filename = join(dirname(__file__), 'data', '202001.temp.csv')
  csv_list = read_csv(filename)

  csv_line = csv_list[0]
  x = [csv_line['temp_2m'], csv_line['temp_5m'], csv_line['temp_10m'], csv_line['temp_33m']]
  y = [2,5,10,33]
  source = ColumnDataSource(data=dict(x=x, y=y))

  #x_min, x_max = get_min_max(csv_list)

  # Set up plot
  plot = figure(plot_height=800, plot_width=800, title="Profili verticali",
              tools="crosshair,pan,reset,save,wheel_zoom")

  plot.line('x', 'y', source=source, line_width=3, line_alpha=0.6)
  plot.circle('x', 'y', source=source, size=8)

  # Set up widgets
  offset = Slider(title="Datetime", value=0, start=0, end=len(csv_list) - 1, step=1)

  # TODO: add text with date

  def update_data(attrname, old, new):
    # Generate the new curve   
    csv_line = csv_list[new]
    x = [csv_line['temp_2m'], csv_line['temp_5m'], csv_line['temp_10m'], csv_line['temp_33m']]
    source.data = dict(x=x, y=y)
  
  offset.on_change('value', update_data)

  # Set up layouts and add to document
  inputs = column(offset)

  curdoc().add_root(row(inputs, plot, width=800))
  curdoc().title = "Profili verticali"

#def main():
#  filename = join(dirname(__file__), 'data', '202001.temp.csv')
#  read_csv(filename, setup)

# call main function
setup()