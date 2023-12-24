```python
import os
from google.cloud import firestore
from google.cloud import storage

class DataStorageService:
    def __init__(self, bucket_name, firestore_db):
        self.bucket_name = bucket_name
        self.firestore_db = firestore_db
        self.storage_client = storage.Client()
        self.firestore_client = firestore.Client()

    def upload_to_bucket(self, source_file_name, destination_blob_name):
        """Uploads a file to the bucket."""
        bucket = self.storage_client.bucket(self.bucket_name)
        blob = bucket.blob(destination_blob_name)

        blob.upload_from_filename(source_file_name)

        print(f"File {source_file_name} uploaded to {destination_blob_name}.")

    def download_from_bucket(self, source_blob_name, destination_file_name):
        """Downloads a file from the bucket."""
        bucket = self.storage_client.bucket(self.bucket_name)
        blob = bucket.blob(source_blob_name)

        blob.download_to_filename(destination_file_name)

        print(f"File {source_blob_name} downloaded to {destination_file_name}.")

    def save_to_firestore(self, collection_name, document_id, data):
        """Saves data to Firestore."""
        doc_ref = self.firestore_client.collection(collection_name).document(document_id)
        doc_ref.set(data)

        print(f"Data saved to Firestore: {collection_name}/{document_id}")

    def get_from_firestore(self, collection_name, document_id):
        """Retrieves data from Firestore."""
        doc_ref = self.firestore_client.collection(collection_name).document(document_id)
        doc = doc_ref.get()

        if doc.exists:
            print(f"Document data: {doc.to_dict()}")
            return doc.to_dict()
        else:
            print(f"No such document: {collection_name}/{document_id}")
            return None

if __name__ == "__main__":
    data_storage_service = DataStorageService('your-bucket-name', 'your-firestore-db')

    # Test upload to bucket
    data_storage_service.upload_to_bucket('test.txt', 'test-upload.txt')

    # Test download from bucket
    data_storage_service.download_from_bucket('test-upload.txt', 'test-download.txt')

    # Test save to Firestore
    data_storage_service.save_to_firestore('test-collection', 'test-document', {'key': 'value'})

    # Test get from Firestore
    data_storage_service.get_from_firestore('test-collection', 'test-document')
```
