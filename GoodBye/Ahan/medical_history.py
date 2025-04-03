import streamlit as st

st.title("📜 Medical History")

st.subheader("Login Required to Save Data")

username = st.text_input("Enter your username")
password = st.text_input("Enter your password", type="password")

if st.button("Login"):
    st.success(f"Welcome {username}! You can now upload your prescription.")

st.subheader("Upload Prescription")
file = st.file_uploader("Choose a file", type=["jpg", "png", "pdf"])

if file:
    st.success("Prescription uploaded successfully!")

st.write("I have just done the outer section. But due to short time I cant make this functionable.")
st.write("Please wait for the final version.")

st.write("Copyright © 2025 [Ahnaf Mahmud Towseem Ahan](https://www.facebook.com/ahnafNahan). [All rights reserved](https://github.com/ANAHAN07/Project-from-songjog-course/blob/main/Medical%20Assistant/LICENSE).")      # LICENSE AND OWENERSHIP