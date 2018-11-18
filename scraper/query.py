import json
import os
from httplib2 import Http
from googleapiclient.discovery import build
from oauth2client import file, client, tools

SCOPES = 'https://www.googleapis.com/auth/drive.readonly'
file_id = os.environ.get('QUERY_FILE_ID')

def get_queries():
    store = file.Storage('token.json')
    creds = store.get()
    # creds = client.Credentials(
    #     filename=None,
    #     scope=SCOPES,
    #     token_uri="https://www.googleapis.com/oauth2/v3/token",
    #     client_id="597746796963-kkue5nft1k9l45ehal4o7eoi6frvbhps.apps.googleusercontent.com",
    #     client_secret="JiWdWK8lUA1GQOSMTyIOMVKY",
    #     refresh_token="1/fsmi-AZajUNN-OvFd1K5ijkfQ2M-6SLw3Q1JkldQA0I"
    # )
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets(os.environ.get('GOOGLE_APPLICATION_CREDENTIALS'), scope=SCOPES)
        creds = tools.run_flow(flow, store, access_type='offline')
    service = build('drive', 'v3', http=creds.authorize(Http()))

    # results = service.files().get_media(fileId=file_id).execute()
    results = service.files().export(fileId=file_id, mimeType='text/plain').execute()
    decoded = results.decode('utf-8-sig')
    json_results = json.loads(decoded)

    return json_results


if __name__ == '__main__':
    QUERIES = get_queries()
    print(QUERIES)
    print(type(QUERIES))
