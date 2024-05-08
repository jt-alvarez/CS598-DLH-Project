import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ["https://www.googleapis.com/auth/drive.readonly", "https://www.googleapis.com/auth/drive.metadata.readonly", "https://www.googleapis.com/auth/drive"]


def authenticate():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
            )
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    return creds


def list_files(service):
    try:
        results = (
            service.files()
            .list(pageSize=10, fields="nextPageToken, files(id, name)")
            .execute()
        )
        items = results.get("files", [])
        return items
    except HttpError as error:
        print(f"An error occurred: {error}")


def download_file(service, file_id):
    try:
        request = service.files().export_media(fileId=file_id, mimeType="text/csv")
        result = request.execute()
        return result.decode("utf-8")
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


def get_file_id_by_name(service, file_name):
    try:
        results = (
            service.files()
            .list(pageSize=1, fields="files(id)", q=f"name='{file_name}'")
            .execute()
        )
        items = results.get("files", [])
        if items:
            return items[0]["id"]
        else:
            print("File not found.")
            return None
    except HttpError as error:
        print(f"An error occurred: {error}")
        return None


def main():
    creds = authenticate()
    service = build("drive", "v3", credentials=creds)

    file_name = "contentToDownload"
    file_id = get_file_id_by_name(service, file_name)
    if file_id:
        file_content = download_file(service, file_id)
        if file_content:
            print("Downloaded content:")
            print(file_content)


if __name__ == "__main__":
    main()
