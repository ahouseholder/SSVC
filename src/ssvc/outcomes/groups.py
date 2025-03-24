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

from ssvc.decision_points.base import (
    DecisionPoint,
    DecisionPointValue as DecisionPointValue,
)
from ssvc.decision_points.helpers import print_versions_and_diffs

# Note: Outcome Groups must be defined in ascending order.


THE_PARANOIDS = DecisionPoint(
    name="theParanoids",
    key="PARANOIDS",
    description="PrioritizedRiskRemediation outcome group based on TheParanoids.",
    namespace="x_community",
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
    print_versions_and_diffs(
        [
            THE_PARANOIDS,
        ]
    )


if __name__ == "__main__":
    main()
