"""
https://docs.bokeh.org/en/latest/docs/gallery/pie_chart.html
"""

from math import pi

import pandas as pd

from bokeh.palettes import Category20
from bokeh.plotting import figure, show
from bokeh.transform import cumsum
from bokeh.io import save

def draw_pie(tag_frequency, save_file_name=None):
    """ Use bokeh to draw a pie chart of frequencies of HTML element tags
    Optionally save plot to file """

    data = pd.Series(tag_frequency).reset_index(name='value').rename(columns={'index': 'element'})
    data['angle'] = data['value']/data['value'].sum() * 2*pi

    data_point_count = len(tag_frequency)
    biggest_pallete = Category20[len(Category20) - 1]
    pallete_len = len(biggest_pallete)
    repeats = (int( data_point_count / pallete_len )) + 1
    pallete = biggest_pallete * repeats
    pallete = pallete[:len(tag_frequency)]  # slice len of data 

    data['color'] = pallete

    p = figure(height=1000, title="Pie Chart", toolbar_location=None,
            tools="hover", tooltips="@element: @value", x_range=(-0.5, 1.0))

    p.wedge(x=0, y=1, radius=0.4,
            start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
            line_color="white", fill_color='color', legend_field='element', source=data)

    p.axis.axis_label = None
    p.axis.visible = False
    p.grid.grid_line_color = None

    show(p)

    if save_file_name:
        save(p, save_file_name)