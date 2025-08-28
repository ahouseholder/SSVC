#!/usr/bin/env python
"""
Models the AIVSS Insecure Supply Chain decision point.
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

# Insecure Supply Chain
#
# 0.0: Secure and auditable supply chain, with formal verification of all third-party components and dependencies.
# 0.1-0.3: Strong supply chain security practices in place (e.g., code signing, dependency verification, regular audits), minimizing the risk of supply chain attacks.
# 0.4-0.6: Some measures to mitigate supply chain risks (e.g., using trusted sources), but vulnerabilities may still exist in third-party components.
# 0.7-1.0: High risk of supply chain vulnerabilities, with no or minimal measures to ensure the security of third-party components and dependencies.
# Examples:
# 0.0: All third-party components are formally verified for security, and the supply chain is continuously monitored for vulnerabilities.
# 0.2: Strong security practices are followed throughout the supply chain, including code signing, dependency verification, and regular audits.
# 0.5: Third-party libraries are used from reputable sources, but they are not thoroughly vetted for security vulnerabilities.
# 0.8: System relies on outdated or unpatched third-party components with known vulnerabilities.

SECURE_AUDITABLE = DecisionPointValue(
    name="Secure and Auditable",
    key="S",
    definition="Secure and auditable supply chain, with formal verification of all third-party components and dependencies.",
)

STRONG_PRACTICES = DecisionPointValue(
    name="Strong Practices",
    key="P",
    definition="Strong supply chain security practices in place, minimizing the risk of supply chain attacks.",
)

SOME_MEASURES = DecisionPointValue(
    name="Some Measures",
    key="M",
    definition="Some measures to mitigate supply chain risks, but vulnerabilities may still exist in third-party components.",
)

HIGH_RISK = DecisionPointValue(
    name="High Risk",
    key="H",
    definition="High risk of supply chain vulnerabilities, with no or minimal measures to ensure the security of third-party components and dependencies.",
)

INSECURE_SUPPLY_CHAIN = AivssDecisionPoint(
    name="Insecure Supply Chain",
    key="SCH",
    version="0.1.0",
    definition="Degree to which the system's supply chain is secure, auditable, and resistant to vulnerabilities in third-party components.",
    values=(SECURE_AUDITABLE, STRONG_PRACTICES, SOME_MEASURES, HIGH_RISK),
)

VERSIONS = [INSECURE_SUPPLY_CHAIN]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
