import re

try:
    with open(r'c:\Users\Sreehari\OneDrive\Desktop\Projects\Omas Restaurant\index.html', 'r', encoding='utf-8') as f:
        idx = f.read()

    start = idx.find('<!-- ===================== HERO')
    end = idx.find('<!-- ===================== FOOTER')

    top = idx[:start] + '<main>\n    <!-- ===================== PAGE HEADER ===================== -->\n    <section class="page-header">\n        <div class="container">\n            <h1 class="page-title">Our Menu</h1>\n            <p class="page-subtitle">A culinary journey through our finest offerings</p>\n        </div>\n    </section>\n\n    <!-- ===================== MENU SECTION ===================== -->\n    <section id="menu" class="menu-section">\n        <div class="container">\n            <h2 class="section-title">Explore Our Menu</h2>\n            {{MENU_PLACEHOLDER}}\n        </div>\n    </section>\n</main>\n'

    top = top.replace('<a href="index.html" class="nav-link active">Home</a>', '<a href="index.html" class="nav-link">Home</a>')
    top = top.replace('<a href="menu.html" class="nav-link">Menu</a>', '<a href="menu.html" class="nav-link active">Menu</a>')

    new_content = top + idx[end:]

    with open(r'c:\Users\Sreehari\OneDrive\Desktop\Projects\Omas Restaurant\menu.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print('Successfully wrote clean menu.html!')
except Exception as e:
    print('Error:', e)
