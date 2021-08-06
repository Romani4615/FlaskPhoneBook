from flask_migrate import current
from flask_wtf import form
from app import app, db
from flask import render_template, flash, redirect, url_for
from app.forms import CreatePostForm, RegisterForm, LoginForm, PhoneBook
from app.models import User, Post
from flask_login import login_required, login_user, logout_user, current_user, login_manager

@app.route('/')
def index():
    name = 'Aaron'
    title = 'Coding Temple Intro to Flask'
    all_posts = Post.query.all()
    return render_template('index.html', name=name, title=title, posts=all_posts)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Grab data from our submitted form
        email = form.email.data
        first_name = form.first_name.data  
        last_name = form.last_name.data  
        password = form.password.data
        print(first_name, last_name, email, password)
        # Create new instance of User
        new_user = User(first_name, last_name, email, password)

        # Add new_user to our database
        db.session.add(new_user)
        db.session.commit()

        # Once new_user is added to db, flash success message
        flash(f'Thank you for signing up {new_user.first_name, new_user.last_name}!', 'danger')

        # Redirect user back to home page
        return redirect(url_for('index'))
    return render_template('register.html', title='Register for CT Blog', form=form)


@app.route('/createpost', methods=['GET', 'POST'])
@login_required   #UNCOMMENT WHEN LOGGED IN



def CreatePost():
    form = CreatePostForm()
    if form.validate_on_submit():
        #grab data from form
        first_name = form.first_name.data
        last_name = form.last_name.data
        phone_number = form.phone_number.data
        address = form.address.data
        print(first_name, last_name, phone_number, address, current_user.id)
        #create new instance of post
        new_post = Post(first_name, last_name, phone_number, current_user.id)

        # add new post to database
        db.session.add(new_post)
        db.session.commit()
        #flash message
        
        flash(f'your post has successfully been created {new_post.title}')
        return redirect(url_for('index'))
    return render_template('createpost.html', form=form)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
       #return the first user object
        user = User.query.filter_by(email=email).first()
        
        
        if user is None or user.check_password(password): 
            flash('Incorrect Email/Password. Try Again', 'danger')
            return redirect(url_for('login'))

        login_user(user)
        flash('You have successfully logged in!', 'success')
        return redirect(url_for('index'))


    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

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