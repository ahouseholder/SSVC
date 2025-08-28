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

# #!/usr/bin/env python
# """
# file: aars
# author: adh
# created_at: 7/31/25 3:29 PM
# """
#
#
# from ssvc.decision_points.aivss.autonomy import LATEST as AUTONOMY
# from ssvc.decision_points.aivss.contextual_awareness import LATEST as CA
# from ssvc.decision_points.aivss.dynamic_identity import LATEST as DID
# from ssvc.decision_points.aivss.goal_driven_planning import LATEST as GDP
# from ssvc.decision_points.aivss.memory_use import LATEST as MEMORY
# from ssvc.decision_points.aivss.multi_agent_interactions import LATEST as MAI
# from ssvc.decision_points.aivss.non_determinism import LATEST as ND
# from ssvc.decision_points.aivss.opacity_reflexivity import LATEST as OR
# from ssvc.decision_points.aivss.self_modification import LATEST as SM
# from ssvc.decision_points.aivss.tool_use import LATEST as TOOL
# from ssvc.decision_points.cvss.qualitative_severity import LATEST as QS
# from ssvc.decision_tables.base import DecisionTable
# from ssvc.namespaces import NameSpace
#
#
# TODO: figure out a way to simplify AARS. As it stands it creates a mapping with over 500k rows.
#
# V1_0_0 = DecisionTable(
#     namespace=AIVSS_NS,
#     name="Agentic AI Risk Score (AARS)",
#     key="AARS",
#     version="0.1.0",
#     definition="A decision table for assessing the Agentic AI Risk Score (AARS) of AI models.",
#     decision_points={
#         dp.id: dp for dp in [AUTONOMY, TOOL, MEMORY, DID, MAI, ND, SM, GDP, CA, OR, QS]
#     },
#     outcome=QS.id,
# )
#
# VERSIONS = (V1_0_0,)
# LATEST = VERSIONS[-1]
#
#
# def main():
#
#     print(LATEST.model_dump_json(indent=2, exclude_none=True))
#
#
# if __name__ == "__main__":
#     main()
