#!/usr/bin/env python
"""
file: v2
author: adh
created_at: 9/21/23 10:31 AM
"""
from copy import deepcopy

from ssvc.decision_points.automatable import AUTOMATABLE_1 as AUTOMATABLE
from ssvc.decision_points.exploitation import EXPLOITATION_1 as EXPLOITATION
from ssvc.decision_points.exposure import EXPOSURE_1_0_1 as EXPOSURE
from ssvc.decision_points.human_impact import HUMAN_IMPACT_1 as HUMAN_IMPACT
from ssvc.decision_points.mission_impact import MISSION_IMPACT_1 as MISSION_IMPACT
from ssvc.decision_points.public_safety_impact import (
    PUBLIC_SAFETY_IMPACT_1 as PUBLIC_SAFETY_IMPACT,
)
from ssvc.decision_points.public_value_added import PUBLIC_VALUE_ADDED_1 as PUBLIC_VALUE_ADDED
from ssvc.decision_points.report_credibility import REPORT_CREDIBILITY_1 as REPORT_CREDIBILITY
from ssvc.decision_points.report_public import REPORT_PUBLIC_1 as REPORT_PUBLIC
from ssvc.decision_points.safety_impact import SAFETY_IMPACT_1 as SAFETY_IMPACT
from ssvc.decision_points.supplier_cardinality import (
    SUPPLIER_CARDINALITY_1 as SUPPLIER_CARDINALITY,
)
from ssvc.decision_points.supplier_contacted import (
    SUPPLIER_CONTACTED_1 as SUPPLIER_CONTACTED,
)
from ssvc.decision_points.supplier_engagement import SUPPLIER_ENGAGEMENT_1 as SUPPLIER_ENGAGEMENT
from ssvc.decision_points.supplier_involvement import SUPPLIER_INVOLVEMENT_1 as SUPPLIER_INVOLVEMENT
from ssvc.decision_points.technical_impact import TECHNICAL_IMPACT_1 as TECHNICAL_IMPACT
from ssvc.decision_points.utility import UTILITY_1_0_1 as UTILITY
from ssvc.decision_points.value_density import VALUE_DENSITY_1 as VALUE_DENSITY
from ssvc.dp_groups.base import SsvcDecisionPointGroup

# convenience imports
from ssvc.dp_groups.coordinator_publication import COORDINATOR_PUBLICATION_1 # noqa
from ssvc.dp_groups.coordinator_triage import COORDINATOR_TRIAGE_1 # noqa
from ssvc.dp_groups.deployer import DEPLOYER_2 # noqa
from ssvc.dp_groups.supplier import SUPPLIER_1 # noqa

SITUATED_SAFETY_IMPACT = deepcopy(SAFETY_IMPACT)

SSVCv2 = SsvcDecisionPointGroup(
    name="SSVCv2",
    description="The second version of the SSVC.",
    key="SSVCv2",
    version="2.0.0",
    decision_points=[
        EXPLOITATION,
        TECHNICAL_IMPACT,
        UTILITY,
        AUTOMATABLE,
        VALUE_DENSITY,
        SAFETY_IMPACT,
        PUBLIC_SAFETY_IMPACT,
        SITUATED_SAFETY_IMPACT,
        MISSION_IMPACT,
        HUMAN_IMPACT,
        EXPOSURE,
        REPORT_PUBLIC,
        SUPPLIER_CONTACTED,
        SUPPLIER_CARDINALITY,
        SUPPLIER_ENGAGEMENT,
        REPORT_CREDIBILITY,
        PUBLIC_VALUE_ADDED,
        SUPPLIER_INVOLVEMENT,
    ],
)


def main():
    print(SSVCv2.to_json(indent=2))
    print(SUPPLIER_1.to_json(indent=2))
    print(DEPLOYER_2.to_json(indent=2))
    print(COORDINATOR_TRIAGE_1.to_json(indent=2))
    print(COORDINATOR_PUBLICATION_1.to_json(indent=2))

if __name__ == "__main__":
    main()
