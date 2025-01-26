import re
import streamlit as st
from feedback import display_feedback_page
from functions import send_email, convert_to_html

# Streamlit App Title
st.set_page_config(page_title="Email Automation Tool", page_icon="📧", layout="wide")
st.title("📧 Email Automation Tool")

# Sidebar for App Credentials, Feedback, and Theme Selection
with st.sidebar:
    st.markdown("<h2 style='color:black;'>App Credentials</h2>", unsafe_allow_html=True)
    sender_email = st.text_input("Sender's Email Address", placeholder="Enter your email address", key="sender_email_unique")
    sender_password = st.text_input("Sender's Email Password", type="password", placeholder="Enter your email password", key="sender_password_unique")

    theme = st.selectbox("Select Theme", ["Light", "Dark"], key="theme_unique")
    
    # Feedback Section Link
    st.markdown("### Feedback")
    feedback_page = st.radio("Go to Feedback Section", ["Email Automation", "Feedback Section"])

if feedback_page == "Email Automation":
    # Create columns with increased space between them
    col1, col2, col3 = st.columns([20, 1, 16])  # Adjust column ratio for more space between them

    # Central Section - Email Composition
    with col1:
        st.markdown("<h2>Email Composition</h2>", unsafe_allow_html=True)

        # Email Subject and Body
        subject = st.text_input("Email Subject", placeholder="Enter the subject of the email", key="subject_input")
        email_body = st.text_area("Email Body", placeholder="Write your email here. Create variables in email body like [name], [company], etc.", height=300, key="email_body_input")

        # Attachment (Optional)
        attachment = st.file_uploader("Attach a File", type=["jpg", "png", "pdf", "docx", "txt"], label_visibility="collapsed")

    # Right Panel - Manage Variables (Recipient Data)
    with col3:
        # Expander with markdown content inside
        with st.expander("Manage Variables", expanded=True):
            st.markdown("<h2>Manage Variables</h2>", unsafe_allow_html=True)

            # Input for recipient data
            recipient_data = st.text_area(
                "Recipient Data (Comma-separated)",
                placeholder="Enter recipient details in the format: email,name,age,role,company\ne.g., john.doe@example.com,John,25,Engineer,CU",
                key="recipient_data_input", height=300
            )

            # Save recipient data for later use
            st.session_state["recipient_data"] = recipient_data

    # Send Email Button Logic
    if st.button("Send Email", key="send_button_sidebar"):
        recipient_data = st.session_state.get("recipient_data", "")  # Get recipient data from right panel
        if not sender_email or not sender_password or not recipient_data:
            st.error("Please fill in all required fields!")
        else:
            subject = st.session_state.get("subject_input", "")
            email_body = st.session_state.get("email_body_input", "")
            # Split recipient data into rows
            recipients = recipient_data.strip().split("\n")
            success_count = 0
            failure_count = 0

            for recipient_line in recipients:
                parts = recipient_line.split(',')
                if len(parts) >= 2:  # Ensure at least email and one variable are provided
                    recipient_email = parts[0].strip()

                    # Validate email format using regex
                    if not re.match(r"[^@]+@[^@]+\.[^@]+", recipient_email):
                        st.warning(f"Invalid email format: {recipient_email}")
                        continue  # Skip this row and proceed to the next recipient

                    # Dynamically create a dictionary from the recipient data (skipping the email)
                    variables = {f'var_{i}': value.strip() for i, value in enumerate(parts[1:], 1)}

                    # Dynamically find placeholders in the email body
                    placeholders = re.findall(r'\[(.*?)\]', email_body)

                    # Substitute placeholders with corresponding values
                    personalized_body = email_body
                    for i, placeholder in enumerate(placeholders):
                        # Check if the placeholder exists in the recipient's data
                        var_name = f'var_{i+1}'
                        if var_name in variables:
                            personalized_body = personalized_body.replace(f'[{placeholder}]', variables[var_name])
                        else:
                            # If no value, leave the placeholder as is
                            personalized_body = personalized_body.replace(f'[{placeholder}]', f'[Missing: {placeholder}]')

                    # Convert to HTML format
                    html_body = convert_to_html(personalized_body)

                    # Send the email
                    try:
                        if send_email(subject, html_body, recipient_email, sender_email, sender_password):
                            success_count += 1
                            st.success(f"Email sent to {recipient_email}")
                    except Exception as e:
                        st.error(f"Error sending to {recipient_email}: {e}")
                        failure_count += 1

            # Show results
            st.success(f"Emails sent successfully to {success_count} recipients.")
            if failure_count > 0:
                st.error(f"Failed to send emails to {failure_count} recipients.")

elif feedback_page == "Feedback Section":
    # Only show feedback section when selected
    display_feedback_page()

    # Displaying submitted feedback
    if "feedback_list" in st.session_state:
        st.markdown("### Submitted Feedback:")
        for idx, feedback_item in enumerate(st.session_state["feedback_list"], 1):
            st.markdown(f"{idx}. {feedback_item}")
