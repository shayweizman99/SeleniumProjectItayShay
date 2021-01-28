import unittest
from selenium import webdriver
from WebPages.mainpage import MainPage
from WebPages.productpage import Products
from WebPages.shoppingcartpage import ShoppingCart
from WebPages.createaccountpage import CreateAccount
from time import sleep
from WebPages.orderspage import OrdersPage


class AOS_tests(unittest.TestCase):

    def setUp(self):
        # self.driver = webdriver.Firefox(executable_path="C:/Selenium/geckodriver.exe")
        self.driver = webdriver.Chrome(executable_path="C:/Selenium/chromedriver.exe")
        self.driver.get("https://www.advantageonlineshopping.com")
        self.mainpage = MainPage(self.driver)
        self.products = Products(self.driver)
        self.shoppingcart = ShoppingCart(self.driver)
        self.createaccount = CreateAccount(self.driver)
        self.orderspage = OrdersPage(self.driver)
        print("setup")
        self.driver.implicitly_wait(10)
        self.mainpage.loader_wait()

    def test_1(self):
        # sleep(5)
        self.mainpage.click_speakers()
        # sleep(5)
        self.products.choose_speaker(3)
        self.products.plus(2)
        self.products.change_color('yellow')
        self.products.add_to_cart()
        self.driver.back()
        self.products.choose_speaker(1)
        self.products.change_color('grey')
        self.products.add_to_cart()
        self.mainpage.home_navigate()
        self.mainpage.click_tablets()
        self.products.choose_tablet(3)
        self.products.plus(3)
        self.products.change_color('black')
        self.products.add_to_cart()
        amount = 0
        for product in self.products.pop_up_info():
            amount += product[1]

        if 6 == amount:
            assert True
        else:
            assert False
    #
    # def test_2(self):
    #     # sleep(5)
    #     self.mainpage.click_speakers()
    #     # sleep(5)
    #     self.products.choose_speaker(2)
    #     # sleep(5)
    #     self.products.plus(3)
    #     self.products.change_color('blue')
    #     self.products.add_to_cart()
    #     self.driver.back()
    #     self.products.choose_speaker(1)
    #     self.products.plus(2)
    #     self.products.change_color('black')
    #     self.products.add_to_cart()
    #     self.mainpage.home_navigate()
    #     self.mainpage.click_tablets()
    #     self.products.choose_tablet(1)
    #     self.products.change_color('grey')
    #     self.products.add_to_cart()
    #     prods_list = self.products.pop_up_info()
    # #       product 1
    #     self.assertEqual(prods_list[0][0], "HP ELITEPAD 1000 G2 TABLET")  # WORKING
    #     self.assertEqual(prods_list[0][1], 1)  # WORKING
    #     self.assertEqual(prods_list[0][2], 'GRAY')  # WORKING
    #     self.assertEqual(prods_list[0][3], 1009.0)  # WOKRING
    # #       product 2
    #     self.assertEqual(prods_list[1][0], "BOSE SOUNDLINK BLUETOOTH SP...")  # WOKRING
    #     self.assertEqual(prods_list[1][1], 2)  # WORKING
    #     self.assertEqual(prods_list[1][2], 'BLACK')  # WOKRING
    #     self.assertEqual(prods_list[1][3], 539.98)  # WORKING
    # #       product 3
    #     self.assertEqual(prods_list[2][0], "BOSE SOUNDLINK WIRELESS SPE...")  # WOKRING
    #     self.assertEqual(prods_list[2][1], 3)  # WORKING
    #     self.assertEqual(prods_list[2][2], 'BLUE')  # WORKING
    #     self.assertEqual(prods_list[2][3], 387.0)  # WORKING
    #
    # def test_3(self): #after adding two products, remove one and check if the shopping cart table was changed
    #     # sleep(5)
    #     self.mainpage.click_speakers()
    #     # sleep(5)
    #     self.products.choose_speaker(2)
    #     # sleep(5)
    #     self.products.add_to_cart()
    #     self.mainpage.home_navigate()
    #     self.mainpage.click_tablets()
    #     self.products.choose_tablet(1)
    #     self.products.add_to_cart()
    #     list_before = len(self.products.pop_up_info()) #list before product removal
    #     self.products.remove_product()
    #     list_after = len(self.products.pop_up_info()) #list after product removal
    #     self.assertNotEqual(list_before, list_after) #validate that the 2 lists lengths aren't equal before and after
    #
    #
    #
    #
    # def test_4(self): #after making an order, go to cart and make sure you are in the right page
    #     #sleep(5)
    #     self.mainpage.click_speakers()
    #     # sleep(5)
    #     self.products.choose_speaker(2)
    #     # sleep(5)
    #     self.products.plus(3)
    #     self.products.change_color('blue')
    #     self.products.add_to_cart()
    #     self.products.click_on_cart_icon()
    #     cart_text = self.shoppingcart.locate_shoppingcart_text().text
    #     error_msg = "it is not SHOPPING CART PAGE"
    #     self.assertIn('SHOPPING CART', cart_text,error_msg)
    #
    # def test_5(self):
    #     # sleep(5)
    #     self.mainpage.click_speakers()
    #     # sleep(5)
    #     self.products.choose_speaker(3)
    #     # sleep(5)
    #     self.products.plus(4)
    #     self.products.change_color('red')
    #     self.products.add_to_cart()
    #     self.mainpage.home_navigate()
    #     self.mainpage.click_mice()
    #     self.products.choose_mice(3)
    #     self.products.plus(5)
    #     self.products.change_color('white')
    #     self.products.add_to_cart()
    #     self.mainpage.home_navigate()
    #     self.mainpage.click_tablets()
    #     self.products.choose_tablet(1)
    #     self.products.change_color('grey')
    #     self.products.add_to_cart()
    #     self.products.click_on_cart_icon()
    #     prods_list = self.products.pop_up_info()
    #     list_total_amount = str(prods_list[0][1] + prods_list[1][1] + prods_list[2][1]) #total products amount
    #     list_total_price = prods_list[0][3] + prods_list [1][3] + prods_list[2][3]
    #     cart_text = self.shoppingcart.locate_shoppingcart_text().text.replace('(', '').replace(')', '') #gets the shopping cart amount from the page and takes out ()
    #     self.assertIn(list_total_amount , cart_text)
    #     self.assertEqual(list_total_price , self.shoppingcart.locate_total_price()) #compare total prices
    #-----------------------------------------------------------------------------------------
    # def test_6(self):
    #     # sleep(5)
    #     self.mainpage.click_speakers()
    #     # sleep(5)
    #     self.products.choose_speaker(2)
    #     # sleep(5)
    #     self.products.add_to_cart()
    #     self.mainpage.home_navigate()
    #     self.mainpage.click_tablets()
    #     self.products.choose_tablet(1)
    #     self.products.add_to_cart()
    #     self.products.click_on_cart_icon()
    #     self.shoppingcart.click_edit_product2()[0] #אמור להקליק על אלמנט ראשון - מספר 0 כי בליסט בפייתון מתחילים מ0 - מתוך ה2 אלמנטים כי עשיתי בפונקציה פיינד ביי אלמנטס
    #     self.shoppingcart.plus_1()
    #     self.products.add_to_cart()  # אמור לעבוד, אם לא פשוט מוסיפים פה פונקציה חדשה שכותבים שלוחצת על הADD_TO_CART
    #     self.products.click_on_cart_icon()
    #     self.shoppingcart.click_edit_product2()[1]
    #     self.shoppingcart.plus_1()
    #     self.products.add_to_cart() #אמור לעבוד, אם לא פשוט מוסיפים פה פונקציה חדשה שכותבים שלוחצת על הADD_TO_CART
    #     self.products.click_on_cart_icon()
    #     first_quantity_to_check = self.shoppingcart.locate_QuantityOfProductInCart_text().the_first_quantity.text
    #     second_quantity_to_check = self.shoppingcart.locate_QuantityOfProductInCart_text().the_second_quantity.text
    #     self.assertEqual(first_quantity_to_check, "2")
    #     self.assertEqual(second_quantity_to_check, "2")
    #
    #     # def test_6(self): #הדרך הפשוטה שבטוח עובדת
    #     #     # sleep(5)
    #     #     self.mainpage.click_speakers()
    #     #     # sleep(5)
    #     #     self.products.choose_speaker(2)
    #     #     # sleep(5)
    #     #     self.products.add_to_cart()
    #     #     self.mainpage.home_navigate()
    #     #     self.mainpage.click_tablets()
    #     #     self.products.choose_tablet(1)
    #     #     self.products.add_to_cart()
    #     #     self.products.click_on_cart_icon()
    #     #       self.shoppingcart.click_edit_product() #לשנות רק את הפונקציה לפיינד ביי אלמנט ולהוסיף את ה href="" מהאתר מהתכונות של האלמנט edit
    #
    #--------------------------------------------------------------------------------------------
    # def test_7(self):
    #     self.mainpage.click_tablets()
    #     self.products.choose_tablet(1)
    #     self.products.plus(2)
    #     self.products.add_to_cart()
    #     self.driver.back()
    #     tablets_text = self.products.locate_tablets_text()
    #     self.assertIn('TABLETS' ,tablets_text )
    #     self.driver.back()
    #     specialoffer_text = self.products.locate_specialoffer_text()
    #     self.assertIn('SPECIAL OFFER' , specialoffer_text)

    def test_8(self):
        self.mainpage.click_speakers()
        self.products.choose_speaker(2)
        self.products.plus(3)
        self.products.change_color('blue')
        self.products.add_to_cart()
        self.driver.back()
        self.products.choose_speaker(1)
        self.products.plus(2)
        self.products.change_color('black')
        self.products.add_to_cart()
        self.products.click_on_cart_icon()
        self.shoppingcart.click_checkout_button()
        self.shoppingcart.click_register_button()
        #creating a new account
        self.createaccount.enter_username('shayshy123')
        self.createaccount.enter_passwords('Shay123')
        self.createaccount.enter_email('Shay123@gmail.blayt')
        self.createaccount.enter_fullname('itay', 'zilberman')
        self.createaccount.enter_phone('5005050505')
        self.createaccount.enter_city('afula')
        self.createaccount.enter_address('dvora 45')
        self.createaccount.enter_state('IL')
        self.createaccount.enter_postalcode('181818')
        self.createaccount.enter_country('israel')
        self.createaccount.click_i_agree_and_register()
        #finished creating an account
        self.createaccount.order_payment_next_btn()
        self.createaccount.safepay_username_and_password()
        #move to shopping cart and check if empty
        self.products.click_on_cart_icon()
        cart_text = self.shoppingcart.shopping_cart_empty_text()
        self.assertIn("Your shopping cart is empty" , cart_text) # test to make sure the cart is empty

        sleep(10)
    def tearDown(self):
        # self.driver.close()
        print("teardown")


    if __name__ == '__main__':  # run all the unit test we defined
        unittest.main()
