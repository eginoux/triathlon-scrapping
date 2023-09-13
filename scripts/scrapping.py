# Imports
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

# Driver installation
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Define URL
url = "https://www.acn-timing.com/?lng=FR#/events/2141423449174261/ctx/20230725_alpehuez/generic/198021_2/home/TRI2"

# Load web page
driver.get(url)

# Set maximum time of loading
driver.implicitly_wait(10)

# Set lists of elements
names = []

# Find all names
name_elements = driver.find_elements(By.CLASS_NAME, "text-bold")
for name in name_elements:
    information = name.get_attribute("span").text
    # information = name.find_element(By.TAG_NAME, "span").text
    names.append(information)

# Close driver
driver.quit()

# Save data
results = pd.DataFrame(list(zip(names)), columns=['Name'])
results.to_csv("data/test_names.csv",index=False)
