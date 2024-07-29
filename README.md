<h1 align="center">HyphernORM</h1>

> A simple and lightweight ORM for small python projects.

<div align="center">

![GitHub last commit](https://img.shields.io/github/last-commit/freitaseric/hyphern)
![Codecov](https://img.shields.io/codecov/c/github/freitaseric/hyphern)
![PyPI - Downloads](https://img.shields.io/pypi/dm/hyphern)

![PyPI - Python Version](https://img.shields.io/pypi/pyversions/hyphern)
![PyPI - Version](https://img.shields.io/pypi/v/hyphern)

</div>

## Table of Contents

1. [Installation](#installation)
2. [Minimal Usage](#minimal-usage)
3. [Authors](#authors)
4. [License](#license)

## Installation

Install from pip:

```shell
# When pip is installed
$ pip install hyphern

# When pip is not installed
$ python3 -m pip install hyphern
```

Install from source:

```shell
$ git clone https://github.com/freitaseric/hyphern.git --depth=1
$ pip install ./hyphern/
```

## Minimal Usage

Without model classes:

```python
import hyphern

db = hyphern.Database(file="test.db")

# using raw queries
db.query("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    );
""")
db.commit()

# using assisted query
db.execute(
    action=hyphern.QueryActions.INSERT,
    table="users",
    values={"username": "EricFreitas", "password": hyphern.passwd("my super secret password")}
)
```

With model classes:

```python
# models/user.py
from hyphern import Model, IntegerField, TextField, PasswordField


class User(Model):
    id = IntegerField(primary=True)
    username = TextField(not_null=True, unique=True)
    password = PasswordField(not_null=True, unique=True)
```

```python
# __init__.py
from models.user import User

User.sync(force=False)

User.create(username="Eric Freitas", password="my super secret password")  # Ok

User.create(username="Eric Freitas",
            password="my super secret password")  # Error: an entry with this "username" already exists!
```

## Authors

- [@freitaseric](https://github.com/freitaseric)

## License

This repository is [MIT Licensed](./README.md)