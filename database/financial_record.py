from sqlalchemy import Column, Integer, String, Float, DateTime
from base import Base

class FinancialRecord(Base):
    __tablename__ = "financial_records"

    id = Column(Integer, primary_key=True)
    _person = Column("person", String(50), nullable=False)
    _record_type = Column("record_type", String(20), nullable=False)
    _amount = Column("amount", Float, nullable=False)
    _date = Column("date", DateTime, nullable=False)
    _time = Column("time", String(10), nullable=False)

    def __init__(self, person, record_type, amount, date, time):
        self.person = person
        self.record_type = record_type
        self.amount = amount
        self.date = date
        self.time = time


    @property
    def person(self):
        return self._person

    @person.setter
    def person(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._person = value
        else:
            raise ValueError("Person must be a non-empty string")


    @property
    def record_type(self):
        return self._record_type

    @record_type.setter
    def record_type(self, value):
        if value in ["Income", "Expense"]:
            self._record_type = value
        else:
            raise ValueError("Record type must be 'Income' or 'Expense'")


    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._amount = value
        else:
            raise ValueError("Amount must be a positive number")


    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, DateTime):
            self._date = value
        else:
            raise ValueError("Date must be a datetime object")


    @property
    def time(self):
        return self._time

    @time.setter
    def time(self, value):
        if isinstance(value, str) and len(value) == 5 and value[2] == ":":
            self._time = value
        else:
            raise ValueError("Time must be in the format 'HH:MM'")
