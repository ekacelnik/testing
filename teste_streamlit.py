import streamlit as st
import pandas as pd

st.markdown("### Welcome to my first st-app :balloon:")
st.write("Here's our first attempt at using data to create a graph from a pandas dataframe:")
df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
})

st.line_chart(data=df, x='first column', y='second column', width=0, height=0, use_container_width=True)