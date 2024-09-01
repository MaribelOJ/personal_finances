from sqlalchemy import Column, Integer, String, Boolean
from models.base_class import Base #clase de la que se hereda

class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer,autoincrement=True , primary_key=True)
    category_name = Column(String(50))
    category_description = Column(String(120))
    category_status = Column(Boolean, default=True)
    