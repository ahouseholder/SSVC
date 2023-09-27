#!/usr/bin/env python
"""
file: _basics
author: adh
created_at: 9/20/23 4:51 PM
"""
from dataclasses import dataclass

from dataclasses_json import dataclass_json


def main():
    pass


if __name__ == "__main__":
    main()


@dataclass_json
@dataclass(kw_only=True)
class _Versioned:
    """
    Mixin class for versioned SSVC objects.
    """

    version: str = "0.0.0"


@dataclass_json
@dataclass(kw_only=True)
class _Namespaced:
    """
    Mixin class for namespaced SSVC objects.
    """

    namespace: str = "ssvc"


@dataclass_json
@dataclass(kw_only=True)
class _Base:
    """
    Base class for SSVC objects.
    """

    name: str
    description: str
    key: str