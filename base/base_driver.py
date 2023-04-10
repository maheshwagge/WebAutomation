import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class BaseDriver:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    # handle dynamic scroll

    def page_scroll(self):
        pagelength = self.driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight); var pagelength=document.body.scrollHeight;return pageLenght;")
        match = False
        while match == False:
            lastCount = pagelength
            time.sleep(4)
            pagelength = self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight); var pagelength=document.body.scrollHeight;return pageLenght;")
            if lastCount == pagelength:
                match = True
        time.sleep(4)

    def wait_for_presence_of_all_elements(self, locator_type, locator):
        list_of_elements = self.wait.until(EC.presence_of_all_elements_located((locator_type, locator)))
        return list_of_elements

    def wait_until_element_clickable(self, locator_type, locator):
        element = self.wait.until(EC.element_to_be_clickable((locator_type, locator)))
        return element
