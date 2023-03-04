from src.application.exceptions.celebration_expection import (
    CelebrationNotFoundException,
)
from src.domain.entities.celebration_entity import CelebrationEntity


class GetCelebrationUseCase:
    def __init__(self, repository):
        self.repository = repository

    def get_celebration(self, id: str) -> CelebrationEntity:
        try:
            celebration_result = self.repository.get(id)
        except:
            raise CelebrationNotFoundException("Celebration not found")

        return celebration_result
