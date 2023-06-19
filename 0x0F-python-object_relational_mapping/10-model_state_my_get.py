#!/usr/bin/python3
"""
script that prints the State object with the name
passed as argument from the database hbtn_0e_6_usa
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
    state_obj = session.query(State).filter(
            State.name == argv[4]).first()
    if state_obj:
        print(state_obj.id)
    else:
        print("Not found")
    session.close()
