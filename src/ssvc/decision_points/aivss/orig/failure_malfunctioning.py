#!/usr/bin/env python
"""
Models the AIVSS Failure/Malfunctioning decision point.
"""

#  Copyright (c) 2025 Carnegie Mellon University.
#  NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
#  ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
#  CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND,
#  EITHER EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT
#  NOT LIMITED TO, WARRANTY OF FITNESS FOR PURPOSE OR
#  MERCHANTABILITY, EXCLUSIVITY, OR RESULTS OBTAINED FROM USE
#  OF THE MATERIAL. CARNEGIE MELLON UNIVERSITY DOES NOT MAKE
#  ANY WARRANTY OF ANY KIND WITH RESPECT TO FREEDOM FROM
#  PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#  Licensed under a MIT (SEI)-style license, please see LICENSE or contact
#  permission@sei.cmu.edu for full terms.
#  [DISTRIBUTION STATEMENT A] This material has been approved for
#  public release and unlimited distribution. Please see Copyright notice
#  for non-US Government use and distribution.
#  This Software includes and/or makes use of Third-Party Software each
#  subject to its own license.
#  DM24-0278

from ssvc.decision_points.aivss.base import AivssDecisionPoint
from ssvc.decision_points.base import DecisionPointValue
from ssvc.decision_points.helpers import print_versions_and_diffs

# Failure/Malfunctioning
#
# 0.0: System designed for high availability and fault tolerance, with formal verification of its reliability.
# 0.1-0.3: Robust error handling, monitoring, and redundancy mechanisms in place, significantly reducing the risk of failures or malfunctions.
# 0.4-0.6: Some measures to ensure reliability (e.g., basic error handling), but risks remain, and the system may experience downtime or produce incorrect outputs under certain conditions.
# 0.7-1.0: High risk of failures or malfunctions, with no or minimal measures to ensure the system's reliability.
# Examples:
# 0.0: System is designed with multiple layers of redundancy and failover mechanisms, and its reliability is formally verified.
# 0.2: System has robust error handling, monitoring, and self-healing capabilities.
# 0.5: System has basic error handling and logging, but may experience downtime due to unexpected errors.
# 0.8: System is prone to crashes or errors, and there are no mechanisms to ensure its continuous operation.

FORMALLY_VERIFIED = DecisionPointValue(
    name="Formally Verified",
    key="F",
    definition="System designed for high availability and fault tolerance, with formal verification of its reliability.",
)

ROBUST = DecisionPointValue(
    name="Robust",
    key="R",
    definition="Robust error handling, monitoring, and redundancy mechanisms in place, significantly reducing the risk of failures or malfunctions.",
)

BASIC_MEASURES = DecisionPointValue(
    name="Basic Measures",
    key="B",
    definition="Some measures to ensure reliability, but risks remain, and the system may experience downtime or produce incorrect outputs under certain conditions.",
)

HIGH_RISK = DecisionPointValue(
    name="High Risk",
    key="H",
    definition="High risk of failures or malfunctions, with no or minimal measures to ensure the system's reliability.",
)

FAILURE_MALFUNCTIONING = AivssDecisionPoint(
    name="Failure/Malfunctioning",
    key="FM",
    version="0.1.0",
    definition="Degree to which the system is designed to prevent, detect, and recover from failures or malfunctions.",
    values=(FORMALLY_VERIFIED, ROBUST, BASIC_MEASURES, HIGH_RISK),
)

VERSIONS = [FAILURE_MALFUNCTIONING]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
