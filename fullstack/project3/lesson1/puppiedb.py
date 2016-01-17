from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class Shelter(Base):


    __tablename__ = 'shelter'

    name = Column(String(80), nullable=False)
    address = Column(String(80))
    city = Column(String(80))
    state = Column(String(80))
    zipCode = Column(Integer(5))
    website = Column(String(80))
    id = Column(Integer, primary_key=True)


class Puppy(Base):

    
    __tablename__ = 'name'

    name = Column(String(80), nullable=False)
    dob = Column(String(9))
    gender = Column(String(2))
    weight = Column(Integer(3))
    shelter_id = Column(Integer, ForeignKey=('Shelter.id'))
