from datetime import datetime
from uuid import uuid4

from pydantic import UUID4, BaseModel, Field


class CelebrationEntity(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    of: str = Field(..., min_length=3, max_length=100)
    to: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=1, max_length=400)
    created_at: datetime | None = Field(default_factory=datetime.now)
    updated_at: datetime | None = Field(default_factory=datetime.now)
