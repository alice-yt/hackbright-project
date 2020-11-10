"""Script to seed database."""

import os
import json
from random import random
from datetime import datetime
from faker import Faker

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

Faker.seed(0)
for user in range(10):
    fake.name()
    fake.email(domain=None)
    fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True)

    for user_entry in range(250):
        random_sleeptime = date_time_between_dates(datetime_start=2019-01-01, datetime_end=2019-12-31, tzinfo=None)
        random_hours_of_sleep = random.randint(4, 13)
        random_waketime = random_sleeptime + random_hours_of_sleep
    
    for sleep_quality in range(250):
        random_sleep_quality = random.randint(0, 5)
    
    for stress_level in range(250):
        random_stress_level = random.randint(0, 5)

    for energy_level in range(250):
        random_stress_level = random.randint(0, 5)
    
    for productivity_level in range(250):
        random_stress_level = random.randint(0, 5)

    for exercise_level in range(250):
        random_stress_level = random.randint(0, 5)
    
    for alcoholic_units in range(250):
        list_of_alcoholic_units = ['0', '1', '2', '3', '4', '5+']
        random.choice(list_of_alcoholic_units)

    for moods in range(250):
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
            11: 'Add another',
        }
    random.choice(list(moods.values()))

    for medications in range(250):
    medications = {
        1: 'None', 
        2: 'Add medication and dosage',
    }
    random.choice(list(medications.values()))

    for symptoms in range(250):
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
            10: 'Add another',
        }
        random.choice(list(symptoms.values()))


# Load sleep data from JSON file
# with open('data/sleepdata.json') as f:
#     sleep_data = json.loads(f.read())

# Create sleep data, store them in list so we can use them
# to create fake sleep entries
# sleepdata_in_db = []
# for user_entry in sleep_data:    
#     sleep_quality, stress_level, energy_level, productivity_level, exercise_level, alcoholic_units = (user_entry['sleep_quality'], 
#                                                                                                       user_entry['stress_level'], 
#                                                                                                       user_entry['energy_level'], 
#                                                                                                       user_entry['productivity_level'], 
#                                                                                                       user_entry['exercise_level'], 
#                                                                                                       user_entry['alcoholic_units'])
#     sleeptime = datetime.strptime(user_entry['sleeptime'], '%c') 
#     waketime = datetime.strptime(user_entry['waketime'], '%c')  

#     db_user_entry = crud.create_user_entry(datetime_of_input, 
#                                            datetime_of_entry, 
#                                            sleeptime, 
#                                            waketime, 
#                                            sleep_quality, 
#                                            stress_level, 
#                                            energy_level, 
#                                            productivity_level, 
#                                            exercise_level, 
#                                            alcoholic_units)

#     sleepdata_in_db.append(db_user_entry)

