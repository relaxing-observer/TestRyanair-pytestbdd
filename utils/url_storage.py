class PageUrl:
    """
    Links of pages for required tests.
    """
    __links_storage = {
        'main': 'https://www.ryanair.com/',
    }

    @staticmethod
    def get_page_link(name):
        return PageUrl.__links_storage[name]

class IdentityPhraseUrl:
    SearchFlightsPage = "trip/flights/select"
    SearchHotelsPage = "rooms.ryanair.com"
