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

from ssvc._mixins import _Base, _Commented, _Keyed, _Namespaced, _Valued, _Versioned
from ssvc.namespaces import NameSpace

logger = logging.getLogger(__name__)


_RDP = {}
REGISTERED_DECISION_POINTS = []


def register(dp):
    """
    Register a decision point.
    """
    global _RDP

    key = (dp.namespace, dp.name, dp.key, dp.version)

    if key in _RDP:
        logger.warning(f"Duplicate decision point {key}")

    _RDP[key] = dp
    REGISTERED_DECISION_POINTS.append(dp)


def _reset_registered():
    """
    Reset the registered decision points.
    """
    global _RDP
    global REGISTERED_DECISION_POINTS

    _RDP = {}
    REGISTERED_DECISION_POINTS = []


class SsvcDecisionPointValue(_Base, _Keyed, _Commented, BaseModel):
    """
    Models a single value option for a decision point.
    """

    def __str__(self):
        return self.name


class SsvcDecisionPoint(
    _Valued, _Keyed, _Versioned, _Namespaced, _Base, _Commented, BaseModel
):
    """
    Models a single decision point as a list of values.
    """

    namespace: str = NameSpace.SSVC
    values: tuple[SsvcDecisionPointValue, ...]

    @model_validator(mode="after")
    def _prepend_value_keys(self):
        delim = ":"
        for value in self.values:
            if delim not in value.key:
                value.key = delim.join((self.namespace, self.key, value.key))
        return self

    @model_validator(mode="after")
    def _register(self):
        """
        Register the decision point.
        """
        register(self)
        return self


def main():
    opt_none = SsvcDecisionPointValue(
        name="None", key="N", description="No exploit available"
    )
    opt_poc = SsvcDecisionPointValue(
        name="PoC", key="P", description="Proof of concept exploit available"
    )
    opt_active = SsvcDecisionPointValue(
        name="Active", key="A", description="Active exploitation observed"
    )
    opts = [opt_none, opt_poc, opt_active]

    dp = SsvcDecisionPoint(
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
