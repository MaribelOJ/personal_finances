from pickle import BININT #representa un marcador interno para serializar enteros grandes de forma eficiente
from sqlalchemy import SMALLINT, Column, String, Boolean
from models.base_class import Base #clase de la que se hereda
from datetime import datetime

class Category(Base):
    __tablename__ = 'category'
    category_id = Column(SMALLINT(3),autoincrement=True , primary_key=True)
    category_name = Column(String(50))
    category_description = Column(String(120))
    category_status = Column(Boolean(1), default=True)
    