#!/usr/bin/env python
"""
Models the AIVSS Insecure Apps/Plugins decision point.
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

# Insecure Apps/Plugins
#
# 0.0: Secure development and integration practices for apps/plugins enforced, with formal verification of their security.
# 0.1-0.3: Strong security guidelines and vetting process for apps/plugins, minimizing the risk of vulnerabilities introduced by third-party integrations.
# 0.4-0.6: Some security measures for apps/plugins (e.g., sandboxing), but risks remain, and vulnerabilities may be introduced through insecure integrations.
# 0.7-1.0: High risk of vulnerabilities from insecure apps/plugins, with no or minimal measures to ensure the security of third-party integrations.
# Examples:
# 0.0: All apps/plugins undergo a rigorous security review and are formally verified before being allowed to integrate with the system.
# 0.2: Strong security guidelines are in place for app/plugin development, and a vetting process is used to minimize risks.
# 0.5: Apps/plugins are sandboxed, but they may still have access to sensitive data or functionalities.
# 0.8: Apps/plugins can be easily installed without any security checks, potentially introducing vulnerabilities into the system.

FORMALLY_VERIFIED = DecisionPointValue(
    name="Formally Verified",
    key="F",
    definition="Secure development and integration practices for apps/plugins enforced, with formal verification of their security.",
)

STRONG_GUIDELINES = DecisionPointValue(
    name="Strong Guidelines",
    key="S",
    definition="Strong security guidelines and vetting process for apps/plugins, minimizing the risk of vulnerabilities introduced by third-party integrations.",
)

SOME_MEASURES = DecisionPointValue(
    name="Some Measures",
    key="M",
    definition="Some security measures for apps/plugins, but risks remain, and vulnerabilities may be introduced through insecure integrations.",
)

HIGH_RISK = DecisionPointValue(
    name="High Risk",
    key="H",
    definition="High risk of vulnerabilities from insecure apps/plugins, with no or minimal measures to ensure the security of third-party integrations.",
)

INSECURE_APPS_PLUGINS = AivssDecisionPoint(
    name="Insecure Apps/Plugins",
    key="AP",
    version="0.1.0",
    definition="Degree to which the system is protected from vulnerabilities introduced by insecure apps/plugins and third-party integrations.",
    values=(FORMALLY_VERIFIED, STRONG_GUIDELINES, SOME_MEASURES, HIGH_RISK),
)

VERSIONS = [INSECURE_APPS_PLUGINS]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
