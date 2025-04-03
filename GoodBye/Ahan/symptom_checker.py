import streamlit as st
import requests
from bs4 import BeautifulSoup


st.title("🔍 Symptom Checker")


if "results" not in st.session_state:
    st.session_state.results = []


query = st.text_input("Enter your symptoms:")


if st.button("Search"):
    if query:
        search_url = f"https://www.google.com/search?q={query} medical advice"
        headers = {"User-Agent": "Mozilla/5.0"}
        
        try:
            response = requests.get(search_url, headers=headers)
            response.raise_for_status()  # Raise error if request fails
            
            soup = BeautifulSoup(response.text, "html.parser")
            results = soup.find_all("h3")
            st.session_state.results = [result.text for result in results[:5]]

        except requests.exceptions.RequestException as e:
            st.error(f"Error fetching results: {e}")


if st.session_state.results:
    st.subheader("🔹 Search Results:")
    for result in st.session_state.results:
        st.write(result)


st.write("The search engine is still under maintainance!!")
st.write("Please wait for the final version.")


st.subheader("Fever")
st.write("""
* What it is?\n
A temporary increase in body temperature, usually due to an infection.
* Possible Causes:\n
   * Viral/Bacterial infections (Flu, COVID-19, Malaria)
   * Heatstroke
   * Inflammatory diseases (Rheumatoid Arthritis)
   * Cancer (in rare cases)
""")

st.subheader("Cough")
st.write("""
* What it is?\n 
A sudden, forceful expulsion of air to clear the throat or lungs.
* Possible Causes:\n
    Common Cold, Flu, or COVID-19
    Bronchitis or Pneumonia
    Asthma or Allergies
    GERD (Acid Reflux)
""")

st.subheader("Headache")
st.write("""
* What it is?\n
 Pain in any part of the head.
* Possible Causes:\n
    Migraine or Tension Headaches
    Sinus Infection
    Dehydration or Stress
    High Blood Pressure
""")

st.subheader("Sore Throat")
st.write("""
* What it is?\n 
Pain in any part of the head.
* Possible Causes:\n
    Migraine or Tension Headaches
    Sinus Infection
    Dehydration or Stress
    High Blood Pressure
""")

st.subheader("Fatigue")
st.write("""
* What it is?\n
Extreme tiredness or lack of energy.
* Possible Causes:\n
    Anemia (Low Iron)
    Thyroid Disorders
    Diabetes
    Sleep Disorders or Depression
""")

st.subheader("Shortness of Breath")
st.write("""
* What it is?\n 
Difficulty breathing or feeling unable to get enough air.
* Possible Causes:\n
    Asthma or COPD (Chronic Obstructive Pulmonary Disease)
    Pneumonia or COVID-19
    Heart Disease or Anxiety
    Pulmonary Embolism (Blood Clot in the Lungs)
""")

st.subheader("Chest Pain")
st.write("""
* What it is?\n 
Pain, pressure, or discomfort in the chest area.
* Possible Causes:\n
    Heart Attack or Angina (Reduced Blood Flow to the Heart)
    Acid Reflux (Heartburn)
    Lung Infection or Pneumonia
    Panic Attack
""")

st.subheader("Dizziness")
st.write("""
* What it is?\n 
A sensation of feeling unsteady or lightheaded.
* Possible Causes:\n
    Low Blood Pressure or Dehydration
    Inner Ear Problems (Vertigo)
    Neurological Conditions (Stroke)
    Low Blood Sugar (Hypoglycemia)
""")

st.subheader("Stomach Pain")
st.write("""
* What it is?\n 
Discomfort or cramping in the abdominal area.
* Possible Causes:\n
    Gastritis or Stomach Ulcers
    Food Poisoning or Irritable Bowel Syndrome (IBS)
    Appendicitis (Severe, Sudden Pain)
    Kidney Stones
""")

st.subheader("Skin Rash")
st.write("""
* What it is?\n
Redness, itching, or swelling of the skin.
* Possible Causes:\n
    Allergies (Food, Medication, or Contact Dermatitis)
    Eczema or Psoriasis
    Fungal or Bacterial Infections
    Autoimmune Disorders (Lupus)
""")

st.write("Those are some symptons. That people's frequantly searches.")


st.write("Copyright © 2025 [Ahnaf Mahmud Towseem Ahan](https://www.facebook.com/ahnafNahan). [All rights reserved](https://github.com/ANAHAN07/Project-from-songjog-course/blob/main/Medical%20Assistant/LICENSE).")      # LICENSE AND OWENERSHIP