import pandas as pd
import os
import datetime

cache_dir=".cache"

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

def get_cached(key, retrieve):
    cache_file = os.path.join(cache_dir, get_cache_filename(key))
    if os.path.isfile(cache_file):
        print("Reading {key} data from cache".format(key=key))
        return pd.read_csv(cache_file)
    print("Fetching {key} dataframe from web.".format(key=key))
    df = retrieve()
    cache_df(df, key)
    print("Cached results for dataframe {key}".format(key=key))
    return df

def get_cache_path():
    if os.path.isdir(cache_dir):
        return cache_dir
    os.mkdir(cache_dir)
    return cache_dir

def get_cache_filename(key):
    return "{key}-{date}".format(key=key, date=datetime.datetime.now().strftime("%d-%b-%Y"))

def cache_df(df, key):
    cache_path = get_cache_path()
    file_name = os.path.join(cache_dir, get_cache_filename(key))
    df.to_csv(file_name, index=False) 
    return file_name
