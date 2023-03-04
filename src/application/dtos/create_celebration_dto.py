from pydantic import BaseModel


class CreateCelebrationDTO(BaseModel):
    of: str
    to: str
    description: str
