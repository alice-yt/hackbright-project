"""Server for Sleep Journal app"""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import db, User, User_entry, Mood, User_entry_mood, Medication, User_entry_medication, Symptom, User_entry_symptom, connect_to_db 
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
    print('reached menu')

    return render_template('menu.html')


@app.route('/log_entry')
def log_combined_entry():
    """Log entry"""

    return render_template('combined_form.html')


@app.route('/user_entries')
def all_user_entries():
    """View all user entries of user within the session"""


    user = session.get('user')
    if not user:
        return redirect('/') 

    user = crud.get_user_by_id(session['user'])
    user_entries = user.user_entry
    
    return render_template('all_user_entries.html', user_entries=user_entries)


@app.route('/sleep_insights')
def view_sleep_analysis():
    """View charts and analysis of sleep"""

    return render_template('sleep_insights.html')


@app.route('/users')
def all_users():
    """Show list of users"""

    users = crud.get_users()

    return render_template('all_users.html', users=users)  


@app.route('/users/<user_id>')
def show_user(user_id):
    """Show user email and entries by clicking on the user on /users page"""

    user = crud.get_user_by_id(user_id)
    user_entries = user.user_entry

    return render_template('user_details.html', user=user, user_entries=user_entries)


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


@app.route('/api/login', methods=['POST'])
def api_login_user():
    """Separate login page to test AJAX response"""

    email = request.form.get('login-email')
    password = request.form.get('login-password')

    user = crud.get_user_by_email(email)

    if user.password == password:
        print('user password')
        session['user'] = user.user_id
        return 'Login successful'
    
    else:
        return 'Login unsuccessful'


@app.route('/', methods=['POST'])
def login_user():
    """Login User"""
    print('LOGIN')
    email = request.form.get('login-email')
    password = request.form.get('login-password')

    user = crud.get_user_by_email(email)
    print('USER')
    if user.password == password:
        print('user password')
        session['user'] = user.user_id
        flash('Logged in!')
        
    else:
        print('no user')
        flash('This email is not recognized in our system')
    
    return redirect('/menu')
  

@app.route('/log_entry', methods=['POST'])
def add_time_and_input_fields():
    """get sleep times and all input fields with sliders"""
    sleeptime = request.form.get('sleeptime')
    waketime = request.form.get('waketime')
    sleep_quality = request.form.get('sleep_quality')
    stress_level = request.form.get('stress')
    energy_level = request.form.get('energy')
    productivity_level = request.form.get('productivity')
    exercise_level = request.form.get('exercise')
    alcoholic_units = request.form.get('alcoholic_units')

    """create user entry with sleep times and all input fields with sliders"""
    user_entry = crud.create_user_entry(session['user'], sleeptime, waketime, sleep_quality, stress_level, energy_level, productivity_level, exercise_level, alcoholic_units)

    """get moods, meds, and symptoms checkbox inputs from form"""
    moods = request.form.getlist('mood')
    medications = request.form.getlist('medication')
    symptoms = request.form.getlist('symptom')

    """for mood, meds, and symptoms, associate it with a user entry id and mood/med/symptom id"""
    for mood_name in moods: 
        mood = Mood.query.filter_by(mood=mood_name).first()
        user_entry_mood = User_entry_mood(
            user_entry_id=user_entry.user_entry_id, 
            mood_id=mood.mood_id
        )
        db.session.add(user_entry_mood)
        db.session.commit()

    for med_name in medications:
        med = Medication.query.filter_by(medication=med_name).first()
        user_entry_med = User_entry_medication(
            user_entry_id=user_entry.user_entry_id, 
            medication_id=med.medication_id
        )
        db.session.add(user_entry_med)
        db.session.commit()

    for symptom in symptoms:
        sym = Symptom.query.filter_by(symptom=symptom).first()
        user_entry_symptom = User_entry_symptom(
            user_entry_id=user_entry.user_entry_id, 
            symptom_id=sym.symptom_id
        )
        db.session.add(user_entry_symptom)
        db.session.commit()

    flash("Your entry has been successfully added!")

    return redirect('/menu')


# currently displays a 404 error
@app.route('/user_entries/<user_entry_id>') 
def show_user_entry(user_entry_id):
    """Show all of the entry's details"""

    user = crud.get_user_by_id(user_id)
    user_entries = user.user_entry

    return render_template('user_entry_details.html', user=user, user_entry=user_entry)


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)