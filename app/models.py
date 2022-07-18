from email.policy import default
from lib2to3.pytree import Base
import string
import types
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from database import Base
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Blog(Base):
    __tablename__ = "bossss"
    id = Column(String, primary_key=True, default=generate_uuid)
    types = Column(String)
    grid_file = Column(String)
    pole_file = Column(String)
    critical_distances = Column(String)