import pandas as pd

def load_data(filepath):
    return pd.read_csv(filepath)

def preprocess(df):

    categorical_cols = [
        "age_group",
        "app_category",
        "emotion",
        "time_of_day"
    ]

    df = pd.get_dummies(
        df,
        columns=categorical_cols,
        drop_first=True
    )

    return df
