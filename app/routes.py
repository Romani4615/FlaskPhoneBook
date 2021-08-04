from flask_wtf import form
from app import app
from flask import render_template, redirect, url_for
from app.forms import PhoneBook

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/PhoneBook', methods=['GET', 'POST'])
def phonebook():
    form = PhoneBook()
    if form.validate_on_submit():
        print('VALID FORM')
        name = form.name.data
        phone_number = form.phone_number.data
        address = form.address.data
        print(name, phone_number, address)
        return redirect(url_for('phonebook'))
    return render_template('PhoneBook.html', title='Your Friendly Neighborhood Phone Book', form=form)