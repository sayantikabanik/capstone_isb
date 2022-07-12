import panel as pn
from base import (
    burnout_widget,
    suggestion_widget,
    recommendation_widget,
    comp_widget,
    location_widget
)


def plot():
    plot_component = pn.Row(burnout_widget)
    plot_component_02 = pn.Column(comp_widget, pn.Row(location_widget, height=200))
    plot_component_text = pn.Row(recommendation_widget, suggestion_widget)
    view = pn.template.FastListTemplate(
        site="Burn out analysis",
        title="For organisation",
        main=[plot_component, plot_component_02, plot_component_text]
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
