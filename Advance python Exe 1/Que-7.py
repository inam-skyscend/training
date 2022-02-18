# 7. Receive an email and print the detial of from, to, subject. Also parse the content of
# the attachment and if pdf or jpeg file.

import email
import imaplib
from passw import mail_psw

server=imaplib.IMAP4_SSL("imap.gmail.com")
server.login("inamhusain2001@gmail.com",mail_psw)

server.select('inbox')

# status,data=server.search(None,'(TO "vkshah.ce@spcevng.ac.in")')
status,data=server.search(None,'(TO "2018095900008554@spu.ac.in" SUBJECT "Test")')
print(status)
print(data)
#
# l=[]
# for block in data:
#     l+=block.split()
# print(l)
# for i in l:
    # the fetch function fetch the email given its id
    # and format that you want the message to be
status, mail_data = server.fetch(b'3086', '(RFC822)')
print("STAUS", status)
print("MAIL DATA", mail_data)

raw_email = mail_data[0][1] # here's the body, which is raw text of the whole email
# including headers and alternate payloads
raw_email_string = raw_email.decode('utf-8')
email_message = email.message_from_string(raw_email_string)
print(email_message)
# result,data=server.fetch(b'1','(RFC822)')
# print(data)