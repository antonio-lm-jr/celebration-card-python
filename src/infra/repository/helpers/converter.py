from src.domain.entities.celebration_entity import CelebrationEntity


def entity_to_db(celebration: CelebrationEntity) -> dict[str, any]:
    parser: dict[str, any] = {
        "id": str(celebration.id),
        "of": celebration.of,
        "to": celebration.to,
        "description": celebration.description,
        "created_at": celebration.created_at.isoformat(),
        "updated_at": celebration.updated_at.isoformat(),
    }

    return parser


def db_to_entity(celebration: dict[str, any]) -> CelebrationEntity:
    parser = CelebrationEntity(
        id=celebration.get("id"),
        of=celebration.get("of"),
        to=celebration.get("to"),
        description=celebration.get("description"),
        created_at=celebration.get("created_at"),
        updated_at=celebration.get("updated_at"),
    )

    return parser
