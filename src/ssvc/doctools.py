#!/usr/bin/env python
#  Copyright (c) 2023 Carnegie Mellon University and Contributors.
#  - see Contributors.md for a full list of Contributors
#  - see ContributionInstructions.md for information on how you can Contribute to this project
#  Stakeholder Specific Vulnerability Categorization (SSVC) is
#  licensed under a MIT (SEI)-style license, please see LICENSE.md distributed
#  with this Software or contact permission@sei.cmu.edu for full terms.
#  Created, in part, with funding and support from the United States Government
#  (see Acknowledgments file). This program may include and/or can make use of
#  certain third party source code, object code, documentation and other files
#  (“Third Party Software”). See LICENSE.md for more details.
#  Carnegie Mellon®, CERT® and CERT Coordination Center® are registered in the
#  U.S. Patent and Trademark Office by Carnegie Mellon University
"""
Provides tools to assist with generating documentation for SSVC decision points.

Writes the following files for each decision point:
- a markdown table that can be used in the decision point documentation
- a json example that can be used in the decision point documentation
- a markdown file that builds an insert using mkdocs tabs to switch between the markdown description and the json
  example

Examples

To generate the documentation for the decision points, use the following command:

    python -m ssvc.doctools --overwrite --outdir ./tmp/md_out --jsondir ./tmp/json_out`

To regenerate the existing docs, use the following command:

    python -m ssvc.doctools --overwrite --outdir docs/_generated/decision_points --jsondir data/json/decision_points

"""
import logging
import os

from ssvc.decision_points.base import REGISTERED_DECISION_POINTS, SsvcDecisionPoint
from ssvc.dp_groups.ssvc.collections import SSVCv1, SSVCv2, SSVCv2_1  # noqa

logger = logging.getLogger(__name__)


def _filename_friendly(name: str) -> str:
    """
    Given a string, return a version that is friendly for use in a filename.

    Args:
        name (str): The string to make friendly for use in a filename.

    Returns:
        str: A version of the string that is friendly for use in a filename.
    """
    return name.lower().replace(" ", "_").replace(".", "_")


MD_TABLE_ROW_TEMPLATE = "| {value.name} | {value.description} |"

# indent by 4 spaces to make it a code block
MD_INCLUDE_TEMPLATE = """<!-- This content is autogenerated by doctools.py. Do not Edit. -->
!!! note "{dp.name} v{dp.version}"

    === "Text" 
    
        {table}
        
    === "JSON"
    
        ```json
        {{% include "{json_file}" %}}
        ```
"""


def to_markdown_table(dp: SsvcDecisionPoint) -> str:
    """
    Generate a markdown table for a decision point.

    Args:
        dp (SsvcDecisionPoint): The decision point to generate a markdown table for.

    Returns:
        str: The markdown table.
    """
    rows = []
    # prepend the header
    rows.append(f"{dp.description}")
    rows.append("")
    indent = " " * 8
    rows.append(f"{indent}| Value | Definition |")
    rows.append(f"{indent}|:-----|:-----------|")

    # add a row for each value
    for value in dp.values:
        rows.append(indent + MD_TABLE_ROW_TEMPLATE.format(value=value))

    return "\n".join(rows)


# create a runtime context that ensures that dir exists
class EnsureDirExists:
    """
    A runtime context that ensures that a directory exists or creates it otherwise.

    Example:

        with EnsureDirExists(dir):
            assert os.path.exists(dir)
    """

    def __init__(self, dir: str):
        """
        Create a new EnsureDirExists context.

        Args:
            dir (str): The directory to ensure exists.

        Returns:
            EnsureDirExists: The new EnsureDirExists context.
        """
        self.dir = dir

    def __enter__(self):
        os.makedirs(self.dir, exist_ok=True)

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


def remove_if_exists(file):
    try:
        os.remove(file)
        logger.debug(f"Removed {file}")
    except FileNotFoundError:
        logger.debug(f"File {file} does not exist, nothing to remove")


