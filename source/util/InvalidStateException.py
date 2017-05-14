class InvalidStateException(Exception):
    def __init__(self, new_value, expected_type):
        self.new_value = new_value
        self.expected_type = expected_type

    def __str__(self):
        return "State has value" \
               + " [" + str(self.new_value) + "] " \
               + "of type " + str(type(self.new_value)) \
               + " expected a state with type " \
               + str(self.expected_type) + ". "
