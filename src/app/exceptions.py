"""Custom infrastructure exceptions."""

from typing import Optional


class BaseCustomInfrastructureException(Exception):
    """Base class for all custom exceptions."""

    error_type: str
    status_code: int
    message: str


class CustomDBException(BaseCustomInfrastructureException):
    """Base class for all custom exception databases."""

    error_type: str
    status_code: int
    message: str


class RedisDBException(CustomDBException):
    """Redis working error."""

    error_type: str
    status_code: int
    message: str


class SQLRepositoryException(CustomDBException):
    """SQL repository working error."""

    error_type = "SQL_REPOSITORY_ERROR"
    status_code = 500

    def __init__(self, message: Optional[str] = None):
        self.message = message or self.__doc__
        super().__init__(self.message)


class SQLRepositoryHealthException(CustomDBException):
    """SQL repository connection error."""

    error_type = "SQL_REPOSITORY_ERROR"
    status_code = 500

    def __init__(self, message: Optional[str] = None):
        self.message = message or self.__doc__
        super().__init__(self.message)


class RedisCacheDBException(CustomDBException):
    """Cache operation failed."""

    error_type = "REDIS_ERROR"
    status_code = 202

    def __init__(self, message: Optional[str] = None):
        self.message = message or self.__doc__
        super().__init__(self.message)


class RedisHealthException(CustomDBException):
    """Redis connection error."""

    error_type = "REDIS_ERROR"
    status_code = 500

    def __init__(self, message: Optional[str] = None):
        self.message = message or self.__doc__
        super().__init__(self.message)


class TransactionException(CustomDBException):
    """Transaction error."""

    error_type = "TRANSACTION_ERROR"
    status_code = 500

    def __init__(self, message: Optional[str] = None):
        self.message = message or self.__doc__
        super().__init__(self.message)
