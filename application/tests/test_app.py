import unittest
from flask import url_for
from urllib.request import urlopen


from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from application import app, db
from application.models import Books, Customers, CustomerBooks

class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config.update(
        SQLALCHEMY_DATABASE_URI=getenv('LIVE_TEST_DATABASE_URI'),
        DEBUG=True,
        WTF_CSRF_ENABLED=False
        )
        return app


    def setUp(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options) 
        db.create_all()
        self.driver.get("http://localhost:5000")
        
    def tearDown(self):
        self.driver.quit()
        db.drop_all()

class TestRunning(TestBase):    
    def test_app_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)

class TestButtons(TestBase):
    def test_home_button(self):
        self.driver.find_element_by_xpath('/html/body/a[1]').click()
        assert url_for('home') in self.driver.current_url
    
    def test_add_book_button(self):
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        assert url_for('addbook') in self.driver.current_url
    
    def test_library_button(self):
        self.driver.find_element_by_xpath('/html/body/a[3]').click()
        assert url_for('library') in self.driver.current_url
   
    def test_add_customer_button(self):
        self.driver.find_element_by_xpath('/html/body/a[4]').click()
        assert url_for('addcustomer') in self.driver.current_url
    
    def test_view_customers_button(self):
        self.driver.find_element_by_xpath('/html/body/a[5]').click()
        assert url_for('customerlist') in self.driver.current_url
    
    def test_add_book_to_customer_button(self):
        self.driver.find_element_by_xpath('/html/body/a[6]').click()
        assert url_for('borrowbook') in self.driver.current_url


#Variables
test_add_bookName="The Very Hungry Caterpillar"
test_add_author="Eric Carle"
test_book_loaned="No"
test_add_customerName="Jeremy"
test_add_surname="Corbyn"
test_add_email="test@email.com"
test_add_bookID="1"
test_add_customerID="1"
test_add_returnDate="01/01/0101"
test_edit_bookName="It"
test_edit_author="Stephen King"
test_edit_book_loaned="Yes"
test_edit_customerName="Boris"
test_edit_surname="Johnson"
test_edit_email="PM@email.com"



class TestCreateFunctionality(TestBase):

    def test_add_book_submit_button(self):
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="bookName"]').send_keys(test_add_bookName)
        self.driver.find_element_by_xpath('//*[@id="author"]').send_keys(test_add_author)
        self.driver.find_element_by_xpath('//*[@id="book_loaned"]').send_keys('No')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('library') in self.driver.current_url


    
    def test_add_customer_submit_button(self):
        self.driver.find_element_by_xpath('/html/body/a[4]').click()
        self.driver.find_element_by_xpath('//*[@id="customerName"]').send_keys(test_add_customerName)
        self.driver.find_element_by_xpath('//*[@id="surname"]').send_keys(test_add_surname)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_add_email)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('customerlist') in self.driver.current_url
    
    

    def test_add_book_to_customers_booklist_submit_button(self):
        self.driver.find_element_by_xpath('/html/body/a[6]').click()
        self.driver.find_element_by_xpath('//*[@id="book"]').send_keys(test_add_bookID)
        self.driver.find_element_by_xpath('//*[@id="customer"]').send_keys(test_add_customerID)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('borrowbook') in self.driver.current_url
    

class TestReadFunctionality(TestBase):
    
    def test_read_customers_borrowed_books(self):
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="bookName"]').send_keys(test_add_bookName)
        self.driver.find_element_by_xpath('//*[@id="author"]').send_keys(test_add_author)
        self.driver.find_element_by_xpath('//*[@id="book_loaned"]').send_keys('No')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.driver.find_element_by_xpath('/html/body/a[4]').click()
        self.driver.find_element_by_xpath('//*[@id="customerName"]').send_keys(test_add_customerName)
        self.driver.find_element_by_xpath('//*[@id="surname"]').send_keys(test_add_surname)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_add_email)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.driver.find_element_by_xpath('/html/body/a[6]').click()
        self.driver.find_element_by_xpath('//*[@id="book"]').send_keys(test_add_bookID)
        self.driver.find_element_by_xpath('//*[@id="customer"]').send_keys(test_add_customerID)
        self.driver.find_element_by_xpath('//*[@id="returnDate"]').send_keys(test_add_returnDate)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.driver.find_element_by_xpath('/html/body/form[3]/button').click()
        assert url_for('read_customers_borrowed',id=test_add_customerID) in self.driver.current_url

class TestUpdateFunctionality(TestBase):

    def test_edit_book(self):
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="bookName"]').send_keys(test_add_bookName)
        self.driver.find_element_by_xpath('//*[@id="author"]').send_keys(test_add_author)
        self.driver.find_element_by_xpath('//*[@id="book_loaned"]').send_keys('No')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.driver.find_element_by_xpath('/html/body/form[2]/button').click()
        self.driver.find_element_by_xpath('//*[@id="bookName"]').send_keys(test_edit_bookName)
        self.driver.find_element_by_xpath('//*[@id="author"]').send_keys(test_edit_author)
        self.driver.find_element_by_xpath('//*[@id="book_loaned"]').send_keys('Yes')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('library') in self.driver.current_url
    
    def test_edit_customer(self):
        self.driver.find_element_by_xpath('/html/body/a[4]').click()
        self.driver.find_element_by_xpath('//*[@id="customerName"]').send_keys(test_add_customerName)
        self.driver.find_element_by_xpath('//*[@id="surname"]').send_keys(test_add_surname)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_add_email)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.driver.find_element_by_xpath('/html/body/form[2]/button').click()
        self.driver.find_element_by_xpath('//*[@id="customerName"]').send_keys(test_edit_bookName)
        self.driver.find_element_by_xpath('//*[@id="surname"]').send_keys(test_edit_author)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_edit_email)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('customerlist') in self.driver.current_url

class TestDeleteFunctionality(TestBase):

    def test_delete_book(self):
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="bookName"]').send_keys(test_add_bookName)
        self.driver.find_element_by_xpath('//*[@id="author"]').send_keys(test_add_author)
        self.driver.find_element_by_xpath('//*[@id="book_loaned"]').send_keys('No')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.driver.find_element_by_xpath('/html/body/form[1]/button').click()
        assert url_for('library') in self.driver.current_url
    
    def test_delete_customer(self):
        self.driver.find_element_by_xpath('/html/body/a[4]').click()
        self.driver.find_element_by_xpath('//*[@id="customerName"]').send_keys(test_add_customerName)
        self.driver.find_element_by_xpath('//*[@id="surname"]').send_keys(test_add_surname)
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_add_email)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        self.driver.find_element_by_xpath('/html/body/form[1]/button').click()
        assert url_for('customerlist') in self.driver.current_url