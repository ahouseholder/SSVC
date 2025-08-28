#!/usr/bin/env python
"""
file: aars
author: adh
created_at: 7/31/25 3:29 PM
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

from ssvc.decision_points.aivss.dynamic_identity import LATEST as DID
from ssvc.decision_points.aivss.multi_agent_interactions import LATEST as MAI
from ssvc.decision_tables.aivss import AIVSS_NS
from ssvc.decision_tables.base import DecisionTable
from ssvc.outcomes.basic.lmh import LATEST as LMH

# 1.3 Systemic and Relational Risks
# This principle recognizes that agents operate within a larger ecosystem, creating network and
# trust-based vulnerabilities.
# ● Dynamic Identity: The ability to shift roles or permissions.
# ● Multi-Agent Interactions: The capacity to interact with other agents.

V1_0_0 = DecisionTable(
    namespace=AIVSS_NS,
    name="Systemic and Relational Risks",
    key="SYSREL",
    version="0.1.0",
    definition="A decision table for assessing the systemic and relational risks of AI models "
    "in the context of Agentic AI Risk Score (AARS)",
    decision_points={dp.id: dp for dp in [DID, MAI, LMH]},
    outcome=LMH.id,
    mapping=[
        {
            "x_org.owasp#aivss:DYNID:0.1.0": "N",
            "x_org.owasp#aivss:MAI:0.1.0": "N",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:DYNID:0.1.0": "P",
            "x_org.owasp#aivss:MAI:0.1.0": "N",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:DYNID:0.1.0": "N",
            "x_org.owasp#aivss:MAI:0.1.0": "P",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:DYNID:0.1.0": "F",
            "x_org.owasp#aivss:MAI:0.1.0": "N",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:DYNID:0.1.0": "P",
            "x_org.owasp#aivss:MAI:0.1.0": "P",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:DYNID:0.1.0": "N",
            "x_org.owasp#aivss:MAI:0.1.0": "F",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:DYNID:0.1.0": "F",
            "x_org.owasp#aivss:MAI:0.1.0": "P",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:DYNID:0.1.0": "P",
            "x_org.owasp#aivss:MAI:0.1.0": "F",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:DYNID:0.1.0": "F",
            "x_org.owasp#aivss:MAI:0.1.0": "F",
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
