from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()
myFirstRestaurant = Restaurant(name = "Pizzza Paladin")
session.add(myFirstRestaurant)
session.commit()
session.query(Restaurant).all()
cheesepenis = MenuItem(name = "Penis Cheese", description = "Made with penis", course = "Entree", price = "cheap", restaurant = myFirstRestaurant)
session.add(cheesepenis)
session.commit()
session.query(MenuItem).all()
# mewEmployee = Employee(name = "Revolting Allen")
from employee import Base, Employee, Address
another_engine = create_engine('sqlite:///employeeData.db')
Base.metadata.bind = another_engine
DBSession2 = sessionmaker(bind = another_engine)
sesh2 = DBSession2()
myFirstEmployee = Employee(name = "Revolting Allen")
revoltingAddress = Address(street = "1 Prepuce Lane", zip = "00001", employee = myFirstEmployee
)
# session.add(myFirstEmployee)
sesh2.add(myFirstEmployee)
mySecondEmployee = Employee(name = "Revolting Allen")
revoltingAddress = Address(street = "1 Prepuce Lane", zip = "00001", employee = mySecondEmployee)
sesh2.add(mySecondEmployee)
sesh2.commit()
sesh2.query(Employee).all()
session.query(Restaurant).all()
