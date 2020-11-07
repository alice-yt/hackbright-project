""" CRUD operations """
from model import db, User, User_entry, Mood, User_entry_mood, Medication, User_entry_medication, Symptom, User_entry_symptom, connect_to_db

from datetime import datetime

def create_user(full_name, email, password):
    """Create and return a new user."""

    user = User(full_name=full_name,email=email, password=password)

    db.session.add(user)
    db.session.commit()

    return user

def create_user_entry(datetime_of_input, datetime_of_entry, sleeptime, waketime, sleep_quality, stress_level, energy_level, productivity_level, exercise_level, alcoholic_units):
    """Create and return a new user entry."""

    user_entry = User_entry(datetime_of_input=datetime_of_input, 
                            datetime_of_entry=datetime_of_entry, 
                            sleeptime=sleeptime, 
                            waketime=waketime, 
                            sleep_quality=sleep_quality, 
                            stress_level=stress_level, 
                            energy_level=energy_level, 
                            productivity_level=productivity_level, 
                            exercise_level=exercise_level, 
                            alcoholic_units=alcoholic_units)

    db.session.add(user_entry)
    db.session.commit()

    return user_entry

    

# def get_movies():
#     """Create and return all movies."""

#     return Movie.query.all()

# def get_users():
#     """ Get list of users"""

#     return User.query.all()

# def get_user_by_id(user_id):
#     """ gets user by id"""

#     return User.query.get(user_id)

# def get_movie_by_id(movie_id):
#     """ gets movie by id """

#     return Movie.query.get(movie_id)

# def create_rating(user, movie, score):
#     """Create and return a new rating."""
    
#     rating = Rating(user=user, 
#                     movie=movie, 
#                     score=score)
    
#     db.session.add(rating)
#     db.session.commit()

#     return rating

# def get_user_by_email(email):

#     return User.query.filter(User.email == email).first()



if __name__ == '__main__':
    from server import app
    connect_to_db(app)