#!/usr/bin/env python

"""
Defines the formatting for SSVC Decision Points.
"""
#  Copyright (c) 2023-2025 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University

import logging

from pydantic import BaseModel, model_validator

from ssvc._mixins import (
    _Base,
    _Commented,
    _Keyed,
    _Namespaced,
    _SchemaVersioned,
    _Valued,
    _Versioned,
)

logger = logging.getLogger(__name__)


_DECISION_POINT_REGISTRY = {}

REGISTERED_DECISION_POINTS = []

FIELD_DELIMITER = ":"

_VALUES_REGISTRY = {}


def register(dp):
    """
    Register a decision point.
    """
    global _DECISION_POINT_REGISTRY

    key = dp.str

    for value_str, value_summary in dp.value_summaries_dict.items():
        if value_str in _VALUES_REGISTRY:
            logger.warning(f"Duplicate value summary {value_str}")

        _VALUES_REGISTRY[value_str] = value_summary

    if key in _DECISION_POINT_REGISTRY:
        logger.warning(f"Duplicate decision point {key}")

    _DECISION_POINT_REGISTRY[key] = dp
    REGISTERED_DECISION_POINTS.append(dp)


def _reset_registered():
    """
    Reset the registered decision points.
    """
    global _DECISION_POINT_REGISTRY
    global REGISTERED_DECISION_POINTS

    global _VALUES_REGISTRY

    _DECISION_POINT_REGISTRY = {}
    _VALUES_REGISTRY = {}
    REGISTERED_DECISION_POINTS = []


class DecisionPointValue(_Base, _Keyed, _Commented, BaseModel):
    """
    Models a single value option for a decision point.

    Each value should have the following attributes:

    - name (str): A name
    - description (str): A description
    - key (str): A key (a short, unique string) that can be used to identify the value in a shorthand way
    - _comment (str): An optional comment that will be included in the object.
    """

    def __str__(self):
        return self.name


class ValueSummary(_Versioned, _Keyed, _Namespaced, BaseModel):
    """
    A ValueSummary is a simple object that represents a single value for a decision point.
    It includes the parent decision point's key, version, namespace, and the value key.
    These can be used to reference a specific value in a decision point.
    """

    value: str

    def __str__(self):
        s = FIELD_DELIMITER.join([self.namespace, self.key, self.version, self.value])
        return s

    @property
    def str(self):
        """
        Return the ValueSummary as a string.

        Returns:
            str: A string representation of the ValueSummary, in the format "namespace:key:version:value".

        """
        return self.__str__()


class DecisionPoint(
    _Valued, _Keyed, _SchemaVersioned, _Namespaced, _Base, _Commented, BaseModel
):
    """
    Models a single decision point as a list of values.

    Decision points should have the following attributes:

    - name (str): The name of the decision point
    - description (str): A description of the decision point
    - version (str): A semantic version string for the decision point
    - namespace (str): The namespace (a short, unique string): For example, "ssvc" or "cvss" to indicate the source of the decision point
    - key (str): A key (a short, unique string within the namespace) that can be used to identify the decision point in a shorthand way
    - values (tuple): A tuple of DecisionPointValue objects
    """

    values: tuple[DecisionPointValue, ...]

    def __str__(self):
        return FIELD_DELIMITER.join([self.namespace, self.key, self.version])

    @property
    def str(self) -> str:
        """
        Return the DecisionPoint represented as a short string.

        Returns:
            str: A string representation of the DecisionPoint, in the format "namespace:key:version".

        """
        return self.__str__()

    @model_validator(mode="after")
    def _register(self):
        """
        Register the decision point.
        """
        register(self)
        return self

    @property
    def value_summaries(self) -> list[ValueSummary]:
        """
        Return a list of value summaries.
        """
        return list(self.value_summaries_dict.values())

    @property
    def value_summaries_dict(self) -> dict[str, ValueSummary]:
        """
        Return a dictionary of value summaries keyed by the value key.
        """
        summaries = {}
        for value in self.values:
            summary = ValueSummary(
                key=self.key,
                version=self.version,
                namespace=self.namespace,
                value=value.key,
            )
            key = summary.str
            summaries[key] = summary

        return summaries

    @property
    def value_summaries_str(self):
        """
        Return a list of value summaries as strings.

        Returns:
            list: A list of strings, each representing a value summary in the format "namespace:key:version:value".

        """
        return list(self.value_summaries_dict.keys())


def main():
    opt_none = DecisionPointValue(
        name="None", key="N", description="No exploit available"
    )
    opt_poc = DecisionPointValue(
        name="PoC", key="P", description="Proof of concept exploit available"
    )
    opt_active = DecisionPointValue(
        name="Active", key="A", description="Active exploitation observed"
    )
    opts = [opt_none, opt_poc, opt_active]

    dp = DecisionPoint(
        _comment="This is an optional comment that will be included in the object.",
        values=opts,
        name="Exploitation",
        description="Is there an exploit available?",
        key="E",
        version="1.0.0",
    )

    print(dp.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
