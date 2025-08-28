#!/usr/bin/env python
"""
Models the AIVSS Data Poisoning decision point.
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

# Data Poisoning
#
# 0.0: System provably resistant to data poisoning, with formal guarantees on the integrity and security of the training data.
# 0.1-0.3: Strong data validation, anomaly detection, and provenance tracking mechanisms in place, making it very difficult to successfully poison the training data.
# 0.4-0.6: Some measures to mitigate data poisoning (e.g., outlier detection), but risks remain, and targeted poisoning attacks may still be possible.
# 0.7-1.0: High risk of data poisoning, with no or minimal measures to ensure the integrity and security of the training data.
# Examples:
# 0.0: Training data is stored on an immutable ledger with cryptographic verification of its integrity.
# 0.2: Robust data validation, anomaly detection, and provenance tracking mechanisms are used to prevent and detect data poisoning.
# 0.5: Basic outlier detection is used, but sophisticated poisoning attacks may still succeed.
# 0.8: Training data can be easily tampered with, and there are no mechanisms to detect poisoning.

PROVABLY_RESISTANT = DecisionPointValue(
    name="Provably Resistant",
    key="P",
    definition="System provably resistant to data poisoning, with formal guarantees on the integrity and security of the training data.",
)

STRONG_DEFENSES = DecisionPointValue(
    name="Strong Defenses",
    key="S",
    definition="Strong data validation, anomaly detection, and provenance tracking mechanisms in place, making it very difficult to successfully poison the training data.",
)

SOME_MITIGATION = DecisionPointValue(
    name="Some Mitigation",
    key="M",
    definition="Some measures to mitigate data poisoning, but risks remain, and targeted poisoning attacks may still be possible.",
)

HIGH_RISK = DecisionPointValue(
    name="High Risk",
    key="H",
    definition="High risk of data poisoning, with no or minimal measures to ensure the integrity and security of the training data.",
)

DATA_POISONING = AivssDecisionPoint(
    name="Data Poisoning",
    key="DPO",
    version="0.1.0",
    definition="Degree to which the system is resistant to data poisoning attacks and ensures the integrity of training data.",
    values=(PROVABLY_RESISTANT, STRONG_DEFENSES, SOME_MITIGATION, HIGH_RISK),
)

VERSIONS = [DATA_POISONING]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
