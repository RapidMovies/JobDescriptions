from bs4 import BeautifulSoup
import re
from create_site import create_site
from datetime import datetime
import sys

assert len(sys.argv) == 3, f"Correct Usage: python {sys.argv[0]} <URL> <REQID>"
site = sys.argv[1]
reqid = sys.argv[2]

with open("target.html") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

desc = soup.find("div", {"id": "job-details"})
position = soup.find("h1", {"class": "t-24"}).text
position = re.sub(r"\s+", r" ", position)

_details = soup.find(
    "div", {"class": "job-details-jobs-unified-top-card__primary-description-container"}
)
location = re.match(r"([^·]*) · ", _details.text.strip()).group(1)

_company_box = soup.find("div", {"class": "jobs-company__box"})
company = _company_box.find("div", {"class": "artdeco-entity-lockup__title"})
company = company.text.strip()
_details = _company_box.find_all("div", {"class": "t-14"})
_details = next(d for d in _details if "mt5" in d["class"]).text.strip()
_match = re.match(r"([^\n]*)\s*([^\s].*) employees\s*([^\s].*) on LinkedIn", _details)
industry = _match.group(1)
employees = _match.group(2)
li_employees = _match.group(3)
now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

ret_site = create_site(site, position, str(desc))
row_to_add = [
    company,
    industry,
    employees,
    li_employees,
    f'=HYPERLINK(""{ret_site}"",""{position}"")',
    reqid,
    location,
    now,
    "",
    "pending",
]
row_to_add = ",".join(f'"{e}"' if "," in e else e for e in row_to_add)
with open("job_application_tracker.csv", "a") as f:
    f.write(row_to_add + "\n")
