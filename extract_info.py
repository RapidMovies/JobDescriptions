from bs4 import BeautifulSoup
import re

with open("target.html") as f:
    soup = BeautifulSoup(f.read(), "html.parser")

desc = soup.find("div", {"id": "job-details"})
position = soup.find("h1", {"class": "t-24"}).text

_details = soup.find(
    "div", {"class": "job-details-jobs-unified-top-card__primary-description-container"}
)
location = re.match(r"([^·]*) · ", _details.text.strip()).group(1)

_company_box = soup.find("div", {"class": "jobs-company__box"})
company = _company_box.find("div", {"class": "artdeco-entity-lockup__title"})
company = company.text.strip()
_details = _company_box.find_all("div", {"class": "t-14"})
_details = next(d for d in _details if "mt5" in d["class"]).text.strip()
_match = re.match(r'([^\n]*)\s*([^\s].*) employees\s*([^\s].*) on LinkedIn', _details)
industry = _match.group(1)
employees = _match.group(2)
li_employees = _match.group(3)

print([company, industry, employees, li_employees, position, '#REQID', location])
