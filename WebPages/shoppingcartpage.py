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

    def shopping_cart_empty_text(self):
        self.driver.find_element_by_xpath("//section/article/div[1]/div/label").text

# -------------------------------------------------------------------------


# def click_edit_product2(self):
#     return self.driver.find_elements_by_css_selector(
#         "a[class='edit ng-scope']")
#
#
# # פונקציה שפועלת אחרי הפונקציה הקודמת של העריכה של מוצר מהעגלה ולוחצת על הפלוס וככה מוסיפה עוד 1 לכמות מוצר בעגלה
# def plus_1(self):  # כמעט בטוח שהפונקציה הזו מיותרת והפלאס הקודמת תעבוד פה אבל ליתר בטחון מקסימום נמחק
#     return self.driver.find_element_by_css_selector(
#         "div[class='plus']")
#
#
# def locate_QuantityOfProductInCart_text(self):
#     self.loader_wait()
#     the_first_quantity = self.driver.find_element_by_xpath(
#         '//label[@class="ng-binding"]/a[@href="#/product/16?color=55CDD5&quantity=2&pageState=edit"]').text
#     the_second_quantity = self.driver.find_element_by_xpath(
#         '//label[@class="ng-binding"]/td[@class="smollCell quantityMobile"]').text