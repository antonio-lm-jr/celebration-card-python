from src.domain.exceptions.base_domain import BaseDomainException


class OfException(BaseDomainException):
    def __init__(self, code, message):
        super().__init__(code, message)
