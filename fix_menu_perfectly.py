import re

try:
    with open(r'c:\Users\Sreehari\OneDrive\Desktop\Projects\Omas Restaurant\index.html', 'r', encoding='utf-8') as f:
        idx = f.read()

    main_start = idx.find('<main>')
    footer_start = idx.find('<!-- ===================== FOOTER')

    top = idx[:main_start] + '<main>\n    <!-- ===================== PAGE HEADER ===================== -->\n    <section class="page-header">\n        <div class="container">\n            <h1 class="page-title">Our Menu</h1>\n            <p class="page-subtitle">A culinary journey through our finest offerings</p>\n        </div>\n    </section>\n\n    <!-- ===================== MENU SECTION ===================== -->\n    <section id="menu" class="menu-section">\n        <div class="container">\n            <h2 class="section-title">Explore Our Menu</h2>\n            {{MENU_PLACEHOLDER}}\n        </div>\n    </section>\n</main>\n'

    # Note: index.html has a <footer>. We just copy everything from the footer to the end.
    bottom = idx[footer_start:]

    # But wait, index.html might have some script tags that are different? No, script.js is the same.
    # Also we need to make sure the nav link for 'Menu' is active instead of 'Home'.
    top = top.replace('<a href="index.html" class="nav-link active">Home</a>', '<a href="index.html" class="nav-link">Home</a>')
    top = top.replace('<a href="menu.html" class="nav-link">Menu</a>', '<a href="menu.html" class="nav-link active">Menu</a>')

    with open(r'c:\Users\Sreehari\OneDrive\Desktop\Projects\Omas Restaurant\menu.html', 'w', encoding='utf-8') as f:
        f.write(top + bottom)
    
    print('Created perfectly clean menu.html skeleton from index.html')
except Exception as e:
    print('Error:', e)
