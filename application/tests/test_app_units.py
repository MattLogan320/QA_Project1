from flask import url_for
from os import getenv
from flask_testing import TestCase
from application import app, db
from application.models import Books, Customers, CustomerBooks

class TestBase(TestCase):

    def create_app(self):

        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('UNIT_TEST_DATABASE_URI'),
            SECRET_KEY=getenv('TEST_SECRET_KEY',),
            DEBUG=True,
            WTF_CSRF_ENABLED=False
                )
        return app
    
    def setUp(self):
        db.create_all()
        #To test update and delete functionality we need some existing data
        testBook=Books(bookName='This is a test book', author='This is a test author', book_loaned='No')
        testCustomer=Customers(customerName='TestName',surname='TestSurname',email='Testemail@test.com')
        db.session.add(testBook)
        db.session.add(testCustomer)
        db.session.commit()
        testAddBookToCustomer=CustomerBooks(fk_book_id=testBook.id,fk_customer_id=testCustomer.id,returnDate='01/01/0101')
        db.session.add(testAddBookToCustomer)
        db.session.commit()


    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestAddFunctionality(TestBase):

    def test_add_book(self):
        response = self.client.post('/addbook', data=dict(bookName = "Test1", author = "Test1", book_loaned = "No"),
        follow_redirects=True)
        self.assertIn(b'Test1', response.data)

    def test_add_customer(self):
        response = self.client.post('/customer', data=dict(customerName = "Test2", surname = "Test2"),
        follow_redirects=True)
        self.assertIn(b'Test2', response.data)
    
    def test_borrow_book(self):
        response = self.client.post('/addbook', data=dict(bookName = "Test3", author = "Test3", book_loaned = "No"),
        follow_redirects=True)
        response = self.client.post('/customer', data=dict(customerName = "Test3", surname = "Test3"),
        follow_redirects=True)
        response=self.client.post('/addbookcustomer', data=dict(fk_book_id=2,fk_customer_id=2),
        follow_redirects=True)
        self.assertIn(b'customerlist',response.data)

class TestReadFunctionality(TestBase):

    def test_read_book(self):
        response=self.client.get(url_for('library'))
        self.assertIn(b'This is a test book', response.data)

    def test_read_book(self):
        response=self.client.get(url_for('library'))
        self.assertIn(b'This is a test book', response.data)

    def test_read_customer(self):
        response=self.client.get(url_for('customerlist'))
        self.assertIn(b'TestName', response.data)
    
    def test_read_customer_books(self):
        response=self.client.get(url_for('read_customers_borrowed',id=1))
        self.assertIn(b'This is a test book', response.data)

class TestUpdateFunctionality(TestBase):

    def test_update_book(self):
        response= self.client.post('/library/edit/1', data=dict(bookName='Test4',author='Test4',book_loaned='Yes'),
        follow_redirects=True)
        self.assertIn(b'Test4', response.data)
    
    def test_update_customer(self):
        response= self.client.post('/customerlist/edit/1', data=dict(customerName='Test5',surname='Test5',email='Test5@test5.com'),
        follow_redirects=True)
        self.assertIn(b'Test5', response.data)
    
#class TestDeleteFunctionality(TestBase):
    def test_delete_book(self):
        response=self.client.post('/library/delete/1',
        follow_redirects=True)
        self.assertNotIn(b'This is a test book', response.data)
    
    def delete_customer(self):
        response=self.client.post('/customerlist/delete/1',
        follow_redirects=True)
        self.assertNotIn(b'TestName', response.data)
