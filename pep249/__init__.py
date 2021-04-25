"""
An abstract implementation of the DB-2.0 API, as outlined in PEP-249.

This package contains abstract base classes which should help with
building conformant database APIs. Inheriting from these base classes
will enforce implementation of the relevant functions, and will implement
some functionality (e.g. context managers) for free.

"""
from .connection import Connection, TransactionlessConnection
from .cursor import Cursor, TransactionalCursor, CursorExecuteMixin, CursorFetchMixin
from .transactions import (
    TransactionFreeContextMixin,
    TransactionContextMixin,
    DummyTransactionContextMixin,
)
from .exceptions import *
from .extensions import *
from .types import *

__version__ = "0.0.1b3"

__all__ = [
    "Connection",
    "TransactionlessConnection",
    "Cursor",
    "TransactionalCursor",
    "CursorExecuteMixin",
    "CursorFetchMixin",
    "ConnectionErrorsMixin",
    "CursorConnectionMixin",
    "IterableCursorMixin",
    "TransactionFreeContextMixin",
    "TransactionContextMixin",
    "DummyTransactionContextMixin",
    "Error",
    "InterfaceError",
    "DatabaseError",
    "DataError",
    "OperationalError",
    "IntegrityError",
    "InternalError",
    "ProgrammingError",
    "NotSupportedError",
    "ConcreteErrorMixin",
    "SQLQuery",
    "QueryParameters",
    "ResultRow",
    "ResultSet",
    "ColumnDescription",
    "ProcName",
    "ProcArgs",
]
