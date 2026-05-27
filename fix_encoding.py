import re
import os

path = r'c:\Users\Sreehari\OneDrive\Desktop\Projects\Omas Restaurant\menu.html'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace ? followed by digit in price spans
content = re.sub(r'class="menu-item-price">[^<\d]*(\d)', r'class="menu-item-price">₹\1', content)

# Fix Oma's
content = content.replace("Oma?Ts", "Oma's")
content = content.replace("Oma'Ts", "Oma's")
content = content.replace("Oma?Ts", "Oma's")
content = content.replace("Omas", "Oma's")
content = content.replace("Oma?s", "Oma's")

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Fixed encoding issues in menu.html")
