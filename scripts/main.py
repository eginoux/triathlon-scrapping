import pandas as pd
from scripts.scraping import scrape_mens_results, scrape_women_results
from scripts.data import get_clean_data


def get_results():
    """
    Lorem ipsum
    """
    # mens_df = scrape_mens_results()
    # women_df = scrape_women_results()
    # dataframe = get_clean_data(mens_df, women_df)
    name = input("Enter a valid participant name: ")
    question = input("Do you want to specify a category? [Y/n] ")
    if question == "Y":
        category = input("Enter a valid category: ")
    else:
        category == None

    if category == None:
        my_row = dataframe[dataframe["Name"] == name]
        date_time_columns = list(dataframe.select_dtypes(include = ["datetime64[ns]"]).columns)
        for column in date_time_columns:
            my_time = my_row[column].dt.time.astype(str).values
            my_time = my_time[0]
            mean_time = dataframe[column].mean()
            mean_time = mean_time.strftime("%H:%M:%S")
            print(f"{name} {column} was {my_time} and the average {column} for all categories was {mean_time}")
    else:
        my_row = dataframe[dataframe["Name"] == name]
        dataframe = dataframe[dataframe["Category"] == category]
        date_time_columns = list(dataframe.select_dtypes(include = ["datetime64[ns]"]).columns)
        for column in date_time_columns:
            my_time = my_row[column].dt.time.astype(str).values
            my_time = my_time[0]
            mean_time = dataframe[column].mean()
            mean_time = mean_time.strftime("%H:%M:%S")
            print(f"{name} {column} was {my_time} and the average {column} for {category} was {mean_time}")



if __name__ == "__main__":
    try:
        get_results()
    except:
        print("Someting went wrong")
