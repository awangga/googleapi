def BloggerInsert(service,bloggerID,body):
    srv = service.posts()
    return srv.insert(blogId=bloggerID, body=body).execute()

def DocsGet(service,documentId):
    srv = service.documents()
    return srv.get(documentId=documentId).execute()

def DriveCopy(service,fileId,body):
    srv = service.files()
    return srv.copy(fileId=fileId, body=body).execute()

def GmailSend(service,body):
    srv = service.users().messages()
    return srv.send(userId="me", body=body).execute()