# 4. Send an email using only plain text.

import smtplib
from passw import mail_psw

server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login('inamhusain2001@gmail.com', mail_psw)
#
sender = 'inamhusain2001@gmail.com'
receiver = 'idcreater2001@gmail.com'
# #
message ="hello my name is inam"
#
server.sendmail(sender, receiver, message)
#
server.quit()
