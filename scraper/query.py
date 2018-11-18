import json
import os
from httplib2 import Http
from googleapiclient.discovery import build
from oauth2client import file, client, tools

QUERY_FILE_ID = os.environ.get('QUERY_FILE_ID')

def get_queries():
    store = file.Storage('token.json')
    creds = store.get()

   # creds = client.Credentials(
    #     filename=None,
    #     scope=SCOPES,
    #     token_uri="https://www.googleapis.com/oauth2/v3/token",
    #     refresh_token="1/fsmi-AZajUNN-OvFd1K5ijkfQ2M-6SLw3Q1JkldQA0I"
    # )

    if not creds or creds.invalid:

        CLIENT_ID = os.environ.get('CLIENT_ID')
        CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
        REDIRECT_URI = os.environ.get('REDIRECT_URI')
        AUTH_URI = os.environ.get('AUTH_URI')
        TOKEN_URI = os.environ.get('TOKEN_URI')
        REVOKE_URI = os.environ.get('REVOKE_URI')

        SCOPES = 'https://www.googleapis.com/auth/drive.readonly'

        flow = client.OAuth2WebServerFlow(
                client_id=CLIENT_ID,
                client_secret=CLIENT_SECRET,
                redirect_uri=REDIRECT_URI,
                auth_uri = AUTH_URI,
                token_uri = TOKEN_URI,
                revoke_uri = REVOKE_URI,
                scope=SCOPES,
                access_type='offline',
                prompt='consent'
                )

        creds = tools.run_flow(flow, store)

    service = build('drive', 'v3', http=creds.authorize(Http()))

    # results = service.files().get_media(fileId=file_id).execute()
    results = service.files().export(fileId=QUERY_FILE_ID, mimeType='text/plain').execute()
    decoded = results.decode('utf-8-sig')
    json_results = json.loads(decoded)

    return json_results


if __name__ == '__main__':
    QUERIES = get_queries()
    print(QUERIES)
    print(type(QUERIES))
