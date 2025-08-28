#!/usr/bin/env python
"""
AIVSS Adversarial Attack Surface Decision Table
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

from ssvc.decision_points.aivss.orig.adversarial_attack_surface import (
    LATEST as AA,
)
from ssvc.decision_points.aivss.orig.membership_inference import LATEST as MINF
from ssvc.decision_points.aivss.orig.model_extraction import LATEST as ME
from ssvc.decision_points.aivss.orig.model_inversion import LATEST as MI
from ssvc.decision_tables.aivss import AIVSS_NS
from ssvc.decision_tables.base import DecisionTable

V1_0_0 = DecisionTable(
    namespace=AIVSS_NS,
    key="AAS",
    name="Adversarial Attack Surface",
    version="0.1.0",
    definition="A decision table for assessing the adversarial attack surface of AI systems.",
    decision_points={dp.id: dp for dp in [MI, ME, MINF, AA]},
    outcome=AA.id,
)


VERSIONS = [
    V1_0_0,
]
LATEST = VERSIONS[-1]


def main():

    print(LATEST.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
