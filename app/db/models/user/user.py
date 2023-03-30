from datetime import datetime
from typing import Optional, Union
from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    id: Union[UUID,int]
    name: str
    note: Optional[str]
    active: bool
    created_date: datetime = datetime.now()

    
