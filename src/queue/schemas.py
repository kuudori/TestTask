import datetime
from typing import Optional

from pydantic import BaseModel, Field


class QueueStatus(BaseModel):
    s_name: str = Field(min_length=1, max_length=512)
    c_name: str = Field(min_length=1, max_length=512)
    c_id: str = Field(min_length=1, max_length=32)
    a_type: str = Field(min_length=1, max_length=128)
    direction: str = Field(min_length=1, max_length=32)
    activation: str = Field(min_length=1, max_length=32)
    c_state: str = Field(min_length=1, max_length=32)
    control: str = Field(min_length=1, max_length=32)


class QueueStatusResponse(BaseModel):
    id: int
    s_name: str
    c_name: str
    c_id: str
    a_type: str
    direction: str
    activation: str
    c_state: str
    control: str
    created_at: Optional[datetime.datetime]

    class Config:
        orm_mode = True
