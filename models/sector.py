from pydantic import BaseModel
from typing import Optional

class Sector(BaseModel):
    id : Optional[str] = None
    name : Optional[str] = None
    field : Optional[str] = None
