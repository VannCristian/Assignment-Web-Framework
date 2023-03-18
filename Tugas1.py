import pandas as pd
import numpy as np
import streamlit as st

st.title("Tugas 1 - membuat line chart")

st.header("Data")
import streamlit as st
import pandas as pd
df = pd.DataFrame({
  'first column': [10, 30, 50, 70],
  'second column': [20, 40, 60, 80]
})

df

st.header("Line Chart")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["A", "B", "C"])
st.line_chart(chart_data)