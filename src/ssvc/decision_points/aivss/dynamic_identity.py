#!/usr/bin/env python
"""
file: dynamic_identity
author: adh
created_at: 7/31/25 2:40 PM
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

# 4. Dynamic Identity: Does it change roles or permissions based on its task?
# 0.0 - Predefined identities per agent or tool, granular least-permissions scopes, hard-coded access
# 0.5 - Human-in-the-loop identity delegation, deterministic assignment of permissions with policy engine
# 1.0 - No access limitations to dynamic identities, agentic individual permission/scope selection

V1_0_0 = AivssDecisionPoint(
    name="Dynamic Identity",
    key="DYNID",
    version="0.1.0",
    definition="A decision point for assessing the Dynamic Identity capabilities of an agentic AI System.",
    values=(
        DecisionPointValue(
            name="None/Not Present",
            key="N",
            definition="Predefined identities per agent or tool, granular least-permissions scopes, hard-coded access",
        ),
        DecisionPointValue(
            name="Partial/Limited",
            key="P",
            definition="Human-in-the-loop identity delegation, deterministic assignment of permissions with policy engine",
        ),
        DecisionPointValue(
            name="Full/Unconstrained",
            key="F",
            definition="No access limitations to dynamic identities, agentic individual permission/scope selection",
        ),
    ),
)

VERSIONS = (V1_0_0,)
LATEST = VERSIONS[-1]


def main():
    from ssvc.decision_points.helpers import print_versions_and_diffs

    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
