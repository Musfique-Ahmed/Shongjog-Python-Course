import streamlit as st

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills & Experience", "Contact"])

# Home Page
if page == "Home":
    st.title("👋 Welcome to My Portfolio!")
    st.image("https://avatars.githubusercontent.com/u/9919?s=200&v=4", width=150)  # Placeholder image
    st.write("Hi, I'm Musfique Ahmed, a Data Science student passionate about AI and Machine Learning.")
    st.write("This portfolio showcases my projects, skills, and experience.")

# Projects Page
elif page == "Projects":
    st.title("🚀 My Projects")
    projects = [
        {"name": "Doc App", "desc": "AI-powered digital hospital system.", "link": "https://github.com/Anik-Mushfik/doc-app"},
        {"name": "CMED", "desc": "Cloud-based rural healthcare system.", "link": "https://github.com/Anik-Mushfik/cmed"},
    ]
    for project in projects:
        st.subheader(project["name"])
        st.write(project["desc"])
        st.markdown(f"[GitHub Link]({project['link']})")
        st.write("---")

# Skills & Experience Page
elif page == "Skills & Experience":
    st.title("📌 Skills & Experience")
    st.write("- Python, Machine Learning, Data Science")
    st.write("- Streamlit, Flask, Tkinter")
    st.write("- Git, GitHub, SQL, Pandas")
    st.write("- Teaching Python for Kids & General Students")
    st.write("- Working on AI-driven projects at AIMS Lab, UIU")

# Contact Page
elif page == "Contact":
    st.title("📞 Contact Me")
    st.write("📧 Email: anikmushfik@gmail.com")
    st.write("🔗 [LinkedIn](https://linkedin.com/in/musfique-ahmed-aa89a5293)")
    st.write("🐙 [GitHub](https://github.com/Anik-Mushfik)")
    st.write("📱 Phone: 01961905838")

# Run this with: streamlit run <filename>.py
