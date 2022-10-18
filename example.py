from googleapi import service,body,execute

apiscope=['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/documents', 'https://www.googleapis.com/auth/drive','https://www.googleapis.com/auth/blogger','https://www.googleapis.com/auth/gmail.send','https://www.googleapis.com/auth/gmail.readonly']
jsonsecfile='my_json_file.json'
tokenpickle='token.pickle'

srv=service.Open('gmail',apiscope,jsonsecfile,tokenpickle)


