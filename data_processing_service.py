```python
import os
from google.cloud import bigquery

class DataProcessingService:
    def __init__(self):
        self.client = bigquery.Client()

    def run_query(self, query):
        """Run a SQL query on BigQuery."""
        query_job = self.client.query(query)

        return query_job.result()

    def analyze_sentiment_data(self):
        """Analyze sentiment data."""
        query = """
        SELECT sentiment, COUNT(*) as count
        FROM `your-project-id.your-dataset.your-table`
        GROUP BY sentiment
        ORDER BY count DESC
        """
        return self.run_query(query)

    def analyze_entity_data(self):
        """Analyze entity data."""
        query = """
        SELECT entity, COUNT(*) as count
        FROM `your-project-id.your-dataset.your-table`
        GROUP BY entity
        ORDER BY count DESC
        """
        return self.run_query(query)

    def analyze_syntax_data(self):
        """Analyze syntax data."""
        query = """
        SELECT syntax, COUNT(*) as count
        FROM `your-project-id.your-dataset.your-table`
        GROUP BY syntax
        ORDER BY count DESC
        """
        return self.run_query(query)

    def analyze_image_data(self):
        """Analyze image data."""
        query = """
        SELECT label, COUNT(*) as count
        FROM `your-project-id.your-dataset.your-table`
        GROUP BY label
        ORDER BY count DESC
        """
        return self.run_query(query)

    def analyze_audio_data(self):
        """Analyze audio data."""
        query = """
        SELECT transcription, COUNT(*) as count
        FROM `your-project-id.your-dataset.your-table`
        GROUP BY transcription
        ORDER BY count DESC
        """
        return self.run_query(query)

if __name__ == "__main__":
    data_processing_service = DataProcessingService()

    # Test sentiment data analysis
    sentiment_data = data_processing_service.analyze_sentiment_data()
    for row in sentiment_data:
        print(f"Sentiment: {row['sentiment']}, Count: {row['count']}")

    # Test entity data analysis
    entity_data = data_processing_service.analyze_entity_data()
    for row in entity_data:
        print(f"Entity: {row['entity']}, Count: {row['count']}")

    # Test syntax data analysis
    syntax_data = data_processing_service.analyze_syntax_data()
    for row in syntax_data:
        print(f"Syntax: {row['syntax']}, Count: {row['count']}")

    # Test image data analysis
    image_data = data_processing_service.analyze_image_data()
    for row in image_data:
        print(f"Label: {row['label']}, Count: {row['count']}")

    # Test audio data analysis
    audio_data = data_processing_service.analyze_audio_data()
    for row in audio_data:
        print(f"Transcription: {row['transcription']}, Count: {row['count']}")
```
