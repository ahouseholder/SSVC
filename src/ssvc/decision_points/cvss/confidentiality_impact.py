#!/usr/bin/env python
"""
file: confidentiality_impact
author: adh
created_at: 9/20/23 1:46 PM
"""
from copy import deepcopy

from ssvc.decision_points.base import SsvcValue
from ssvc.decision_points.cvss.base import CvssDecisionPoint

CONFIDENTIALITY_IMPACT_1 = CvssDecisionPoint(
    name="Confidentiality Impact",
    description="This metric measures the impact on confidentiality of a successful exploit of the vulnerability on the target system.",
    key="C",
    version="1.0.0",
    values=[
        SsvcValue(
            name="None",
            key="N",
            description="No impact on confidentiality.",
        ),
        SsvcValue(
            name="Partial",
            key="P",
            description="There is considerable informational disclosure. Access to critical system files is possible. There is a loss of important information, but the attacker doesn't have control over what is obtainable or the scope of the loss is constrained.",
        ),
        SsvcValue(
            name="Complete",
            key="C",
            description="A total compromise of critical system information. A complete loss of system protection resulting in all critical system files being revealed. The attacker has sovereign control to read all of the system's data (memory, files, etc).",
        ),
    ],
)

CONFIDENTIALITY_IMPACT_2 = deepcopy(CONFIDENTIALITY_IMPACT_1)
CONFIDENTIALITY_IMPACT_2.version = "2.0.0"
CONFIDENTIALITY_IMPACT_2.values = [
    SsvcValue(
        name="None",
        key="N",
        description="There is no loss of confidentiality within the impacted component.",
    ),
    SsvcValue(
        name="Low",
        key="L",
        description="There is some loss of confidentiality. Access to some restricted information is obtained, but the attacker does not have control over what information is obtained, or the amount or kind of loss is constrained. The information disclosure does not cause a direct, serious loss to the impacted component.",
    ),
    SsvcValue(
        name="High",
        key="H",
        description="There is total loss of confidentiality, resulting in all resources within the impacted component being divulged to the attacker. Alternatively, access to only some restricted information is obtained, but the disclosed information presents a direct, serious impact. For example, an attacker steals the administrator's password, or private encryption keys of a web server.",
    ),
]


def main():
    print(CONFIDENTIALITY_IMPACT_1.to_json(indent=2))
    print(CONFIDENTIALITY_IMPACT_2.to_json(indent=2))


if __name__ == "__main__":
    main()
