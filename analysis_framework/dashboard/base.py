import panel as pn
import numpy as np
pn.extension('echarts')
from analysis_framework.utils import burnout_index_calculation

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
    print(amber, green, red)
    gauge = pn.indicators.LinearGauge(
        name='Burnout check', value=50, bounds=(0, 100), format='{value:.0f} % for the org',
        colors=[(np.round(green, 1), 'green'), (amber, 'gold'), (1, 'red')], show_boundaries=True
    )
    return gauge


def suggestion_widget():
    suggestion = pn.Column(
        '# Suggestion',
        pn.layout.Divider(),
        text,
        background='whitesmoke', width=400
    )
    return suggestion


def recommendation_widget():
    recommendation = pn.Column(
        '# Recommendation',
        pn.layout.Divider(),
        text,
        background='whitesmoke', width=400
    )
    return recommendation


def location_widget():
    menu_items = [('Option A', 'a'), ('Option B', 'b'), ('Option C', 'c'), None, ('Help', 'help')]
    location = pn.widgets.MenuButton(name='Location', items=menu_items, button_type='primary')
    return location


def comp_widget():
    company = pn.widgets.Select(name='Company', options=['Infosys', 'Wipro', 'TCS'], size=3)
    return company

