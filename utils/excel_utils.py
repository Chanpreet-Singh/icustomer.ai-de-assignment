import traceback
import pandas as pd

from utils import file_utils

def read_csv_file(file_path):
    df = pd.DataFrame()
    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
    return df

def dump_csv_file(data, file_path, need_header=True, need_index=False):
    status = False
    try:
        data.to_csv(file_path, header=need_header, index=need_index)
        if file_utils.get_file_size(file_path) > 0:
            status = True
    except Exception as e:
        print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
    return status

def convert_list_into_dataframe(data_list):
    return pd.DataFrame(data_list)

def reorder_columns_in_df(df, column_list):
    return df[column_list]
