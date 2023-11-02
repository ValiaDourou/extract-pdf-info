#pip install pytesseract 
from PIL import Image 
from pytesseract import pytesseract 
import re


def find_date(image_path):
 # Defining the path to tesseract.exe 
 path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
 
 #Open the image
 img = Image.open(image_path) 
 
 # Providing the tesseract executable location to pytesseract library 
 pytesseract.tesseract_cmd = path_to_tesseract 
 
 #Extract text from image
 text = pytesseract.image_to_string(img) 
 
 #Find the date with regex
 x = re.findall("[0-3][0-9]/[0-1][0-9]/[0-9][0-9][0-9][0-9]", text)
 
 # Displaying the extracted text 
 print(x)

find_date("368080144_290519130490318_2642191076935064121_n.jpg")
