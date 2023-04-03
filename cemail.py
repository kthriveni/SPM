import smtplib
from smtplib import SMTP
from email.message import EmailMessage
def sendmail(to,otp):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('your ','passcode')
    msg=EmailMessage()
    msg['From']='eswar@codegnan.com'
    msg['Subject']='Account Sign up OTP'
    msg['To']=to
    body=f'Your one time otp for registration is {otp}' 
    msg.set_content(body)
    server.send_message(msg)
    server.quit()
