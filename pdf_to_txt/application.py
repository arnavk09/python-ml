from PIL import Image
import pytesseract as tess
from pdf2image import convert_from_path
tess.pytesseract.tesseract_cmd = r'C:\Users\Arnav\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

'''This Code converts the input PDF to an Image for further processing by Tesseract.'''
filepath_pdf = input(r"Enter File Path WITHOUT '' :")
pdf_pages = convert_from_path(filepath_pdf, 350, poppler_path=r'C:\Program Files\poppler-0.68.0\bin')
i = 1
for page in pdf_pages:
    converted_image_name = "ImageForOCR_" + str(i) + ".jpg"
    page.save(converted_image_name, "JPEG")
    i = i+1
    print("Saved the image file as ",converted_image_name,". Tesseract will further process it.")
'''End of PDF to Image code'''

def fileWriter(x):
    ocr_converted_fileName = input("Enter File Name you want to save as :")
    file = open(ocr_converted_fileName, "w")
    file.write(x)
    print("OCR Completed. File saved as ",ocr_converted_fileName)
    file.close()

def mainFunction():
    img = Image.open(converted_image_name)
    text = tess.image_to_string(img)
    fileWriter(text)

'''Driver Function'''

mainFunction()