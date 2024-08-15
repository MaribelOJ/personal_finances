from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from core.security import get_hashed_password
from core.utils import generate_user_id
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from appv1.schemas.role import RoleBase

def create_role_sql(db: Session, role: RoleBase):
    sql_query = text(
        "INSERT INTO roles (rol_name) "
        "VALUES (:name)"
    )
    db.execute(sql_query, {"name":role.rol_name})
    db.commit()
    return True  

# Consultar rol por nombre
def get_role_by_name(db: Session, r_name: str):

    try:
        sql = text("SELECT * FROM roles WHERE rol_name =:name")
        result = db.execute(sql, {"name":r_name}).fetchone()
        return result

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al buscar rol por nombre: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar usuario")
    
#Consultar todos los roles
def get_all_roles(db: Session):
    try:
        sql = text("SELECT * FROM roles")
        result = db.execute(sql).fetchall()
        return result

    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al buscar roles: {e}")
        raise HTTPException(status_code=500, detail="Error al buscar roles")