"""
from datetime import datetime
from uuid import uuid4

from pydantic import UUID4, BaseModel, Field


class CelebrationEntity(BaseModel):
    id: UUID4 = Field(default_factory=uuid4)
    of: str = Field(..., min_length=3, max_length=100)
    to: str = Field(..., min_length=3, max_length=100)
    description: str = Field(..., min_length=1, max_length=400)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime = Field(default_factory=datetime.now)
"""

from datetime import datetime

from src.domain.exceptions.description_exception import DescriptionException
from src.domain.exceptions.of_exception import OfException
from src.domain.exceptions.to_exception import ToException


class CelebrationEntity:
    def __init__(
        self,
        id: str,
        of: str,
        to: str,
        description: str,
        created_at: datetime,
        updated_at: datetime,
    ) -> None:
        self.id = id
        self.of = of
        self.to = to
        self.description = description
        self.created_at = created_at
        self.updated_at = updated_at

    def validate(self):
        if len(self.of) < 3:
            raise OfException("of_min_length", "Needs at least 3 chars")

        if len(self.of) > 100:
            raise OfException("of_max_length", "Must be less than 100 chars")

        if len(self.to) < 3:
            raise ToException("to_min_length", "Needs at least 3 chars")

        if len(self.to) > 100:
            raise ToException("to_max_length", "Must be less than 100 chars")

        if len(self.description) > 400:
            raise DescriptionException(
                "description_max_length", "Must be less than 400 chars"
            )
