from src.domain.entities.celebration_entity import CelebrationEntity


class CelebrationRepositoryInterface:
    def create(self, celebration: CelebrationEntity):
        ...
