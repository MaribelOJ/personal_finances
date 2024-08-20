from typing import List
from fastapi import APIRouter, Depends, HTTPException
from appv1.crud.categories import create_category_sql,get_category_by_name,get_all_categories
from db.database import get_db
from sqlalchemy.orm import Session
from appv1.schemas.category import CategoryBase,CategoryResponse
from sqlalchemy import text

router = APIRouter()


@router.post("/createCategory")
async def insert_category(category: CategoryBase, db: Session = Depends(get_db)):
   
   respuesta = create_category_sql(db,category) 
   if respuesta:
      return {"mensaje":"categoria registrada con exito"}
      
@router.get("/get-category-by-name/", response_model=CategoryResponse)
async def read_category_by_name(name: str, db: Session = Depends(get_db)):
   category = get_category_by_name(db,name)
   if category is None:
      raise HTTPException(status_code=404, detail="Categoría no encontrado")
   return category

@router.get("/get-all-categories/", response_model=List[CategoryResponse])
async def read_all_categories(db: Session = Depends(get_db)):
   categories = get_all_categories(db)
   if len(categories)==0:
      raise HTTPException(status_code=404, detail="Ninguna categoria encontrada")
   return categories