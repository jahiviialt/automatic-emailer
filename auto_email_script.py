import smtplib
from email.message import EmailMessage
#if your email has 2-step verification, instead of your normal password, use an app password.
sender = "your email here"
password = "your email password here"

recipents = [
    #list of recipient emails here

]

msg = EmailMessage()
msg["Subject"] = "Automated Email"
msg["From"] = sender
msg["To"] = ", ".join(recipents)

msg.set_content("""
    The content of your text goes here """)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)

print("Email sent to all recipients.")
