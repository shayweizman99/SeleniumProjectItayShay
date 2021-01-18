from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

class table():
    def table_info(self):
        cart = self.driver_find_element_by_id("shoppingCartLink") #move with the mouse the shopping cart link
        ActionChains(self.driver).move_to_element(cart).perform()

        wait = WebDriverWait(self.driver , 10)
        wait.until(EC.visibility_of_element_located(By.CSS_SELECTOR,"table[ng-show='cart.productsInCart.length > 0']>tbody"))

        table = self.driver.find_element_by_css_selector("table[ng-show='cart.productsInCart.length > 0']>tbody") #finds the table
        rows = table.find_elements_by_tag_name('tr') # find rows
        products = []
        for row in rows:
            cells = row.find_elements_by_tag_name('td')
            color = cells[1].find_element_by_css_selector("span[class='ng-binding']").text
            price = cells[2].find_element_by_tag_name('p').text
            amount =cells[1].find_element_by_tag_name('label')[0].text
            name = cells[1].find_element_by_tag_name('h3').text
            product = [name, amount, color, price]
            products.append(product)
        return products



