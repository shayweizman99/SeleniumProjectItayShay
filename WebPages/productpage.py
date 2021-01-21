from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver


class Products():
    def __init__(self, driver):
        self.driver = driver
        self.speakers_id = {1: "20", 2: "25", 3: "24", 4: "21", 5: "22", 6: "19", 7: "23"}
        self.colors = {'black': "//span[@title = 'BLACK']", 'grey': "//span[@title = 'GRAY']",
                       'red': "//span[@title = 'RED' and @id = 'bunny']"
            , 'turquoise': "//span[@title = 'TURQUOISE' and @id = 'bunny']",
                       'blue': "//span[@title = 'BLUE' and @id = 'bunny']"
            , 'yellow': "//span[@title = 'YELLOW' and @id = 'bunny']",
                       'purple': "//span[@title = 'PURPLE' and @id = 'bunny']"
            , 'white': "//span[@title = 'WHITE']"}
        self.tablets_id = {1: "16", 2: "17", 3: "18"}
        self.mice_id = {1: "29", 2: "28", 3: "27", 4: "30", 5: "33", 6: "32", 7:"26" , 8: "31", 9: "34"}


    def loader_wait(self):  # waits 15 until the loader to end
        WebDriverWait(self.driver, 15).until(EC.invisibility_of_element((By.XPATH, '//div[@class="loader"]')))

    def choose_speaker(self, num):
        self.loader_wait()
        self.driver.find_element_by_id(self.speakers_id[num]).click()

    def choose_tablet(self, num):
        self.loader_wait()
        self.driver.find_element_by_id(self.tablets_id[num]).click()

    def choose_mice(self,num):
        self.loader_wait()
        self.driver.find_element_by_id(self.mice_id[num]).click()

    def plus(self, num):
        self.loader_wait()
        for times in range(num - 1):
            self.driver.find_element_by_css_selector("div[class='plus']").click()

    def add_to_cart_btn(self):  # returns add to card button element
        return self.driver.find_element_by_name("save_to_cart")

    def add_to_cart(self):
        self.loader_wait()
        self.add_to_cart_btn().click()

    def change_color(self, color):
        self.loader_wait()
        self.driver.find_element_by_xpath(self.colors[color]).click()

    def click_on_cart_icon(self):
        self.loader_wait()
        self.driver.find_element_by_id("shoppingCartLink").click()



    def pop_up_info(self):
        self.loader_wait()
        cart = self.driver.find_element_by_id("shoppingCartLink")  # move with the mouse the shopping cart link
        ActionChains(self.driver).move_to_element(cart).perform()

        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(
            (By.CSS_SELECTOR, "table[ng-show='cart.productsInCart.length > 0']>tbody")))

        table = self.driver.find_element_by_css_selector(
            "table[ng-show='cart.productsInCart.length > 0']>tbody")  # finds the table
        rows = table.find_elements_by_tag_name('tr')  # find rows
        products = []
        for row in rows:
            column = row.find_elements_by_tag_name('td')
            color = column[1].find_element_by_css_selector("span[class='ng-binding']").text
            price = column[2].find_element_by_tag_name('p').text
            price = price[1:]
            price = price.replace(',', '')
            price = float(price)
            amount = column[1].find_element_by_tag_name('label').text.split()[1]
            amount = int(amount)
            name = column[1].find_element_by_tag_name('h3').text
            product = [name, amount, color, price]
            products.append(product)
        return products

    def locate_delete_btn(self):
        return self.driver.find_element_by_css_selector("div[icon-x][class='removeProduct iconCss iconX']")

    def remove_product(self):
        self.locate_delete_btn().click()