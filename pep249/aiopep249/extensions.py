"""
Async implementations of optional extensions to the DB-API 2.0, as
outlined in PEP 249.

https://www.python.org/dev/peps/pep-0249/#optional-db-api-extensions

"""
from typing import Optional, Iterator
from .types import ResultRow
# pylint: disable=unused-import
from ..extensions import ConnectionErrorsMixin, CursorConnectionMixin


class IterableAsyncCursorMixin:
    """
    An naive implementation of an optional extension to PEP 249 which
    turns the cursor into an asynchronous iterator/iterable.

    This enables code like:

    ```python
    >>> async def async_execute(cursor: AsyncCursor):
    ...     cursor.execute(SQL_QUERY)
    ...     # An alternative to cursor.fetchone()
    ...     value = await cursor.__anext__()
    ...     # Iterate over the values
    ...     async for value in cursor:
    ...         do_thing_with(value)
    ```
    """

    async def __anext__(self) -> Optional[ResultRow]:
        return await self.fetchone()

    async def __aiter__(self) -> Iterator[ResultRow]:
        while True:
            next_item = await self.__anext__()
            if next_item is None:
                return
            yield next_item
