from sqlalchemy_utils import create_database, drop_database, database_exists
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from base import Base

connection_string = "mysql+pymysql://root:root123@localhost:3306/finance"

if database_exists(connection_string):
    drop_database(connection_string)

create_database(connection_string)

engine = create_engine(connection_string)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

def get_session():
    return Session()
