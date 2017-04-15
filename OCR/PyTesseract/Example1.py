#Tesseract 
#
#
#Download: http://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-setup-3.05.00dev.exe
#
#make sure that TESSDATA_PREFIX Windows environment variable is set to the directory, containing tessdata directory. For example:
#TESSDATA_PREFIX=C:\Program Files (x86)\Tesseract-OCR
#In the command Line(cmd), write: setx TESSDATA_PREFIX=C:\Program Files (x86)\Tesseract-OCR


try:
     import Image
except ImportError:
     from PIL import Image

import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files (x86)/Tesseract-OCR/tesseract'

print(pytesseract.image_to_string(Image.open('F:\\Data\\txt.png'), lang='es'))


x = pytesseract.image_to_string(Image.open('F:\\Data\\txt.png'), lang='es')


from google import search
for url in search(x, tld='com.pk', lang='es', stop=5):
    print(url)

