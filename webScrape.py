import pytesseract
from PIL import Image
import re as re

# Load the screenshot image
screenshot_path = 'jordanPatton.png'  # Update this with your screenshot file path
image = Image.open(screenshot_path)

# Use Tesseract to extract text from the image
text = pytesseract.image_to_string(image)
nameObject = re.search(r'([\w\s]{1,20})\|[\w\s]{1,20}',text)
name = nameObject.group(1)

# Print the extracted text
print(name)
