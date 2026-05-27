import os

html_path = r'c:\Users\Sreehari\OneDrive\Desktop\Projects\Omas Restaurant\menu.html'
with open(html_path, 'r', encoding='utf-8') as f:
    content = f.read()

start_idx = content.find('<h2 class="section-title">Explore Our Menu</h2>') + len('<h2 class="section-title">Explore Our Menu</h2>')
end_idx = content.find('<!-- ===================== FOOTER')

if start_idx != -1 and end_idx != -1:
    new_content = content[:start_idx] + '\n        {{MENU_PLACEHOLDER}}\n    </div>\n    </section>\n\n    ' + content[end_idx:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('Cleaned menu.html!')
else:
    print('Could not find start or end index')
