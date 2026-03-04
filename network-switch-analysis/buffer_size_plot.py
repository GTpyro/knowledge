import pandas as pd
import plotly.express as px
# import streamlit as st

data_url = "https://github.com/GTpyro/knowledge/raw/refs/heads/main/network-switch-analysis/Network%20Switch%20Performance.xlsx"


# @st.cache_data
def get_data(data_url: str) -> pd.DataFrame:
    return pd.read_excel(data_url)


switch_metrics = get_data(data_url)
switch_metrics["Total Port Count"] = (
    switch_metrics["port 1 count"]
    + switch_metrics["port 2 count"]
    + switch_metrics["port 3 count"]
    + switch_metrics["port 4 count"]
)
switch_metrics["Expected Switching Capacity"] = (
    switch_metrics["port 1 count"] * switch_metrics["port 1 speed"]
    + switch_metrics["port 2 count"] * switch_metrics["port 2 speed"]
    + switch_metrics["port 3 count"] * switch_metrics["port 3 speed"]
    + switch_metrics["port 4 count"] * switch_metrics["port 4 speed"]
) / 1000
switch_metrics["Average Port Speed (Gbps)"] = (
    switch_metrics["Expected Switching Capacity"] / switch_metrics["Total Port Count"]
)
switch_metrics["Time to Fill Buffer (s)"] = (
    switch_metrics["Buffer Size (MB)"]
    * 8
    / switch_metrics["Average Port Speed (Gbps)"]
    / 1000
)

fig6 = px.scatter(
    switch_metrics,
    x="Time to Fill Buffer (s)",
    y="Buffer Size (MB)",
    title="Network Switch Comparison",
    color="Manufacturer",
    labels={
        "Time to Fill Buffer (s)": "Round Trip Time (s)",
    },
    # size="Total Port Count",
    # symbol="Total Port Count",
    hover_data=["Model", "Switching Capacity (Gbps)"],
    log_x=True,
    log_y=True,
)
fig6.write_html("network_switch_comparison.html")
fig6.write_image("network_switch_comparison.png")
