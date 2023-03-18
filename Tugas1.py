import pandas as pd
import numpy as np
import streamlit as st

st.title("Tugas 1 - membuat line chart")

st.header("Data")
# df = pd.DataFrame({"murid": [adi, 30, 40, 50], "nilai": [15, 25, 45, 55]})
df = pd.DataFrame(np.random.randn(20, 3))
st.write(df)

st.header("Line Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)