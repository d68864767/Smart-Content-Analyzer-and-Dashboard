# Deployment Guide

This guide will walk you through the steps to deploy the "Smart Content Analyzer and Dashboard" on Google Cloud Platform (GCP).

## Prerequisites

- A Google Cloud Platform account
- Google Cloud SDK installed on your local machine
- Python 3.7 or later installed on your local machine
- Node.js installed on your local machine

## Steps

1. **Clone the repository**

    Clone the project repository to your local machine.

    ```
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Set up a Google Cloud Project**

    Create a new project on Google Cloud Platform. Note down the Project ID.

3. **Enable APIs**

    Enable the following APIs for your project:
    - Google Cloud Natural Language API
    - Google Cloud Vision API
    - Google Cloud Speech-to-Text API
    - Google Cloud Storage
    - Google Cloud Firestore
    - Google Cloud BigQuery (optional)

4. **Create a Service Account**

    Create a new service account and download the JSON key file. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of the JSON key file.

    ```
    export GOOGLE_APPLICATION_CREDENTIALS="/path/to/keyfile.json"
    ```

5. **Create a Storage Bucket**

    Create a new storage bucket on Google Cloud Storage. Note down the bucket name.

6. **Set Environment Variables**

    Set the following environment variables:

    ```
    export PROJECT_ID="<your-project-id>"
    export BUCKET_NAME="<your-bucket-name>"
    ```

7. **Install Dependencies**

    Install the Python and Node.js dependencies.

    ```
    pip install -r requirements.txt
    npm install
    ```

8. **Deploy the Application**

    Deploy the application on Google Cloud Platform.

    ```
    gcloud app deploy
    ```

9. **Access the Application**

    After the deployment is successful, you can access the application at `https://<your-project-id>.appspot.com`.

## Notes

- Make sure to replace `<repository-url>`, `<repository-directory>`, `<your-project-id>`, and `<your-bucket-name>` with your actual values.
- The `requirements.txt` and `package.json` files list the Python and Node.js dependencies respectively. These files should be present in your project directory.
- The `gcloud app deploy` command deploys the application as described in the `app.yaml` file in your project directory. Make sure this file is correctly configured.
- The application uses Google Cloud Firestore for data storage. Make sure Firestore is in Datastore mode.
- The application uses Google Cloud Storage for file storage. Make sure the bucket is correctly configured and accessible by the service account.
- The application uses Google Cloud BigQuery for data processing. This is optional and can be enabled if needed.
