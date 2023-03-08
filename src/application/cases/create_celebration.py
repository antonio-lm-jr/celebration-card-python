from datetime import datetime
from uuid import uuid4

from src.application.dtos.create_celebration_dto import CreateCelebrationDTO
from src.domain.entities.celebration_entity import CelebrationEntity


class CreateCelebrationUseCase:
    def __init__(self, repository):
        self.repository = repository

    def create_celebration(
        self, dto: CreateCelebrationDTO
    ) -> CelebrationEntity:
        celebration = CelebrationEntity(
            id=str(uuid4()),
            of=dto.of,
            description=dto.description,
            to=dto.to,
            created_at=datetime.now(),
            updated_at=datetime.now(),
        )

        celebration.validate()

        self.repository.create(celebration)

        return celebration
