import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_ADDRESS = "gsjosjoa27.7@gmail.com"
APP_PASSWORD = "xfxe zzyn ovzg anih"

RECEIVER_EMAIL = "gsjosjoa27.7@gmail.com"

msg = MIMEMultipart()
msg["From"] = EMAIL_ADDRESS
msg["To"] = RECEIVER_EMAIL
msg["Subject"] = "Automated Email Test"

body = """Hello,

This is an auto-generated email sent using Python.

Regards,
Python Bot
"""

msg.attach(MIMEText(body, "plain"))

try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(EMAIL_ADDRESS, APP_PASSWORD)
    server.send_message(msg)
    server.quit()
    print(" Email sent successfully!")
except Exception as e:
    print(" Error:", e)
