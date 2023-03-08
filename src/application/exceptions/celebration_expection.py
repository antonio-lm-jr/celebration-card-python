from .base import BaseException


class CelebrationNotFoundException(BaseException):
    def __init__(self, message: str):
        super().__init__(status_code="not_found", message=message)
