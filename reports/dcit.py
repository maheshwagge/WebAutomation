from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 10)
driver.get("https://www.amazon.in/")
driver.maximize_window()

# In the search box, enter ' data catalog' and search'
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").send_keys("data catalog")
driver.find_element(By.XPATH, "//input[@id='twotabsearchtextbox']").submit()
driver.implicitly_wait(5)
print("done")

first_book_title = "The Data Catalog: Sherlock Holmes Data Sleuthing for Analytics"

# check for title
title = driver.find_element(By.XPATH, "//span[normalize-space()='The Data Catalog: Sherlock Holmes Data Sleuthing for Analytics']").text.strip()
assert first_book_title == title
print(title)
driver.find_element(By.XPATH, "//span[normalize-space()='The Data Catalog: Sherlock Holmes Data Sleuthing for Analytics']").click()
time.sleep(10)