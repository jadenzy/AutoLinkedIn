import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

# The ID and range of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = "1wPSluF2x99HR2ITwUYvRRn6-LRP2_4eUGMsR-nIb2CU"
SAMPLE_RANGE_NAME = "Sheet1!B:C"

ID = ""
PASSWORD = ""

def main():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                "credentials.json", SCOPES
        )
        creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open("token.json", "w") as token:
            token.write(creds.to_json())

    try:
        service = build("sheets", "v4", credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = (
            sheet.values()
            .get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME)
            .execute()
        )
        values = result.get("values", [])

        if not values:
            print("No data found.")
            return
        else:
            values = values[1:]
            result = {}
            for item in values:
                result[item[0]] = item[1]
            return result
    except HttpError as err:
        print(err)

    
from selenium import webdriver
import time
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys 
def connect(data):
    s = Service()
    setting = Options() 
    setting.add_argument('--incognito')
    setting.add_experimental_option('excludeSwitches', ["enable-automation"])
    setting.add_experimental_option("detach", True)
    #setting.add_argument('--headless') # Uncomment to run in headless mode
    driver = webdriver.Chrome(service = s, options = setting)
    driver.get("https://www.linkedin.com/login")
    
    username = driver.find_element(By.ID, "username") 
    username.send_keys(ID)
    # Getting the password element                                  
    password = driver.find_element(By.ID, "password")
    # Sending the keys for password    
    password.send_keys(PASSWORD)      
    # Getting the tag for submit button                     
    driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button').click() 
    
    def click_button(button_xpath):
            try:
                button = wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath)))
                driver.execute_script("arguments[0].scrollIntoView(true);", button)
                button.click()
                return True
            except (TimeoutException, ElementClickInterceptedException):
                return False
                
    notFind = 0
    for name, url in data.items():
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        # Try to click the 'Connect' button, if it fails try the 'Accept' button
        if not click_button("//button[.//span[text()='Connect']]"):
            if not click_button("//button[.//span[text()='Accept']]"):
                notFind += 1 
    print(f"Total number of people found: {len(data)}, connect or accept to: {len(data) - notFind}")

if __name__ == "__main__":
    data = main()
    connect(data)
    