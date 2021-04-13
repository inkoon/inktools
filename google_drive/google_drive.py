import os
import tarfile

from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import client, file, tools

SCOPES = "https://www.googleapis.com/auth/drive.file"
AUTH = "authentication"
CLIENT_SECRET = "client_secret_891729516543-3f96fvdnl64gtjfma4a102esljqkkogn.apps.googleusercontent.com.json"
ZIP_EXTENSION = ".tar.gz"


class GoogleDriveObject:
    # google drive id
    klue_electra = "1WXh7zRmt1j-nz3e4anbTPdXU8A5eTGxj"


class GoogleDriveClient:
    def __init__(self, args):
        self.args = args
        self.scopes = SCOPES
        self.auth = AUTH
        self.client_secret = CLIENT_SECRET

    def build(self):
        self.store = file.Storage(os.path.join(self.auth, "storage.json"))
        self.creds = self.store.get()
        if not self.creds or self.creds.invalid:
            print("make new storage data file")
            flow = client.flow_from_clientsecrets(
                os.path.join(self.auth, self.client_secret), self.scopes
            )
            self.creds = tools.run_flow(flow, store, args)

        self.client = build("drive", "v3", http=self.creds.authorize(Http()))

    def _zip(self, dir_name):
        base_name = os.path.basename(dir_name.strip("/"))
        tar = tarfile.open(f"{base_name}{ZIP_EXTENSION}", "w:gz")
        tar.add(dir_name, arcname=base_name)
        tar.close()

    def upload_obj_to_drive(self, target_dir_id, file_path):
        if not os.path.exists(file_path):
            raise Exception("There is no such file or directory")

        remove_tar = False
        file_name = os.path.basename(file_path.strip("/"))
        if os.path.isdir(file_path):
            print(f"Zipping {file_name} as tar.gz...")
            self._zip(file_path)
            file_path = f"{file_name}{ZIP_EXTENSION}"
            file_name = file_path
            remove_tar = True

        # TODO: check overlap

        metadata = {"name": file_name, "parents": [target_dir_id], "mimeType": None}
        res = self.client.files().create(body=metadata, media_body=file_path).execute()
        if res:
            print(f"Uploaded \"{file_name}\" ({res['mimeType']})")

        if remove_tar:
            os.remove(file_path)

    # TODO: def download_obj_from_drive
