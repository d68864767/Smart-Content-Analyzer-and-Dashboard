```python
import os
from google.cloud import vision

class ImageAnalysisService:
    def __init__(self):
        self.client = vision.ImageAnnotatorClient()

    def analyze_image(self, image_path):
        """Analyze an image for object detection, label annotation, and OCR."""
        with open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)

        # Object detection
        objects = self.client.object_localization(image=image).localized_object_annotations
        print('Objects:')
        for object_ in objects:
            print(f'{object_.name} (confidence: {object_.score})')

        # Label annotation
        labels = self.client.label_detection(image=image).label_annotations
        print('Labels:')
        for label in labels:
            print(f'{label.description} (confidence: {label.score})')

        # OCR
        response = self.client.text_detection(image=image)
        texts = response.text_annotations
        print('Texts:')
        for text in texts:
            print(f'"{text.description}"')

if __name__ == "__main__":
    image_analysis_service = ImageAnalysisService()

    # Test image analysis
    image_analysis_service.analyze_image('test.jpg')
```
