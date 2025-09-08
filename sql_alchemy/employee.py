
from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,Session
from sqlalchemy import Text,Boolean

from engine import engine

class Base(DeclarativeBase):
    pass

class Employee(Base):

    __tablename__="employee"

    #columns
    #colums static property 
    id:Mapped[int]=mapped_column(primary_key=True,autoincrement=True)
    name:Mapped[str]=mapped_column(Text,nullable=False)
    email:Mapped[str]=mapped_column(Text,nullable=False,unique=True)

#if table does not exit it will create it
# Base.metadata.create_all(engine)

with Session(engine) as session:
    
    name="Ndovu3"
    email="ndovu3@gmail.com"

    emp=Employee(name=name,email=email)
    session.add(emp)
    session.commit()
