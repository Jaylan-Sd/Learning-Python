from app import Base

from sqlalchemy import Column,Integer,String

class Student(Base):

    __tablename__ = "student"\

    id = Column(BigInt,primary_key = True, autoincrement = True)
    name = Column(String,nullable = False)
    email = Column(String,nullable = False, unique = True)
    admission_no = Column(BigInt,nullable = False, unique = True)

    
