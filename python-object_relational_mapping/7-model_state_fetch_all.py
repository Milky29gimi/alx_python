# All states via SQLAlchemy

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

# Get MySQL username, password, and database name from command-line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Define the MySQL connection URL
connection_url = f'mysql://{username}:{password}@localhost:3306/{database}'

# Create the SQLAlchemy engine
engine = create_engine(connection_url)

# Bind the engine to the Base class
Base.metadata.bind = engine

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Retrieve all State objects and sort them by states.id in ascending order
states = session.query(State).order_by(State.id).all()

# Display the results
for state in states:
    print(f"{state.id}: {state.name}")

# Close the session
session.close()

# Retrieve all State objects and sort them by states.id in ascending order
states = session.query(State).order_by(State.id).all()

# Display the results
for state in states:
    print(f"{state.id}: {state.name}")

# Close the session
session.close()