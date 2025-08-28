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
# AIVSS Adaptability Decision Table
# """
# from ssvc.decision_tables.base import DecisionTable
# from ssvc.namespaces import NameSpace
#
#
# PART_ONE = DecisionTable(
#     namespace=AIVSS_NS,
#     name="Cloud Security Part One",
#     version="0.1.0",
#     definition="A decision table for assessing the Cloud Security Taxonomy of AI systems.",
#     decision_points={dp.id: dp for dp in [MM, DP, SDD, MS, FM, CS]},
#     outcome=CS.id,
# )
#
# PART_TWO = DecisionTable(
#     namespace=AIVSS_NS,
#     name="Cloud Security Part Two",
#     version="0.1.0",
#     definition="A decision table for assessing the Cloud Security Taxonomy of AI systems.",
#     decision_points={dp.id: dp for dp in [INS, AP, DOS, LGC, CS]},
#     outcome=CS.id,
# )
#
# This table has 4^9= 262,144 possible combinations, which is too large for practical use.
# Building the graph takes too long because it's an N^2 problem, which
# would result in 68,719,476,736 comparisons
# V1_0_0 = DecisionTable(
#     namespace=AIVSS_NS,
#     name="Cloud Security",
#     version="0.1.0",
#     definition="A decision table for assessing the Cloud Security Taxonomy of AI systems.",
#     decision_points={dp.id: dp for dp in [MM, DP, SDD, MS, FM, INS, AP, DOS, LGC, CS]},
#     outcome=CS.id,
# )
#
# #
# # VERSIONS = [PART_ONE, PART_TWO]
# # LATEST = VERSIONS[-1]
#
#
# def main():
#
#     for version in VERSIONS:
#         print(f"## {version.name} Decision Table Object")
#         print()
#         print(version.model_dump_json(indent=2))
#         print()
#
#
# if __name__ == "__main__":
#     main()
