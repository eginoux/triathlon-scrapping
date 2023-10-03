import pandas as pd
import os
from scripts.params import *
from scripts.scraping import scrape_mens_results, scrape_women_results
from scripts.data import get_clean_data


# Check if raw_data directory exists
if not os.path.exists(DATA_DIR_PATH):
    os.makedirs(DATA_DIR_PATH)
    print("Data directory created ✅")

# Check if mens file is in data directory
if os.path.exists(CSV_MENS_PATH):
    mens_dataframe = pd.read_csv(CSV_MENS_PATH)
    print("Getting mens data from local directory ✅")
else:
    mens_dataframe = scrape_mens_results()

# Check if women file is in data directory
if os.path.exists(CSV_WOMEN_PATH):
    women_dataframe = pd.read_csv(CSV_WOMEN_PATH)
    print("Getting women data from local directory ✅")
else:
    women_dataframe = scrape_women_results()

dataframe = get_clean_data(mens_dataframe, women_dataframe)

def get_results(dataframe):
    """
    Takes a data frame and then:
    - Asks for a participant name
    - Asks for a category or not and which one
    Print results of participant and average, min and max results depending category or
    whole competitors
    """
    name_list = list(dataframe["Name"].unique())
    category_list = list(dataframe["Category"].unique())
    name = input("Enter a valid participant: [LASTNAME Name] ")
    while not name in name_list:
        name = input("Participant not found. Enter a valid participant: [LASTNAME Name] ")

    answers = ["Y", "y", "N", "n"]
    question = input("Do you want to specify a category? [Y/n] ")
    while not question in answers:
        question = input("Eneter a valid option for category: [Y/n]")
    if question == "Y" or question == "y":
        category = input("Enter a valid category: ")
        while not category in category_list:
            print(category_list)
            category = input("Category not found. Please enter a valid category: ")
    else:
        category = None

    if category != None:
        my_row = dataframe[dataframe["Name"] == name]
        dataframe = dataframe[dataframe["Category"] == category]
        date_time_columns = list(dataframe.select_dtypes(include = ["datetime64[ns]"]).columns)
        print(f"{30 * '#'} Please find {name} results below {30 * '#'}")
        for column in date_time_columns:
            my_time = my_row[column].dt.time.astype(str).values
            my_time = my_time[0]
            mean_time = dataframe[column].mean()
            mean_time = mean_time.strftime("%H:%M:%S")
            min_time = dataframe[column].min()
            min_time = min_time.strftime("%H:%M:%S")
            max_time = dataframe[column].max()
            max_time = max_time.strftime("%H:%M:%S")
            print(f"{column} was {my_time} (average was {mean_time}, min was {min_time} and max was {max_time} for {category} category)")
    else:
        my_row = dataframe[dataframe["Name"] == name]
        date_time_columns = list(dataframe.select_dtypes(include = ["datetime64[ns]"]).columns)
        print(f"{22 * '#'} Please find {name} results below {22 * '#'}")
        for column in date_time_columns:
            my_time = my_row[column].dt.time.astype(str).values
            my_time = my_time[0]
            mean_time = dataframe[column].mean()
            mean_time = mean_time.strftime("%H:%M:%S")
            min_time = dataframe[column].min()
            min_time = min_time.strftime("%H:%M:%S")
            max_time = dataframe[column].max()
            max_time = max_time.strftime("%H:%M:%S")
            print(f"{column} was {my_time} (average was {mean_time}, min was {min_time} and max was {max_time})")




if __name__ == "__main__":
    try:
        get_results(dataframe)
    except:
        import traceback
        traceback.print_exc()
