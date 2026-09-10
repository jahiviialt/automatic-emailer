import smtplib
from email.message import EmailMessage

sender = "mrdoge2007@gmail.com"
password = "bxxq kmbh nmwd rqbl"

recipents = [
    "9494383@philasd.org",
    "joslyn1st@gmail.com",
    "mrdoge2009@gmail.com"

]

msg = EmailMessage()
msg["Subject"] = "Automated Email by Mosi"
msg["From"] = sender
msg["To"] = ", ".join(recipents)

msg.set_content("""
    Hello mum and nerdmay!
    This email was sent automatically using a Python Script!
    it seems cool for datasets with lots of emails yes...""")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(sender, password)
    smtp.send_message(msg)

print("Email sent to all recipients.")