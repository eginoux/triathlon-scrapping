# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Driver installation
web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Define URL
url = "https://www.acn-timing.com/?lng=FR#/events/2141423449174261/ctx/20230725_alpehuez/generic/198021_2/home/TRI2"

# Load web page
web_driver.get(url)

# Get select button
x_path_next_button = "//button[@class='v-pagination__navigation']"
WebDriverWait(web_driver, 20).until(EC.presence_of_element_located((By.XPATH, x_path_next_button)))
next_page_button = web_driver.find_element(By.XPATH, x_path_next_button)

# Click on button
next_page_button.click()
