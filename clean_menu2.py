import re

html_path = r'c:\Users\Sreehari\OneDrive\Desktop\Projects\Omas Restaurant\menu.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace everything from <section id="menu" to <!-- ======== FOOTER
new_content = re.sub(
    r'(<section id="menu" class="menu-section">)(.*?)(<!-- ===================== FOOTER)', 
    r'\1\n        <div class="container">\n            <h2 class="section-title">Explore Our Menu</h2>\n            {{MENU_PLACEHOLDER}}\n        </div>\n    </section>\n\n    \3', 
    content, 
    flags=re.DOTALL
)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('Cleaned menu.html completely!')
