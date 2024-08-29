from fastapi import HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from core.security import get_hashed_password
from core.utils import generate_user_id
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from appv1.schemas.user import UserCreate, UserUpdate
    
def get_permissions(db: Session, rol: str, module: str):
    try:
        sql = text("SELECT p_select, p_insert, p_update, p_delete FROM permissions WHERE rol_name = :rol AND module_name = :module")
        result = db.execute(sql, {"rol": rol, "module": module}).fetchone()
        return result
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al obtener permisos: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener permisos")

    
def get_all_permissions(db: Session, rol: str):
    try:
        sql = text("SELECT module_name, p_select FROM permissions WHERE rol_name = :rol")
        result = db.execute(sql, {"rol": rol}).mappings().all()
        return result
    except SQLAlchemyError as e:
        db.rollback()
        print(f"Error al obtener permisos: {e}")
        raise HTTPException(status_code=500, detail="Error al obtener permisos")
