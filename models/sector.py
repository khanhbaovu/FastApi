from pydantic import BaseModel
from typing import Optional

class Sector(BaseModel):
    id : Optional[str] = None
    name : str
    field : Optional[str] = None
