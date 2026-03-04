from great_tables import GT, style, loc, html
import pandas as pd


data = {
    "Category": [
        "Cat 5",
        "Cat 5e",
        "Cat 6",
        "Cat 6e",
        "Cat 6a",
        "Cat7",
        "Cat 8.1",
        "Cat 9",
    ],
    "Year Introduced": [
        1995,
        2001,
        2002,
        2002,
        2008,
        2010,
        2016,
        None,
    ],
    "Data rate at 100m (Gbps)": [
        0.1,
        1,
        1,
        1,
        10,
        10,
        0,
        None,
    ],
    "Max data rate (Gbps)": [
        0.1,
        2.5,
        10,
        10,
        10,
        10,
        40,
        None,
    ],
    "Max length (m)": [
        100,
        100,
        100,
        100,
        100,
        100,
        30,
        None,
    ],
    "Notes": [
        "Deprecated since 2001",
        "Max data rate at 30m",
        "Max data rate at 55m",
        "Not an official standard so <br>not recommended for use",
        "Recommended cable for <br>long runs in most residential <br>and commercial scenarios",
        "Does not use RJ-45 <br>connectors. Limited availability. <br>Do not use",
        "Often referred to as Cat 8",
        "Does not exist as of 2026",
    ],
}

df = pd.DataFrame(data)


# apply styling
rows_to_highlight = ["Cat 5e", "Cat 6", "Cat 6a"]
my_table = (
    GT(df)
    .tab_header(title="Ethernet Cable Performance")
    .fmt_number(columns="Year Introduced", decimals=0, use_seps=False)
    .tab_style(
        style=[
            style.text(weight="bold"),
        ],
        locations=loc.body(rows=lambda df: df["Category"].isin(rows_to_highlight)),
    )
    .tab_style(
        style=[
            style.text(color="#A9A9A9"),
        ],
        locations=loc.body(rows=lambda df: ~df["Category"].isin(rows_to_highlight)),
    )
    .cols_label(
        cases={
            "Year Introduced": html("Year<br>Introduced"),
            "Data rate at 100m (Gbps)": html("Data rate at<br>100m (Gbps)"),
            "Max data rate (Gbps)": html("Max data<br>rate (Gbps)"),
            "Max length (m)": html("Max<br>length (m)"),
        }
    )
)

my_table.save("cable_speed_table.png")
