import os
import pickle

from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

def Credentials(apiscope,jsonsecfile,tokenpickle):
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

def Service(servicename,credentials):
    return build(servicename, getApiVersion(servicename), credentials=credentials)
    
def Open(servicename,apiscope,jsonsecfile,tokenpickle):
    credentials=Credentials(apiscope,jsonsecfile,tokenpickle)
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
