from typing import List
from fastapi import APIRouter, Depends, HTTPException
from appv1.crud.roles import create_role_sql, get_role_by_name, get_all_roles
from db.database import get_db
from sqlalchemy.orm import Session
from appv1.schemas.role import RoleBase
from sqlalchemy import text

router = APIRouter()


@router.post("/createRole")
async def insert_user(user: RoleBase, db: Session = Depends(get_db)):
   
   respuesta = create_role_sql(db,user) 
   if respuesta:
    return {"mensaje":"Rol regustrado con exito"}
   
@router.get("/get-role-by-name/", response_model=RoleBase)
async def read_role_by_name(name: str, db: Session = Depends(get_db)):
   roles = get_role_by_name(db,name)
   if roles is None:
      raise HTTPException(status_code=404, detail="Rol no encontrado")
   return roles

@router.get("/get-all-roles/", response_model=List[RoleBase])
async def read_all_users(db: Session = Depends(get_db)):
   roles = get_all_roles(db)
   if len(roles)==0:
      raise HTTPException(status_code=404, detail="Ningún rol encontrado")
   return roles
