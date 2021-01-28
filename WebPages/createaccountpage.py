from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class CreateAccount():
    def __init__(self,driver):
        self.driver = driver

    def enter_username(self,username):
        self.driver.find_element_by_xpath("//*[@id='formCover']/div[1]/div[1]/sec-view[1]/div/input").send_keys(username)

    def enter_passwords(self, password):
        self.driver.find_element_by_xpath("//*[@id='formCover']/div[1]/div[2]/sec-view[1]/div/input").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='formCover']/div[1]/div[2]/sec-view[2]/div/input").send_keys(password)

    def enter_email(self,email):
        self.driver.find_element_by_xpath("//*[@id='formCover']/div[1]/div[1]/sec-view[2]/div/input").send_keys(email)

            #personal details
    def enter_fullname(self, fname, lname):
        self.driver.find_element_by_css_selector("input[name='first_nameRegisterPage']").send_keys(fname)
        self.driver.find_element_by_css_selector("input[name='last_nameRegisterPage']").send_keys(lname)

    def enter_phone(self, phone):
        self.driver.find_element_by_css_selector("input[name='phone_numberRegisterPage']").send_keys(phone)

        #address
    def enter_city(self, city):
        self.driver.find_element_by_name("cityRegisterPage").send_keys(city)

    def enter_address(self, address):
        self.driver.find_element_by_name("addressRegisterPage").send_keys(address)

    def enter_state(self, state):
        self.driver.find_element_by_css_selector("input[name='state_/_province_/_regionRegisterPage']").send_keys(state)

    def enter_postalcode(self, postalcode):
        self.driver.find_element_by_name("postal_codeRegisterPage").send_keys(postalcode)

    def enter_country(self , country_value):
        # self.driver.find_element_by_name("countryListboxRegisterPage").send_keys(country).send_keys(Keys.ENTER)
        country_dropdown = self.driver.find_element_by_css_selector("select[name='countryListboxRegisterPage']")
        select_country = Select(country_dropdown)
        select_country.select_by_visible_text(country_value)
        # country_dropdown.select_by_visible_text(country)
        # country_dropdown.select_by_value('1')

    def click_i_agree_and_register(self):
        self.driver.find_element_by_css_selector("input[name='i_agree']").click()
        self.driver.find_element_by_id("register_btnundefined").click()

    def order_payment_next_btn(self):
        self.driver.find_element_by_id("next_btn").click()

    def safepay_username_and_password(self , username, password):
        self.driver.find_element_by_name("safepay_username").send_keys(username)
        self.driver.find_element_by_name("safepay_password").send_keys(password)
        self.driver.find_element_by_id("pay_now_btn_SAFEPAY").click() # PAY NOW button

    def click_orders_page(self):
        user = self.driver_find_element_by_id("menuUserLink")  # move with the mouse the shoppi
        ActionChains(self.driver).click(user).perform()
        self.driver.find_element_by_xpath("//a/div/label[@translate='My_Orders']").click()