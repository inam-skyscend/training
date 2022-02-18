# 5. Send an email using HTML Text.
import smtplib
from passw import mail_psw
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase


server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login('inamhusain2001@gmail.com', mail_psw)

sender = 'inamhusain2001@gmail.com'
receiver = 'idcreater2001@gmail.com'

msg = MIMEMultipart("")
msg['subject'] = 'Test Python Email - Attachment'
msg['From'] = sender
msg['To'] = receiver


html = """\
<html>
  <body>
    <p><b>Python Mail Test</b><br>
       This is HTML email with attachment.<br>
       Click on <a href="https://fedingo.com">Fedingo Resources</a> 
       for more python articles.
    </p>
  </body>
</html>
"""
# #
part2 = MIMEText(html, "html")
# # #
msg.attach(part2)

server.sendmail(sender, receiver,msg.as_string())

server.quit()