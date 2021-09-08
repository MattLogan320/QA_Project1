from flask import render_template, url_for, redirect, request
from application import app, db
from application.models import Books, Customers, CustomerBooks
from application.forms import BookForm, CustomerForm, UpdateBookForm, UpdateCustomerForm, CustomerBookForm

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')


#Create Functions
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

@app.route('/customer', methods= ['GET', 'POST'])
def addcustomer():
    form=CustomerForm()
    if form.validate_on_submit():
        customerList=Customers(
          customerName=form.customerName.data,
          surname=form.surname.data,
          email=form.email.data  
        )
        db.session.add(customerList)
        db.session.commit()
        return redirect(url_for('customerlist'))
    else:
        print('Please fill out all fields')
    return render_template('customers.html', title='Add customer', form =form)

@app.route('/addbookcustomer', methods=['GET', 'POST'])
def borrowbook():
	bookList = Books.query.all()
	customerList = Customers.query.all()
	form = CustomerBookForm()
	if form.validate_on_submit():
		customerBook = CustomerBooks(
			fk_book_id = form.book.data,
			fk_customer_id = form.customer.data,
            returnDate = form.returnDate.data
		)
		db.session.add(customerBook)
		db.session.commit()
	return render_template('addbookcustomer.html', title='Borrow book', books=bookList, customers=customerList, form=form)

#Read Functions
@app.route('/library')
def library():
    bookList= Books.query.all()
    return render_template('library.html', title='Library', books=bookList)

@app.route('/customerlist')
def customerlist():
    customerList= Customers.query.all()
    return render_template('customerlist.html', title='Customer List', customers=customerList)

@app.route('/read/<id>', methods= ['GET'])
def read_customers_borrowed(id):
    bookList=Books.query.join(CustomerBooks).filter_by(fk_customer_id=id).all()
    return render_template('read.html',title='Borrowed books', books=bookList)

#Update Functions
@app.route('/library/edit/<id>',methods=['GET','POST'])
def book_edit(id):
    book= Books.query.filter_by(id=id).first()
    form= UpdateBookForm()
    if form.validate_on_submit():
        book.bookName=form.bookName.data
        book.author=form.author.data
        book.book_loaned=form.book_loaned.data
        db.session.commit()
        return redirect(url_for('library'))
    elif request.method == 'GET':
        form.bookName.data= book.bookName
        form.author.data= book.author
        form.book_loaned.data= book.book_loaned
    return render_template('editbook.html', title= 'Edit Book Details', form=form)

@app.route('/customerlist/edit/<id>', methods=['GET','POST'])
def edit_customer(id):
    customer=Customers.query.filter_by(id=id).first()
    form=UpdateCustomerForm()
    if form.validate_on_submit():
        customer.customerName=form.customerName.data
        customer.surname=form.surname.data
        customer.email=form.email.data
        db.session.commit()
        return redirect(url_for('customerlist'))
    elif request.method== 'GET':
        form.customerName.data = customer.customerName
        form.surname.data= customer.surname
        form.email.data= customer.email
    return render_template('editcustomer.html', title='Edit customer details', form=form)

#Delete Functions
@app.route('/library/delete/<id>', methods=['GET','POST'])
def book_delete(id):
    customerBook=CustomerBooks.query.join(Books).filter_by(id=id).all()
    for book in customerBook:
        db.session.delete(book)
    book= Books.query.filter_by(id=id).first()
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for('library'))

@app.route('/customerlist/delete/<id>', methods=['GET','POST'])
def customer_delete(id):
    customerBook=CustomerBooks.query.join(Customers).filter_by(id=id).all()
    for customer in customerBook:
        db.session.delete(customer)
    customer=Customers.query.filter_by(id=id).first()
    db.session.delete(customer)
    db.session.commit()
    return redirect(url_for('customerlist'))

