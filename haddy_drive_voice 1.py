import os
import pyttsx3
from google.oauth2 import service_account
from googleapiclient.discovery import build

# Path to service account JSON file via environment variable
SERVICE_ACCOUNT_FILE = os.getenv('GOOGLE_APPLICATION_CREDENTIALS', 'service_account.json')
SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def authenticate_with_google_drive():
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('drive', 'v3', credentials=credentials)
    return service

def list_drive_files(service, page_size=10):
    results = service.files().list(pageSize=page_size, fields="files(id, name)").execute()
    return results.get('files', [])

def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def chatbot_response_to_drive_query():
    service = authenticate_with_google_drive()
    files = list_drive_files(service)

    if not files:
        response = "No files found in your Google Drive."
    else:
        response = "Here are the top files in your Google Drive:\n"
        for file in files:
            response += f"- {file['name']} (ID: {file['id']})\n"

    print(response)
    speak_text(response)

# Run the chatbot flow
chatbot_response_to_drive_query()
