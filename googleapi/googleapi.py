import os
import pickle
import base64

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload

def getCredentials(apiscope,jsonsecfile,tokenpickle):
    SCOPES = apiscope
        global values_input, service
        creds = None
        if os.path.exists(tokenpickle):
            with open(tokenpickle, 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(jsonsecfile, SCOPES)
                creds = flow.run_local_server(port=0)
            with open(tokenpickle, 'wb') as token:
                pickle.dump(creds, token)
    return creds

def getService(servicename,credentials):
    return build(servicename, getApiVersion(servicename), credentials=credentials)

def getApiVersion(servicename):
    if servicename == 'gmail' or servicename == 'docs':
        apiversion = 'v1'
    elif servicename == 'blogger' or servicename == 'drive':
        apiversion = 'v3'
    elif servicename == 'sheets':
        apiversion = 'v4'
    else:
        apiversion = 'v4'
    return apiversion

def bodyBloggerPost(bloggerID,title,content):
    body = {
              "kind": "blogger#post",
              "blog": {
                "id": bloggerID
              },
              "title": title,
              "content": content
    }
    return body

def bodyDocs(title,description):
    body = {
        'name': title,
        'description': description
    }
    return body

def bodyDocsReplace(key,value):
    """
    Replace {{key}} with value
    """
    body = {'replaceAllText': {
                'containsText': {
                    'text': '{{' + key + '}}',
                    'matchCase':  True
                },
                'replaceText': value,
            }}
    return body

def bodyGmailSend(msg):
    encoded_message = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    body = {
        'raw': encoded_message
    }
    return body

def bodySheetUpdate(cell,values):
    body = {
        "valueInputOption": "RAW",
        "data": [
            {
                "range": cell,
                "values": [[values]]
            },
        ]
    }
    return body

def execBloggerInsert(service,bloggerID,body):
    srv = service.posts()
    return srv.insert(blogId=bloggerID, body=body).execute()

def execDocsGet(service,documentId):
    srv = service.documents()
    return srv.get(documentId=documentId).execute()

def execDriveCopy(service,fileId,body):
    srv = service.files()
    return srv.copy(fileId=fileId, body=body).execute()

def execGmailSend(service,body):
    srv = service.users().messages()
    return srv.send(userId="me", body=create_message).execute()

def getInfo(response,field)
    return response.get(field)