from typing import Annotated, Optional
from pydantic import BaseModel
from datetime import datetime
from pydantic import BaseModel, EmailStr, StringConstraints

class CategoryBase(BaseModel):
    category_id: Optional[int] = None
    category_name: Annotated[str,StringConstraints(max_length=80)]
    category_description: Annotated[str,StringConstraints(max_length=150)]
    category_status: bool = True
    
class CategoryResponse(CategoryBase):
    pass