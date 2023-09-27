import pandas as pd

def get_results(name, dataframe, category = None):
    """
    Lorem ipsum
    """
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
