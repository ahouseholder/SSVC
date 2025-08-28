#!/usr/bin/env python
"""
file: opacity_reflexivity
author: adh
created_at: 7/31/25 3:40 PM
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

# 10. Opacity and Reflexivity: How difficult is it to understand or audit its internal reasoning?
# 0.0 - Complete chain-of-thought logging, hard-coded decision trees with logged outcomes, usage baselines with anomaly alerting, explainable AI logging
# 0.5 - Agent-reported motivations and reasoning, non-granular usage statistics
# 1.0 - No insights into agent motivations or goals, minimal event logging for agent or tool discovery, minimal tool execution logging

V1_0_0 = AivssDecisionPoint(
    name="Opacity and Reflexivity",
    key="OR",
    version="0.1.0",
    definition="A decision point for assessing the Opacity and Reflexivity of an agentic AI System.",
    values=(
        DecisionPointValue(
            name="None/Not Present",
            key="N",
            definition="Complete chain-of-thought logging, hard-coded decision trees with logged outcomes, usage baselines with anomaly alerting, explainable AI logging",
        ),
        DecisionPointValue(
            name="Partial/Limited",
            key="P",
            definition="Agent-reported motivations and reasoning, non-granular usage statistics",
        ),
        DecisionPointValue(
            name="Full/Unconstrained",
            key="F",
            definition="No insights into agent motivations or goals, minimal event logging for agent or tool discovery, minimal tool execution logging",
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
