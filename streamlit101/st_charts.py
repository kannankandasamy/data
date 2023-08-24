import streamlit as st
import pandas as pd
import numpy as np

st.header("Charts")
st.subheader("Line chart")

chart_df = pd.DataFrame(
    np.random.randn(20,3),
    columns = ['a','b','c']
)

st.line_chart(chart_df)

chart_df = pd.DataFrame(
    np.random.randn(20,2),
    columns = ['a','b']
)

st.line_chart(chart_df)
