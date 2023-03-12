from tinydb import TinyDB, where


class TinyDBConnAdapter:
    def __init__(self, url_db) -> None:
        self.db = TinyDB(url_db)

    def insert(self, celebration: dict):
        self.db.insert(celebration)

    def get(self, id: str) -> dict:
        celebration_result = self.db.get(where("id") == id)
        return celebration_result

    def delete(self, id: str):
        self.db.remove(where("id") == id)
