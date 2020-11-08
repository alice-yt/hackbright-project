"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system('dropdb sleepjournal')
os.system('createdb sleepjournal')

model.connect_to_db(server.app)
model.db.create_all()

# Load sleep data from JSON file
with open('data/sleepdata.json') as f:
    sleep_data = json.loads(f.read())

# Create sleep data, store them in list so we can use them
# to create fake sleep entries
sleepdata_in_db = []
for user_entry in sleep_data:    
    sleep_quality, stress_level, energy_level, productivity_level, exercise_level, alcoholic_units = (user_entry['sleep_quality'], 
                                                                                                      user_entry['stress_level'], 
                                                                                                      user_entry['energy_level'], 
                                                                                                      user_entry['productivity_level'], 
                                                                                                      user_entry['exercise_level'], 
                                                                                                      user_entry['alcoholic_units'])

    datetime_of_input = datetime.strptime(user_entry['datetime_of_input'], '%c')
    datetime_of_entry = datetime.strptime(user_entry['datetime_of_entry'], '%c')
    sleeptime = datetime.strptime(user_entry['sleeptime'], '%c') 
    waketime = datetime.strptime(user_entry['waketime'], '%c')  

    db_user_entry = crud.create_user_entry(datetime_of_input, 
                                           datetime_of_entry, 
                                           sleeptime, 
                                           waketime, 
                                           sleep_quality, 
                                           stress_level, 
                                           energy_level, 
                                           productivity_level, 
                                           exercise_level, 
                                           alcoholic_units)

    sleepdata_in_db.append(db_user_entry)