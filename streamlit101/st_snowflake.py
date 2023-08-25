import streamlit as st

st.header("Get data from Snowflake")

conn = st.experimental_connection('snowpark')
df = conn.query("""select product_id, sum(total_amount) as Amount  from sales_fact 
                group by product_id;""", ttl=600)

st.write(df)

st.subheader("Chart below")
st.line_chart(df)