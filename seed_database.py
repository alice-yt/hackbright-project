"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime
from faker import Faker

import crud
import model
import server

os.system('dropdb sleepjournal')
os.system('createdb sleepjournal')

model.connect_to_db(server.app)
model.db.create_all()

for n in range(10):
    print(fake.name())
    print(fake.email(domain=None))
    print(fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))

    for _ in range(10):
        

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

medications = {
    1: 'None', 
    2: 'Add medication and dosage',
}

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

