from src.domain.entities.celebration_entity import CelebrationEntity


class CelebrationRepositoryInterface:
    def create(self, celebration: CelebrationEntity):
        ...

    def get(self, id: str):
        ...

    def delete(self, id: str):
        ...
