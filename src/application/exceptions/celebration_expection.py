from .base import BaseException


class CelebrationNotFoundException(BaseException):
    def __init__(self, message=None):
        super().__init__(message)
