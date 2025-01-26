import streamlit as st

def display_how_to_use_page():
    st.markdown("""
    ## How to Use This App

    Follow the steps below to use the Email Automation Tool:

    1. **Go to Google App Password Setup**:
        - Visit [Google App Passwords](https://support.google.com/mail/answer/185833?hl=en) or search for "Google App Password" on Google.
        - Click on **"Create and manage your app passwords"** in the "App passwords" section.
        - Create an app name (e.g., "Email Automation").
        - Click **Create** to generate your app password.
        - Copy the app password code.
    """)

    # Display the first image for "App Password Setup"
    st.image("images/a1.png", caption="App Password Setup")

    st.markdown("""
    2. **Add Your Credentials**:
        - Go to the left panel of the app and enter your **Sender's Email** and the **App Password** you copied earlier in the respective fields.

    3. **Compose Your Email**:
        - Enter the **Subject** of the email in the "Email Subject" field.
        - Write your email content in the "Email Body" section.
        - To create dynamic variables in your email body, use square brackets `[]`. For example, you can use `[name]`, `[company]`, etc., as placeholders in your email.
    """)

    # Display the second image for "Email Body Example"
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.image("images/a3.png", caption="Email Body Example")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    4. **Manage Recipient Variables**:
        - In the "Manage Variables" section, enter recipient data in the format:
            - **Recipient's Email, Variable 1, Variable 2, ...**
            - Example: `john.doe@example.com, John, 30, Engineer, CU`.
        - **Important**: 
            - Make sure to use lowercase for variable names (e.g., `[age]`, `[name]`, etc.), not uppercase (e.g., `[Age]`).
    """)

    # Display the third image for "Manage Variables"
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.image("images/a2.png", caption="Manage Variables")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    5. **Preview Email Before Sending**:
        - To ensure your email looks correct before sending, use the **Preview** option under the "Manage Variables" section.
        - Click on the **Preview** dropdown to view how your email will look after replacing variables with actual values.
    """)

    # Display the fifth image for "Preview Email"
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.image("images/a5.png", caption="Click on Preview to view how the email will look before sending it")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    6. **Optional: Add Attachments**:
        - If needed, you can attach files (e.g., images, PDFs) using the "Attach a File" option.

    7. **Send Emails**:
        - Once you've filled out the required fields, click the **Send Email** button.
        - You can add as many lines of recipients as needed, one per line, and the app will send personalized emails to each recipient with the corresponding variables replaced in the email body.

    8. **Feedback Page**:
        - To provide feedback on the app, go to the **Feedback Page** by clicking the option in the sidebar. You can leave your comments or suggestions for improvements.
    """)

    # Display the fourth image for "Feedback Page"
    st.markdown('<div style="text-align: center;">', unsafe_allow_html=True)
    st.image("images/a4.png", caption="Feedback Page")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    Enjoy automating your emails with ease!
    """)
