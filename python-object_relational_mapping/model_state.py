"""
    A python file that contains the class definition of a State and an instance Base = declarative_base():
    """
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state in the states table.
    """

    tablename = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    """
    Unique identifier for the state.
    Type: Integer
    Constraints: Primary key, not null.
    """

    name = Column(String(128), nullable=False)
    """
    Name of the state.
    Type: String
    Constraints: Maximum length of 128 characters, not null.
    """