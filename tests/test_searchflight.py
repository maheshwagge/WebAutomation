import pytest
from pageobjects.yatra_launch_page import LaunchPage


@pytest.mark.usefixtures("setup")
class TestSearchFlightAndVerifyFilter:

    def test_search_flights(self):
        lp = LaunchPage(self.driver,10)

        lp.depart_from("New Delhi")

        lp.going_to("New York")

        lp.select_date("24/12/2022")

        lp.click_search_flight()

        lp.page_scroll()

        # sf = SearchFlightsResults(self.driver, self.wait)
        # sf.filter_flights()
























