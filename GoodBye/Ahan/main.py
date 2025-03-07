import streamlit as st

st.set_page_config(
    page_title="Medical Diagnosis Assistant",
    page_icon="⚕️",  
    layout="wide"
)

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Symptom Checker", "Health Advice", "Doctor Directory", 
                                  "Hospital Directory", "Medical History", "Pet Care", "AI Chatbox", "Pharmacy", "Contact to Website Author"])

if page == "Symptom Checker":
    import symptom_checker
elif page == "Health Advice":
    import health_advice
elif page == "Doctor Directory":
    import doctor_directory
elif page == "Hospital Directory":
    import hospital_directory
elif page == "Medical History":
    import medical_history
elif page == "Pet Care":
    import pet_care
elif page == "AI Chatbox":
    import ai_chatbox
elif page == "Pharmacy":
    import pharmacy
elif page == "Contact to Website Author":
    from contact_author import contact_box
    contact_box()
