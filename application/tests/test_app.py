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
        SQLALCHEMY_DATABASE_URI=getenv('TEST_DATABASE_URI'),
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

class TestRunnig(TestBase):    
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
test_add_bookID="1"
test_add_customerID="1"
test_edit_bookName="It"
test_edit_author="Stephen King"
test_edit_book_loaned="Yes"



class TestCreateFunctionality(TestBase):

    def test_add_book_button(self):
        self.driver.find_element_by_xpath('/html/body/a[2]').click()
        self.driver.find_element_by_xpath('//*[@id="bookName"]').send_keys(test_add_bookName)
        self.driver.find_element_by_xpath('//*[@id="author"]').send_keys(test_add_author)
        self.driver.find_element_by_xpath('//*[@id="book_loaned"]').send_keys('No')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('library') in self.driver.current_url

    def test_add_book(self):
        response = self.post('/addbook', data=dict(bookName = "Test1", author = "Test1", book_loaned = "No"),
        follow_redirects=True)
        self.assertIn(b'Test1', response.data)
    
    def test_add_customer_button(self):
        self.driver.find_element_by_xpath('/html/body/a[4]').click()
        self.driver.find_element_by_xpath('//*[@id="customerName"]').send_keys(test_add_customerName)
        self.driver.find_element_by_xpath('//*[@id="surname"]').send_keys(test_add_surname)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('customerlist') in self.driver.current_url
    
    def test_add_customer(self):
        response = self.post('/customer', data=dict(customerName = "Test1", surname = "Test1"),
        follow_redirects=True)
        self.assertIn(b'Test1', response.data)

    def test_add_book_to_customers_booklist_button(self):
        self.driver.find_element_by_xpath('/html/body/a[6]').click()
        self.driver.find_element_by_xpath('//*[@id="book"]').send_keys(test_add_bookID)
        self.driver.find_element_by_xpath('//*[@id="customer"]').send_keys(test_add_customerID)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('borrowbook') in self.driver.current_url
    



class TestUpdateFunctionality(TestBase):

    def test_edit_book(self):
        self.driver.find_element_by_xpath('/html/body/a[3]').click()
        self.driver.find_element_by_xpath('/html/body/form[2]/button').click()
        self.driver.find_element_by_xpath('//*[@id="bookName"]').send_keys(test_edit_bookName)
        self.driver.find_element_by_xpath('//*[@id="author"]').send_keys(test_edit_author)
        self.driver.find_element_by_xpath('//*[@id="book_loaned"]').send_keys('Yes')
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        assert url_for('library') in self.driver.current_url


#class TestDeleteFunctionality(TestBase):