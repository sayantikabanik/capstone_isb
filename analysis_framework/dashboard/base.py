import panel as pn
import pandas as pd
import numpy as np
import hvplot.pandas
import holoviews as hv
from holoviews import opts, dim


hv.extension('bokeh')
from analysis_framework.utils import burnout_index_calculation
from analysis_framework.utils import static as rs

text = """
   Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
   ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
   ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
   reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
   Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
   mollit anim id est laborum.
   """


def burnout_widget():
    obj = burnout_index_calculation.Burnout()
    amber, green, red = obj.combine_scores()
    data = pd.DataFrame({'Not burned out': green, 'TOB': amber, 'Burned out': red}, index=['burnout_percentage'])
    chart = data.hvplot.bar(stacked=True, color=["green", 'yellow', 'red'],
                            width=400,
                            legend_position='right',
                            legend_offset=(200, 200))
    return chart


def suggestion_widget():
    suggestion = pn.Column(
        '# Suggestion',
        pn.layout.Divider(),
        text,
        background='whitesmoke', width=400
    )
    return suggestion


def recommendation_widget():
    obj = burnout_index_calculation.Burnout()
    amber, green, red = obj.combine_scores()
    if amber <= 40:
        amber_text = rs.amber["0-40"]
    elif 40 < amber < 80:
        amber_text = rs.amber["40-80"]
    else:
        amber_text = rs.amber["80-100"]

    if red <= 40:
        red_text = rs.red["0-40"]
    elif 40 < red < 80:
        red_text = rs.red["40-80"]
    else:
        red_text = rs.red["80-100"]
    recommendation = pn.Column(
        '# Recommendation',
        pn.layout.Divider(),
        pn.Column(amber_text, red_text),
        background='whitesmoke', width=400
    )
    return recommendation


def location_widget():
    menu_items = [('Option A', 'a'), ('Option B', 'b'), ('Option C', 'c'), None, ('Help', 'help')]
    location = pn.widgets.MenuButton(name='Location', items=menu_items, button_type='primary')
    return location


def cluster_widget():
    menu_items = [('Option A', '1'), ('Option B', '2'), ('Option C', '3'), None, ('Help', 'help')]
    cluster = pn.widgets.MenuButton(name='cluster', items=menu_items, button_type='primary')
    return cluster


def comp_widget():
    menu_items = [('Option A', 'Infosys'), ('Option B', 'TCS'), ('Option C', 'Wipro'), None, ('Help', 'HCL')]
    company = pn.widgets.MenuButton(name='company', items=menu_items, button_type='primary')
    return company
