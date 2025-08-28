#!/usr/bin/env python
"""
Models the AIVSS Denial of Service (DoS) decision point.
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

# Denial of Service (DoS)
#
# 0.0: System provably resistant to DoS attacks, with formal guarantees on its availability under high load or malicious traffic.
# 0.1-0.3: Strong defenses against DoS attacks (e.g., traffic filtering, rate limiting, auto-scaling), making it very difficult to disrupt the system's availability.
# 0.4-0.6: Some measures to mitigate DoS attacks (e.g., basic rate limiting), but the system may still be vulnerable to sophisticated attacks.
# 0.7-1.0: Highly vulnerable to DoS attacks, with no or minimal measures to protect the system's availability.
# Examples:
# 0.0: System is designed to withstand massive traffic spikes and is formally verified for its resistance to DoS attacks.
# 0.2: System uses a combination of traffic filtering, rate limiting, and auto-scaling to mitigate DoS attacks.
# 0.5: System has basic rate limiting, but can still be overwhelmed by a large number of requests.
# 0.8: System can be easily made unavailable by sending a large number of requests or malicious traffic.

PROVABLY_RESISTANT = DecisionPointValue(
    name="Provably Resistant",
    key="P",
    definition="System provably resistant to DoS attacks, with formal guarantees on its availability under high load or malicious traffic.",
)

STRONG_DEFENSES = DecisionPointValue(
    name="Strong Defenses",
    key="S",
    definition="Strong defenses against DoS attacks, making it very difficult to disrupt the system's availability.",
)

SOME_MEASURES = DecisionPointValue(
    name="Some Measures",
    key="M",
    definition="Some measures to mitigate DoS attacks, but the system may still be vulnerable to sophisticated attacks.",
)

HIGHLY_VULNERABLE = DecisionPointValue(
    name="Highly Vulnerable",
    key="H",
    definition="Highly vulnerable to DoS attacks, with no or minimal measures to protect the system's availability.",
)

DENIAL_OF_SERVICE = AivssDecisionPoint(
    name="Denial of Service (DoS)",
    key="DOS",
    version="0.1.0",
    definition="Degree to which the system is resistant or vulnerable to Denial of Service (DoS) attacks.",
    values=(
        PROVABLY_RESISTANT,
        STRONG_DEFENSES,
        SOME_MEASURES,
        HIGHLY_VULNERABLE,
    ),
)

VERSIONS = [DENIAL_OF_SERVICE]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
