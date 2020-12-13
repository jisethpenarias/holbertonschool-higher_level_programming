#!/usr/bin/python3
"""
adds the State object “Louisiana” to the database
"""

from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    # create a new objec
    add_state = State(name="Louisiana")
    # add a new object
    session.add(add_state)
    # commits (persists) those changes to the database.
    session.commit()

    print(session.query(State).filter_by(name="Louisiana").first().id)
    session.close()
