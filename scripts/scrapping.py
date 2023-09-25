# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

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
for i, row in enumerate(rows):
    out = []
    columns = row.find_elements(By.TAG_NAME, "td")
    for column in columns:
        out.append(column.text)

# Close driver
web_driver.quit()

# Save data
# results = pd.DataFrame(list(zip(names)), columns=['Name'])
# results.to_csv("data/test_names.csv", index=False)
