from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import os
from scripts.params import *


def scrape_mens_results():
    """
    Scrapping mens results for website and returns a data frame with data ordered like website
    """
    # Driver installation
    web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Load web page
    web_driver.get(URL)

    # Set variables
    data = []
    print("Scraping mens data ⏳")

    # Get elements
    data = []
    for i in range(PAGES_NUMBER):
        # Wait until presence of element
        WebDriverWait(web_driver, 20).until(EC.presence_of_element_located((By.XPATH, X_PATH_TABLE)))
        # Set table and rows to go through
        table = web_driver.find_element(By.XPATH, X_PATH_TABLE)
        rows = table.find_elements(By.XPATH, X_PATH_ROW_MENS)
        # Get Data
        for i, row in enumerate(rows):
            out = []
            columns = row.find_elements(By.TAG_NAME, "td")
            for column in columns:
                out.append(column.text)
            data.append(out)
        # Go to the next page
        WebDriverWait(web_driver, 10).until(EC.presence_of_element_located((By.XPATH, X_PATH_NEXT_BUTTON)))
        next_page_button = web_driver.find_element(By.XPATH, X_PATH_NEXT_BUTTON)
        next_page_button.click()

    # Close driver
    web_driver.quit()

    # Create data frame
    mens_df = pd.DataFrame(data, columns = STARTING_COLUMNS)
    mens_df.drop(columns=DROP_COLUMNS, inplace=True)
    print("Mens data scraped ✅")

    # Save file
    if not os.path.exists(DATA_DIR_PATH):
        os.makedirs(DATA_DIR_PATH)
    mens_df.to_csv(CSV_MENS_PATH, index=False)
    print("Mens data saved ✅")

    return mens_df


def scrape_women_results():
    """
    Scrapping women results for website and returns a data frame with data ordered like website
    """
    # Driver installation
    web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # Load web page
    web_driver.get(URL)

    # Get elements
    data = []
    print("Scraping women data ⏳")
    for i in range(PAGES_NUMBER):
        # Wait until presence of element
        WebDriverWait(web_driver, 20).until(EC.presence_of_element_located((By.XPATH, X_PATH_TABLE)))
        # Set table and rows to go through
        table = web_driver.find_element(By.XPATH, X_PATH_TABLE)
        rows = table.find_elements(By.XPATH, X_PATH_ROW_WOMEN)
        # Get Data
        for i, row in enumerate(rows):
            out = []
            columns = row.find_elements(By.TAG_NAME, "td")
            for column in columns:
                out.append(column.text)
            data.append(out)
        # Go to the next page
        WebDriverWait(web_driver, 10).until(EC.presence_of_element_located((By.XPATH, X_PATH_NEXT_BUTTON)))
        next_page_button = web_driver.find_element(By.XPATH, X_PATH_NEXT_BUTTON)
        next_page_button.click()

    # Close driver
    web_driver.quit()

    # Create data frame
    women_df = pd.DataFrame(data, columns=STARTING_COLUMNS)
    women_df.drop(columns=DROP_COLUMNS, inplace=True)
    print("Women data scraped ✅")

    # Save file
    if not os.path.exists(DATA_DIR_PATH):
        os.makedirs(DATA_DIR_PATH)
    women_df.to_csv(CSV_WOMEN_PATH, index=False)
    print("Women data saved ✅")

    return women_df
