import streamlit as st
import pandas as pd

st.write("""
# Sales model
Below are our sales predictions for this customer.
""")

# df = pd.read_csv("my_data.csv")
# st.line_chart(df)
# file = st.file_uploader("Pick a file")

"""
# My first app
Here's our first attempt at using data to create a table:
"""

# df = pd.DataFrame({
#   'first column': [1, 2, 3, 4],
#   'second column': [10, 20, 30, 40]
# })

# df


st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))
