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

from ssvc.decision_points.aivss.contextual_awareness import LATEST as CA
from ssvc.decision_points.aivss.memory_use import LATEST as MEMORY
from ssvc.decision_points.aivss.tool_use import LATEST as TOOL
from ssvc.decision_tables.aivss import AIVSS_NS
from ssvc.decision_tables.base import DecisionTable
from ssvc.outcomes.basic.lmh import LATEST as LMH

# 1.2 Environmental Interaction and Perception
# This principle covers how an agent perceives and manipulates its environment, extending its
# impact far beyond its own code.
# 51
# ● Dynamic Tool Use: The capability to use external tools (APIs, file systems, etc.).
# ● Persistent Memory: The use of memory to inform future actions.
# ● Contextual Awareness: The sensitivity to external inputs and context.

V1_0_0 = DecisionTable(
    name="Environmental Interaction and Perception",
    key="EIP",
    namespace=AIVSS_NS,
    version="0.1.0",
    definition="A decision table for assessing the environmental interaction and perception capabilities of AI models "
    "in the context of Agentic AI Risk Score (AARS).",
    decision_points={dp.id: dp for dp in [TOOL, MEMORY, CA, LMH]},
    outcome=LMH.id,
    mapping=[
        {
            "x_org.owasp#aivss:TU:0.1.0": "N",
            "x_org.owasp#aivss:MU:0.1.0": "N",
            "x_org.owasp#aivss:CA:0.1.0": "N",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "P",
            "x_org.owasp#aivss:MU:0.1.0": "N",
            "x_org.owasp#aivss:CA:0.1.0": "N",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "N",
            "x_org.owasp#aivss:MU:0.1.0": "P",
            "x_org.owasp#aivss:CA:0.1.0": "N",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "N",
            "x_org.owasp#aivss:MU:0.1.0": "N",
            "x_org.owasp#aivss:CA:0.1.0": "P",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "F",
            "x_org.owasp#aivss:MU:0.1.0": "N",
            "x_org.owasp#aivss:CA:0.1.0": "N",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "P",
            "x_org.owasp#aivss:MU:0.1.0": "P",
            "x_org.owasp#aivss:CA:0.1.0": "N",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "N",
            "x_org.owasp#aivss:MU:0.1.0": "F",
            "x_org.owasp#aivss:CA:0.1.0": "N",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "P",
            "x_org.owasp#aivss:MU:0.1.0": "N",
            "x_org.owasp#aivss:CA:0.1.0": "P",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "N",
            "x_org.owasp#aivss:MU:0.1.0": "P",
            "x_org.owasp#aivss:CA:0.1.0": "P",
            "basic:LMH:1.0.0": "L",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "N",
            "x_org.owasp#aivss:MU:0.1.0": "N",
            "x_org.owasp#aivss:CA:0.1.0": "F",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "F",
            "x_org.owasp#aivss:MU:0.1.0": "P",
            "x_org.owasp#aivss:CA:0.1.0": "N",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "P",
            "x_org.owasp#aivss:MU:0.1.0": "F",
            "x_org.owasp#aivss:CA:0.1.0": "N",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "F",
            "x_org.owasp#aivss:MU:0.1.0": "N",
            "x_org.owasp#aivss:CA:0.1.0": "P",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "P",
            "x_org.owasp#aivss:MU:0.1.0": "P",
            "x_org.owasp#aivss:CA:0.1.0": "P",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "N",
            "x_org.owasp#aivss:MU:0.1.0": "F",
            "x_org.owasp#aivss:CA:0.1.0": "P",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "P",
            "x_org.owasp#aivss:MU:0.1.0": "N",
            "x_org.owasp#aivss:CA:0.1.0": "F",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "N",
            "x_org.owasp#aivss:MU:0.1.0": "P",
            "x_org.owasp#aivss:CA:0.1.0": "F",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "F",
            "x_org.owasp#aivss:MU:0.1.0": "F",
            "x_org.owasp#aivss:CA:0.1.0": "N",
            "basic:LMH:1.0.0": "M",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "F",
            "x_org.owasp#aivss:MU:0.1.0": "P",
            "x_org.owasp#aivss:CA:0.1.0": "P",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "P",
            "x_org.owasp#aivss:MU:0.1.0": "F",
            "x_org.owasp#aivss:CA:0.1.0": "P",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "F",
            "x_org.owasp#aivss:MU:0.1.0": "N",
            "x_org.owasp#aivss:CA:0.1.0": "F",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "P",
            "x_org.owasp#aivss:MU:0.1.0": "P",
            "x_org.owasp#aivss:CA:0.1.0": "F",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "N",
            "x_org.owasp#aivss:MU:0.1.0": "F",
            "x_org.owasp#aivss:CA:0.1.0": "F",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "F",
            "x_org.owasp#aivss:MU:0.1.0": "F",
            "x_org.owasp#aivss:CA:0.1.0": "P",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "F",
            "x_org.owasp#aivss:MU:0.1.0": "P",
            "x_org.owasp#aivss:CA:0.1.0": "F",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "P",
            "x_org.owasp#aivss:MU:0.1.0": "F",
            "x_org.owasp#aivss:CA:0.1.0": "F",
            "basic:LMH:1.0.0": "H",
        },
        {
            "x_org.owasp#aivss:TU:0.1.0": "F",
            "x_org.owasp#aivss:MU:0.1.0": "F",
            "x_org.owasp#aivss:CA:0.1.0": "F",
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
