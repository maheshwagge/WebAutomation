import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from base.base_driver import BaseDriver


class LaunchPage(BaseDriver):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)
        self.driver = driver


    def depart_from(self, depart_location):
        #depart_from = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
        depart_from = self.wait_until_element_clickable(By.XPATH, "//input[@id='BE_flight_origin_city']")
        depart_from.click()
        depart_from.send_keys(depart_location)
        depart_from.send_keys(Keys.ENTER)

    def going_to(self, going_to_location):
        #going_to = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
        going_to = self.wait_until_element_clickable(By.XPATH, "//input[@id='BE_flight_arrival_city']")
        going_to.click()
        time.sleep(10)
        going_to.send_keys(going_to_location)
        #search_results = self.wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]//li")))
        search_results = self.wait_for_presence_of_all_elements(By.XPATH, "//div[@class='viewport']//div[1]//li")
        print(len(search_results))
        for results in search_results:
            print(results.text)
            if "New York (JFK)" == results.text:
                results.click()
                time.sleep(4)
                break

    def select_date(self, departure_date):

        origin = self.wait_until_element_clickable(By.XPATH, "//input[@id='BE_flight_origin_date']")
        origin.click()
        time.sleep(4)

        # all_dates = self.wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")))\
        #     .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        all_dates = self.wait_until_element_clickable(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']") \
            .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
        for date in all_dates:
            if date.get_attribute("date-date") == departure_date:
                date.click()
                break

    def click_search_flight(self):
        self.driver.find_element(By.XPATH, "(//input[@value='Search Flights").click()
        time.sleep(4)
