import json
import os
from httplib2 import Http
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials


def get_queries():
    """Return JSON object of query terms from remote doc storage"""

    #AUTH_URI = os.environ.get('AUTH_URI')
    CLIENT_ID = os.environ.get('CLIENT_ID')
    CLIENT_SECRET = os.environ.get('CLIENT_SECRET')
    #REDIRECT_URI = os.environ.get('REDIRECT_URI')
    REFRESH_TOKEN = os.environ.get('REFRESH_TOKEN')
    #REVOKE_URI = os.environ.get('REVOKE_URI')
    SCOPES = os.environ.get('SCOPES')
    TOKEN_URI = os.environ.get('TOKEN_URI')
    QUERY_FILE_ID = os.environ.get('QUERY_FILE_ID')

    credentials = Credentials(
         token=None,
         client_id=CLIENT_ID,
         client_secret=CLIENT_SECRET,
         token_uri=TOKEN_URI,
         scopes=SCOPES,
         refresh_token=REFRESH_TOKEN
         # redirect_uri=REDIRECT_URI,
         # auth_uri = AUTH_URI,
         # revoke_uri = REVOKE_URI,
         # access_type='offline',
         # prompt='consent',
    )

    service = build('drive', 'v3', credentials=credentials)

    results = service.files().export(fileId=QUERY_FILE_ID, mimeType='text/plain').execute()
    decoded = results.decode('utf-8-sig')
    json_results = json.loads(decoded)

    return json_results


if __name__ == '__main__':
    QUERIES = get_queries()
    print(QUERIES)
    print(type(QUERIES))
