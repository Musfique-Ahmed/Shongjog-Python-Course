import streamlit as st
import pandas as pd

st.title("🐾 Pet Care")

data = pd.read_csv("bangladesh_pet_care.csv")

df = pd.DataFrame(data)

# Use session state for search query
if "pet_doctor_results" not in st.session_state:
    st.session_state.pet_doctor_results = df

search_query = st.text_input("🔍 Search Pet Doctor by Name:")

if st.button("Search"):
    st.session_state.pet_doctor_results = df[df["Name"].str.contains(search_query, case=False, na=False)]

st.dataframe(st.session_state.pet_doctor_results)


st.write("The search engine is still under maintainance!!")
st.write("I wanted this section in 3 parts like: i)Doctor datas, ii)Pet medication articles, iii)AI chatbox for instant suggestions.")
st.write("Please wait for the final version.")


st.write("Copyright © 2025 [Ahnaf Mahmud Towseem Ahan](https://www.facebook.com/ahnafNahan). [All rights reserved](https://github.com/ANAHAN07/Project-from-songjog-course/blob/main/Medical%20Assistant/LICENSE).")      # LICENSE AND OWENERSHIP