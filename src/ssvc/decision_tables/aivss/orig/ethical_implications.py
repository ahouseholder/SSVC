#!/usr/bin/env python
"""
AIVSS Data Sensitivity Decision Table
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

from ssvc.decision_points.aivss.orig.accountability import LATEST as AC
from ssvc.decision_points.aivss.orig.bias_and_discrimination import (
    LATEST as BD,
)
from ssvc.decision_points.aivss.orig.ethical_implications import LATEST as EI
from ssvc.decision_points.aivss.orig.societal_impact import LATEST as SI
from ssvc.decision_points.aivss.orig.transparency_and_explainability import (
    LATEST as TE,
)
from ssvc.decision_tables.aivss import AIVSS_NS
from ssvc.decision_tables.base import DecisionTable

V1_0_0 = DecisionTable(
    namespace=AIVSS_NS,
    key="ETHICS",
    name="Ethical Implications",
    version="0.1.0",
    definition="A decision table for evaluating the ethical implications of AI systems.",
    decision_points={dp.id: dp for dp in [BD, TE, AC, SI, EI]},
    outcome=EI.id,
)


VERSIONS = [
    V1_0_0,
]
LATEST = VERSIONS[-1]


def main():

    print(LATEST.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
