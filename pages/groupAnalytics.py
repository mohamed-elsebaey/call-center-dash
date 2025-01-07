import dash
from dash import html

dash.register_page(
    __name__, path="/GroupAnalytics", title="Group Analytics", name="Group Analytics"
)

layout = html.Div(
    [
        html.Div(
            [
                html.Div(
                    [
                        html.H2("Inbound Calls by Group"),
                    ],
                    className="inbound-calls",
                ),
                html.Div(
                    [
                        html.H2("Calls Answered by WorkGroup"),
                    ],
                    className="calls-answered",
                ),
            ],
            className="right-section",
        ),
        html.Div([], className="calls-flow-section"),
    ],
    className="group-analytics-layout",
)
