from sqlalchemy import Column, String,Integer, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class subject(Base):
    __tablename__ = 'subject'
    id = Column(String(20), primary_key = True)
    sub = Column(String(30))
    time = Column(String(30))
    selected = Column(Integer)

class timetable(Base):
    __tablename__ = 'timetable'
    id = Column(String(20), primary_key=True)
    mon = Column(String(30))
    tue = Column(String(30))
    wed = Column(String(30))
    thu = Column(String(30))
    fri = Column(String(30))
    sat = Column(String(30))
    sun = Column(String(30))


engine = create_engine('mysql+mysqlconnector://root:1234a@localhost:3306/test')
DBSession = sessionmaker(bind=engine)
session = DBSession()

sub = session.query(subject).filter_by(id=1).one()
print(sub.time)
stu_time = session.query(timetable).filter_by(id=1).one()
print(stu_time.mon)
    # if not stu_time:
    #     session.query(timetable).filter_by(id=username).update({sub.time: sub.sub})
    #     session.commit()
    #     session.query(subject).filter_by(id=id).update({'selected': sub.selected + 1})
    #     session.commit()

session.close()