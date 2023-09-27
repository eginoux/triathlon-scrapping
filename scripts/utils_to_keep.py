# Imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# url = "https://www.acn-timing.com/?lng=FR#/events/2141423449174261/ctx/20230725_alpehuez/generic/198021_2/home/TRI2"
# x_path_next_button = "//button[@aria-label='Next page']"


def go_next_page(url, x_path_next_button):
    """
    Go through every pages of a website by specifying the URL and the x_path
    of button to click on
    """
    # Driver installation
    web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Load web page
    web_driver.get(url)

    # Go through all pages
    while True:
        WebDriverWait(web_driver, 10).until(EC.presence_of_element_located((By.XPATH, x_path_next_button)))
        next_page_button = web_driver.find_element(By.XPATH, x_path_next_button)
        action = webdriver.ActionChains(web_driver)
        action.pause(3)
        action.perform()
        next_page_button.click()
