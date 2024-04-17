import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send_email(subject, body, to_email, attachment_path):
    # Email configurations
    smtp_server = 'gmail.com'
    smtp_port = 587
    sender_email = 'ibrahmed98@gmail.com'
    sender_password = 'karmaA!358051'
    
    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject
    
    # Attach body to email
    msg.attach(MIMEText(body, 'plain'))
    
    # Attach CSV file
    with open(attachment_path, 'rb') as file:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(file.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f'attachment; filename= {attachment_path.split("/")[-1]}')
        msg.attach(part)
    
    # Start a secure SMTP session and send the email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())

# Example usage:
subject = 'CSV File Attached'
body = 'Please find the attached CSV file.'
to_email = 'ibrahmed98@gmail.com'
attachment_path = 'C:\\Users\\Administrator\\Desktop\\repo\\data_analysis\\Global YouTube Statistics.csv'

send_email(subject, body, to_email, attachment_path)
