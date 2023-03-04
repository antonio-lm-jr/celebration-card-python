"""
from typing import Protocol

from src.application.dtos.create_celebration_dto import CreateCelebrationDTO
from src.domain.entities.celebration_entity import CelebrationEntity


class CreateCelebrationUseCaseInterface(Protocol):
    def create_celebration(
        self,
        dto: CreateCelebrationDTO,
    ) -> CelebrationEntity:
        ...
"""
