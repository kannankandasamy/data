import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.header("Write functions")

# words in *...* written in italic and inside :...: will be an emoji
st.write("hello *world* :smiley:")

st.write(1234)

df = pd.DataFrame({
    'first col':[1,2,3,4],
    'second col':[10,20,30,40]
})

#st.write(df)

st.write("Pandas Dataframe below: ", df, "dataframe above")

df2 = pd.DataFrame(
    np.random.randn(200,3),
    columns = ['A','B','C']
)

#to hide indexes
#st.dataframe(df2)
#st.dataframe(df2.style.hide(axis="index"))
st.markdown(df2.style.hide(axis="index").to_html(), unsafe_allow_html=True)

c= alt.Chart(df2).mark_circle().encode(
    x='A',y="B", size = "C", tooltip = ['A','B','C']
)
st.write(c)