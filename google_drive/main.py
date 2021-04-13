import argparse

from google_drive import GoogleDriveClient, GoogleDriveObject


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--job", choices=["upload", "download"], required=True, type=str
    )
    parser.add_argument("--target_dir", required=True, type=str)
    parser.add_argument("--file_name_or_path", required=True, type=str)
    args = parser.parse_args()

    client = GoogleDriveClient(args)
    client.build()

    if args.job == "upload":
        client.upload_obj_to_drive(getattr(GoogleDriveObject, args.target_dir), args.file_name_or_path)


if __name__ == "__main__":
    main()
