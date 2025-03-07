import streamlit as st
import smtplib
from email.message import EmailMessage

# setup of auto email sends
EMAIL_ADDRESS = "ahanclientservice@gmail.com"
EMAIL_PASSWORD = "cnej hhhb atoo bbmh" # My api

def send_email(name, user_email, message):
    """Function to send an email to the website author."""
    try:
        msg = EmailMessage()
        msg["Subject"] = f"New Message from {name}"
        msg["From"] = user_email
        msg["To"] = EMAIL_ADDRESS
        msg.set_content(f"Name: {name}\nEmail: {user_email}\n\nMessage:\n{message}")

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False


def contact_box():
    st.title("📩 Contact the Website Author")

    # Website Information
    st.write("""
    This website is a **Stock Market Dashboard** that provides real-time stock data, analysis tools, 
    an AI chatbot, and educational resources to help users understand and navigate the stock market.
    
    🔗 **GitHub:** [Visit GitHub](https://github.com/ANAHAN07)  
    📧 **Email:** ahanclientservice@gmail.com
    """)

    # Contact Form
    st.header("Send a Message")
    name = st.text_input("Your Name")
    user_email = st.text_input("Your Email")
    message = st.text_area("Your Message")

    if st.button("Send Message"):
        if name and user_email and message:
            if send_email(name, user_email, message):
                st.success("✅ Message sent successfully! I'll get back to you soon.")
        else:
            st.warning("⚠️ Please fill out all fields before sending.")

if __name__ == "__main__":
    contact_box()