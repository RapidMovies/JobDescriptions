import os


def store_jd(url: str, position: str, desc: str):
    print(end=" Job Description... ")
    assert "/" in url, f'"/" does not appear in "{url}"'
    unallowed = {"<", ">", ":", '"', "\\", "|", "?", "*"}
    for c in unallowed:
        url = url.replace(c, f"(c{ord(c)})")
    url = url[url.index("//") + 2 :]
    url = "site/" + url
    ret_site = "https://rapidmovies.github.io/JobDescriptions/" + url

    try:
        os.makedirs(url)
    except FileExistsError:
        pass

    desc = f"<!-- {position} -->\n" + desc
    with open(f"{url}/index.html", "w") as f:
        f.write(desc)

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

    print("DONE")
    return ret_site
