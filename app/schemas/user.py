from datetime import datetime
from typing import Optional, Union
from uuid import UUID

from pydantic import BaseModel


class User(BaseModel):
    id: Union[UUID]
    name: str
    note: Optional[str]
    active: bool
    created_date: datetime

    def to_json(self):
        return {
            'name': self.name,
            'note': self.note,
            'active': self.active,
            'created_date': self.created_date,
        }
