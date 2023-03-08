from src.domain.exceptions.base_domain import BaseDomainException


class ToException(BaseDomainException):
    def __init__(self, code, message):
        super().__init__(code, message)
