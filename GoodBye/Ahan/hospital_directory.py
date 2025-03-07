import streamlit as st
import pandas as pd

st.title("🏥 Hospital Directory")

data = pd.read_csv("Hospitals count in Bangladesh - Districtwise Divisionwise Upazilawise.csv")

df = pd.DataFrame(data)

# Use session state for search query
if "hospital_results" not in st.session_state:
    st.session_state.hospital_results = df

search_query = st.text_input("🔍 Search Hospital by Name:")

if st.button("Search"):
    st.session_state.hospital_results = df[df["Name"].str.contains(search_query, case=False, na=False)]

st.dataframe(st.session_state.hospital_results)

st.write("The search engine is still under maintainance!!")
st.write("Please wait for the final version.")

st.write("Copyright © 2025 [Ahnaf Mahmud Towseem Ahan](https://www.facebook.com/ahnafNahan). [All rights reserved](https://github.com/ANAHAN07/Project-from-songjog-course/blob/main/Medical%20Assistant/LICENSE).")      # LICENSE AND OWENERSHIP