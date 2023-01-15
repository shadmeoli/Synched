from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


# initilizer
Base = declarative_base()


# user registration
class Users(Base):

	__tablename__ = "users"
	# columns
	id = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String)
	email = Column(String, unique=True)


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


