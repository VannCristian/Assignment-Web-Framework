import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image


# 1. Write and Magic

st.title("1. Write and Magic")
st.write('Hello, masbro :sunglasses:')

df = pd.DataFrame({'col1': [1,2,3]})
df 

# 2. Text Element

st.title("2. Text Element")

st.markdown('my name is :red[Vannes] **:blue[Cristian]**')

st.markdown('The **_:green[closer]_** you think you are , the **_:green[Less]_** you will actually see')

# 3. Data Display Elements
st.title("3. Data Display Elements")
df = pd.DataFrame(
   np.random.randn(10, 5),
   columns=('col %d' % i for i in range(5)))

st.table(df)

# 4. Chart Elements
st.title("4. Chart Elements")
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

st.area_chart(chart_data)

# 5. Input Widget
st.title("5. Input Widget")

options = st.multiselect(
    'apakah saya ganteng?',
    ['Yes', 'Yes banget', 'Super ganteng', 'ultimate ganteng'],
    ['Super ganteng', 'Yes banget'])

st.write('You selected:', options)


# 6. Media Elements
st.title("6. Media Elements")

img = Image.open("Ellie.JPG")

st.image(img, caption='Ellie from The Last Of Us 2')


# 7. Layouts and Containers
st.title("7. Layouts and Containers")

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

with st.container():
   st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the container")




# 8. Status Element
st.title("8. Status Element")
st.warning('hati-hati pacar di rebut', icon="⚠️")

st.error("[ERROR]: maaf anda kurang beruntung", icon="🪲")

# 9. Control Flow
st.title("9. Control Flow")

name = st.text_input('Name')
if not name:
  st.warning('Please input a name.')
  st.stop()
st.success('Thank you for inputting a name.')

# 10. Utilities
st.title("10. Utilities")

st.help(pandas.DataFrame)