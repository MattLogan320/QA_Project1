from application import db

#creating the schema for the books, with the author and availability included
class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bookName = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    book_loaned = db.Column(db.String(5), nullable=False)
    customerBook1= db.relationship('CustomerBooks', backref=db.backref('book',lazy = True))


class Customers(db.Model):
    id =db.Column(db.Integer, primary_key=True)
    customerName = db.Column(db.String(100), nullable=False)
    surname = db.Column(db.String(100), nullable=False)
    customerBook2= db.relationship('CustomerBooks', backref=db.backref('customer',lazy = True))

class CustomerBooks(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    fk_book_id=db.Column(db.Integer,db.ForeignKey('books.id'))
    fk_customer_id = db.Column(db.Integer,db.ForeignKey('customers.id'))