import panel as pn
from base import (
    burnout_widget_client,
    burnout_widget_benchmark,
    suggestion_widget,
    recommendation_widget,
    comp_widget_c,
    location_widget_c,
    cluster_widget_c,
    comp_widget_b,
    location_widget_b,
    cluster_widget_b,
    pros_widget,
    cons_widget
)


def plot():
    plot_component_client = pn.Row(pn.Column(comp_widget_c, location_widget_c, cluster_widget_c, height=300), burnout_widget_client)
    plot_component_competitor = pn.Row(pn.Column(comp_widget_b, location_widget_b, cluster_widget_b, height=300), burnout_widget_benchmark)
    plot_component_whole = pn.Row(plot_component_client, plot_component_competitor)
    plot_component_text = pn.Column(suggestion_widget, recommendation_widget, margin=(0, 100, 100, 100))
    plot_pros_cons = pn.Column(pros_widget, cons_widget, margin=(0, 100, 100, 100))
    plot_text_whole = pn.Row(plot_component_text, plot_pros_cons)
    view = pn.template.FastListTemplate(
        site="Burn out analysis",
        title="For organisation",
        main=[plot_component_whole, plot_text_whole]
    )
    return view


if __name__ == "__main__":
    pn.serve(
        plot,
        port=5006,
        websocket_origin=['*'],
        autoreload=True,
        start=True,
        location=True,
        )
