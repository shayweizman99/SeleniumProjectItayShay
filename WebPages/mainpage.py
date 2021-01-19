from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class MainPage():
    def __init__(self, driver):
        self.driver = driver

    def loader_wait(self):  # waits 15 until the loader to end
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element((By.XPATH, '//div[@class="loader"]')))

    def speakers(self):  # finds speakers page element
        return self.driver.find_element_by_id("speakersImg")

    def click_speakers(self):  # clicks speakers page element
        self.loader_wait()
        self.speakers().click()

    def tablets(self):
        return self.driver.find_element_by_id("tabletsImg")

    def click_tablets(self):
        self.loader_wait()
        self.tablets().click()

    def home_button(self):
        return self.driver.find_element_by_xpath("//a[@class='ng-scope']")

    def home_navigate(self):
        self.loader_wait()
        self.home_button().click()