import os

# Variables
URL = "https://www.acn-timing.com/?lng=FR#/events/2141423449174261/ctx/20230725_alpehuez/generic/198021_2/home/TRI2"
X_PATH_TABLE = "//tbody[@class='table-data']"
X_PATH_ROW_MENS = "//tr[@class='last-record-line']"
X_PATH_ROW_WOMEN = "//tr[@class='cr-pink last-record-line']"
X_PATH_NEXT_BUTTON = "//button[@aria-label='Next page']"
PAGES_NUMBER = 16
STARTING_COLUMNS = ["Position", "Number", "Name", "Country", "Pos_in_swim",
                    "Swim_time", "T1","Pos_in_bike", "Bike_time", "CUM", "T2",
                    "Pos_in_run", "Run_time", "Race_control", "Time", "Rank",
                    "Category", "Pic", "Star"]
DROP_COLUMNS = ["Country", "CUM", "Pic", "Star"]
DATA_DIR = "raw_data"
USER_PATH = os.getcwd()

# Constants
CSV_MENS_PATH = os.path.join(USER_PATH, DATA_DIR, "medium_mens_results.csv")
CSV_WOMEN_PATH = os.path.join(USER_PATH, DATA_DIR, "medium_women_results.csv")
