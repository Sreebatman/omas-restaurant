import re

html_path = r'c:\Users\Sreehari\OneDrive\Desktop\Projects\Omas Restaurant\menu.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<section id="menu"')
footers = list(re.finditer('<!-- ===================== FOOTER', content))

if footers:
    last_footer_idx = footers[-1].start()
else:
    last_footer_idx = len(content)

top = content[:start_idx]
bottom = content[last_footer_idx:]

new_content = top + '<section id="menu" class="menu-section">\n<div class="container">\n<h2 class="section-title">Explore Our Menu</h2>\n{{MENU_PLACEHOLDER}}\n</div>\n</section>\n</main>\n' + bottom

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print('SKELETON FIXED!')
