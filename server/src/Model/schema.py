from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# initilizer for inheritance
Base = declarative_base()


# user registration
class Users(Base):

	__tablename__ = "users"
	# columns
	id = Column('uid', Integer, primary_key=True, autoincrement=True)
	name = Column('name', String)
	email = Column('email', String, unique=True)
	password = Column('password', String)


# custom playlist
class Playlists(Base):

	__tablename__ = "playlists"
	# columns
	id = Column(Integer, primary_key=True)
	owner = Column(String, unique=True)
	song_name = Column(String)
	genre = Column(String)



# people a user follows
class Follows(Base):

	__tablename__ = "follows"
	# columns
	id = Column(Integer, primary_key=True)
	name = Column(String)


