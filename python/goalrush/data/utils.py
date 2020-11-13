import pandas as pd

def format_df(df, format):
    if format == "df":
        return df
    elif format == "list":
        return df_to_list(df)

def df_to_list(df):
    pass

def combine_rows(row):
    values = row.values
    return values[~pd.isnull(values)].tolist()