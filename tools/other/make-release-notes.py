import html
import os
import re

import markdown
import pandas as pd


os.chdir(os.path.dirname(os.path.abspath(__file__)))

# DEFINE BR AND OUTPUT FILEPATH
BR = "30.0"

XLSX = "latest.xlsx"
INTERNAL_MD = f"../docs/changelog/versions/BR3X/BR{BR}.md"


DOMAIN_NAME_MAP = {
    "Demographics": "Demo",
    "Behavior & Child-Caregiver Interaction": "MH",
    "Neurocognition & Language": "NCL",
    "Novel Tech & Wearable Sensors": "NT",
    "Physical Health": "PH",
    "Social & Environmental Determinants": "SED"
}

# FUNCTIONS

def load_and_filter_xlsx(xlsx_path):
    """
    Load the XLSX file, rename columns, filter rows, fill missing
    values, and strip whitespace.
    """
    df = pd.read_excel(xlsx_path, dtype=str)

    df = df.rename(
        columns={
            "RTDs": "Type",
            "RTDs Text (markdown format)": "Text",
        }
    )

    # Only include items marked for autoparsing.
    df = df[
        df["Autoparsed?"].str.contains(
            "Yes",
            case=False,
            na=False,
        )
    ]

    # Fill missing values and strip whitespace.
    df = df.fillna("")
    df = df.apply(
        lambda column: (
            column.str.strip()
            if column.dtype == "object"
            else column
        )
    )

    return df


def map_type(value):
    """
    Convert the source RTDs type to the label used in the table.
    """
    value = str(value).lower()

    if "issue" in value:
        return "Issue"

    if "pending" in value:
        return "Pending Update"

    return None


def markdown_to_html(value):
    """
    Convert Markdown to HTML - remove outer paragraph wrapper when present
    """
    converted = markdown.markdown(
        str(value),
        extensions=["extra", "sane_lists"],
    )

    return re.sub(
        r"^<p>(.*)</p>$",
        r"\1",
        converted,
        flags=re.DOTALL,
    )

def get_type_icon(issue_type):
    """
    Define icons for issues vs pending updates
    """
    if issue_type == "Issue":
        return '<i class="fas fa-bug icon-bug"></i>'

    return '<i class="fa-solid fa-rotate icon-rotate"></i>'


def build_table(rows):
    """
    Build HTML table with Domain, Table/Topic, and Summary columns (with issue-type icons embedded in Table/Topic)
    """
    table_parts = [
        """
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Domain</th>
<th>Table/Topic</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
"""
    ]

    for issue_type, domain, table, summary_html in rows:
        type_icon = get_type_icon(issue_type)

        table_parts.extend(
            [
                "<tr>",
                f"<td>{html.escape(str(domain))}</td>",
                (
                    f"<td>{type_icon} "
                    f"{html.escape(str(table))}</td>"
                ),
                f"<td>{summary_html}</td>",
                "</tr>",
            ]
        )

    table_parts.append("</tbody>")
    table_parts.append("</table>")

    return "\n".join(table_parts)

def insert_into_markdown(md_path, table_html):
    """
    Replace the content between the known-issues table markers.
    """
    start_marker = "<!-- BEGIN KNOWN_ISSUES_TABLE -->"
    end_marker = "<!-- END KNOWN_ISSUES_TABLE -->"

    with open(md_path, "r", encoding="utf-8") as file:
        content = file.read()

    start_index = content.find(start_marker)
    end_index = content.find(end_marker)

    if start_index == -1 or end_index == -1:
        raise ValueError(
            "Could not find the known-issues table markers in "
            f"{md_path}."
        )

    if end_index < start_index:
        raise ValueError(
            "The known-issues table end marker appears before "
            "the start marker."
        )

    end_index += len(end_marker)

    replacement = (
        f"{start_marker}\n"
        f"{table_html}\n"
        f"{end_marker}"
    )

    new_content = (
        content[:start_index]
        + replacement
        + content[end_index:]
    )

    with open(md_path, "w", encoding="utf-8") as file:
        file.write(new_content)

    print("Known issues table successfully updated.")


# WORK

df = load_and_filter_xlsx(XLSX)

df["Domain"] = df["Domain"].replace(DOMAIN_NAME_MAP)

# Sort by domain, issue type, and table/topic.
# df = df.sort_values(
#     by=[
#         "Domain",
#         "TypeSortOrder",
#         "Table/Topic",
#     ],
#     key=lambda column: (
#         column.str.lower()
#         if column.dtype == "object"
#         else column
#     ),
# )

# Drop unnecessary columns when present.
df = df.drop(
    columns=["Name", "Status", "PR"],
    errors="ignore",
)

# Remove rows already documented on the resolved issues page.
df = df[df["RTDs_Status"] != "Archived to BR"]

# Normalize BR values, such as "30" to "30.0".
df["BR"] = df["BR"].apply(
    lambda value: (
        f"{value}.0"
        if "." not in str(value)
        else str(value)
    )
)

# Keep only rows matching the specified BR.
df = df[df["BR"] == BR]

# Map the issue type and remove unsupported types.
df["MappedType"] = df["Type"].apply(map_type)
df = df[df["MappedType"].notna()]

# Convert summary Markdown to HTML.
df["SummaryHTML"] = df["Text"].apply(markdown_to_html)

# Control the order in which issue types appear.
type_sort_order = {
    "Issue": 0,
    "Pending Update": 1,
}

df["TypeSortOrder"] = df["MappedType"].map(type_sort_order)

# Sort by type, domain, and table/topic.
df = df.sort_values(
    by=[
        "Domain",
        "TypeSortOrder",
        "Table/Topic",
    ],
    key=lambda column: (
        column.str.lower()
        if column.dtype == "object"
        else column
    ),
)

# Prepare rows for the single combined table.
table_rows = [
    (
        row["MappedType"],
        row["Domain"],
        row["Table/Topic"],
        row["SummaryHTML"],
    )
    for _, row in df.iterrows()
]

# Generate and insert the table.
combined_table_html = build_table(table_rows)
insert_into_markdown(INTERNAL_MD, combined_table_html)

