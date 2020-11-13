import pandas as pd

def format_df(df, format):
    if format == "df":
        return df
    elif format == "list":
        return df_to_list(df)
    else:
        raise Exception("Format {fmt} not supported, should be either df or list,".format(fmt=format))

def df_to_list(df):
    return list(df.to_dict(orient="index").values())

def combine_rows(row):
    values = row.values
    return values[~pd.isnull(values)].tolist()