#!/usr/bin/env python
"""
file: self_modification
author: adh
created_at: 7/31/25 3:10 PM
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

# 7. Self-Modification: Can it change its own code, models, or core logic?
# 0.0 - No self-modification capabilities, out-of-band user prompt reinforcement training
# 0.5 - Write access to memory/context data sources, dynamic and session-only goal modification, dynamic user prompt reinforcement training
# 1.0 - Write access to deployment code, write access to model weights, no limitations on goal modifications, write access to persistent memory/context data sources

V1_0_0 = AivssDecisionPoint(
    name="Self-Modification",
    key="SM",
    version="0.1.0",
    definition="A decision point for assessing the Self-Modification capabilities of an agentic AI System.",
    values=(
        DecisionPointValue(
            name="None/Not Present",
            key="N",
            definition="No self-modification capabilities, out-of-band user prompt reinforcement training",
        ),
        DecisionPointValue(
            name="Partial/Limited",
            key="P",
            definition="Write access to memory/context data sources, dynamic and session-only goal modification, dynamic user prompt reinforcement training",
        ),
        DecisionPointValue(
            name="Full/Unconstrained",
            key="F",
            definition="Write access to deployment code, write access to model weights, no limitations on goal modifications, write access to persistent memory/context data sources",
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
