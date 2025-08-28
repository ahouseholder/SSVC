#!/usr/bin/env python
"""
file: contextual_awareness
author: adh
created_at: 7/31/25 3:30 PM
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

# 9. Contextual Awareness: How sensitive is its behavior to subtle changes in prompts or external data?
# 0.0 - No access to external context modifying data sources, no internet access, hard-coded system prompts
# 0.5 - Limited and non-volatile external context data sources, intranet or limited internet access, curated and filtered update feeds
# 1.0 - Dynamic and multi-agent goal negotiation, no limitations on context modifying data sources, open internet access, unrestricted update feeds

V1_0_0 = AivssDecisionPoint(
    name="Contextual Awareness",
    key="CA",
    version="0.1.0",
    definition="A decision point for assessing the Contextual Awareness capabilities of an agentic AI System.",
    values=(
        DecisionPointValue(
            name="None/Not Present",
            key="N",
            definition="No access to external context modifying data sources, no internet access, hard-coded system prompts",
        ),
        DecisionPointValue(
            name="Partial/Limited",
            key="P",
            definition="Limited and non-volatile external context data sources, intranet or limited internet access, curated and filtered update feeds",
        ),
        DecisionPointValue(
            name="Full/Unconstrained",
            key="F",
            definition="Dynamic and multi-agent goal negotiation, no limitations on context modifying data sources, open internet access, unrestricted update feeds",
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
