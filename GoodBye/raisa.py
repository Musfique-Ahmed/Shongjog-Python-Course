import streamlit as st
import pandas as pd
import json
import os
import threading
import plyer
import time
from datetime import datetime

st.sidebar.title (" Follow Me 💲 ")
page = st.sidebar.radio (" Go to -> ", [ "📝 Sign Up", "Adding Subject", "Study Plan", "Study Reminder", "Mark Completed and Progress",  ])

STUDY_PLAN_FILE = os.path.join(os.getcwd(), "study_plan.json")
REMINDERS_FILE = os.path.join(os.getcwd(), "reminders.json")

def load_study_plan():
    if os.path.exists(STUDY_PLAN_FILE):
        with open(STUDY_PLAN_FILE, "r") as file:
            return json.load(file)
    return []

def save_study_plan(study_plan):
    with open(STUDY_PLAN_FILE, "w") as file:
        json.dump(study_plan, file)

def load_reminders():
    if os.path.exists(REMINDERS_FILE):
        with open(REMINDERS_FILE, "r") as file:
            return json.load(file)
    return []

def save_reminders(reminders):
    with open(REMINDERS_FILE, "w") as file:
        json.dump(reminders, file)

st.session_state.setdefault("study_plan", load_study_plan())
st.session_state.setdefault("reminders", load_reminders())



if page == "📝 Sign Up":
    st.title("📚 Student Study Planner")
    st.subheader("Sign Up")
    name = st.text_input("📌 Full Name")
    user_class = st.text_input("🎓 Class")
    school = st.text_input("🏫 School Name")
    password = st.text_input("🔑 Password", type="password")

    USER_FILE = os.path.join(os.getcwd(), "users.json")

    def load_users():
        if os.path.exists(USER_FILE):
            with open(USER_FILE, "r") as file:
                return json.load(file)
        return {}

    def save_users(users):
        with open(USER_FILE, "w") as file:
            json.dump(users, file)

    def register_user(name, user_class, school, password):
        users = load_users()
        users[name] = {"class": user_class, "school": school, "password": password}
        save_users(users)
        return True

    if st.button("Register"):
        if register_user(name, user_class, school, password):
            st.success("✅ Registration successful!")
        else:
            st.error("❌ Registration unsuccessful!. Try again.")



elif page == "Information":
    st.title("📚 Student Study Planner")
    st.subheader("🕵️‍♂️ Enter the Following Information")

    name = st.text_input("Enter your name:").strip()
    student_class = st.text_input("Enter your class:").strip()
    school = st.text_input("Enter your school name:").strip()

    if st.button("Submit Information"):
        if name and student_class and school:
            st.success(f"🖐 Hello {name}, you are in class {student_class} at {school}!")
        else:
            st.error("⚠️ Please fill all blanks before submitting.")



elif page == "Adding Subject":
    st.title("📚 Student Study Planner")
    st.subheader("💲 Adding Subject")
    
    subject = st.text_input("Enter Subject:")
    study_time = st.slider("Study Time (minutes)", 15, 200, 60)

    st.subheader("Choose your subjects wisely! Focus on what challenges and excites you, and make sure to balance your workload. Every subject you add is a step toward your goals—stay organized and keep pushing forward!😊📚" )
    st.image("images.jpg")

    if "study_plan" not in st.session_state:
        st.session_state.study_plan = []

    if st.button("Add Subject"):
        if subject:  
            st.session_state.study_plan.append({"Subject": subject, "Study Time": study_time, "Completed": False})
            save_study_plan(st.session_state.study_plan)
            st.success(f"Added {subject} - {study_time} mins")
        else:
            st.error("⚠️ Please enter a subject before adding.")



elif page == "Study Plan":
    st.title("📚 Student Study Planner")
    st.subheader("📆 Your Study Plan")
    
    if st.session_state.study_plan:
        df = pd.DataFrame(st.session_state.study_plan)
        st.dataframe(df, height=400, width=700) 
    else:
        st.info("No subjects added yet!")
    
    st.subheader("A Study Planner is a tool designed to help students organize their study schedules efficiently. It allows users to manage their subjects, allocate study time, and track progress to enhance productivity and academic performance.")



elif page == "Study Reminder":
    st.title("📚 Student Study Planner")
    st.subheader("⏰ Study Reminder")
    
    if "reminders" not in st.session_state:
        st.session_state.reminders = []
        
    from datetime import datetime
    import winsound  
    
    def study_reminder(study_time, subject, reminder_type):
        while True:
            current_time = datetime.now().strftime("%H:%M")

            if current_time == study_time.strftime("%H:%M"):
                if reminder_type == "Notification":
                    plyer.notification.notify(
                        title="📢 Study Reminder",
                        message=f"⏰ Time to study {subject}! 📖",
                        timeout=10  
                        )

                elif reminder_type == "Alarm":
                    duration = 1000  
                    frequency = 2500  
                    winsound.Beep(frequency, duration)

                break  
            time.sleep(30)  

    study_time = st.time_input("📅 What time do you want to study?")
    
    subjects = [item["Subject"] for item in st.session_state.study_plan]
    if not subjects:
        subjects = ["Mathematics"] 

    subject = st.selectbox("📖 What subject do you want to study?", subjects)
    reminder_type = st.selectbox("🔔 How do you want the reminder?", ["Notification", "Alarm"])

    if st.button("✅ Set Reminder"):
        time_str = study_time.strftime("%H:%M")
        reminder_data = {"time": time_str, "subject": subject, "type": reminder_type}
        
        st.session_state.reminders.append(reminder_data)
        save_reminders(st.session_state.reminders)
        
        st.success(f"📅 Reminder set for {study_time} - '{subject}'!")

        reminder_thread = threading.Thread(target=study_reminder, args=(study_time, subject, reminder_type))
        reminder_thread.daemon = True
        reminder_thread.start()
        
    
    if st.session_state.reminders:
        st.subheader("Your existing reminders:")
        for idx, reminder in enumerate(st.session_state.reminders):
            st.write(f"{idx+1}. {reminder['subject']} at {reminder['time']} ({reminder['type']})")



else: 
    st.title("📚 Student Study Planner")
    st.subheader("✔️ Mark Completed")
    
    changed = False
    for i, task in enumerate(st.session_state.study_plan):
        completed = st.checkbox(f"{task['Subject']} - {task['Study Time']} mins", 
                              value=task.get('Completed', False),
                              key=f"complete_{i}")
        if completed != task.get('Completed', False):
            task["Completed"] = completed
            changed = True
    
    if changed:
        save_study_plan(st.session_state.study_plan)

    st.subheader("📊 Study Progress")
    completed = sum(1 for task in st.session_state.study_plan if task.get("Completed", False))
    total = len(st.session_state.study_plan)
    st.write(f"✅ Completed {completed}/{total} subjects today!")

    if completed == total and total > 0:  
       st.subheader("🎇 Congrats! You completed all subjects! 🎉")
    else:
       st.subheader("⚡ You need to work harder! Keep going! 💪")