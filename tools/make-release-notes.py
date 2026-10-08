import html
import os
import re

import markdown
import pandas as pd
from utils import load_and_filter

# Generates release notes based on Final BR column

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# DEFINE BR AND OUTPUT FILEPATH
BR = "30.2"

XLSX= "data/latest.xlsx"
# Parse text describing issue from google sheet
sheet_id = "1P6QFJaZjb-F5roWkzQXkoGFW1E95t9rge6RfNmmKozc"
sheet_gid = "0"
# Populate known issues page
INTERNAL_MD = f"../docs/changelog/versions/BR3X/BR{BR}.md"

# FUNCTIONS

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
    Convert Markdown to HTML and remove an outer paragraph wrapper
    when present.
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
    Define icons for issues and pending updates.
    """
    if issue_type == "Issue":
        return '<i class="fas fa-bug icon-bug"></i>'

    return '<i class="fa-solid fa-rotate icon-rotate"></i>'

def build_domain_sections(rows):
    sections = []
    current_domain = None
    table_parts = []

    def close_table():
        if table_parts:
            table_parts.extend([
                "</tbody>",
                "</table>",
            ])
            sections.append("\n".join(table_parts))

    for issue_type, domain, issue_id, table, summary_html in rows:
        if domain != current_domain:
            if current_domain is not None:
                close_table()
            current_domain = domain
            sections.append(
                f"#### {html.escape(str(domain))}"
            )
            table_parts = [
                """
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>ID</th>
<th>Table/Topic</th>
<th>Summary</th>
</tr>
</thead>
<tbody>
"""
            ]

        type_icon = get_type_icon(issue_type)
        table_parts.extend(
            [
                "<tr>",
                f"<td>{html.escape(str(issue_id))}</td>",
                (
                    f"<td>{type_icon} "
                    f"{html.escape(str(table))}</td>"
                ),
                f"<td>{summary_html}</td>",
                "</tr>",
            ]
        )
    if current_domain is not None:
        close_table()

    return "\n\n".join(sections)

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

    print(f"Release notes populated for BR {BR}")


# WORK
df = load_and_filter(XLSX, sheet_id, sheet_gid)

# Extra step for release notes: only keep rows where Final BR == {BR}
df = df[(df['Final BR'] == BR)]

# Normalize BR values, such as "30" to "30.0".
# df["BR"] = df["BR"].apply(
#     lambda value: (
#         f"{value}.0"
#         if "." not in str(value)
#         else str(value)
#     )
# )

# Map the issue type and remove unsupported types.
df["MappedType"] = df["Type"].apply(map_type)
df = df[df["MappedType"].notna()]

# Convert summary Markdown to HTML.
df["SummaryHTML"] = df["Text"].apply(markdown_to_html)

# Control the order in which issue types appear within each domain.
type_sort_order = {
    "Issue": 0,
    "Pending Update": 1,
}

df["TypeSortOrder"] = df["MappedType"].map(type_sort_order)

# Sort by domain, issue type, and table/topic.
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

# Prepare rows for the combined table.
table_rows = [
    (
        row["MappedType"],
        row["Domain"],
        row["ID"],
        row["Table/Topic"],
        row["SummaryHTML"],
    )
    for _, row in df.iterrows()
]

# Generate and insert domain subsections.
domain_sections = build_domain_sections(table_rows)
insert_into_markdown(INTERNAL_MD, domain_sections)