from src.domain.entities.celebration_entity import CelebrationEntity


class ConnInterface:
    def insert(self, celebration: CelebrationEntity):
        ...

    def get(self, id: str):
        ...
