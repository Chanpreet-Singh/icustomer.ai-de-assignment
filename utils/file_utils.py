import os

def check_file(file_path):
    return os.path.exists(file_path)

def get_file_size(file_path):
    file_size = 0
    if check_file(file_path):
        file_size = os.path.getsize(file_path)
    return file_size