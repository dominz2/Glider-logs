from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

chromeOptions = webdriver.ChromeOptions()
prefs = {"download.default_directory": "D:\STUDIA\Machine_learning\Web_scraping\exercises\Selenium\Oles"}
chromeOptions.add_experimental_option("prefs", prefs)
PATH = "C:\Program Files (x86)\chromedriver.exe"
'''Creating object "service" which manages the starting and stopping of the Chrome Driver'''
service = Service(PATH)
driver = webdriver.Chrome(service=service, chrome_options=chromeOptions)

driver.get("http://www.crosscountry.aero/flights?rgl=LY&rgi=PL&tpa=1&p=20&i=1")

'''Filling the logging form'''
# username = os.environ.get('username')
password = os.environ.get('password')
username_crosscountry = driver.find_element(By.NAME, "j_username")
password_crosscountry = driver.find_element(By.NAME, "j_password")
username_crosscountry.send_keys("dominz2")
password_crosscountry.send_keys(password)

driver.find_element(By.ID, "loginButton").click()

i = 0
j = 0

while True:

    i += 1
    j += 1
    if j % 20 == 0:
        '''Changing page every 20 records'''
        i = 1

        next_page = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, "(//div[@id='pagingNav']//a)[last()]"))
        )
        next_page.click()
    '''Try is used to handle exceptions
    There are some records where there are no logs.
    '''
    try:
        view = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, f"(//td[@class='tdc']//a)[{i}]"))
        )
        view.click()

        element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, "IGC Log"))
        )
        element.click()

        download = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.LINK_TEXT, "Download Igc file"))
        )
        download.click()
    finally:
        driver.back()
        continue
