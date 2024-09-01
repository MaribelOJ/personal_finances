from typing import Optional
from pydantic import BaseModel
from pydantic import BaseModel, StringConstraints

class CategoryBase(BaseModel):
    category_id: Optional[int] = None
    category_name: str
    category_description: str
    category_status: bool = True
    
class CategoryResponse(CategoryBase):
    pass