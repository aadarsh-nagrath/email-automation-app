import streamlit as st
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib

def send_email(subject, body, to_email, from_email, password, attachment=None):
    try:
        # Setup the MIME
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        # Attach the body with the msg
        msg.attach(MIMEText(body, 'html'))

        # Check if there's an attachment
        if attachment is not None:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename={attachment.name}')
            msg.attach(part)

        # Setup the SMTP server and send email
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()

        return True
    except Exception as e:
        return f"Failed to send email: {str(e)}"
    
def convert_to_html(body):
    return body.replace("\n", "<br>")  # Convert newlines to <br> for line breaks in HTML
