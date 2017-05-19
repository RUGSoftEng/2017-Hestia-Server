from os import path


def get_config_path():
    current_dir_path = path.dirname(__file__)
    base_path = path.dirname(current_dir_path)
    return base_path + "/Configurations/"

def get_plugins_path(collection):
    config_path = get_config_path()
    return config_path + collection + "/"

def get_info_plugin(collection, plugin_name):
    plugins = get_plugins_path(collection)
    return plugins + plugin_name
