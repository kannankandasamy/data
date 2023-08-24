import streamlit as st

st.title("My first st app")

nm = st.text_input("Enter your name","Kannan")
st.write(f"hello {nm}")

num = st.sidebar.text_input("Enter another name ", "test")

st.header("st.button")

if st.button("click here"):
    st.write("clicked hello button")
else:
    st.write("goodbye")