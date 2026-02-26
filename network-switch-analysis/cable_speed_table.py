import pandas as pd
import streamlit as st


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
        "Not an official standard so not recommended for use",
        "Recommended cable for long runs in most residential and commercial scenarios",
        "Does not use RJ-45 connectors. Limited availability. Do not use",
        "Often referred to as Cat 8",
        "Does not exist as of 2026",
    ],
}

df = pd.DataFrame(data)


# apply styling
def highlight_rows(row) -> list:
    if row["Category"] in ["Cat 5e", "Cat 6", "Cat 6a"]:
        return ["font-weight: bold"] * len(row)
    return ["color: grey"] * len(row)


st.dataframe(
    df.style.apply(highlight_rows, axis=1),
    hide_index=True,
    width="content",
    placeholder="-",
)
