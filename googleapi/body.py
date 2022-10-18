def BloggerPost(bloggerID,title,content):
    body = {
              "kind": "blogger#post",
              "blog": {
                "id": bloggerID
              },
              "title": title,
              "content": content
    }
    return body

def Docs(title,description):
    body = {
        'name': title,
        'description': description
    }
    return body

def DocsReplace(key,value):
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

def GmailSend(msg):
    import base64
    encoded_message = base64.urlsafe_b64encode(msg.as_bytes()).decode()
    body = {
        'raw': encoded_message
    }
    return body

def SheetUpdate(cell,values):
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
