def string_to_bool(string):
    if string == "True" or string == "true":
        return True
    elif string == "False" or string == "false":
        return False
    else:
        raise Exception("Invalid conversion to bool form: " + string)
