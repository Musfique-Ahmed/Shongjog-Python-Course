import streamlit as st
import pandas as pd

st.title("👨‍⚕️ Doctor Directory")

data = pd.read_csv("Doctor_Directory.csv")

df = pd.DataFrame(data)

if "doctor_results" not in st.session_state:
    st.session_state.doctor_results = df

search_query = st.text_input("🔍 Search Doctor by Name:")

if st.button("Search"):
    st.session_state.doctor_results = df[df["Name"].str.contains(search_query, case=False, na=False)]

st.dataframe(st.session_state.doctor_results)

st.write("The search engine is still under maintainance!!")
st.write("Please wait for the final version.")

st.write("Copyright © 2025 [Ahnaf Mahmud Towseem Ahan](https://www.facebook.com/ahnafNahan). [All rights reserved](https://github.com/ANAHAN07/Project-from-songjog-course/blob/main/Medical%20Assistant/LICENSE).")      # LICENSE AND OWENERSHIP