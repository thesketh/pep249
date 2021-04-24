# An Abstract PEP-249 Implementation

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

This library contains an abstract implementation of [PEP-249](https://www.python.org/dev/peps/pep-0249)
which should make it easier to implement new databases in Python. These abstract
implementations are fully typed and the docstrings contain some (plagiarised) information
from the standard.

To demonstrate usage of this library, I'm putting together a wrapper on top of the 
excellent [DuckDB](https://duckdb.org/) library which adds full typing, context managers, 
distinct cursors, and easier to manage error types. [This wrapper is available here](https://github.com/thesketh/pyduckdb),
and is currently a bit rough around the edges.

Tested in Python 3.7, but not extensively. This library has not been condoned by the PEP
authors, who might hate it. 

## Why would I use this?

If you're looking to implement a DB-API 2.0 interface for a database, this library
should make it easier to do so. Inheriting from the appropriate abstract base classes
will ensure that classes can't be instantiated without fully implementing the required 
behaviour. Implementations will be fully typed, and some functionality is provided 
'for free' (e.g. context managers, cursor iteration).

## Installation

```bash
python3 -mpip install pep249abc
```

## Usage

This library's base classes define a protocol which requires implementation. If you
inherit from these classes, your editor should whinge at you until you've implemented
the rest of the specification (or if you deviate from it).

```python
import pep249


class Cursor(pep249.Cursor):
    ...


class Connection(pep249.Connection):
    ...

```

To use the mixin types (e.g. to implement extensions, or to implement `execute*()` for 
the `Connection`), use multiple inheritance:

```python
import pep249

class Connection(
   pep249.CursorExecuteMixin, pep249.ConcreteErrorMixin, pep249.Connection
):
    ...

```

## What has been implemented?

All of the core functionality, some 'common but slightly non-compliant' stuff (e.g. 
`TransactionalCursor`, a `Cursor` with transaction support), and some select extensions:

 - A mixin to [add the error types to the `Connection`](https://www.python.org/dev/peps/pep-0249/#connection-error).
 - A mixin to [add a reference to the `Connection` to the `Cursor`](https://www.python.org/dev/peps/pep-0249/#id28).
 - A mixin to [add support for next](https://www.python.org/dev/peps/pep-0249/#next) 
   and [iteration](https://www.python.org/dev/peps/pep-0249/#iter).

## What has not been implemented?

Most of the optional extensions.

 - [`Cursor.rownumber`](https://www.python.org/dev/peps/pep-0249/#rownumber).
 - [`Cursor.scroll()`](https://www.python.org/dev/peps/pep-0249/#scroll).
 - [`Cursor.messages`](https://www.python.org/dev/peps/pep-0249/#cursor-messages).
 - [`Connection.messages`](https://www.python.org/dev/peps/pep-0249/#connection-messages).
 - [`Cursor.lastrowid`](https://www.python.org/dev/peps/pep-0249/#lastrowid).
 - [`Cursor/Connection.errorhandler`](https://www.python.org/dev/peps/pep-0249/#optional-error-handling-extensions).
 - [Two phase commit extensions](https://www.python.org/dev/peps/pep-0249/#optional-two-phase-commit-extensions). 

Most of these are missing simply because I haven't encountered them in the wild and they
weren't supported by the reference implementation I had in mind. If you'd like to see
these implemented, please raise an issue! If you have examples of the features in use,
that would be helpful.

## What could be improved?

Probably a lot! In particular, I'm not happy with `Cursor.description` or the type 
constructors. The spec is quite opaque on these and I haven't done much research on how
these work or how they should tie in.

## What are the future plans?

Hopefully, an async implementation of these abstract classes, taking some inspiration 
from [aiosqlite](https://pypi.org/project/aiosqlite/).
