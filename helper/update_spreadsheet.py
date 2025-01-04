from google.oauth2 import service_account
from googleapiclient.discovery import build


def update_spreadsheet(row_to_add, spreadsheet_id, service_key_path):
    print(end="Updating Spreadsheet... ")
    RANGE_NAME = "Sheet1"
    credentials = service_account.Credentials.from_service_account_file(
        service_key_path, scopes=["https://www.googleapis.com/auth/spreadsheets"]
    )
    service = build("sheets", "v4", credentials=credentials)

    # Append the new row
    body = {"values": [row_to_add]}  # 'values' should be a list of lists
    udt = (
        service.spreadsheets()
        .values()
        .append(
            spreadsheetId=spreadsheet_id,
            range=RANGE_NAME,
            valueInputOption="USER_ENTERED",  # Can also use 'RAW'
            insertDataOption="INSERT_ROWS",  # Use 'OVERWRITE' to replace
            body=body,
        )
        .execute()
    )["updates"]
    try:
        print(f"{udt['updatedRows']} row(s), {udt['updatedColumns']} column(s), {udt['updatedCells']} cell(s) updated within {udt['updatedRange']}")
    except:
        print(udt)
        print(f"{udt['updatedRows']} row(s), {udt['updatedColumns']} column(s), {udt['updatedCells']} cell(s) updated within {udt['updatedRange']}")
