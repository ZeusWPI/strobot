from sqlalchemy import create_engine, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = ""
Base = declarative_base()


class Email(Base):
    __tablename__ = 'email'
    id = Column(Integer, primary_key=True)
    subject = Column(String, nullable=True)
    to = Column(String)
    sender = Column(String)
    datetime = Column(DateTime)
    lastping = Column(DateTime)


engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

