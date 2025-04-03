import streamlit as st

st.title (" 🎯 Fun Quiz Game ")
st.title (" Test your knowledge! Choose the correct answers below. ")

quiz_data = [

    { "title": "General Knowledge",
    "question" : "What is the largest ocean in the world?" ,
    "options" : [ " Atlantic Ocean ", " Indian Ocean ", " Pacific Ocean ", " Arctic Ocean " ] ,
    "answer" : " Pacific Ocean " } ,
     
    { "question" : "Who wrote the play Romeo and Juliet?" ,
     "options" : [ "William Shakespeare", "Charles Dickens", "Mark Twain", "Jane Austen" ] ,
     "answer" : "William Shakespeare"} ,

    { "question" : "How many continents are there on Earth?" ,   
    "options" : [ " 5 ", " 6 ", " 7 ", " 8 " ] ,
    "answer" : " 7 " } ,


    { "title": "Science & Technology",
    "question" : "What gas do plants absorb during photosynthesis?" ,   
    "options" : [ " Oxygen ", " Carbon Dioxide ", " Nitrogen ", " Hydrogen " ] ,
    "answer" : " Carbon Dioxide " } ,

    { "question" : "Which planet is known as the 'Evening Star'?" ,   
    "options" : [ " Mars ", " Venus ", " Jupiter ", " Saturn " ] ,
    "answer" : " Venus " } ,

    { "question" : "What is the powerhouse of the cell?" ,   
    "options" : [ " Nucleus ", " Mitochondria ", " Ribosome ", " Golgi apparatus " ] ,
    "answer" : " Mitochondria " } ,


    { "title": "Mathematics",
    "question" : "What is 15 × 6?" ,   
    "options" : [ " 80 ", " 134 ", " 17 ", " 90 " ] ,
    "answer" : " 90 " } ,
 
    { "question" : "If a triangle has angles of 30° and 60°, what is the third angle?" ,   
    "options" : [ " 60° ", " 90° ", " 120° ", " 80° " ] ,
    "answer" : " 90° " } ,

    { "question" : "What is the value of π (pi) up to two decimal places?" ,   
    "options" : [ " 3.12 ", " 3.14 ", " 4.2 ", " 23 " ] ,
    "answer" : " 3.14 " } ,


    { "title": "History",
    "question" : "Who was the first President of the United States?" ,   
    "options" : [ " Abraham Lincoln ", " Thomas Jefferson ", " George Washington ", " John Adams " ] ,
    "answer" : " George Washington " } ,

    { "question" : "In which year did the French Revolution begin?" ,   
    "options" : [ " 1765 ", " 1789 ", " 1804 ", " 1966 " ] ,
    "answer" : " 1789 " } ,
    
    { "question" : "The Great Wall of China was built to protect against which group?" ,   
    "options" : [ " Romans ", " Mongols ", " Persians ", " Greeks " ] ,
    "answer" : " Mongols " } ,


    { "title": "Sports",
     "question" : "How many players are there in a standard soccer team?" ,   
    "options" : [ " 9 ", " 10 ", " 11 ", " 12 " ] ,
    "answer" : " 11 " } ,

    { "question" : "Which country has won the most FIFA World Cups?" ,   
    "options" : [ " Argentina ", " Germany ", " Italy ", " Brazil " ] ,
    "answer" : " Brazil " } ,
    
    { "question" : "What is the national sport of Japan?" ,   
    "options" : [ " Judo ", " Sumo Wrestling ", " Karate ", " Baseball " ] ,
    "answer" : " Sumo Wrestling " } ,
 
]    



score = 0

if "user_answer" not in st.session_state:
    st.session_state.user_answers = [" "] * len (quiz_data)

for i, q in enumerate (quiz_data):
    st.subheader (f"Q{i+1}: {q['question']}")
    user_answer = st.radio("Choose an answer:", q["options"], key=f"q{i}")
    st.session_state.user_answers[i] = user_answer

if st.button("Submit Answers"):
    correct_answers = [q["answer"] for q in quiz_data]
    for i in range(len(quiz_data)):
        if st.session_state.user_answers[i] == correct_answers[i]:
            score += 1

    st.success(f"✅ You scored {score} out of {len(quiz_data)}!")

    for i, q in enumerate(quiz_data):
        if st.session_state.user_answers[i] == q["answer"]:
            st.write(f"✔️ {q['question']} - Correct")
        else:
            st.write(f"❌ {q['question']} - Correct answer: {q['answer']}")


if st.button("Try Again🧲"):
    st.session_state.user_answers = [""] * len(quiz_data)
    st.rerun()

