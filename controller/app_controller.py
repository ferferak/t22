from database.setup import get_session
from database.financial_record import FinancialRecord
from validation.validators import validate_person, validate_type, validate_amount, validate_datetime

class AppController:
    def __init__(self):
        self.session = get_session()

    def add_record(self, person, record_type, amount, date, time):
        try:
            validate_person(person)
            validate_type(record_type)
            validate_amount(amount)
            validate_datetime(date, time)

            record = FinancialRecord(person=person, record_type=record_type, amount=amount, date=date, time=time)
            self.session.add(record)
            self.session.commit()
            return record
        except Exception as e:
            print(f"Error: {e}")
            self.session.rollback()
