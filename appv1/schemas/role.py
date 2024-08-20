from typing import Annotated
from pydantic import BaseModel
from pydantic import BaseModel,StringConstraints


class RoleBase(BaseModel):
    rol_name: Annotated[str,StringConstraints(max_length=80)]


