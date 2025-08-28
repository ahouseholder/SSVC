#!/usr/bin/env python
"""
Models the AIVSS Sensitive Data Disclosure decision point.
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

# Sensitive Data Disclosure
#
# 0.0: System provably prevents sensitive data disclosure, with formal guarantees on the privacy of sensitive information.
# 0.1-0.3: Strong access controls, encryption, and output sanitization mechanisms in place, making it very difficult to extract sensitive data from the system.
# 0.4-0.6: Some measures to prevent data leakage (e.g., output filtering), but vulnerabilities remain, and sensitive information may be disclosed under certain circumstances.
# 0.7-1.0: High risk of sensitive data disclosure, with no or minimal measures to protect sensitive information processed or stored by the system.
# Examples:
# 0.0: System uses homomorphic encryption or other privacy-preserving techniques to prevent any sensitive data disclosure.
# 0.2: Strong access controls, encryption, and output sanitization are used to prevent data leakage.
# 0.5: Model outputs are filtered to remove potentially sensitive information, but some leakage may still occur.
# 0.8: Model may reveal sensitive information in its outputs, and there are no safeguards against data exfiltration.

PROVABLY_PREVENTS = DecisionPointValue(
    name="Provably Prevents Disclosure",
    key="P",
    definition="System provably prevents sensitive data disclosure, with formal guarantees on the privacy of sensitive information.",
)

STRONG_CONTROLS = DecisionPointValue(
    name="Strong Controls",
    key="S",
    definition="Strong access controls, encryption, and output sanitization mechanisms in place, making it very difficult to extract sensitive data from the system.",
)

SOME_MEASURES = DecisionPointValue(
    name="Some Measures",
    key="M",
    definition="Some measures to prevent data leakage, but vulnerabilities remain, and sensitive information may be disclosed under certain circumstances.",
)

HIGH_RISK = DecisionPointValue(
    name="High Risk",
    key="H",
    definition="High risk of sensitive data disclosure, with no or minimal measures to protect sensitive information processed or stored by the system.",
)

SENSITIVE_DATA_DISCLOSURE = AivssDecisionPoint(
    name="Sensitive Data Disclosure",
    key="SDD",
    version="0.1.0",
    definition="Degree to which the system prevents or is vulnerable to sensitive data disclosure.",
    values=(PROVABLY_PREVENTS, STRONG_CONTROLS, SOME_MEASURES, HIGH_RISK),
)

VERSIONS = [SENSITIVE_DATA_DISCLOSURE]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
