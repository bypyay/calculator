import urllib.request
import re
import json

url = 'https://www.calculator.net/sitemap.html'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
with urllib.request.urlopen(req) as resp:
    html = resp.read().decode('utf-8', errors='ignore')

sections = re.findall(r'<h3><a[^>]*>(.*?)</a></h3>(.*?)(?=(?:<h3>|$))', html, flags=re.DOTALL)

all_tools = []
cat_map = {
    'Financial Calculators': 'financial',
    'Fitness and Health Calculators': 'health',
    'Math Calculators': 'math',
    'Other Calculators': 'everyday',
    'Calculators for Your Site': 'widgets'
}

for cat_title, content in sections:
    cat_key = cat_map.get(cat_title, 'other')
    if cat_key == 'widgets':
        continue
    links = re.findall(r'<a href="(/[^"]+\.html)">([^<]+)</a>', content)
    for href, title in links:
        slug = href.replace('.html', '').replace('/', '')
        if slug in ['sitemap', 'about-us', 'contact-us']:
            continue
        all_tools.append({
            'id': slug,
            'title': title.strip(),
            'category': cat_key,
            'category_title': cat_title.strip()
        })

print(f'Total scraped tools: {len(all_tools)}')
with open('all_calc_tools.json', 'w', encoding='utf-8') as f:
    json.dump(all_tools, f, indent=2)