# using sqlalchemy `create_engine` to connect to the database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# schema objects 
from schema import Users, Playlists, Follows

Base = declarative_base()



# engine initilizer
engine = create_engine("sqlite:///synched.db")
Base.metadata.create_all(bind=engine)



# session initilizer
Session = sessionmaker(bind=engine)
session = Session()



# performing crud operation to the database
def new_user():

	new_user_registration = Users()

	try:
		session.add(new_user_registration)
		session.commit()

		# print(True)

	except Exception as e:
		print (e)


# new user
print(new_user("shad", "shadcodes@gmail.com","1234asdf"))