from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def createMessage(sender,receiver,subject,message,tipe):
    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject
    # Turn these into plain/html MIMEText objects
    part1 = MIMEText(message, tipe)
    msg.attach(part1)
    return msg