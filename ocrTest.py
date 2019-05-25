try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import os

#pytesseract.pytesseract.tesseract_cmd = r"C:/Programme/Tesseract-OCR"

# Simple image to string
print(pytesseract.image_to_string(Image.open('C:/Users/jansu/Desktop/testocrdata/ocrtestdaten1.png'), lang='deu'))

base_dir = os.path.join(os.path.dirname('C:/Users/jansu/Desktop/testocrdata/'), 'tensorflowtest')

print(base_dir)






