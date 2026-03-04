from great_tables import GT, style, loc, html
import pandas as pd

data = {
    "Application": [
        "File transfer across<br> a <b>fast home</b> network",
        "File transfer across<br> a <b>slow home</b> network",
        "Streaming <b>multiple videos</b><br> while surfing the web",
        "<b>Core switch</b> at a<br> small business",
    ],
    "RTT": [20, 20, 100, 200],
    "C": [1000, 100, 100, 5000],
    "N": [50, 50, 1000, 10000],
    "B": [20, 2, 0.3, 10],
    "Comments": [
        "A <b>higher end</b> <br>switch is needed",
        "Only a <b>moderate</b> <br>switch is needed",
        "A very <b>modest</b> <br>switch is needed",
        "Only a <b>moderate</b> s<br>witch is needed",
    ]
}

df = pd.DataFrame(data)
my_table = (
    GT(df)
    .tab_header(title="Buffer Size Examples")
    .fmt_number(columns="B", drop_trailing_zeros=True)
    .cols_label(
        cases={
            "RTT": html("Round Trip <br>Time (RTT) (ms)"),
            "C": html("Link Bandwidth<br> (Mbps)"),
            "N": html("Number of <br>Simultaneous Flows"),
            "B": html("Buffer <br>Size (MB)")
        }
    )
)
my_table.save("network_rtt_table.png")