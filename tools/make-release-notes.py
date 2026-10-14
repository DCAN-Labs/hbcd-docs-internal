import html
import os

from utils import load_and_filter
from utils import map_type
from utils import get_type_icon
from utils import markdown_to_html
from utils import insert_into_markdown

# Generates release notes based on Final BR column
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# DEFINE BR AND INPUT/OUTPUT FILEPATHS
BR = "30.2"
XLSX= "data/latest.xlsx"
INTERNAL_MD = f"../docs/changelog/versions/BR3X/BR{BR}.md"

# FUNCTIONS (unique to release notes generation)

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
<th>Type & ID</th>
<th>Measure/Topic</th>
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
                f"<td>{type_icon} {html.escape(str(issue_id))}</td>",
                f"<td>{html.escape(str(table))}</td>",
                f"<td>{summary_html}</td>",
                "</tr>",
            ]
        )
    if current_domain is not None:
        close_table()

    return "\n".join(sections)

# WORK
df = load_and_filter(XLSX)

# Filter - only include items where Final BR == {BR}
df = df[(df['Final BR'] == BR)]

# df.to_csv(f"test.csv", index=False)

# Map the issue type and remove unsupported types.
df["MappedType"] = df["Type"].apply(map_type)
df = df[df["MappedType"].notna()]

# Convert summary Markdown to HTML.
df["SummaryHTML"] = df["Text"].apply(markdown_to_html)

# Sort by domain, and table/topic.
df = df.sort_values(
    by=[
        "Domain",
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
print(f"Release notes populated for BR {BR}")

