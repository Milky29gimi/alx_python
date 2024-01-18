# All states via SQLAlchemy

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if name == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: python script.py [mysql username] [mysql password] [database name]")
        sys.exit(1)

    # Get MySQL credentials from command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create engine and session
    engine = create_engine(f"mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}")
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states and sort by states.id in ascending order
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()