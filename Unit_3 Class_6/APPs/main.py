import streamlit as st

st.title("Welcome to Streamlit!")
st.write("This is a sample web app!")

name = st.text_input("Enter your name: ")
st.write("Hello", name)