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

from ssvc.decision_points.helpers import print_versions_and_diffs
from ssvc.outcomes.x_community.paranoids import THE_PARANOIDS

# Note: Outcome Groups must be defined in ascending order.


def main():
    print_versions_and_diffs(
        [
            THE_PARANOIDS,
        ]
    )


if __name__ == "__main__":
    main()
