from plugins.philips.SearchStrategy import SearchStrategy


class LastSearch(SearchStrategy):
    """
    This search method searches for the last added light to the bridge.
    """
    @classmethod
    def search(cls, response, types):
        found = False
        for key, value in response.items():
            if value['state'] and value['type'] in types:
                found = True
                lamp_id = int(key)

        if not found:
            raise Exception("No lights were found")

        return lamp_id
