import streamlit as st
import pandas as pd

st.title("My first st app")

nm = st.text_input("Enter your name","Kannan")
st.write(f"hello {nm}")

num = st.sidebar.text_input("Enter another name ", "test")

st.header("st.button")

if st.button("click here"):
    st.write("clicked hello button")
else:
    st.write("goodbye")

#st.subheader("Secrets")
#st.write(st.secrets['message'])

st.subheader("File Uploader")
up_file = st.file_uploader("Choose a file")

if up_file is not None:
    df = pd.read_csv(up_file)
    st.write(df)
    st.subheader("Descriptive statistics")
    st.write(df.describe())