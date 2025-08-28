#!/usr/bin/env python
"""
Models the AIVSS Loss of Governance/Compliance decision point.
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

# Loss of Governance/Compliance
#
# 0.0: System meets or exceeds all relevant regulatory and governance requirements, with a proactive approach to adapting to new regulations and a strong focus on maintaining compliance.
# 0.1-0.3: Strong compliance framework and controls in place, ensuring adherence to relevant regulations and governance policies.
# 0.4-0.6: Some compliance efforts, but gaps remain, and the system may not fully meet all regulatory or governance requirements.
# 0.7-1.0: High risk of non-compliance with regulations or governance policies, with no or minimal measures to ensure adherence.
# Examples:
# 0.0: System is designed to be compliant by design, with automated mechanisms to ensure adherence to regulations and policies.
# 0.2: System is regularly audited for compliance, and a dedicated team ensures that all requirements are met.
# 0.5: Some efforts are made to comply with regulations, but there are significant gaps and no formal compliance program.
# 0.8: System does not meet data privacy regulations, and there are no mechanisms to ensure compliance with internal policies.

EXCEEDS_REQUIREMENTS = DecisionPointValue(
    name="Exceeds Requirements",
    key="E",
    definition="System meets or exceeds all relevant regulatory and governance requirements, with a proactive approach to adapting to new regulations and a strong focus on maintaining compliance.",
)

STRONG_FRAMEWORK = DecisionPointValue(
    name="Strong Framework",
    key="S",
    definition="Strong compliance framework and controls in place, ensuring adherence to relevant regulations and governance policies.",
)

SOME_EFFORTS = DecisionPointValue(
    name="Some Efforts",
    key="M",
    definition="Some compliance efforts, but gaps remain, and the system may not fully meet all regulatory or governance requirements.",
)

HIGH_RISK = DecisionPointValue(
    name="High Risk",
    key="H",
    definition="High risk of non-compliance with regulations or governance policies, with no or minimal measures to ensure adherence.",
)

LOSS_OF_GOVERNANCE_COMPLIANCE = AivssDecisionPoint(
    name="Loss of Governance/Compliance",
    key="LGC",
    version="0.1.0",
    definition="Degree to which the system maintains compliance with regulatory and governance requirements.",
    values=(EXCEEDS_REQUIREMENTS, STRONG_FRAMEWORK, SOME_EFFORTS, HIGH_RISK),
)

VERSIONS = [LOSS_OF_GOVERNANCE_COMPLIANCE]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
