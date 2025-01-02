import sys
import os
from tld import get_tld

site = sys.argv[1]
assert '/' in site, f'"/" does not appear in "{site}"'

domain_name = get_tld(site, as_object=True).fld
site = site[site.index(domain_name):]

os.makedirs(site)
