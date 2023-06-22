import ssl
from email.message import EmailMessage
from mydetails import password, email
import ssl
import smtplib



email_sender= email
email_password=password
email_reciever="janaray620@anwarb.com"

subject="invitation for welcome and farewell program"
body="""
this is the invitaion of welcome and farewell program
"""

em=EmailMessage()
em['from']=email_sender
em['To']=email_reciever
em['subject']=subject
em.set_content(body)

content = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com',465,context=content) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())



