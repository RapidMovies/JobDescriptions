from dotenv import dotenv_values
from helper.extract_info import extract_info
from helper.update_spreadsheet import update_spreadsheet
import sys

assert len(sys.argv) == 3, f"Correct Usage: python {sys.argv[0]} <URL> <REQID>"
url = sys.argv[1]
req_id = sys.argv[2]
spreadsheet_id = dotenv_values(".env")["SPREADSHEET_ID"]

with open("page.html") as f:
    page_html = f.read()

row = extract_info(page_html, url, req_id)
update_spreadsheet(row, spreadsheet_id, "service_key.json")
