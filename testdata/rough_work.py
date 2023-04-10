import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
wait = WebDriverWait(driver, 10)
driver.get("https://www.yatra.com/")
driver.maximize_window()
depart_from = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_origin_city']")))
depart_from.click()
depart_from.send_keys("New Delhi")
depart_from.send_keys(Keys.ENTER)

going_to = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='BE_flight_arrival_city']")))
going_to.click()
time.sleep(10)
going_to.send_keys("New York")
search_results = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='viewport']//div[1]//li")))
#search_results = driver.find_elements(By.XPATH,"//div[@class='viewport']//div[1]//li")
print(len(search_results))
for results in search_results:
    print(results.text)
    if "New York (JFK)" in results.text:
        results.click()
        time.sleep(4)
        break

origin = driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
origin.click()
time.sleep(4)

all_dates = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")))\
    .find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td[@class!='inActiveTD']")
for date in all_dates:
    if date.get_attribute("date-date") == "24/12/2022":
        date.click()
        time.sleep(4)
        break

driver.find_element(By.XPATH, "//input[@value='Search Flights']").click()
time.sleep(4)
# handle dynamic scroll
#page_length = driver.execute_script("window.scrollTo(0, document.body.scrollHeight); var pageLength=document.body.scrollHeight;return pageLenght;")

#
# # select filter one stop
# driver.find_element(By.XPATH, "//p[@class='font-lightgrey bold'][normalize-space()='1']").click()
# time.sleep(4)
# all_stop = wait.until(EC.presence_of_all_elements_located((By.XPATH,
#                                                            "//span[contains(text(),'Non Stop') or contains(text(),'1 Stop') or contains(text(),'2 Stop')]")))
# print(len(all_stop))
#
