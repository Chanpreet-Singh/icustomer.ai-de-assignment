import os
import shutil
import traceback


def create_folder(folder_path, overwrite=False):
    try:
        if overwrite and check_folder_exists(folder_path):
            remove_folder_tree(folder_path)
        if not check_folder_exists(folder_path):
            os.mkdir(folder_path)
    except Exception as e:
        print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))

def check_folder_exists(folder_path):
    return os.path.isdir(folder_path)

def remove_folder_tree(folder_path):
    try:
        shutil.rmtree(folder_path)
    except Exception as e:
        print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))