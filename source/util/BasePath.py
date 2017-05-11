from os import path

def get_base_path():
    dir_path = path.dirname(__file__)
    base_path = dir_path + "/../"
    return base_path
