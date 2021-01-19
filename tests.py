import unittest
from selenium import webdriver
from WebPages.mainpage import MainPage
from WebPages.productpage import Products

from time import sleep


class AOS_tests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path="C:/Selenium/geckodriver.exe")
        self.driver.get("https://www.advantageonlineshopping.com")
        self.mainpage = MainPage(self.driver)
        self.products = Products(self.driver)
        print("setup")
        self.driver.implicitly_wait(10)

    # def test_1(self):
    #     sleep(5)
    #     self.mainpage.click_speakers()
    #     sleep(5)
    #     self.products.choose_speaker(3)
    #     self.products.plus(2)
    #     self.products.change_color('yellow')
    #     self.products.add_to_cart()
    #     self.driver.back()
    #     self.products.choose_speaker(1)
    #     self.products.change_color('grey')
    #     self.products.add_to_cart()
    #     self.mainpage.home_navigate()
    #     self.mainpage.click_tablets()
    #     self.products.choose_tablet(3)
    #     self.products.plus(3)
    #     self.products.change_color('black')
    #     self.products.add_to_cart()
    #     amount = 0
    #     for product in self.products.pop_up_info():
    #         amount += product[1]
    #
    #     if 6 == amount:
    #         assert True
    #     else:
    #         assert False

    def test_2(self):
        sleep(5)
        self.mainpage.click_speakers()
        sleep(5)
        self.products.choose_speaker(2)
        sleep(5)
        self.products.plus(3)
        self.products.change_color('blue')
        self.products.add_to_cart()
        self.driver.back()
        self.products.choose_speaker(1)
        self.products.plus(2)
        self.products.change_color('black')
        self.products.add_to_cart()
        self.mainpage.home_navigate()
        self.mainpage.click_tablets()
        self.products.choose_tablet(1)
        self.products.change_color('grey')
        self.products.add_to_cart()
        print("----------------------")
        print("----------------------")
        # כאן תכנס לולאה אשר תבדוק מחיר (כמות כפול מחיר בסיס),צבע,כמות ושם
        # self.assertEqual(self.products.pop_up_info()[0][0], "HP ELITEPAD 1000 G2 TABLET")  # WORKING
        # self.assertEqual(self.products.pop_up_info()[0][1], 1)  # WORKING
        # self.assertEqual(self.products.pop_up_info()[0][2], 'GRAY')  # WORKING
        # self.assertEqual(self.products.pop_up_info()[0][3], 1009.0)  # WOKRING
        #
        # self.assertEqual(self.products.pop_up_info()[1][0], "BOSE SOUNDLINK BLUETOOTH SP...")  # WOKRING
        # self.assertEqual(self.products.pop_up_info()[1][1], 2)  # WORKING
        # self.assertEqual(self.products.pop_up_info()[1][2], 'BLACK')  # WOKRING
        # self.assertEqual(self.products.pop_up_info()[1][3], 539.98)  # WORKING
        #
        # self.assertEqual(self.products.pop_up_info()[2][0], "BOSE SOUNDLINK WIRELESS SPE...")  # WOKRING
        # self.assertEqual(self.products.pop_up_info()[2][1], 3)  # WORKING
        # self.assertEqual(self.products.pop_up_info()[2][2], 'BLUE')  # WORKING
        # self.assertEqual(self.products.pop_up_info()[2][3], 387.0)  # WORKING

        # print(self.products.pop_up_info()[2][0], "NAME")
        print(type(self.products.pop_up_info()[1][1]))
        # print(self.products.pop_up_info()[2][2], "COLOR")
        print(type(self.products.pop_up_info()[2][3]))

    # def test_3(self):
    #     pass

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

    def tearDown(self):
        # self.driver.close()
        pass

    if __name__ == '__main__':  # run all the unit test we defined
        unittest.main()
