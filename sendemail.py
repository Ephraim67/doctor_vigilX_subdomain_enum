# Sending an Email Using Python
# Using the smtplib to send an email

import smtplib

# Sender's credentials
sender_email = "your_email@example.com"  # Your email address
username = "your_smtp_username"  # Your SMTP account username
password = "your_smtp_password"  # Your SMTP account password

# Spoofed email information
spoofed_email = "spoofed_email@example.com"  # Spoofed email address
spoofed_name = 'John Doe'  # Spoofed full name

# Victim's email address
victim_email = "victim_email@example.com"

# Email subject and body
subject = "This is a subject"
message_body = "This is the email body."

# Constructing email headers
header = f"To: {victim_email}\nFrom: {spoofed_name} <{spoofed_email}>\nSubject: {subject}\n"

# Constructing the complete message
message = f"{header}\n{message_body}\n"

# Sending the email
try:
    with smtplib.SMTP_SSL("smtp.server.com", 465) as session:  # SMTP server and port
        session.login(username, password)
        session.sendmail(sender_email, victim_email, message)
    print("Email Sent Successfully!")
except smtplib.SMTPException as e:
    print(f"Error: Unable To Send The Email! {e}")
