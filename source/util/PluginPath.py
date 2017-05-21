from os import path


def get_plugin_path():
    current_dir_path = path.dirname(__file__)
    base_path = path.dirname(current_dir_path)
    return base_path + "/plugins/"
