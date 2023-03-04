from src.application.dtos.create_celebration_dto import CreateCelebrationDTO
from src.domain.entities.celebration_entity import CelebrationEntity


class CreateCelebrationUseCase:
    def __init__(self, repository):
        self.repository = repository

    def create_celebration(self, dto: CreateCelebrationDTO) -> CelebrationEntity:
        celebration = CelebrationEntity(
            of=dto.of, description=dto.description, to=dto.to
        )

        self.repository.create(celebration)

        return celebration
