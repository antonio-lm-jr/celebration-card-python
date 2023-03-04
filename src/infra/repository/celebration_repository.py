from src.domain.entities.celebration_entity import CelebrationEntity
from src.infra.repository.helpers.converter import db_to_entity, entity_to_db


class CelebrationRepository:
    def __init__(self, conn):
        self.conn = conn

    def create(self, celebration: CelebrationEntity):
        parsed = entity_to_db(celebration)
        self.conn.insert(parsed)

    def get(self, id: str):
        celebration_result = self.conn.get(id)
        parsed = db_to_entity(celebration_result)
        return parsed
