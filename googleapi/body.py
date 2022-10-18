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
    import base64
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
