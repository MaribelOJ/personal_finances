from typing import Annotated
from pydantic import BaseModel
from pydantic import BaseModel


class RoleBase(BaseModel):
    rol_name: str

class RoleCreate(RoleBase):
    pass

