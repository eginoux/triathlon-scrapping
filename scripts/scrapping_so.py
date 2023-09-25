import logging,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


wd = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
t0 = time.time()
url = "https://www.acn-timing.com/?lng=FR#/events/2141423449174261/ctx/20230725_alpehuez/generic/198021_2/home/TRI2"
wd.get(url)
WebDriverWait(wd, 20).until(EC.presence_of_element_located((By.XPATH, "//tbody[@class='table-data']")))
table = wd.find_element(By.XPATH, "//tbody[@class='table-data']")
rows = table.find_elements(By.XPATH, "//tr[@class='last-record-line']")
for i,row in enumerate(rows):
    out = []
    cols = row.find_elements(By.TAG_NAME, "td")
    for c in cols:
        out.append(c.text)
    print(out)
