import streamlit as st
st.title("Columns Example")
col1, col2 = st.columns(2)
with col1:
    st.header("Column 1")
    st.write("This is the first column")
    st.button("Button for Col1")

with col2:
    st.header("Column 2")
    st.write("This is the second column")
    st.button("Button for Co2")