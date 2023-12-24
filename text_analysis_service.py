```python
import os
from google.cloud import language_v1
from google.cloud.language_v1 import enums

class TextAnalysisService:
    def __init__(self):
        self.client = language_v1.LanguageServiceClient()

    def analyze_sentiment(self, text_content):
        """Analyzing Sentiment in a String"""

        # Available types: PLAIN_TEXT, HTML
        type_ = enums.Document.Type.PLAIN_TEXT

        # Optional. If not specified, the language is automatically detected.
        # For list of supported languages:
        # https://cloud.google.com/natural-language/docs/languages
        language = "en"
        document = {"content": text_content, "type": type_, "language": language}

        # Available values: NONE, UTF8, UTF16, UTF32
        encoding_type = enums.EncodingType.UTF8

        response = self.client.analyze_sentiment(document, encoding_type=encoding_type)
        return response

    def analyze_entities(self, text_content):
        """Analyzing Entities in a string"""

        type_ = enums.Document.Type.PLAIN_TEXT
        language = "en"
        document = {"content": text_content, "type": type_, "language": language}

        encoding_type = enums.EncodingType.UTF8

        response = self.client.analyze_entities(document, encoding_type=encoding_type)
        return response

    def analyze_syntax(self, text_content):
        """Analyzing Syntax in a string"""

        type_ = enums.Document.Type.PLAIN_TEXT
        language = "en"
        document = {"content": text_content, "type": type_, "language": language}

        encoding_type = enums.EncodingType.UTF8

        response = self.client.analyze_syntax(document, encoding_type=encoding_type)
        return response

if __name__ == "__main__":
    text_analysis_service = TextAnalysisService()

    # Test sentiment analysis
    sentiment_response = text_analysis_service.analyze_sentiment('I am happy.')
    print(f"Sentiment: {sentiment_response.document_sentiment.score}")

    # Test entity analysis
    entity_response = text_analysis_service.analyze_entities('Google Cloud is a suite of cloud computing services.')
    for entity in entity_response.entities:
        print(f"Entity: {entity.name}, Type: {enums.Entity.Type(entity.type).name}")

    # Test syntax analysis
    syntax_response = text_analysis_service.analyze_syntax('This is a syntax analysis test.')
    for token in syntax_response.tokens:
        print(f"Token text: {token.text.content}, Part of speech: {enums.PartOfSpeech.Tag(token.part_of_speech.tag).name}")
```
