# 6. Send an email including HTML text and also 2 attachments one pdf file and one jpeg file.

# 5. Send an email using HTML Text.
import smtplib
from passw import mail_psw
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import imghdr


server=smtplib.SMTP_SSL('smtp.gmail.com',465)
server.login('inamhusain2001@gmail.com', mail_psw)

sender = 'inamhusain2001@gmail.com'
receiver = '2018095900008554@spu.ac.in'

msg = MIMEMultipart("")
msg['subject'] = 'Test'
msg['From'] = sender
msg['To'] = receiver

#html code
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
part1 = MIMEText(html, "html")
# # #
msg.attach(part1)

# image
filename="istockphoto-1327488839-612x612.jpeg"

with open(filename, "rb") as attachment:
#     # Add file as application/octet-stream
#     # Email client can usually download this automatically as attachment
    part2 = MIMEBase("application", "octet-stream")
    part2.set_payload(attachment.read())

encoders.encode_base64(part2)

# # # # Add header as key/value pair to attachment part
part2.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
# # #
msg.attach(part2)


# pdf
filename="Python Advance Exercise - 1.pdf"

with open(filename, "rb") as attachment:
#     # Add file as application/octet-stream
#     # Email client can usually download this automatically as attachment
    part3 = MIMEBase("application", "octet-stream")
    part3.set_payload(attachment.read())

encoders.encode_base64(part3)

# # # # Add header as key/value pair to attachment part
part3.add_header(
    "Content-Disposition",
    f"attachment; filename= {filename}",
)
# # #
msg.attach(part3)


server.sendmail(sender, receiver,msg.as_string())

server.quit()