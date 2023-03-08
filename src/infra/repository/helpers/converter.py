from datetime import datetime
from typing import Any

from src.domain.entities.celebration_entity import CelebrationEntity


def entity_to_db(celebration: CelebrationEntity) -> dict[str, Any]:
    parser: dict[str, Any] = {
        "id": str(celebration.id),
        "of": celebration.of,
        "to": celebration.to,
        "description": celebration.description,
        "created_at": celebration.created_at.isoformat(),
        "updated_at": celebration.updated_at.isoformat(),
    }

    return parser


def db_to_entity(celebration: dict[str, Any]) -> CelebrationEntity:
    parser = CelebrationEntity(
        id=celebration["id"],
        of=celebration["of"],
        to=celebration["to"],
        description=celebration["description"],
        created_at=datetime.strptime(
            celebration["created_at"], "%Y-%m-%dT%H:%M:%S.%f"
        ),
        updated_at=datetime.strptime(
            celebration["updated_at"], "%Y-%m-%dT%H:%M:%S.%f"
        ),
    )

    return parser
