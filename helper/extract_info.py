from bs4 import BeautifulSoup
from datetime import datetime
from helper.store_jd import store_jd
import re


def extract_info(page_html: str, url: str, req_id: str):
    print(end="Extracting Information from HTML page... ")
    soup = BeautifulSoup(page_html, "html.parser")

    page_html = str(soup.find("div", {"id": "job-details"}))
    position = soup.find("h1", {"class": "t-24"}).text
    position = re.sub(r"\s+", r" ", position)

    _det_class = "job-details-jobs-unified-top-card__primary-description-container"
    _details = soup.find("div", {"class": _det_class})
    location = re.match(r"([^·]*) · ", _details.text.strip()).group(1)

    _company_box = soup.find("div", {"class": "jobs-company__box"})
    company = _company_box.find("div", {"class": "artdeco-entity-lockup__title"})
    company = company.text.strip()
    _details = _company_box.find_all("div", {"class": "t-14"})
    _details = next(d for d in _details if "mt5" in d["class"]).text.strip()
    _pattern = r"([^\n]*)\s*([^\s].*) employees\s*([^\s].*) on LinkedIn"
    industry, employees, li_members = re.match(_pattern, _details).groups()
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    img_url = _company_box.find("img")["src"]
    print("DONE")
    page_path = store_jd(url, position, str(page_html))

    row = [
        f'=IMAGE("{img_url}")',
        company,
        industry,
        employees,
        li_members,
        f'=HYPERLINK("{page_path}","{position}")',
        req_id,
        location,
        now,
        "",
        "Pending",
    ]

    return row
