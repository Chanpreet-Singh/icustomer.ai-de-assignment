import string
import random
import secrets
import datetime

def get_unique_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(secrets.choice(characters) for x in range(length))
    return random_string

def get_random_timestamp(start_date, end_date):
    random_timestamp = random.uniform(start_date.timestamp(), end_date.timestamp())
    return random_timestamp

def get_random_choice_from_list(list_of_choices):
    return random.choice(list_of_choices)