def dump_decision_point(
    jsondir: str, outdir: str, dp: SsvcDecisionPoint, overwrite: bool
) -> dict:
    """
    Generate the markdown table, json example, and markdown table file for a decision point.

    Args:
        jsondir (str): The directory to write the json example to.
        outdir (str): The directory to write the markdown table file to.
        dp (SsvcDecisionPoint): The decision point to generate documentation for.
        overwrite (bool): Whether to overwrite existing files.

    Returns:
        dict: A dictionary with the following keys:
            - include_file: The path to the markdown table file.
            - symlink: The path to the symlink that points to the markdown table file.
            - json_file: The path to the json example file.
    """
    # - generate markdown table
    # make dp.name safe for use in a filename
    basename = _filename_friendly(dp.name) + f"_{_filename_friendly(dp.version)}"
    # - generate json example
    json_file = dump_json(basename, dp, jsondir, overwrite)

    # - generate markdown table file
    r = dump_markdown(basename, dp, json_file, outdir, overwrite)
    r["json_file"] = json_file
    return r


def dump_markdown(
    basename: str, dp: SsvcDecisionPoint, json_file: str, outdir: str, overwrite: bool
) -> dict:
    """
    Generate the markdown table file for a decision point.

    Args:
        basename (str): The basename of the markdown table file.
        dp (SsvcDecisionPoint): The decision point to generate documentation for.
        json_file (str): The path to the json example file.
        outdir (str): The directory to write the markdown table file to.
        overwrite (bool): Whether to overwrite existing files.

    Returns:
        dict: A dictionary with the following keys:
            - include_file: The path to the markdown table file.
            - symlink: The path to the symlink that points to the markdown table file.
    """
    include_file = f"{outdir}/{basename}.md"

    relative_json_file = os.path.relpath(json_file, outdir)

    if overwrite:
        remove_if_exists(include_file)
    with EnsureDirExists(outdir):
        try:
            with open(include_file, "x") as f:
                formatted_template = MD_INCLUDE_TEMPLATE.format(
                    dp=dp,
                    json_file=relative_json_file,
                    table=(to_markdown_table(dp)),
                )
                f.write(formatted_template)
        except FileExistsError:
            logger.warning(
                f"File {include_file} already exists, use --overwrite to replace"
            )

    # update the symlink
    # because we don't want to have to edit each markdown file every time something changes
    symlink = f"{outdir}/{_filename_friendly(dp.name)}.md"
    remove_if_exists(symlink)
    relative_md_file = os.path.relpath(include_file, outdir)
    os.symlink(relative_md_file, symlink)

    result = {
        "include_file": include_file,
        "symlink": symlink,
    }

    return result


def dump_json(
    basename: str, dp: SsvcDecisionPoint, jsondir: str, overwrite: bool
) -> str:
    """
    Generate the json example for a decision point.

    Args:
        basename (str): The basename of the json example file.
        dp (SsvcDecisionPoint): The decision point to generate documentation for.
        jsondir (str): The directory to write the json example to.
        overwrite (bool): Whether to overwrite existing files.

    Returns:
        str: The path to the json example file.
    """
    json_file = f"{jsondir}/{basename}.json"
    if overwrite:
        remove_if_exists(json_file)
    with EnsureDirExists(jsondir):
        try:
            with open(json_file, "x") as f:
                f.write(dp.to_json(indent=2))
        except FileExistsError:
            logger.warning(
                f"File {json_file} already exists, use --overwrite to replace"
            )
    return json_file


def main():
    # we are going to generate three files for each decision point:
    # - a markdown table that can be used in the decision point documentation
    # - a json example that can be used in the decision point documentation
    # - a markdown file that builds an mkdocs table to switch between the markdown description and the json
    #   example using markdown-include plugin of mkdocs

    # parse command line args
    import argparse

    parser = argparse.ArgumentParser(
        description="Generate decision point documentation"
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="overwrite existing files",
        default=False,
    )

    parser.add_argument("--outdir", help="output directory", default="./tmp/md_out")
    parser.add_argument(
        "--jsondir", help="json output directory", default="./tmp/json_out"
    )
    args = parser.parse_args()

    overwrite = args.overwrite
    outdir = args.outdir
    jsondir = args.jsondir

    # for each decision point:
    for dp in REGISTERED_DECISION_POINTS:
        dump_decision_point(jsondir, outdir, dp, overwrite)


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    if not logger.hasHandlers():
        hdlr = logging.StreamHandler()
        logger.addHandler(hdlr)

    main()
