import panel as pn
import pandas as pd
import numpy as np
import hvplot.pandas
import holoviews as hv
from holoviews import opts, dim
from analysis_framework.utils.text_summarization import summarize_text as stext

hv.extension('bokeh')
from analysis_framework.utils import burnout_index_calculation
from analysis_framework.utils import static as rs

location_widget = pn.widgets.Select(name='Location', options=rs.locations_dropdown)
cluster_widget = pn.widgets.Select(name='cluster', options=rs.cluster_option)
comp_widget = pn.widgets.Select(name='company', options=rs.company_dropdown)


@pn.depends(location_widget.param.value,
            cluster_widget.param.value,
            comp_widget.param.value)
def burnout_widget(location_widget, cluster_widget, comp_widget):
    obj = burnout_index_calculation.Burnout(location_widget,
                                            comp_widget,
                                            cluster_widget)
    amber, green, red = obj.combine_scores()
    data = pd.DataFrame({'Not burned out': green, 'TOB': amber, 'Burned out': red}, index=['burnout_percentage'])
    chart = data.hvplot.bar(stacked=True, color=["green", 'yellow', 'red'],
                            width=400,
                            legend_position='right',
                            legend_offset=(200, 200))
    return chart


@pn.depends(location_widget.param.value,
            cluster_widget.param.value,
            comp_widget.param.value)
def suggestion_widget(location_widget, cluster_widget, comp_widget):
    obj = burnout_index_calculation.Burnout(location_widget,
                                            comp_widget,
                                            cluster_widget)
    filtered_output = obj.filtered_data()
    suggestion = pn.Column(
        '# Suggestion',
        pn.layout.Divider(),
        stext(filtered_output),
        background='whitesmoke', width=400
    )
    return suggestion


@pn.depends(location_widget.param.value,
            cluster_widget.param.value,
            comp_widget.param.value)
def recommendation_widget(location_widget, cluster_widget, comp_widget):
    obj = burnout_index_calculation.Burnout(location_widget,
                                            comp_widget,
                                            cluster_widget)
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
