class Links:
    """
    Links of pages for required tests.
    """
    __links_storage={
        'main':'https://www.ryanair.com/',
    }
    @staticmethod
    def get_page_link(name):
        return Links.__links_storage[name]
