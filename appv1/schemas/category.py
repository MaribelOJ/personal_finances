from typing import Annotated
from pydantic import BaseModel
from datetime import datetime
from pydantic import BaseModel, EmailStr, StringConstraints

class CategoryBase(BaseModel):
    category_name: Annotated[str,StringConstraints(max_length=80)]
    category_description: Annotated[str,StringConstraints(max_length=150)]
    category_status: bool = True
    
class CategoryResponse(CategoryBase):
    category_id: int
