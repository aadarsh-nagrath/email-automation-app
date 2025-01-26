# Email Automation Tool

A simple email automation tool to send personalized emails to multiple recipients. The tool dynamically replaces placeholders in the email body with recipient-specific data, allowing for personalized communication. 

## Features

- **Dynamic Placeholder Handling**: Automatically substitutes placeholders in the email body with recipient data.
- **Recipient Data Management**: Easily input and manage recipient data (e.g., name, age, role, etc.).
- **Email Sending**: Sends emails with personalized content to multiple recipients.
- **Attachment Support**: Attach files to emails.
- **Recipient Validation**: Validates email format before sending.

## Requirements

To run the app, you need the following Python packages:

- streamlit
- re
- smtplib
- email
- feedback (for managing user feedback)

Install dependencies with:

```bash
pip install streamlit
```

## Setup

1. Clone the repository or download the code.
2. Set up your app credentials by providing your email address and password.
3. Run the app:

```bash
streamlit run app.py
```

4. Open the app in your browser.

## How to Use

1. **Enter Your Email Credentials**: Provide your sender email address and password in the sidebar.
2. **Compose the Email**: 
   - Enter the subject of the email.
   - Write the body of the email. Use placeholders in the format `[placeholder]` (e.g., `[name]`, `[age]`).
3. **Manage Recipient Data**:
   - Enter the recipient's email and corresponding values (e.g., name, age, etc.) in the recipient data section.
   - Each recipient’s data should be separated by commas (e.g., `email, name, age, role, company`).
4. **Send Emails**: 
   - Click "Send Email" to send personalized emails to all the recipients.
   - Attachments can be included if necessary.

## Example

### Input Email Body:
```
Hello [name], your age is [age] and you work as a [role] at [company].
```

### Input Recipient Data:
```
john.doe@example.com, John, 25, Engineer, CU
jane.doe@example.com, Jane, 30, Designer, XYZ
```

### Output Email for `john.doe@example.com`:
```
Hello John, your age is 25 and you work as an Engineer at CU.
```

### Output Email for `jane.doe@example.com`:
```
Hello Jane, your age is 30 and you work as a Designer at XYZ.
```

## Feedback

We value your feedback! Please provide any suggestions or issues you face while using the app through the **Feedback** section in the sidebar.
