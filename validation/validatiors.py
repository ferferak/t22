import re
from datetime import datetime

def validate_person(name):
    if isinstance(name, str) and re.match(r"^[a-zA-Z\s]{3,50}$", name):
        return name
    raise ValueError("Invalid name!")

def validate_type(record_type):
    if record_type in ["income", "expense", "investment"]:
        return record_type
    raise ValueError("Invalid record type!")

def validate_amount(amount):
    if isinstance(amount, (int, float)) and amount > 0:
        return amount
    raise ValueError("Invalid amount!")

def validate_datetime(date, time):
    try:
        datetime.strptime(date, "%Y-%m-%d")
        datetime.strptime(time, "%H:%M")
        return date, time
    except ValueError:
        raise ValueError("Invalid date or time!")
