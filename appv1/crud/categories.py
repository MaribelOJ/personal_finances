# Crear un usuario

from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from core.security import get_hashed_password
from core.utils import generate_user_id
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from appv1.schemas.category import CategoryBase

def create_category_sql(db: Session, category: CategoryBase):
    try:
        sql_query = text(
        "INSERT INTO category(category_id, category_name, category_description, category_status) "
        "VALUES (:id, :name, :description, :status)"
        )
        params = {
            "id": generate_user_id(),
            "name": category.category_name,
            "description": category.category_description,
            "status": category.category_status,
        }
        db.execute(sql_query, params)
        db.commit()
        return True  # Retorna True si la inserción fue exitosa
    except IntegrityError as e:
        db.rollback()  # Revertir la transacción en caso de error de integridad (llave foránea)
        print(f"Error al crear usuario: {e}")
        if 'Duplicate entry' in str(e.orig):
            if 'PRIMARY' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El ID generado ya existe, vuelva a intentar")
            if 'for key \'mail\'' in str(e.orig):
                raise HTTPException(status_code=400, detail="Error. El email ya está registrado")
        else:
            raise HTTPException(status_code=400, detail="Error. No hay Integridad de datos al crear usuario")
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al crear usuario: {e}")
        raise HTTPException(status_code=500, detail="Error al crear usuario")


# Consultar categoría por nombre
def get_category_by_name(db: Session, c_name: str):

    try:
        sql = text("SELECT * FROM category WHERE category_name = :name")
        result = db.execute(sql, {"name":c_name}).fetchone()
        return result

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al buscar categoria por nombre: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar categoria")
    

#Consultar todas las categorías
def get_all_categories(db: Session):
    try:
        sql = text("SELECT * FROM category WHERE category_status = true")
        result = db.execute(sql).fetchall()
        return result

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al buscar categorías: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar categorías")