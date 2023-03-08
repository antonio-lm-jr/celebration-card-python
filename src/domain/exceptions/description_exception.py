from src.domain.exceptions.base_domain import BaseDomainException


class DescriptionException(BaseDomainException):
    def __init__(self, status_code, message):
        super().__init__(status_code, message)
