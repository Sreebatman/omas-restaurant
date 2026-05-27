import re

f = open(r'c:\Users\Sreehari\OneDrive\Desktop\Projects\Omas Restaurant\menu.html', 'r', encoding='utf-8')
c = f.read()
f.close()

cats = re.findall(r'data-category="([^"]+)"', c)
fils = re.findall(r'data-filter="([^"]+)"', c)

print('FILTER buttons:', fils)
print()
print('CATEGORY groups:', sorted(set(cats)))
print()
print('Unique categories count:', len(set(cats)))
