import panel as pn
pn.extension('echarts')


def plot():
    widget_01 = pn.indicators.LinearGauge(
    name='Burnout check', value=20, bounds=(0, 100), format='{value:.0f} %',
    colors=['green', 'gold', 'red'], horizontal=True, width=125
)
    widget_02 = pn.widgets.Select(name='Company', options=['Infosys', 'Wipro', 'TCS'], size=3)

    menu_items = [('Option A', 'a'), ('Option B', 'b'), ('Option C', 'c'), None, ('Help', 'help')]
    widget_03 = pn.widgets.MenuButton(name='Location', items=menu_items, button_type='primary')

    text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
    ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation 
    ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in
    reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
    mollit anim id est laborum.
    """

    recommendation = pn.Column(
        '# Recommendation',
        pn.layout.Divider(),
        text,
        background='whitesmoke', width=400
    )

    suggestion = pn.Column(
        '# Suggestion',
        pn.layout.Divider(),
        text,
        background='whitesmoke', width=400
    )

    plot_component = pn.Row(widget_01)
    plot_component_02 = pn.Column(widget_02, pn.Row(widget_03, height=200))
    plot_component_text = pn.Row(recommendation, suggestion)
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
