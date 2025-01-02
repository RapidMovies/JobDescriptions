import sys
import os
import re

## ADD NEW SITE ##

assert len(sys.argv) == 3, "Correct Usage: python createsite.py <URL> <title>"

site = sys.argv[1]
title = sys.argv[2]
assert '/' in site, f'"/" does not appear in "{site}"'
site = site[site.index('//')+2:]
site = "site/" + site
print('https://rapidmovies.github.io/JobDescriptions/' + site)

try:
    os.makedirs(site)
except FileExistsError:
    pass
with open('target.html') as f:
    target = f"<!-- {title} -->\n" + f.read()
with open(f'{site}/index.html', 'w') as f:
    f.write(target)

## UPDATE INDEX.HTML ##

all_pages = []
for root, _, files in os.walk('site'):
    for file in files:
        assert file == 'index.html', f'What is {file} doing at {root}?'
        with open(f"{root}/{file}") as f:
            title = f.read().split('\n')[0][5:-4]
        all_pages.append(f'    <li><a href="./{root}">{title}</li>')
all_pages = "\n".join(all_pages)

html = f"""<html xmlns="http://www.w3.org/1999/xhtml" >
<head>
    <title>Job Descriptions</title>
</head>
<body>
  <h1>Job Descriptions</h1>
  <ol>
{all_pages}
  </o1>
</body>
</html>"""

with open('index.html', 'w') as f:
    f.write(html)
