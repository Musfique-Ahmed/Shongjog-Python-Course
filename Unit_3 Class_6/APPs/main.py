import streamlit as st

st.title("Welcome to Streamlit!")
st.write("This is a sample web app!")

name = st.text_input("Enter your name: ")
num = st.number_input("enter numebr")
st.selectbox("Choose", ["A","b" , "C"])
st.write("Hello", name)

st.button("Click me")
st.file_uploader("Upload File")