import streamlit as st

# Task 2: Sidebar Navigation Menu
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Projects", "Skills & Experience", "Contact"])

# Task 3: Design Each Page
if page == "Home":
    st.title("Welcome to My Portfolio")
    st.image("https://via.placeholder.com/150", caption="Professional Image")
    st.write("Hi there! I'm DAIYAN, a PYTHON DEVELOPER. Welcome to my portfolio site. Here you'll find information about my projects, skills, experience, and how to contact me.")

elif page == "Projects":
    st.title("Projects")
    projects = [
        {"title": "Project 1", "description": "Brief description of Project 1", "github": "https://github.com/yourusername/project1"},
        {"title": "Project 2", "description": "Brief description of Project 2", "github": "https://github.com/yourusername/project2"},
        {"title": "Project 3", "description": "Brief description of Project 3", "github": "https://github.com/yourusername/project3"}
    ]
    
    for project in projects:
        st.subheader(project["title"])
        st.write(project["description"])
        st.write(f"[GitHub Repository]({project['github']})")

elif page == "Skills & Experience":
    st.title("Skills & Experience")
    skills = ["python", "driving car", "data analysis", "laptop motherboard work", "any work"]
    experience = ["Job 1 ZTE", "Job 2 at HP", "Internship at AN ENTERPRIZE"]
    
    st.subheader("Skills")
    for skill in skills:
        st.markdown(f"- {skill}")
    
    st.subheader("Experience")
    for exp in experience:
        st.markdown(f"- {exp}")

elif page == "Contact":
    st.title("Contact")
    st.write("Feel free to reach out to me through the following channels:")
    st.write("Email: [youremail@example.com](mail:ahnaf.rahman.daiyan@gmail.com)")
    st.write("LinkedIn: [Your LinkedIn Profile](https://linkedin.com/in/yourusername)")
    st.write("GitHub: [Your GitHub Profile](https://github.com/yourusername)")
    st.write("Phone: +8801407450808")

# Task 4: Improve User Experience
# Add images/icons, use st.markdown() for styling, and use st.columns() for better layout
st.sidebar.title("Improvement Options")