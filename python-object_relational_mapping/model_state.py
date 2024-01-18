# A python file that contains the class definition of a State and an instance Base = declarative_base():
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class states
class State(Base):
    # table name
    tablename = 'states'
# id column name
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)