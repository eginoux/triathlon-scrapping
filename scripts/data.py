import pandas as pd


def get_clean_data(mens_df, women_df):
    """
    Takes mens and women data frames and return a cleaned data frame
    """
    # Drop duplicates
    mens_df.drop_duplicates(inplace=True)
    women_df.drop_duplicates(inplace=True)

    # Concatenate data frames
    df = pd.concat([mens_df, women_df])

    # Drop Did Not Finish (DNF) and non starting (STRT) rows
    dataframe = df.copy()
    dataframe = dataframe[~dataframe["Position"].isin(["DNF", "STRT"])]

    # Drop inaccurately recorded sessions
    dataframe.dropna(axis=0, inplace=True)

    # Convert numeric columns into integers
    dataframe = dataframe.astype({"Number": "int",
                                "Pos_in_swim": "int",
                                "Pos_in_bike": "int",
                                "Pos_in_run": "int"})
    dataframe["Position"] = dataframe["Position"].apply(lambda x: x.replace(".", ""))
    dataframe["Position"] = dataframe["Position"].astype(int)

    # Standardize timings for T2 & Run_time
    dataframe["T2"] = dataframe["T2"].apply(lambda x: "00:" + x if len(x) == 2 else x)
    dataframe["Run_time"] = dataframe["Run_time"].apply(lambda x: "00:" + x if len(x) <= 5 else x)

    # Convert timing columns into date_time
    dataframe["Swim_time"] = pd.to_datetime(dataframe["Swim_time"], format="%M:%S")
    dataframe["T1"] = pd.to_datetime(dataframe["T1"], format="%M:%S")
    dataframe["Bike_time"] = pd.to_datetime(dataframe["Bike_time"], format="%H:%M:%S")
    dataframe["T2"] = pd.to_datetime(dataframe["T2"], format="%M:%S")
    dataframe["Run_time"] = pd.to_datetime(dataframe["Run_time"], format="%H:%M:%S")
    dataframe["Time"] = pd.to_datetime(dataframe["Time"], format="%H:%M:%S")

    # Set the right date of race
    date_time_columns = list(dataframe.select_dtypes(include = ["datetime64[ns]"]).columns)
    for column in date_time_columns:
        dataframe[column] = dataframe[column].astype(str)
        dataframe[column] = dataframe[column].apply(lambda x: x.replace("1900-01-01", "2023-07-28"))
        dataframe[column] = pd.to_datetime(dataframe[column])

    # Reorder the data frame
    dataframe.sort_values(by = "Time", ascending=True, inplace=True)

    # Create a new position column
    dataframe["Pos_after_cleaning"] = range(1, len(dataframe) + 1)
    dataframe = dataframe[['Position', 'Pos_after_cleaning', 'Number', 'Name',
                        'Pos_in_swim','Swim_time','T1','Pos_in_bike', 'Bike_time',
                        'T2','Pos_in_run', 'Run_time','Race_control', 'Time',
                        'Rank', 'Category']]

    return dataframe
