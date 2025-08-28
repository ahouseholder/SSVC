#!/usr/bin/env python
"""
file: non_determinism
author: adh
created_at: 7/31/25 3:00 PM
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

# 6. Non-Determinism: How unpredictable are its outputs for a given input?
# 0.0 - Simple probabilistic agent with schema-validated inputs and outputs, well-defined decision trees based on known business logic, agentic calling of hard-coded deterministic tools with well-defined outputs and error-handling
# 0.5 - Hard-coded or schema-validated inputs with probabilistic agent outputs or vice versa, limited dynamic decision making with access limited tools or agents
# 1.0 - Multi-agent communication in plain text without predefined schemata, dynamic discover and usage of tools and agents, no limits on input / output format or data

V1_0_0 = AivssDecisionPoint(
    name="Non-Determinism",
    key="ND",
    version="0.1.0",
    definition="A decision point for assessing the Non-Determinism of an agentic AI System.",
    values=(
        DecisionPointValue(
            name="None/Not Present",
            key="N",
            definition="Simple probabilistic agent with schema-validated inputs and outputs, well-defined decision trees based on known business logic, agentic calling of hard-coded deterministic tools with well-defined outputs and error-handling",
        ),
        DecisionPointValue(
            name="Partial/Limited",
            key="P",
            definition="Hard-coded or schema-validated inputs with probabilistic agent outputs or vice versa, limited dynamic decision making with access limited tools or agents",
        ),
        DecisionPointValue(
            name="Full/Unconstrained",
            key="F",
            definition="Multi-agent communication in plain text without predefined schemata, dynamic discover and usage of tools and agents, no limits on input / output format or data",
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
