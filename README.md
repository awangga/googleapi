# googleapi
Google API Wrapper for Python
flow : service-body-execute

## Service
Open google api service with credentials

## Body
Generate json or dictionary for data post to Google API

## Execute
Sending body into Google API and get response

## Example
First thing is import google api module and others helpers you need, after that please define apiscope,jsonsecfile and tokenpickel
```python
from googleapi import service,body,execute
from helper import email

apiscope=['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/blogger','https://www.googleapis.com/auth/gmail.send','https://www.googleapis.com/auth/gmail.readonly']
jsonsecfile='my_json_file.json'
tokenpickle='token.pickle'
```

### Sending email
```python
srv=service.Open('gmail',apiscope,jsonsecfile,tokenpickle)

msg=email.createMessage('Rolly Maulana Awangga <awangga@ulbi.ac.id>','rolly@awang.ga','my info',"hello gaes","plain")

json=body.GmailSend(msg)
print(json)

resp=execute.GmailSend(srv,json)
print(resp)
```