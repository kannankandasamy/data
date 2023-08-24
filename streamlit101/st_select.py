import streamlit as st

st.header("Different select options")

#Single select code
st.subheader("Simple select box")
option = st.selectbox(
    "Your favorite color",
    ('Blue','Green','Black')
)
st.write("Your selected color : ", option)

#Multiselect code
st.subheader("Multi select box")
options = st.multiselect(
    "Your favorite colors",
    ['Blue', 'Green','Red', 'Yellow'],
    ['Yellow', 'Red']
)
st.write("Selected colors : ", options)

#Checkbox code
st.subheader("Checkbox")
st.write("Select food to order: ")
puri = st.checkbox("Poori")
idly = st.checkbox("Idly")
coffee = st.checkbox("Coffee")
tea = st.checkbox("Tea")

if puri:
    st.write("Selected puri")
if idly:
    st.write("Selected Idly")
if coffee:
    st.write("Selected coffee")
if tea:
    st.write("Selected tea")
