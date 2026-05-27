import urllib.request
from PyPDF2 import PdfReader
import io

url = "https://www.omasrestaurant.com/menu/omas-6th-mile.pdf"
try:
    print(f"Downloading {url}...")
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as response:
        pdf_file = io.BytesIO(response.read())
        
    reader = PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
        
    print("--- MENU TEXT ---")
    print(text)
except Exception as e:
    print(f"Error: {e}")
