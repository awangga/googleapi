from googleapi import service,body,execute
from helper import email

apiscope=['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/blogger','https://www.googleapis.com/auth/gmail.send','https://www.googleapis.com/auth/gmail.readonly']
jsonsecfile='my_json_file.json'
tokenpickle='token.pickle'

srv=service.Open('gmail',apiscope,jsonsecfile,tokenpickle)

message = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
msg=email.createMessage('Rolly Maulana Awangga <awangga@ulbi.ac.id>','rolly@awang.ga','my info',message,"plain")

json=body.GmailSend(msg)
print(json)

resp=execute.GmailSend(srv,json)
print(resp)

