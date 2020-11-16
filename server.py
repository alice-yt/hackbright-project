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
def homepage():
    """View login page"""

    return render_template('homepage.html')


@app.route('/create_account')
def create_account():
    """View account creation page"""

    return render_template('create_account.html')


@app.route('/menu')
def menu():
    """View menu page"""

    return render_template('menu.html')


@app.route('/enter_entry')
def log_entry():
    """Log sleep and wake time"""

    return render_template('enter_entry.html')


@app.route('/user_entries')
def all_user_entries():
    """View all user entries"""

    user_entries = crud.get_user_entries()

    return render_template('all_user_entries.html', user_entries=user_entries)


# check what this is doing
@app.route('/user_entries/<user_entry_id>') 
def show_user_entry(user_entry_id):
    """Show user entry details"""

    user_entry = crud.get_user_entry_by_id(user_entry_id)

    return render_template('user_entry_details.html', user_entry=user_entry)


@app.route('/sleep_insights')
def view_sleep_analysis():
    """View charts and analysis of sleep"""

    return render_template('sleep_insights.html')


@app.route('/users')
def all_users():

    users = crud.get_users()

    return render_template('all_users.html', users=users)  


# check what this is doing
@app.route('/users/<user_id>')
def show_user(user_id):
    """Show user details"""

    user = crud.get_user_by_id(user_id)

    return render_template('user_details.html', user=user)


@app.route('/create_account', methods=['POST'])
def register_user():
    """Create User"""

    full_name = request.form.get('full-name')
    email = request.form.get('create-email')
    password = request.form.get('create-password')

    user = crud.get_user_by_email(email)
    if user:
        flash('Cannot create an account with that email. Please try again.') 

    else:
        crud.create_user(full_name, email, password)
        flash('Account created! Please log in.')
    
    return redirect('/')


@app.route('/', methods=['GET'])
def login_user():
    """Login User"""
    print('LOGIN')
    email = request.form.get('login-email')
    password = request.form.get('login-password')

    user = crud.get_user_by_email(email)
    print('USER')
    if user.password == password:
        print('user password')
        # session['user'] = User.user_id
        flash('Logged in!')
        
    else:
        print('no user')
        flash('This email is not recognized in our system')
    
    return redirect('/menu')
  

@app.route('/enter_entry', methods=['POST'])
def add_sleep_wake_time():
    """Save sleep and wake time that user submits"""



if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)