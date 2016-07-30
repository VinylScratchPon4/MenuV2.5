import smtplib

sender = 'zak.body@yahoo.com'
receiver = 'louise.body@yahoo.com'

message = 'Hey mum... I just send this email using a python script :D'

try:
   mail = stmplib.SMTP('localhost')
   mail.sendmail(sender, receiver, message)
except smtplib