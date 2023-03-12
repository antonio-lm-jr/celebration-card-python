class DeleteCelebrationUseCase:
    def __init__(self, repository):
        self.repository = repository

    def delete_celebration(self, id: str) -> None:
        self.repository.delete(id)
