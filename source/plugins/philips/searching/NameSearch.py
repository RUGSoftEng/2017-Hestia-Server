from plugins.philips.SearchStrategy import SearchStrategy


class NameSearch(SearchStrategy):
    """
    Searches based on a given name.
    """
    @classmethod
    def search(cls, response, name):
        found = False
        for key, value in response.items():
            if value['name'] == name:
                found = True
                lamp_id = int(key)
                break

        if not found:
            raise Exception("No lights were found")

        return lamp_id
