import streamlit as st
from datetime import time, datetime

st.header("Slider demo")

st.subheader("Sub Slider")

num = st.slider("Enter a number: ", 0, 130, 25)
st.write("Entered number ", num)

st.subheader("Range slider")
values = st.slider(
    "Select a range of values",
    0.0,100.0, (25.0,75.0)
)
st.write("values:", values)

st.subheader("Range time slider")
apmt = st.slider(
    "Select your appointment: ",
    value = (time(11,30), time(13,45)))
st.write("Appointment time : ", apmt)

st.subheader("Date slider")
apmt = st.slider(
    "Select your Date: ",
    value = datetime(2023,8,24,9,30),
    format = "YYYY/MM/DD - hh:mm"
    )
st.write("Appointment date : ", apmt)

st.subheader("Changing theme using slider")
st.code("""
[theme]
primaryColor="#F39C12"
backgroundColor="#2E86C1"
secondaryBackgroundColor="#AED6F1"
textColor="#FFFFFF"
font="monospace"
"""
)
num = st.sidebar.slider("Select a number : ", 0,10,5)
st.write("Selected slider widget : ",num)