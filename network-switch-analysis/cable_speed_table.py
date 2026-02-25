import pandas as pd
import streamlit as st


data = {
    "Category": ["Cat 5e", "Cat 6", "Cat 6a", "Cat 8.1", ],
    "Year Introduced": [2001, 2002, 2008, 2016, ],
    "Data rate at 100m (Gbps)": [1, 1, 10, 0, ],
    "Max data rate (Gbps)": [2.5, 10, 10, 40, ],
    "Max length (m)": [100, 100, 100, 30, ],
    "Notes": [
        "Max data rate at 30m",
        "Max data rate at 55m",
        "Recommended cable for long runs in most residential and commercial scenarios",
        "Often referred to as Cat 8",
    ]
}

df = pd.DataFrame(data)
st.dataframe(df, hide_index=True, width="content")
