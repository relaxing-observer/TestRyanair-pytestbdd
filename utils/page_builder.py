from pages.cars_tab_main_page import CarsTabMainPage
from pages.hotels_tab_main_page import HotelsTabMainPage
from pages.flight_tab_main_page import FlightTabMainPage
from pages.user_main_page import UserMainPage
from pages.search_cars_page import SearchCarsPage
from pages.search_hotels_page import SearchHotelsPage
from pages.search_flights_page import SearchFlightsPage
class PageConstructor:
    __classes_storage = {
        'main':UserMainPage,
        'cars':CarsTabMainPage,
        'hotels':HotelsTabMainPage,
        'flights':FlightTabMainPage,
        'search cars':SearchCarsPage,
        'search hotels':SearchHotelsPage,
        'search flights':SearchFlightsPage,
    }

    @staticmethod
    def get_class(name):
        return PageConstructor.__classes_storage[name]
