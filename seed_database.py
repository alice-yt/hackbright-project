"""Script to seed database."""

import os
import json
import random
from datetime import datetime, timedelta
from faker import Faker
fake = Faker()

import crud
import model
import server

os.system('dropdb sleepjournal')
os.system('createdb sleepjournal')

model.connect_to_db(server.app)
model.db.create_all()

#for a user in range 10,
    #WHERE TO PUT THIS? put users in a list and use random choice to associate random data with random users
        #print a fake name, email, password
            #generate 250 entries for each user
                #for each post for each user:
                #generate a sleep time and a wake time
                    #once a sleep time is generated, generate a random number between 5 and 13 hrs
                    #add datetime to random number to get wake time
                #generate 0 - 5 on sleep quality
                #generate 0 - 5 on stress
                #generate 0 - 5 on energy
                #generate 0 - 5 on productivity
                #generate 0 - 5 on exercise
                #generate 0 - 5+ on alcoholic units
                #generate 0-10 on moods
                #generate 0-10 on medications
                #generate 0-9 on symptoms
    

    # how should this data be captured and returned?
    # where to put users in a list and use random choice to associate random data with random users

for user in range(10):
    name = fake.name()
    email = fake.email(domain=None)
    password = fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

    user = model.User(full_name=name, email=email, password=password)
    model.db.session.add(user)
    model.db.session.commit()

    for user_entry in range(250):
        # start = datetime.fromisoformat('2019-01-01')
        start = datetime(2019, 1, 1, 0, 0, 0, 0)
        # end = datetime.fromisoformat('2019-12-31')
        end = datetime(2019, 12, 31, 23, 59, 59, 0)
        # print('LOOK FOR THIS', start)
        # print(end)
        sleeptime = fake.date_time_between_dates(datetime_start=start, datetime_end=end)
        
        waketime = sleeptime + timedelta(hours=9)
    
        sleep_quality = random.randint(0, 5)
    
        stress_level = random.randint(0, 5)

        energy_level = random.randint(0, 5)
    
        productivity_level = random.randint(0, 5)

        exercise_level = random.randint(0, 5)
    
        list_of_alcoholic_units = ['0', '1', '2', '3', '4', '5+']
        random.choice(list_of_alcoholic_units)

        user_entry = model.User_entry(user_id=user.user_id, sleeptime=sleeptime, waketime=waketime, sleep_quality=sleep_quality, stress_level=stress_level, energy_level=energy_level, productivity_level=productivity_level, exercise_level=exercise_level, alcoholic_units=list_of_alcoholic_units)
        model.db.session.add(user_entry)
        model.db.session.commit()

        # sleeptime = db.Column(db.DateTime)
        # waketime = db.Column(db.DateTime)
        # sleep_quality = db.Column(db.Integer, nullable=False)
        # stress_level = db.Column(db.Integer)
        # energy_level = db.Column(db.Integer)
        # productivity_level = db.Column(db.Integer)
        # exercise_level = db.Column(db.Integer)
        # alcoholic_units = db.Column(db.Integer)

moods = {
    1: 'Happy', 
    2: 'Calm', 
    3: 'Content', 
    4: 'Excited', 
    5: 'Anxious', 
    6: 'Depressed', 
    7: 'Irritated', 
    8: 'Angry', 
    9: 'Self critical', 
    10: 'Confused', 
}

for key in moods:
    random.choice(list(moods.values()))

    mood = model.Mood(mood=mood)
    model.db.session.add(mood)
    model.db.session.commit()

medications = {
    1: 'None', 
}

for key in medications:
    random.choice(list(medications.values()))

    medication = model.Medication(medication=medication)
    model.db.session.add(medication)
    model.db.session.commit()

symptoms = {
    1: 'Fatigue', 
    2: 'Nausea', 
    3: 'Pain', 
    4: 'Headache', 
    5: 'Migrane', 
    6: 'Flu', 
    7: 'Constipation', 
    8: 'Diarrhea', 
    9: 'Bloating', 
}

for key in symptoms:
    random.choice(list(symptoms.values()))

    symptom = model.Symptom(symptom=symptom)
    model.db.session.add(symptom)
    model.db.session.commit()

