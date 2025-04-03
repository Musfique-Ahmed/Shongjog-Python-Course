import streamlit as st

st.sidebar.title("Navigation")
page = st.sidebar.radio("GO to", ["Home", "Projects", "Skills", "Contact"])



if page == "Home":
    st.title("Welcome to my Portfolio!")
    st.image("image.png", "Python", 500)
    st.image("image_2.png")
    st.write("Hi i am Musfique Ahmed, a data Science Student at UIU.")
    st.write("This portfolio showcases my works")

elif page == "Projects":
    st.title("🤯 My Projects!")

    st.subheader("Monkey Pox detector")
    st.write("this project is an ml pproject to detect monkey pox!")
    st.markdown("[GitHubLink](https://github.com/Musfique-Ahmed/monkeypox-perdition-app)")
    st.write("---")


elif page== "Contact":
    st.title("MY contact")
    st.write("Email: anbdgshbh@gmail.com")
    st.write("[GitHub](https://github.com/Musfique-Ahmed)")