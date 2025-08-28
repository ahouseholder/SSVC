#!/usr/bin/env python
"""
file: core_agency
author: adh
created_at: 7/31/25 3:55 PM
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

from ssvc.decision_points.aivss.autonomy import LATEST as AUTONOMY
from ssvc.decision_points.aivss.goal_driven_planning import LATEST as GDP
from ssvc.decision_points.aivss.self_modification import LATEST as SM
from ssvc.decision_tables.aivss import AIVSS_NS
from ssvc.decision_tables.base import DecisionTable
from ssvc.outcomes.basic.lmh import LATEST as LMH

# 1.1 Core Agency and Goal-Seeking Behavior
# This principle addresses the risks arising from an agent's internal drive and ability to act on its
# own initiative. In classical architectures, systems are passive and reactive. Agentic systems are
# proactive and goal-directed.
# ● Autonomy of Action: The ability to operate without direct human command.
# ● Goal-Driven Planning: The capacity to create and execute multi-step plans.
# ● Self-Modification: The potential for an agent to alter its own logic or code.


V1_0_0 = DecisionTable(
    name="Core Agency and Goal-Seeking Behavior",
    key="CAGB",
    namespace=AIVSS_NS,
    version="0.1.0",
    definition="A decision table for assessing the core agency and goal-seeking behavior of AI models "
    "in the context of Agentic AI Risk Score (AARS).",
    decision_points={dp.id: dp for dp in [AUTONOMY, GDP, SM, LMH]},
    outcome=LMH.id,
    mapping=[
        {
            "x_org.owasp#aivss:AUT:0.1.0": "N",
            "x_org.owasp#aivss:GDP:0.1.0": "N",
            "x_org.owasp#aivss:SM:0.1.0": "N",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "P",
            "x_org.owasp#aivss:GDP:0.1.0": "N",
            "x_org.owasp#aivss:SM:0.1.0": "N",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "N",
            "x_org.owasp#aivss:GDP:0.1.0": "P",
            "x_org.owasp#aivss:SM:0.1.0": "N",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "N",
            "x_org.owasp#aivss:GDP:0.1.0": "N",
            "x_org.owasp#aivss:SM:0.1.0": "P",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "F",
            "x_org.owasp#aivss:GDP:0.1.0": "N",
            "x_org.owasp#aivss:SM:0.1.0": "N",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "P",
            "x_org.owasp#aivss:GDP:0.1.0": "P",
            "x_org.owasp#aivss:SM:0.1.0": "N",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "N",
            "x_org.owasp#aivss:GDP:0.1.0": "F",
            "x_org.owasp#aivss:SM:0.1.0": "N",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "P",
            "x_org.owasp#aivss:GDP:0.1.0": "N",
            "x_org.owasp#aivss:SM:0.1.0": "P",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "N",
            "x_org.owasp#aivss:GDP:0.1.0": "P",
            "x_org.owasp#aivss:SM:0.1.0": "P",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "N",
            "x_org.owasp#aivss:GDP:0.1.0": "N",
            "x_org.owasp#aivss:SM:0.1.0": "F",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "F",
            "x_org.owasp#aivss:GDP:0.1.0": "P",
            "x_org.owasp#aivss:SM:0.1.0": "N",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "P",
            "x_org.owasp#aivss:GDP:0.1.0": "F",
            "x_org.owasp#aivss:SM:0.1.0": "N",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "F",
            "x_org.owasp#aivss:GDP:0.1.0": "N",
            "x_org.owasp#aivss:SM:0.1.0": "P",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "P",
            "x_org.owasp#aivss:GDP:0.1.0": "P",
            "x_org.owasp#aivss:SM:0.1.0": "P",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "N",
            "x_org.owasp#aivss:GDP:0.1.0": "F",
            "x_org.owasp#aivss:SM:0.1.0": "P",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "P",
            "x_org.owasp#aivss:GDP:0.1.0": "N",
            "x_org.owasp#aivss:SM:0.1.0": "F",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "N",
            "x_org.owasp#aivss:GDP:0.1.0": "P",
            "x_org.owasp#aivss:SM:0.1.0": "F",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "F",
            "x_org.owasp#aivss:GDP:0.1.0": "F",
            "x_org.owasp#aivss:SM:0.1.0": "N",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "F",
            "x_org.owasp#aivss:GDP:0.1.0": "P",
            "x_org.owasp#aivss:SM:0.1.0": "P",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "P",
            "x_org.owasp#aivss:GDP:0.1.0": "F",
            "x_org.owasp#aivss:SM:0.1.0": "P",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "F",
            "x_org.owasp#aivss:GDP:0.1.0": "N",
            "x_org.owasp#aivss:SM:0.1.0": "F",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "P",
            "x_org.owasp#aivss:GDP:0.1.0": "P",
            "x_org.owasp#aivss:SM:0.1.0": "F",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "N",
            "x_org.owasp#aivss:GDP:0.1.0": "F",
            "x_org.owasp#aivss:SM:0.1.0": "F",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "F",
            "x_org.owasp#aivss:GDP:0.1.0": "F",
            "x_org.owasp#aivss:SM:0.1.0": "P",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "F",
            "x_org.owasp#aivss:GDP:0.1.0": "P",
            "x_org.owasp#aivss:SM:0.1.0": "F",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "P",
            "x_org.owasp#aivss:GDP:0.1.0": "F",
            "x_org.owasp#aivss:SM:0.1.0": "F",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:AUT:0.1.0": "F",
            "x_org.owasp#aivss:GDP:0.1.0": "F",
            "x_org.owasp#aivss:SM:0.1.0": "F",
            "basic:LMH:1.0.0": "H",
        },
    ],
)

VERSIONS = (V1_0_0,)
LATEST = VERSIONS[-1]


def main():
    print(LATEST.model_dump_json(indent=2, exclude_none=True))


if __name__ == "__main__":
    main()
