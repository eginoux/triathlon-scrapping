# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from pathlib import Path

# Driver installation
web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Define URL
url = "https://www.acn-timing.com/?lng=FR#/events/2141423449174261/ctx/20230725_alpehuez/generic/198021_2/home/TRI2"

# Load web page
web_driver.get(url)

# Wait until presence of element
WebDriverWait(web_driver, 20).until(EC.presence_of_element_located((By.XPATH, "//tbody[@class='table-data']")))

# Set table and rows to go through
table = web_driver.find_element(By.XPATH, "//tbody[@class='table-data']")
rows = table.find_elements(By.XPATH, "//tr[@class='last-record-line']")

# Get elements
data = []
for i, row in enumerate(rows):
    out = []
    columns = row.find_elements(By.TAG_NAME, "td")
    for column in columns:
        out.append(column.text)
    data.append(out)

# Close driver
web_driver.quit()

# Save data
results = pd.DataFrame(data, columns=["Position", "Number", "Name", "Country", "Pos_in_swim", "Swim_time", "T1",
                                      "Pos_in_bike", "Bike_time", "CUM", "T2",
                                      "Pos_in_run", "Run_time", "Race_control", "Time", "Rank", "Category", "Pic", "Star"])
results.drop(columns=["Country", "CUM", "Pic", "Star"], inplace=True)
results.to_csv("data/test_page_one.csv", index=False)

# Check if file exists
my_file = Path("data/test_page_one.csv")

if my_file.exists() and len(results) > 0:
    print("Finished ✅")
else:
    print("Something went wrong 😵‍💫")
