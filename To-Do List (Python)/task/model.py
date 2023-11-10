from datetime import datetime
from sqlalchemy import Column, Date, String, Integer
from sqlalchemy.orm import validates
from base import Base

class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())

    #def __repr__(self):
    #    return self.task
