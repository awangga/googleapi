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

def jsonBloggerPost(bloggerID,title,content):
    json = {
              "kind": "blogger#post",
              "blog": {
                "id": bloggerID
              },
              "title": title,
              "content": content
    }
    return json

def jsonDocs(title,description):
    json = {
        'name': title,
        'description': description
    }
    return json

def jsonDocsReplace(key,value):
    """
    Replace {{key}} with value
    """
    json = {'replaceAllText': {
                'containsText': {
                    'text': '{{' + key + '}}',
                    'matchCase':  True
                },
                'replaceText': value,
            }}
    return json

def jsonGmailSend(msg):
    encoded_message = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    json = {
        'raw': encoded_message
    }
    return json

def jsonSheetUpdate(cell,values):
    json = {
        "valueInputOption": "RAW",
        "data": [
            {
                "range": cell,
                "values": [[values]]
            },
        ]
    }
    return json

def execute