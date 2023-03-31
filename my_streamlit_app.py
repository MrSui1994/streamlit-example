import streamlit as st
import pandas as pd
import numpy as np


[theme]
primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"

#左侧边栏
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )   

with st.container():
   st.write("This is inside the container")

   # You can call any Streamlit command, including custom components:
   st.bar_chart(np.random.randn(50, 3))

st.write("This is outside the line_chart")



chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c'])

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"],
    )
st.line_chart(chart_data)

#列
col1, col2, col3 = st.columns(3)
with col1:
    st.header("A cat")
    st.image('col1.webp')
    
with col2:
    st.header("A dog")
    st.image('col2.webp')

with col3:
    st.header("An owl")
    st.image('col3.webp')
#雪花
st.snow()
# 气球
st.balloons()