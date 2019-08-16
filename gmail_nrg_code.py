# -*- coding: utf-8 -*-
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import re

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly', 'https://www.googleapis.com/auth/gmail.modify']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('gmail', 'v1', credentials=creds)

    """Uncomment to print label_name + label_id
    is needed to determine Energy Label id.
    """
    # results = service.users().labels().list(userId='me').execute()
    #
    # labels = results.get('labels', [])
    #
    # if not labels:
    #     print('No labels found.')
    # else:
    #     print('Labels:')
    #     for label in labels:
    #         print(label['name'] + " " + label['id'])

    # Call the Gmail API to fetch INBOX Energy, only unread messages
    results = service.users().messages().list(userId='me', labelIds=['UNREAD', 'Label_5591763986028835289'],
                                              maxResults=1).execute()
    messages = results.get('messages', [])

    if not messages:
        print("No messages found.")
        return None
    else:
        print("Message snippets:")
        for message in messages:
            msg = service.users().messages().get(userId='me', format='full', id=message['id']).execute()
            # marks mail as read
            service.users().messages().modify(userId='me', id=message['id'],
                                              body={'removeLabelIds': ['UNREAD']}).execute()
            snippet = msg['snippet']
            print(snippet)
            verification_code = str(snippet).split("Dein Code für game.energy.ch")[-1]
            verification_code = verification_code.split(re.match('[0-3][0-9]/[0-1][0-9]/2019', verification_code))[
                0].strip()
            print(verification_code)
            return verification_code
# uncomment to run once to fetch label id or for development
# if __name__ == '__main__':
#     main()
