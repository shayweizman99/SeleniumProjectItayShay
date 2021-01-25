from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class CreateAccount():
    def __init__(self,driver):
        self.driver = driver
        #account details
        # self.username = 'ItayNshay123'
        # self.password = 'LastProject123'
        # self.confirmpass = self.password
        # self.email = 'shayweizman199@gmail.com'
        # #personal details
        # self.firstname = 'itay'
        # self.lastname = 'zilberman'
        # self.phone = '0505050505'
        # #address
        # self.city = 'krayot city'
        # self.address = 'yigal alon 90'
        # self.state = 'lorem ipsum'
        # self.postalcode = '1920500'

            #account details
    def enter_username(self,username):
        self.driver.find_element_by_xpath("//*[@id='formCover']/div[1]/div[1]/sec-view[1]/div/input").send_keys(username)

    def enter_passwords(self, password):
        self.driver.find_element_by_xpath("//*[@id='formCover']/div[1]/div[2]/sec-view[1]/div/input").send_keys(password)
        self.driver.find_element_by_xpath("//*[@id='formCover']/div[1]/div[2]/sec-view[2]/div/input").send_keys(password)

    def enter_email(self,email):
        self.driver.find_element_by_xpath("//*[@id='formCover']/div[1]/div[1]/sec-view[2]/div/input").send_keys(email)

            #personal details
    def enter_fullname(self, fname, lname):
        self.driver.find_element_by_xpath("//*[@id='formCover']/div[2]/div[1]/sec-view[1]/div/label").send_keys(fname)
        self.driver.find_element_by_xpath("//*[@id='formCover']/div[2]/div[1]/sec-view[2]/div/input").send_keys(lname)

    def enter_phone(self, phone):
        self.driver.find_element_by_xpath("//*[@id='formCover']/div[2]/div[2]/sec-view/div/label").send_keys(phone)


