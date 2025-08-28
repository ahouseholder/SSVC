#!/usr/bin/env python
"""
Models the AIVSS Model Manipulation decision point.
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
from ssvc.decision_points.helpers import print_versions_and_diffs

# Model Manipulation
#
# 0.0: System provably resistant to model manipulation, with formal verification of robustness against prompt injection and other adversarial techniques.
# 0.1-0.3: Strong defenses against model manipulation (e.g., input filtering, adversarial training, output validation), making it difficult to manipulate the model's behavior.
# 0.4-0.6: Some defenses against manipulation (e.g., basic input sanitization), but vulnerabilities remain, and the model can be manipulated with some effort.
# 0.7-1.0: Highly vulnerable to model manipulation, including prompt injection and other adversarial techniques, with no or minimal defenses in place.
# Examples:
# 0.0: Model's resistance to prompt injection is formally verified.
# 0.2: Model uses a combination of input filtering, adversarial training, and output validation to defend against manipulation.
# 0.5: Model has basic input sanitization, but can still be manipulated by carefully crafted prompts.
# 0.8: Model is easily manipulated by prompt injection attacks.

PROVABLY_RESISTANT = DecisionPointValue(
    name="Provably Resistant",
    key="P",
    definition="System provably resistant to model manipulation, with formal verification of robustness against prompt injection and other adversarial techniques.",
)

STRONG_DEFENSES = DecisionPointValue(
    name="Strong Defenses",
    key="S",
    definition="Strong defenses against model manipulation, making it difficult to manipulate the model's behavior.",
)

SOME_DEFENSES = DecisionPointValue(
    name="Some Defenses",
    key="D",
    definition="Some defenses against manipulation, but vulnerabilities remain, and the model can be manipulated with some effort.",
)

HIGHLY_VULNERABLE = DecisionPointValue(
    name="Highly Vulnerable",
    key="H",
    definition="Highly vulnerable to model manipulation, including prompt injection and other adversarial techniques, with no or minimal defenses in place.",
)

MODEL_MANIPULATION = AivssDecisionPoint(
    name="Model Manipulation",
    key="MM",
    version="0.1.0",
    definition="Degree to which the system is resistant to model manipulation, including prompt injection and adversarial techniques.",
    values=(
        PROVABLY_RESISTANT,
        STRONG_DEFENSES,
        SOME_DEFENSES,
        HIGHLY_VULNERABLE,
    ),
)

VERSIONS = [MODEL_MANIPULATION]
LATEST = VERSIONS[-1]


def main():
    print_versions_and_diffs(VERSIONS)


if __name__ == "__main__":
    main()
