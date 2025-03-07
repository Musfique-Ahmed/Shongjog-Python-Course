import streamlit as st
import pandas as pd

csv_file = "Expense Records.csv"
try:
    df = pd.read_csv(csv_file)
except FileNotFoundError:
    df = pd.DataFrame(columns=["Date", "Category", "Amount" ])

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go To",["Intro","Expense Tracker","Last 5 Transactions","Smart Spending Tips","Contact"])

budget_limit = st.sidebar.number_input("🎯 Set Monthly Budget ($):min_value=0.01, value=500.0")

total_spent = df["Amount"].sum()
if total_spent > budget_limit:
    st.error(f"⚠️ Warning: You exceeded your budget! Spent: ${total_spent:.2f}, Budget: ${budget_limit:.2f}")


if page == "Intro":
    st.title("WELCOME TO MY PORTFOLIO.")
    st.markdown("🚀 **Welcome to My App!**")
    st.subheader("Smart Budget Tracker")
    st.write("The Smart Budget Tracker is a personal finance management app built with Streamlit and Pandas to help users track, manage, and optimize their expenses in an easy-to-use interface. The tool provides real-time insights into spending habits, budget limits, and smart saving tips to encourage better financial decisions.")
    st.subheader("Key Features")
    st.markdown("Multi-Page Navigation (📌)")
    st.markdown("Expense Tracking System (💰)")
    st.markdown("Budget Limit & Warnings (🚨)")
    st.markdown("Expense Summary & Recent Transactions (📜)")
    st.markdown("Smart Spending Tips (💡)")
    

elif page == "Expense Tracker":
    
    st.checkbox("Check This Out")
    st.title("Smart Budget Tracker")
    st.sidebar.header("Add New Expense")

    date = st.sidebar.date_input("Date")
    category = st.sidebar.selectbox("Category",["Food","Transport","Entertainment", "Shopping", "Bills", "Personal","Others"])
    amount = st.sidebar.number_input("Amount ($)", min_value=0.01, format="%.2f")


    if st.sidebar.button("Add Expense"):
        new_data = pd.DataFrame([[date,category,amount]],columns =["Date","Category","Amount"])
        df = pd.concat([df,new_data],ignore_index=True)
        df.to_csv(csv_file,index=False)
        st.sidebar.success("Expense added!")




    st.subheader("📊 Expense Summary")
    st.dataframe(df)
elif page == "Last 5 Transactions":

    st.write("### 📜 Last 5 Transactions:")
    st.dataframe(df.tail(5))

elif page == "Smart Spending Tips":

    st.write("### 💡 Smart Spending Tips:")
    if "Food" in df["Category"].values:
        st.write("🍽️ Consider meal planning to reduce food expenses.")
    if "Transport" in df["Category"].values:
        st.write("🚆 Try using public transport to save on transport costs.")
    if "Entertainment" in df["Category"].values:
        st.write("🎮 Opt for free or low-cost activities like movie nights at home.")
    if "Bills" in df["Category"].values:
        st.write("💡 Reduce electricity usage, switch to energy-saving appliances, or negotiate lower plans.")
    if "Personal" in df["Category"].values:
        st.write("👤So much Spending on your personal never")
    if "Shopping" in df["Category"].values:
        st.write("🛍️ Look for discounts or cashback offers when shopping.")
    if "Others" in df["Category"].values:
        st.write("🔄 Track miscellaneous expenses and eliminate unnecessary ones")
elif page == "Contact":
    st.title("📞 My Contact")
    st.write("You can reach me for any queries or discussions. I’ll be happy to connect and assist.")
    st.markdown("📧 **Email:** anjonavoornilim@gmail.com")
    st.markdown("📞 **Phone:** +8801923659695")
    st.write("Looking forward to staying in touch. Feel free to reach out anytime!")
