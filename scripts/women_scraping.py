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

# Set variables
data = []
x_path_table = "//tbody[@class='table-data']"
x_path_row = "//tr[@class='last-record-line']"
x_path_next_button = "//button[@aria-label='Next page']"
pages_number = 16

# Get elements
for i in range(pages_number):
    # Wait until presence of element
    WebDriverWait(web_driver, 20).until(EC.presence_of_element_located((By.XPATH, x_path_table)))
    # Set table and rows to go through
    table = web_driver.find_element(By.XPATH, x_path_table)
    rows = table.find_elements(By.XPATH, x_path_row)
    # Get Data
    for i, row in enumerate(rows):
        out = []
        columns = row.find_elements(By.TAG_NAME, "td")
        for column in columns:
            out.append(column.text)
        data.append(out)
    # Go to the next page
    WebDriverWait(web_driver, 10).until(EC.presence_of_element_located((By.XPATH, x_path_next_button)))
    next_page_button = web_driver.find_element(By.XPATH, x_path_next_button)
    next_page_button.click()

# Close driver
web_driver.quit()

# Create data frame
results = pd.DataFrame(data, columns=["Position", "Number", "Name", "Country", "Pos_in_swim", "Swim_time", "T1",
                                      "Pos_in_bike", "Bike_time", "CUM", "T2",
                                      "Pos_in_run", "Run_time", "Race_control", "Time", "Rank", "Category", "Pic", "Star"])
results.drop(columns=["Country", "CUM", "Pic", "Star"], inplace=True)

# Save data frame into csv file
results.to_csv("data/medium_men_results.csv", index=False)

# Check if file exists
my_file = Path("data/medium_men_results.csv")

if my_file.exists() and len(results) > 0:
    print("Finished ✅")
else:
    print("Something went wrong 😵‍💫")
