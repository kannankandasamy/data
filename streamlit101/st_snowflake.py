import streamlit as st

st.header("Get data from Snowflake")

conn = st.experimental_connection('snowpark')
df = conn.query("select * from dim_customer;", ttl=600)

st.write(df)