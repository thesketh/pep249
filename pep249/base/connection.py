"""
An abstract database connection implementation, conformant with PEP 249.

"""
# pylint: disable=bad-continuation
from abc import ABCMeta, abstractmethod
from typing import TYPE_CHECKING
from .transactions import TransactionContextMixin, DummyTransactionContextMixin

if TYPE_CHECKING:
    from .cursor import BaseCursor


class BaseConnection:  # pylint: disable=too-few-public-methods
    """A Connection without an associated context."""

    @abstractmethod
    def cursor(self) -> "BaseCursor":
        """Return a database cursor."""
        raise NotImplementedError


class Connection(TransactionContextMixin, BaseConnection, metaclass=ABCMeta):
    """A PEP 249 compliant Connection protocol."""


class TransactionlessConnection(
    DummyTransactionContextMixin, BaseConnection, metaclass=ABCMeta
):
    """
    A PEP 249 compliant Connection protocol for databases without
    transaction support.

    """
