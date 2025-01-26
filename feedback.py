import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from dotenv import load_dotenv

load_dotenv()

# Fetch email credentials and App ID from environment variables
SENDER_EMAIL = os.getenv('SENDER_EMAIL')  # Your email (sender)
APP_ID = os.getenv('APP_ID')  # The app ID


# Function to send email with feedback
def send_feedback_email(feedback):
    try:
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = SENDER_EMAIL  # Send feedback to your own email
        msg['Subject'] = "Email app Feedback"
        
        # Email body with feedback and app ID
        body = f"\nFeedback:\n{feedback}"
        msg.attach(MIMEText(body, 'plain'))

        # Set up the SMTP server and send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Start TLS for security
        server.login(SENDER_EMAIL, APP_ID) 
        server.sendmail(SENDER_EMAIL, SENDER_EMAIL, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"Failed to send email: {e}")
        return False

# Display the feedback form on the Streamlit app
def display_feedback_page():
    st.header("Feedback Section")

    # Text area for user feedback
    feedback_text = st.text_area("Write your feedback or suggestions here:")

    # Button to submit feedback
    if st.button("Submit Feedback"):
        if feedback_text:
            # Send feedback to the specified email
            if send_feedback_email(feedback_text):
                st.success("Feedback submitted successfully and email sent to you!")
            else:
                st.error("Failed to send feedback email.")
        else:
            st.error("Please write something before submitting.")
