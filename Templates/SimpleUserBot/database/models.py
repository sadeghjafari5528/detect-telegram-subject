from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.types import Date
from database.database import Base

association_table = Table('association', Base.metadata,
                          Column('chats_id', Integer, ForeignKey('chats.id')),
                          Column('topics_id', Integer, ForeignKey('topics.id'))
                          )


class Chat(Base):
    __tablename__ = 'chats'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    tID = Column(Integer, unique=True)
    topics = relationship("Book", secondary=association_table,
                         back_populates="chats")

    def __repr__(self):
        return "<Chat(name='%s', tID='%s')>" % (
            self.name, self.tID)


class Topic(Base):
    __tablename__ = 'topics'

    id = Column(Integer, primary_key=True)
    text = Column(String)

    chats = relationship("User", secondary=association_table,
                         back_populates="topics")

    def __repr__(self):
        return "<Topic(text='%s')>" % (self.text)

