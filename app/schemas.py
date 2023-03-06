from pydantic import BaseModel 
from typing import Optional

class Opening(BaseModel):
    moves: str
    name: str
    ecocode: str
    description: Optional[str] = None
        
