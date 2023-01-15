from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# initilizer
Base = declarative_base()


# user registration
class User(Base):

	__tablename__ = "users"
	# columns
	id = Column(Integer, primary_key=True)
	name = Column(String)
	email = Column(String, unique=True)


# custom playlist
class MyPlaylist(Base):

	__tablename__ = "users"
	# columns
	id = Column(Integer, primary_key=True)
	name = Column(String)
	email = Column(String, unique=True)