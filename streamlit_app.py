import streamlit as st
import pandas as pd

st.write("""
# Sales model
Below are our sales predictions for this customer.
""")

# df = pd.read_csv("my_data.csv")
# st.line_chart(df)
file = st.file_uploader("Pick a file")
