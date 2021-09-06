from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Books, Customers, CustomerBooks
from application.forms import BookForm, CustomerForm, UpdateBookForm, UpdateCustomerForm, CustomerBookForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/library')
def library():
    bookList= Books.query.all()
    return render_template('library.html', title='Library', books=bookList)

@app.route('/addbook', methods =['GET','POST'])
def addbook():
    form=BookForm()
    if form.validate_on_submit():
        bookList= Books(
            bookName=form.bookName.data,
            author=form.author.data,
            book_loaned=form.book_loaned.data
        )
        db.session.add(bookList)
        db.session.commit()
        return redirect(url_for('library'))
    else:
        print('Please fill out all boxes')
    return render_template('addbook.html', title= 'Add Book', form=form)

@app.route('/customerlist')
def customerlist():
    customerList= Customers.query.all()
    return render_template('customerlist.html', title='Customer List', customers=customerList)

@app.route('/customer', methods= ['GET', 'POST'])
def addcustomer():
    form=CustomerForm()
    if form.validate_on_submit():
        customerList=Customers(
          customerNam=form.customerName.data,
          surname=form.surname.data  
        )
        db.session.add(customerList)
        db.session.commit()
        return redirect(url_for('customerlist'))
    else:
        print('Please fill out all fields')
    return render_template('customers.html', title='Add customer', form =form)

@app.route('/addbookcustomer', methods=['GET', 'POST'])
def querysetsong():
	bookList = Books.query.all()
	customerList = Customers.query.all()
	form = CustomerBookForm()
	if form.validate_on_submit():
		customerBook = CustomerBooks(
			fk_book_id = form.book.data,
			fk_customer_id = form.customer.data
		)
		db.session.add(customerBook)
		db.session.commit()
	return render_template('addbookcustomer.html', title='Borrow book', books=bookList, customers=customerList, form=form)