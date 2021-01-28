from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver

class table():



    def orders_table_info(self):
        wait = WebDriverWait(self.driver , 10)
        wait.until(EC.visibility_of_element_located("//article/div[2]/div/table"))

        table = self.driver.find_element_by_xpath("//article/div[2]/div/table") #finds the table
        rows = table.find_elements_by_tag_name('tr') # find rows
        order_products = []
        for row in rows:
            cells = row.find_elements_by_tag_name('td')
            color = cells[4].find_element_by_xpath("//table/tbody/tr[2]/td[5]/div").text
            # totalprice = cells[6].find_element_by_xpath("//table/tbody/tr[2]/td[7]/label").text
            amount =cells[5].find_element_by_xpath("//table/tbody/tr[2]/td[6]/label").text
            name = cells[3].find_element_by_tag_name('span').text  #//table/tbody/tr[2]/td[4]/span
            product = [name, amount, color]
            order_products.append(product)
        return order_products




