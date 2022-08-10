import panel as pn
import pandas as pd
import holoviews as hv
import hvplot.pandas
from analysis_framework.utils.text_summarization import summarize_text as stext
from analysis_framework.utils.text_summarization import summarize_text_lsa as stext_lsa
from analysis_framework.utils import burnout_index_calculation
from analysis_framework.utils import static as rs
hv.extension('bokeh')

location_widget_c = pn.widgets.Select(name='Location', options=rs.locations_dropdown, width=180)
cluster_widget_c = pn.widgets.Select(name='Cluster', options=rs.cluster_option,  width=180)
comp_widget_c = pn.widgets.Select(name='Company', options=rs.company_dropdown,  width=180)


location_widget_b = pn.widgets.Select(name='Location', options=rs.locations_dropdown, width=180)
cluster_widget_b = pn.widgets.Select(name='Cluster', options=rs.cluster_option,  width=180)
comp_widget_b = pn.widgets.Select(name='Company', options=rs.company_dropdown,  width=180)

# client
@pn.depends(location_widget_c.param.value,
            cluster_widget_c.param.value,
            comp_widget_c.param.value)
def burnout_widget_client(location_widget_c, cluster_widget_c, comp_widget_c):
    obj = burnout_index_calculation.Burnout(location_widget_c,
                                            comp_widget_c,
                                            cluster_widget_c)
    amber, green, red = obj.combine_scores()
    data = pd.DataFrame({'Not burned out': green, 'TOB': amber, 'Burned out': red}, index=['burnout_percentage'])
    chart = data.hvplot.bar(stacked=True, color=["green", 'yellow', 'red'],
                            width=400,
                            title="CLIENT",
                            legend_position='right',
                            legend_offset=(200, 200))
    return chart

# benchmark
@pn.depends(location_widget_b.param.value,
            cluster_widget_b.param.value,
            comp_widget_b.param.value)
def burnout_widget_benchmark(location_widget_b, cluster_widget_b, comp_widget_b):
    obj = burnout_index_calculation.Burnout(location_widget_b,
                                            comp_widget_b,
                                            cluster_widget_b)
    amber, green, red = obj.combine_scores()
    data = pd.DataFrame({'Not burned out': green, 'TOB': amber, 'Burned out': red}, index=['burnout_percentage'])
    chart = data.hvplot.bar(stacked=True, color=["green", 'yellow', 'red'],
                            width=400,
                            title="COMPETITOR",
                            legend_position='right',
                            legend_offset=(200, 200))
    return chart


def compile_text(df,text_column):
    compiled_text=''
    for text in df[text_column].fillna('NA.'):
        if text!='NA.' and text!='NA':
             compiled_text=compiled_text+' '+text
    return compiled_text


@pn.depends(location_widget_c.param.value,
            cluster_widget_c.param.value,
            comp_widget_c.param.value)
def suggestion_widget(location_widget_c, cluster_widget_c, comp_widget_c):
    obj = burnout_index_calculation.Burnout(location_widget_c,
                                            comp_widget_c,
                                            cluster_widget_c)
    filtered_output = obj.filtered_data()
    display_output = compile_text(filtered_output,'reviewText')
    suggestion = pn.Column(
        '# Feedback',
        pn.layout.Divider(),
        stext(display_output),
        background='#b8d1f5', height=400, width=500
    )
    return suggestion


@pn.depends(location_widget_c.param.value,
            cluster_widget_c.param.value,
            comp_widget_c.param.value)
def recommendation_widget(location_widget_c, cluster_widget_c, comp_widget_c):
    obj = burnout_index_calculation.Burnout(location_widget_c,
                                            comp_widget_c,
                                            cluster_widget_c)
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
        background='#f2f5da', height=600, width=500
    )
    return recommendation


@pn.depends(location_widget_b.param.value,
            cluster_widget_b.param.value,
            comp_widget_b.param.value)
def pros_widget(location_widget_b, cluster_widget_b, comp_widget_b):
    obj = burnout_index_calculation.Burnout(location_widget_b,
                                            comp_widget_b,
                                            cluster_widget_b)
    filtered_output = obj.filtered_data()
    display_output = compile_text(filtered_output,'pros')
    pros = pn.Column(
        '# Pros',
        pn.layout.Divider(),
        stext_lsa(display_output),
        background='#e4ede6', height=500, width=500
    )
    return pros


@pn.depends(location_widget_b.param.value,
            cluster_widget_b.param.value,
            comp_widget_b.param.value)
def cons_widget(location_widget_b, cluster_widget_b, comp_widget_b):
    obj = burnout_index_calculation.Burnout(location_widget_b,
                                            comp_widget_b,
                                            cluster_widget_b)
    filtered_output = obj.filtered_data()
    display_output=compile_text(filtered_output,'cons')
    cons = pn.Column(
        '# Cons',
        pn.layout.Divider(),
        stext_lsa(display_output),
        background='#fac8d3', height=500, width=500
    )
    return cons
