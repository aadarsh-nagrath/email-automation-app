import re
import streamlit as st
from feedback import display_feedback_page
from functions import send_email, convert_to_html
from how_to import display_how_to_use_page

# Set the page config first
st.set_page_config(page_title="Email Automation Tool", page_icon="📧", layout="wide")

# Google Analytics script
google_analytics_script = """
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=G-1SZ7Z8NK69"></script>
    <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-1SZ7Z8NK69');
    </script>
"""

# Inject the Google Analytics script
st.markdown(google_analytics_script, unsafe_allow_html=True)

# Your app code continues here...
st.title("📧 Email Automation Tool")

# Define send_button globally
send_button = None

# Sidebar for App Credentials, Feedback, and Theme Selection
with st.sidebar:
    st.markdown("<h2 style='color:black;'>App Credentials</h2>", unsafe_allow_html=True)
    sender_email = st.text_input("Sender's Email Address", placeholder="Enter your email address", key="sender_email_unique")
    sender_password = st.text_input("Sender's App password", type="password", placeholder="Enter your email password", key="sender_password_unique")

    # Feedback Section Link
    st.markdown("### Feedback")
    feedback_page = st.radio("Navigation", ["Email Automation", "How to Use This App", "Feedback Section"])
    st.markdown("### GO TO >> How to Use Section to understand the app better")

if feedback_page == "Email Automation":
    # Create columns with increased space between them
    col1, col2, col3 = st.columns([20, 1, 16])  # Adjust column ratio for more space between them

    # Central Section - Email Composition
    with col1:
        st.markdown("<h2 style='color:black;'>Email Composition</h2>", unsafe_allow_html=True)

        # Email Subject and Body
        subject = st.text_input("Email Subject", placeholder="Enter the subject of the email", key="subject_input")
        email_body = st.text_area("Email Body", placeholder="Write your email here. Use placeholders like [name], [age], [role], etc.", height=300, key="email_body_input")

        # Attachment (Optional)
        attachment = st.file_uploader("Attach a File", type=["jpg", "png", "pdf", "docx", "txt"], label_visibility="collapsed")

    # Right Panel - Manage Variables (Recipient Data)
    with col3:
        with st.expander("Manage Variables", expanded=True):
            st.markdown("<h2 style='color:black;'>Manage Variables</h2>", unsafe_allow_html=True)

            # Input for recipient data
            recipient_data = st.text_area(
                "Recipient Data (Comma-separated)",
                placeholder="Enter recipient details: email,name,age,role,company\ne.g., john.doe@example.com,John,25,Engineer,Tesla",
                key="recipient_data_input", height=300
            )
            st.session_state["recipient_data"] = recipient_data

        # Preview Section
        with st.expander("Preview Email", expanded=False):
            if recipient_data and email_body:
                recipients = recipient_data.strip().split("\n")
                if recipients:
                    first_recipient = recipients[0]
                    parts = first_recipient.split(',')
                    if len(parts) >= 2:
                        variables = {f'var_{i}': value.strip() for i, value in enumerate(parts[1:], 1)}
                        placeholders = re.findall(r'\[(.*?)\]', email_body)
                        preview_body = email_body
                        for i, placeholder in enumerate(placeholders):
                            var_name = f'var_{i+1}'
                            if var_name in variables:
                                preview_body = preview_body.replace(f'[{placeholder}]', variables[var_name])
                            else:
                                preview_body = preview_body.replace(f'[{placeholder}]', f'[Missing: {placeholder}]')
                        st.markdown(f"**Preview for {parts[0]}:**")
                        st.markdown(preview_body)
                    else:
                        st.warning("Invalid recipient data format for preview.")
            else:
                st.info("Provide email body and recipient data to preview the email.")

        # Send Email button below Manage Variables
        send_button = st.button("Send Email", key="send_button_sidebar")

    # Send Email Button Logic
    if send_button:
        recipient_data = st.session_state.get("recipient_data", "")  # Get recipient data from right panel
        if not sender_email or not sender_password or not recipient_data:
            st.error("Please fill in all required fields!")
        else:
            subject = st.session_state.get("subject_input", "")
            email_body = st.session_state.get("email_body_input", "")
            recipients = recipient_data.strip().split("\n")
            success_count = 0
            failure_count = 0

            for recipient_line in recipients:
                parts = recipient_line.split(',')
                if len(parts) >= 2:
                    recipient_email = parts[0].strip()
                    if not re.match(r"[^@]+@[^@]+\.[^@]+", recipient_email):
                        st.warning(f"Invalid email format: {recipient_email}")
                        continue
                    variables = {f'var_{i}': value.strip() for i, value in enumerate(parts[1:], 1)}
                    placeholders = re.findall(r'\[(.*?)\]', email_body)
                    personalized_body = email_body
                    for i, placeholder in enumerate(placeholders):
                        var_name = f'var_{i+1}'
                        if var_name in variables:
                            personalized_body = personalized_body.replace(f'[{placeholder}]', variables[var_name])
                        else:
                            personalized_body = personalized_body.replace(f'[{placeholder}]', f'[Missing: {placeholder}]')
                    html_body = convert_to_html(personalized_body)
                    try:
                        if attachment:
                            attachment_file = attachment
                        else:
                            attachment_file = None
                        if send_email(subject, html_body, recipient_email, sender_email, sender_password, attachment=attachment_file):
                            success_count += 1
                            st.toast(f"Email sent to {recipient_email}", icon="✅")
                    except Exception as e:
                        st.error(f"Error sending to {recipient_email}: {e}")
                        failure_count += 1
            st.success(f"Emails sent successfully to {success_count} recipients.")
            if failure_count > 0:
                st.error(f"Failed to send emails to {failure_count} recipients.")

elif feedback_page == "How to Use This App":
    display_how_to_use_page()

elif feedback_page == "Feedback Section":
    display_feedback_page()
    if "feedback_list" in st.session_state:
        st.markdown("### Submitted Feedback:")
        for idx, feedback_item in enumerate(st.session_state["feedback_list"], 1):
            st.markdown(f"{idx}. {feedback_item}")
