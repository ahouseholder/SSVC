#!/usr/bin/env python
#  Copyright (c) 2025 Carnegie Mellon University and Contributors.
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
"""
Provides a set of outcome groups for use in SSVC.
"""

from ssvc.decision_points.base import DecisionPointValue as DecisionPointValue
from ssvc.decision_points.ssvc_.base import SsvcDecisionPoint


# Note: Outcome Groups must be defined in ascending order.


MOSCOW = SsvcDecisionPoint(
    name="MoSCoW",
    key="MSCW",
    description="The MoSCoW (Must, Should, Could, Won't) outcome group.",
    version="1.0.0",
    values=(
        DecisionPointValue(name="Won't", key="W", description="Won't"),
        DecisionPointValue(name="Could", key="C", description="Could"),
        DecisionPointValue(name="Should", key="S", description="Should"),
        DecisionPointValue(name="Must", key="M", description="Must"),
    ),
)
"""
The MoSCoW outcome group.
"""

EISENHOWER = SsvcDecisionPoint(
    name="Do, Schedule, Delegate, Delete",
    key="EISENHOWER",
    description="The Eisenhower outcome group.",
    version="1.0.0",
    values=(
        DecisionPointValue(name="Delete", key="D", description="Delete"),
        DecisionPointValue(name="Delegate", key="G", description="Delegate"),
        DecisionPointValue(name="Schedule", key="S", description="Schedule"),
        DecisionPointValue(name="Do", key="O", description="Do"),
    ),
)
"""
The Eisenhower outcome group.
"""


YES_NO = SsvcDecisionPoint(
    name="Yes, No",
    key="YES_NO",
    description="The Yes/No outcome group.",
    version="1.0.0",
    values=(
        DecisionPointValue(name="No", key="N", description="No"),
        DecisionPointValue(name="Yes", key="Y", description="Yes"),
    ),
)
"""
The Yes/No outcome group.
"""

VALUE_COMPLEXITY = SsvcDecisionPoint(
    name="Value, Complexity",
    key="VALUE_COMPLEXITY",
    description="The Value/Complexity outcome group.",
    version="1.0.0",
    values=(
        # drop, reconsider later, easy win, do first
        DecisionPointValue(name="Drop", key="D", description="Drop"),
        DecisionPointValue(
            name="Reconsider Later", key="R", description="Reconsider Later"
        ),
        DecisionPointValue(name="Easy Win", key="E", description="Easy Win"),
        DecisionPointValue(name="Do First", key="F", description="Do First"),
    ),
)
"""
The Value/Complexity outcome group.
"""

THE_PARANOIDS = SsvcDecisionPoint(
    name="theParanoids",
    key="PARANOIDS",
    description="PrioritizedRiskRemediation outcome group based on TheParanoids.",
    version="1.0.0",
    values=(
        DecisionPointValue(name="Track 5", key="5", description="Track"),
        DecisionPointValue(
            name="Track Closely 4", key="4", description="Track Closely"
        ),
        DecisionPointValue(name="Attend 3", key="3", description="Attend"),
        DecisionPointValue(name="Attend 2", key="2", description="Attend"),
        DecisionPointValue(name="Act 1", key="1", description="Act"),
        DecisionPointValue(name="Act ASAP 0", key="0", description="Act ASAP"),
    ),
)
"""
Outcome group based on TheParanoids' PrioritizedRiskRemediation.
Their model is a 6-point scale, with 0 being the most urgent and 5 being the least.
See https://github.com/theparanoids/PrioritizedRiskRemediation
"""


def main():
    pass


if __name__ == "__main__":
    main()
