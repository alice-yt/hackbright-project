from random import choice, randint
from datetime import datetime

from faker import Faker
fake = Faker()
fake.random

for n in range(10):
    print(fake.name())
    print(fake.email(domain=None))
    print(fake.password(length=10, special_chars=True, digits=True, upper_case=True, lower_case=True))

    for _ in range(10):
        print(fake.)


