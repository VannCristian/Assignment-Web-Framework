import streamlit as st
import pandas as pd
import numpy as np
import time

with st.spinner('Wait for it...'):
    time.sleep(5)
st.success('Done!')

st.info('This is a purely informational message', icon="ℹ️")
st.write("Line chart")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)
st.snow()
st.balloons()

st.subheader("Widgets:")

st.write("Slider")
x = st.slider('x')  
st.write(x, 'squared is', x * x)

st.write("Text input")
st.text_input("Your name", key="name")
st.session_state.name



add_selectbox = st.sidebar.selectbox(
    'Would you like to be my girlfriend?',
    ('Yes', 'No', 'Temenan ajah')
)


add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

@st.cache_data(ttl=600)
def load_data(sheets_url):
    csv_url = sheets_url.replace("/edit#gid=", "/export?format=csv&gid=")
    return pd.read_csv(csv_url)

df = load_data(st.secrets["public_gsheets_url"])

# Print results.
for row in df.itertuples():
    st.write(f"{row.Nama} has a :{row.Pet}:")