from typing import Any #permite recibir cualquier tipo de dato

from sqlalchemy.ext.declarative import as_declarative #convierte una clase en una clase base declarativa de SQLAlchemy.Es decir, otras clases pueden heredar de Base para convertirse en modelos de SQLAlchemy.
from sqlalchemy.ext.declarative import declared_attr #permite definir atributos en una clase que son evaluados en el momento en que la clase es declarada.

@as_declarative()
class Base:
    id: Any
    __name__: str

    # to generate tablename from classname
    @declared_attr 
    def __tablename__(cls) -> str: #este método toma cls (la clase que hereda de Base) como parámetro y retorna el nombre de esa clase en minuscula  como nombre de la la tabla
        return cls.__name__.lower()
