#!/usr/bin/env python
"""
file: supplier
author: adh
created_at: 9/21/23 11:41 AM
"""

from ssvc.decision_points.automatable import AUTOMATABLE_1
from ssvc.decision_points.exploitation import EXPLOITATION_1
from ssvc.decision_points.safety_impact import SAFETY_IMPACT_1
from ssvc.decision_points.technical_impact import TECHNICAL_IMPACT_1
from ssvc.decision_points.utility import UTILITY_1, UTILITY_1_0_1
from ssvc.decision_points.value_density import VALUE_DENSITY_1
from ssvc.decision_points.virulence import VIRULENCE_1
from ssvc.dp_groups.base import SsvcDecisionPointGroup

PATCH_DEVELOPER_1 = SsvcDecisionPointGroup(
    name="SSVC Patch Developer",
    description="The decision points used by the patch developer.",
    version="1.0.0",
    decision_points=(
        EXPLOITATION_1,
        UTILITY_1,
        TECHNICAL_IMPACT_1,
        VIRULENCE_1,
        VALUE_DENSITY_1,
        SAFETY_IMPACT_1,
    ),
)
"""
In SSVC v1, Patch Developer v1 represents the decision points used by the patch developer.

It includes decision points:

- Exploitation v1.0.0
- Utility v1.0.0
    - Virulence v1.0.0
    - Value Density v1.0.0
- Technical Impact v1.0.0
- Safety Impact v1.0.0
"""

# alias for forward compatibility
SUPPLIER_1 = PATCH_DEVELOPER_1

# SSVC v2 renamed to SSVC Supplier
SUPPLIER_2 = SsvcDecisionPointGroup(
    name="SSVC Supplier",
    description="The decision points used by the supplier.",
    version="2.0.0",
    decision_points=[
        EXPLOITATION_1,
        UTILITY_1_0_1,
        TECHNICAL_IMPACT_1,
        AUTOMATABLE_1,
        VALUE_DENSITY_1,
        SAFETY_IMPACT_1,
    ],
)
"""
In SSVC v2, Supplier v2 represents the decision points used by the supplier.
It includes decision points:

- Exploitation v1.0.0
- Utility v1.0.1
    - Automatable v1.0.0
    - Value Density v1.0.0
- Technical Impact v1.0.0
- Public Safety Impact v1.0.0
    - Safety Impact v1.0.0
    
Changes from Patch Developer v1:

- Name change from Patch Developer v1 -> Supplier v2
- Utility v1.0.0 -> v1.0.1
- Virulence v1.0.0 replaced by Automatable v1.0.0
- Public Safety Impact v1.0.0 added, which subsumes Safety Impact v1.0.0
"""


def main():
    print(PATCH_DEVELOPER_1.to_json(indent=2))
    print(SUPPLIER_2.to_json(indent=2))


if __name__ == "__main__":
    main()
