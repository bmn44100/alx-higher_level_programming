#!/usr/bin/python3
"""
script that changes the name of a State object from the
database hbtn_0e_6_usa using the module SQLAlchemy
"""


if __name__ == "__main__":
    from sys import argv
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state_change = session.query(State).filter(State.id == 2).first()
    state_change.name = "New Mexico"
    session.commit()
    session.close()
