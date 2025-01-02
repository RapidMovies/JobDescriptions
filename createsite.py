import sys
import os

site = sys.argv[1]
assert '/' in site, f'"/" does not appear in "{site}"'
site = site[site.index('//')+2:]
site = "site/" + site
print(site)

os.makedirs(site)
os.system(f"cp target.html {site}/index.html")
