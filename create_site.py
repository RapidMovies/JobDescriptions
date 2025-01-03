import os

def create_site(site, title, target):
    ## ADD NEW SITE ##]
    assert '/' in site, f'"/" does not appear in "{site}"'
    # unallowed = {'<', '>', ':', '"', '/', '\\', '|', '?', '*'}
    # for c in unallowed:
    #     site = site.replace(c, f"(c{ord(c)})")
    site = site[site.index('//')+2:]
    site = "site/" + site
    ret_site = 'https://rapidmovies.github.io/JobDescriptions/' + site

    try:
        os.makedirs(site)
    except FileExistsError:
        pass
    target = f"<!-- {title} -->\n" + target
    with open(f'{site}/index.html', 'w') as f:
        f.write(target)

    ## UPDATE INDEX.HTML ##

    # TODO: Fix Index.HTML Update
    # all_pages = []
    # for root, _, files in os.walk('site'):
    #     for file in files:
    #         assert file == 'index.html', f'What is {file} doing at {root}?'
    #         with open(f"{root}/{file}") as f:
    #             title = f.read().split('\n')[0][5:-4]
    #         all_pages.append(f'    <li><a href="./{root}">{title}</li>')
    # all_pages = "\n".join(all_pages)

    # html = f"""<html xmlns="http://www.w3.org/1999/xhtml" >
    # <head>
    #     <title>Job Descriptions</title>
    # </head>
    # <body>
    # <h1>Job Descriptions</h1>
    # <ol>
    # {all_pages}
    # </o1>
    # </body>
    # </html>"""

    # with open('index.html', 'w') as f:
    #     f.write(html)

    return ret_site
