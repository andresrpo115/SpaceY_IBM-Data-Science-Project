# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px


# ---------------------------------------------------------
# Load and prepare the SpaceX launch dataset
# ---------------------------------------------------------

spacex_df = pd.read_csv("spacex_launch_dash.csv")

# Get the minimum and maximum payload values for the range slider
min_payload = spacex_df["Payload Mass (kg)"].min()
max_payload = spacex_df["Payload Mass (kg)"].max()


# ---------------------------------------------------------
# Create the Dash application
# ---------------------------------------------------------

app = dash.Dash(__name__)


# ---------------------------------------------------------
# Create the application layout
# ---------------------------------------------------------

app.layout = html.Div(
    children=[
        html.H1(
            "SpaceX Launch Records Dashboard",
            style={
                "textAlign": "center",
                "color": "#503D36",
                "fontSize": 40
            }
        ),

        # -------------------------------------------------
        # TASK 1: Add a launch site dropdown
        # -------------------------------------------------

        dcc.Dropdown(
            id="site-dropdown",
            options=[{"label": "All Sites", "value": "ALL"}] + [
                {"label": site, "value": site}
                for site in spacex_df["Launch Site"].unique()
            ],
            value="ALL",
            placeholder="Select a Launch Site here",
            searchable=True,
            clearable=False
        ),

        html.Br(),

        # -------------------------------------------------
        # TASK 2: Pie chart container
        # -------------------------------------------------

        html.Div(
            dcc.Graph(id="success-pie-chart")
        ),

        html.Br(),

        html.P("Payload range (Kg):"),

        # -------------------------------------------------
        # TASK 3: Add a payload range slider
        # -------------------------------------------------

        dcc.RangeSlider(
            id="payload-slider",
            min=0,
            max=10000,
            step=1000,
            marks={
                0: "0",
                1000: "1000",
                2000: "2000",
                3000: "3000",
                4000: "4000",
                5000: "5000",
                6000: "6000",
                7000: "7000",
                8000: "8000",
                9000: "9000",
                10000: "10000"
            },
            value=[min_payload, max_payload]
        ),

        html.Br(),

        # -------------------------------------------------
        # TASK 4: Scatter chart container
        # -------------------------------------------------

        html.Div(
            dcc.Graph(id="success-payload-scatter-chart")
        )
    ]
)


# ---------------------------------------------------------
# TASK 2: Update the success pie chart
# ---------------------------------------------------------

@app.callback(
    Output(
        component_id="success-pie-chart",
        component_property="figure"
    ),
    Input(
        component_id="site-dropdown",
        component_property="value"
    )
)
def get_pie_chart(selected_site):
    """
    Render a pie chart based on the selected launch site.

    If all sites are selected, the chart displays the number
    of successful launches for each site.

    If a specific site is selected, the chart compares
    successful and failed launches for that site.
    """

    if selected_site == "ALL":

        # Keep only successful launches
        successful_launches = spacex_df[
            spacex_df["class"] == 1
        ]

        # Count successful launches for each site
        success_by_site = (
            successful_launches
            .groupby("Launch Site")
            .size()
            .reset_index(name="Success Count")
        )

        figure = px.pie(
            success_by_site,
            values="Success Count",
            names="Launch Site",
            title="Total Successful Launches by Site"
        )

    else:

        # Filter the dataset for the selected launch site
        filtered_df = spacex_df[
            spacex_df["Launch Site"] == selected_site
        ]

        # Count successful and failed outcomes
        outcome_counts = (
            filtered_df["class"]
            .value_counts()
            .reindex([0, 1], fill_value=0)
            .rename_axis("class")
            .reset_index(name="Launch Count")
        )

        # Replace numeric class values with descriptive labels
        outcome_counts["Outcome"] = outcome_counts["class"].map(
            {
                0: "Failed",
                1: "Successful"
            }
        )

        figure = px.pie(
            outcome_counts,
            values="Launch Count",
            names="Outcome",
            title=f"Launch Outcomes for {selected_site}",
            color="Outcome",
            color_discrete_map={
                "Successful": "green",
                "Failed": "red"
            }
        )

    return figure


# ---------------------------------------------------------
# TASK 4: Update the payload versus launch outcome chart
# ---------------------------------------------------------

@app.callback(
    Output(
        component_id="success-payload-scatter-chart",
        component_property="figure"
    ),
    [
        Input(
            component_id="site-dropdown",
            component_property="value"
        ),
        Input(
            component_id="payload-slider",
            component_property="value"
        )
    ]
)
def get_payload_scatter_chart(selected_site, payload_range):
    """
    Render a scatter chart based on the selected launch site
    and payload range.

    The x-axis represents payload mass, the y-axis represents
    the launch outcome, and point colors represent the booster
    version category.
    """

    minimum_payload = payload_range[0]
    maximum_payload = payload_range[1]

    # Filter records according to the selected payload range
    payload_filtered_df = spacex_df[
        (
            spacex_df["Payload Mass (kg)"] >= minimum_payload
        )
        & (
            spacex_df["Payload Mass (kg)"] <= maximum_payload
        )
    ]

    if selected_site == "ALL":

        # Display launches from all sites
        filtered_df = payload_filtered_df

        chart_title = (
            "Payload Mass versus Launch Outcome for All Sites"
        )

    else:

        # Display launches only from the selected site
        filtered_df = payload_filtered_df[
            payload_filtered_df["Launch Site"] == selected_site
        ]

        chart_title = (
            f"Payload Mass versus Launch Outcome for {selected_site}"
        )

    figure = px.scatter(
        filtered_df,
        x="Payload Mass (kg)",
        y="class",
        color="Booster Version Category",
        hover_data=[
            "Launch Site",
            "Booster Version Category"
        ],
        title=chart_title,
        labels={
            "Payload Mass (kg)": "Payload Mass (kg)",
            "class": "Launch Outcome"
        }
    )

    # Make the binary launch outcome easier to understand
    figure.update_yaxes(
        tickmode="array",
        tickvals=[0, 1],
        ticktext=["Failed", "Successful"]
    )

    return figure


# ---------------------------------------------------------
# Run the Dash application
# ---------------------------------------------------------

if __name__ == "__main__":
    app.run()