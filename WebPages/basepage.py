
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class BasePage(object):  # basic page to inheret from
    def __init__(self, driver):
        self.driver = driver

    def loader_wait (self):
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element((By.XPATH, '//div[@class="loader"]')))

