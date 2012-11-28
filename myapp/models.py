from sqlalchemy import (
    Column,
    Integer,
    Text,
    )
from sqlalchemy import Table, Unicode
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relation
from sqlalchemy.orm import backref


from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    value = Column(Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value

Base.query = DBSession.query_property()

movie_genre_table = Table('movie_genre', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True),
    Column('genre_id', Integer, ForeignKey('genres.id',
        onupdate="CASCADE", ondelete="CASCADE"), primary_key=True)
)

class Movie(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(Unicode(255))
    director = Column(Unicode(255))

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255))
    movies = relation('Movie', secondary=movie_genre_table, backref='genres')
    def __unicode__(self):
        return unicode(self.name)

class Cast(Base):
    __tablename__ = 'casts'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey(Movie.id))
    movie = relation(Movie, backref=backref('cast'))
    character = Column(Unicode(255))
    actor = Column(Unicode(255))
