# Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

# Driver installation
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(options=options)

# Define URL
url = "https://www.acn-timing.com/?lng=FR#/events/2141423449174261/ctx/20230725_alpehuez/generic/198021_2/home/TRI2"

# Load web page
driver.get(url)

# Wait until presence of element
WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, "//tbody[@class='table-date']")))

# Set table and rows to go through
table = driver.find_element(By.XPATH, "//tbody[@class='table-date']")
rows = driver.find_element(By.XPATH, "//tr[@class='last-record-line']")

# Get elements from each row
for i, row in enumerate(rows):
    out = []
    columns = driver.find_element(By.TAG_NAME, "td")
    for column in columns:
        out.append(column)
    print(out)

# Close driver
driver.quit()

# Save data
# results = pd.DataFrame(list(zip(names)), columns=['Name'])
# results.to_csv("data/test_names.csv", index=False)
