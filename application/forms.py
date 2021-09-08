from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class BookForm(FlaskForm):
    
    bookName = StringField('Book Name',
        validators= [DataRequired(), 
                    Length(min=2, max=150)])
    
    author = StringField('Author\'s name' , 
        validators= [DataRequired(), 
                    Length(min=2, max=100)])
    
    loaned=[('Yes','Yes'),('No','No')]
    
    book_loaned = SelectField('Loaned?', choices= loaned,
        validators= [DataRequired()])
    
    submit= SubmitField('Add Book')

class CustomerForm(FlaskForm):

    customerName = StringField('Name', 
        validators= [DataRequired(),
                    Length(min=2, max=100)])
    
    surname = StringField('Surname',
        validators= [DataRequired(),
                    Length(min=2, max=100)])
    
    email = StringField('Email',
        validators= [Length(min=6, max=150)])

    submit= SubmitField('Add')

class UpdateBookForm(FlaskForm):
    
    bookName = StringField('Book Name',
        validators= [DataRequired(), 
                    Length(min=2, max=150)])
    
    author = StringField('Author\'s name' , 
        validators= [DataRequired(), 
                    Length(min=2, max=100)])
    
    loaned=[('Yes','Yes'),('No','No')]
    
    book_loaned = SelectField('Loaned?', choices= loaned,
        validators= [DataRequired()])
    
    submit= SubmitField('Update Book')

class UpdateCustomerForm(FlaskForm):

    customerName = StringField('Name', 
        validators= [DataRequired(),
                    Length(min=2, max=100)])
    
    surname = StringField('Surname',
        validators= [DataRequired(),
                    Length(min=2, max=100)])
    
    email = StringField('Email',
        validators= [Length(min=6, max=150)])

    submit= SubmitField('Update Details')

class CustomerBookForm(FlaskForm):
    book = IntegerField('Book ID',
        validators= [DataRequired()])
    
    customer= IntegerField('Customer ID',
        validators= [DataRequired()])

    returnDate= StringField('Return Date',
        validators= [DataRequired(),
                    Length(min=6, max=10)])
    submit = SubmitField('Loan out book')