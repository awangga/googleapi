from googleapi import service,body,execute

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

apiscope=['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/blogger','https://www.googleapis.com/auth/gmail.send','https://www.googleapis.com/auth/gmail.readonly']
jsonsecfile='my_json_file.json'
tokenpickle='token.pickle'

srv=service.Open('gmail',apiscope,jsonsecfile,tokenpickle)


msg = MIMEMultipart()
msg['From'] = 'awangga@ulbi.ac.id'
msg['To'] = 'rolly@awang.ga'
msg['Subject'] = 'testing'

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")
msg.attach(part1)
msg.attach(part2)

json=body.GmailSend(msg)
print(json)

resp=execute.GmailSend(srv,json)
print(resp)