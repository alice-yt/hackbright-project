"""Server for movie ratings app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db
import crud

from jinja2 import StrictUndefined


app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def login():
    return render_template('homepage.html')

@app.route('menu')
def menu():
    return render_template('menu.html')

@app.route('/user_entries')
def all_user_entries():
    """View all user entries."""

    user_entries = crud.get_user_entries()

    return render_template('all_user_entries.html', user_entries=user_entries)


@app.route('/user_entries/<user_entry_id>')
def show_user_entry(user_entry_id):
    """Show user entry details"""
    user_entry = crud.get_user_entry_by_id(user_entry_id)

    return render_template('user_entry_details.html', user_entry=user_entry)


@app.route('/users')
def all_users():

    users = crud.get_users()

    return render_template('all_users.html', users=users)  


@app.route('/users/<user_id>')
def show_user(user_id):
    """Show user details"""
    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)


@app.route('/users', methods=['POST'])
def register_user():
    """Create User"""
    full_name = request.form.get('full_name')
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user:
        flash('Cannot create an account with that email. Please try again.')    
    else:
        crud.create_user(full_name, email, password)
        flash('Account created! Please log in.')

    return redirect('/')


@app.route('/login', methods=['POST'])
def login_user():
    """Login User"""
    email = request.form.get('email')
    password = request.form.get('password')

    user = crud.get_user_by_email(email)
    if user.password == password:
        session['user'] = User.user_id
        flash('Logged in!')
        
    else:
        flash('This email is not recognized in our system')

    return redirect('/')
  

if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)