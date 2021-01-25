from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

class ShoppingCart():
    def __init__(self,driver):
        self.driver = driver

    def loader_wait(self):  # waits 15 until the loader to end
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element((By.XPATH, '//div[@class="loader"]')))

    def locate_shoppingcart_text(self):
        self.loader_wait()
        return self.driver.find_element_by_css_selector("h3[class='roboto-regular center sticky fixedImportant ng-binding']")

    def locate_total_price(self):
        self.loader_wait()
        presented_price = self.driver.find_element_by_xpath('//table/tfoot/tr[1]/td[2]/span[2]').text
        presented_price = presented_price[1:]
        presented_price = presented_price.replace(',', '')
        presented_price = float(presented_price)
        return presented_price

    def locate_checkout_button(self):
        return self.driver.find_element_by_id("checkOutButton")

    def click_checkout_button(self):
        self.locate_checkout_button().click()

    def locate_registration_button(self):
        return self.driver.find_element_by_id('registration_btnundefined')

    def click_register_button(self):
        self.locate_registration_button().click()

