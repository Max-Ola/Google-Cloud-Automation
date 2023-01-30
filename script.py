import os
import google.auth
from google.cloud import storage

# Set the folder path to be backed up
folder_path = '/path/to/folder'

# Authenticate with Google Cloud
credentials, project = google.auth.default()

# Create a client for Google Cloud Storage
client = storage.Client(credentials=credentials, project=project)

# Upload files to Google Cloud Storage
def upload_to_gcs(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            bucket_name = 'your-bucket-name'
            blob_name = file_path.replace(folder_path, '')
            bucket = client.bucket(bucket_name)
            blob = bucket.blob(blob_name)
            blob.upload_from_filename(file_path)

# Schedule the backup to run every day at 8 PM
def schedule_backup():
    cron_command = "0 20 * * * python3 /path/to/script.py"
    with open("/etc/crontab", "a") as f:
        f.write(cron_command)

if __name__ == '__main__':
    upload_to_gcs(folder_path)
    schedule_backup()
