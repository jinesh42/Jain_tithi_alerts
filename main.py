from __future__ import print_function

import datetime
import os.path
import requests
import json
from heyoo import WhatsApp



from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        #print('Getting the upcoming 10 events')
        events_result = service.events().list(calendarId='yja.org_s2t29hla94rej0pieuc8t17a34@group.calendar.google.com', timeMin=now,
                                              maxResults=1, singleEvents=True,
                                              orderBy='startTime').execute()
    
        events = events_result.get('items', [])
        #page_token = None
        #calendar_list = service.calendarList().list(pageToken=page_token).execute()
        #print(calendar_list['items'])
        #for calendar_list_entry in calendar_list['items']:
        #    print(calendar_list_entry['summary'])

        if not events:
            print('No upcoming events found.')
            return

        # Prints the start and name of the next 10 events
        # ...
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])
            #if event['summary']!='Aatham' or event['summary']!='Chaudas':
            messenger = WhatsApp('EAAKEGEodfAgBAClnpoCgiZCuI7hVfRFfwnfSHUhf0Q0Jil7uZAApJuHj0D40kKUvbh7Uc3XHCLBEp6ZAjZAslYpZCg3b9FOWNfc2VJfzfpGgrdmoCfAijNochfO9dtemhwTWgwPCjcZBGOMs2adtRhkSSQpsA63SeHCZAEHGkNu6sSdjsSTzcSdHlCaYYzXt6557al000iesf2dixl53eZAl',phone_number_id='100823262930169')
                # For sending a Text messages
            messenger.send_message(f"Jai Jinendra!! \n Date : {start}. \n Today is {event['summary']}. \n Please do Ratri Bhojan and Kandamul tyag.", '918879453842')

    except HttpError as error:
        print('An error occurred: %s' % error)


if __name__ == '__main__':
    main()