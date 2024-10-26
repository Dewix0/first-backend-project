
from pydantic import BaseModel, ConfigDict
from typing import Optional


class STaskAdd(BaseModel):
    name:str
    description: Optional[str]=None
    
class STask(STaskAdd):
    id:int
    
    model_config = ConfigDict(from_attributes=True)
    
class STaskId(BaseModel):
    ok: bool = True
    task_id : int
        