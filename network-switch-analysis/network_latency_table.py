from great_tables import GT, style, loc, html
import pandas as pd

data = {
    "Environment": [
        "LAN, wired",
        "LAN, wireless",
        "Within a region",
        "Across regions",
        "Across continents",
        "Worst case global",
    ],
    "Example": [
        "Home or office network",
        "Home or office network",
        "Central India to south India<br> Central Canada to eastern US",
        "US east coast to west coast",
        "Australia to Japan<br>US to Poland",
        "Brazil to Indonesia<br>Australia to Israel",
    ],
    "Latency": [
        "3-10ms",
        "15-25ms",
        "5-25ms",
        "55-80ms",
        "100-200ms",
        "300+ms",
    ],

}

df = pd.DataFrame(data)
my_table = (
    GT(df)
    .tab_header(title="Typical one way latencies")
)
my_table.save("network_latency_table.png")