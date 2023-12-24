```python
import os
from google.cloud import storage

class IngestionService:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name
        self.storage_client = storage.Client()

    def upload_file(self, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        bucket = self.storage_client.bucket(self.bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print(f"File {source_file_name} uploaded to {destination_blob_name}.")

    def list_files(self):
        """Lists all the files in the bucket."""
        blobs = self.storage_client.list_blobs(self.bucket_name)

        for blob in blobs:
            print(blob.name)

    def download_file(self, source_blob_name, destination_file_name):
        """Downloads a file from the bucket."""
        bucket = self.storage_client.bucket(self.bucket_name)
        blob = bucket.blob(source_blob_name)

        blob.download_to_filename(destination_file_name)

        print(f"File {source_blob_name} downloaded to {destination_file_name}.")

if __name__ == "__main__":
    ingestion_service = IngestionService('your-bucket-name')

    # Test upload
    ingestion_service.upload_file('test.txt', 'test-upload.txt')

    # Test list
    ingestion_service.list_files()

    # Test download
    ingestion_service.download_file('test-upload.txt', 'test-download.txt')
```
