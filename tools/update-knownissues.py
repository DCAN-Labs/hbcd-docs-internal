import html
import os
import markdown
import numpy as np
import pandas as pd
import re
from utils import load_and_filter

os.chdir(os.path.dirname(os.path.abspath(__file__)))   

# https://docs.google.com/spreadsheets/d/1P6QFJaZjb-F5roWkzQXkoGFW1E95t9rge6RfNmmKozc/edit?gid=0#gid=0

BR_latest = "30.2"
sheet_id = "1P6QFJaZjb-F5roWkzQXkoGFW1E95t9rge6RfNmmKozc"
sheet_gid = "0"
INTERNAL_MD = "../docs/changelog/knownissues.md"

# FUNCTIONS

# def map_type(value):
#     if "issue" in value:
#         return "Issue"
#     elif "pending" in value:
#         return "Update"
#     elif "resolved" in value:
#         return "Resolved"
#     return None

def target_sort_key(br):
    """Sort Target (BR) values numerically ascending, with TBD sorted last."""
    br = str(br)
    if br.upper() == "TBD":
        return (1, 0.0)
    numeric_part = br[1:] if br.upper().startswith("R") else br
    try:
        return (0, float(numeric_part))
    except ValueError:
        return (0, numeric_part)

def insert_into_markdown(md_path, combined_html):
    START_MARKER = "<!-- BEGIN KNOWN_ISSUES_TABLE -->"
    END_MARKER = "<!-- END KNOWN_ISSUES_TABLE -->"

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    start_index = content.find(START_MARKER)
    end_index = content.find(END_MARKER)
    end_index += len(END_MARKER)

    new_content = (
        content[:start_index]
        + START_MARKER
        + combined_html
        + END_MARKER
        + content[end_index:]
    )

    with open(md_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Known issues table successfully updated.")

# Generate HTML tables 

def build_table(domain, rows):
    table_parts = []

    table_parts.append(f"### {html.escape(str(domain))}")
    table_parts.append("""
<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th>Status</th><th>Table/Topic</th><th>Summary</th>
<th>BR</th></tr>
</thead>
<tbody>
""")

    for issue_id, table, summary_html, br, is_resolved, status in rows:
        status_pill_style = "pill open" if status == "Open" else "pill pending" if status == "Pending" else "pill resolved" if status == "Resolved" else "pill"
        # Keep resolved rows in the page so readers can reveal them.
        row_attrs = ' data-known-issue-row data-resolved="true" hidden' if is_resolved else ' data-known-issue-row data-resolved="false"'
        table_parts.append(f"<tr{row_attrs}>")
        table_parts.append(
            f"<td><span class='{status_pill_style}'>{html.escape(str(status))}</span></td>"
        )
        table_parts.append(f"<td>{html.escape(str(table))}</td>")
        table_parts.append(f"<td>{summary_html} (<b>{html.escape(str(issue_id))}</b>)</td>")
        table_parts.append(
            f"<td style='text-align: center;'><span class=pill>{html.escape(str(br))}</span></td>"
        )
        table_parts.append("</tr>")
    table_parts.append("</tbody></table>")

    return "\n".join(table_parts)

# WORK
df = load_and_filter(sheet_id, sheet_gid)

# Filter out rows where "Status on RTDs" equals Excluded
df=df[df['Status on RTDs'] != 'Excluded']

# Save local copy for versioning
df.to_csv("data/latest-gsheet-derived.tsv", sep='\t', index=False)

# for rows where df['Status on RTDs'] == 'Resolved', set the 'type' to 'resolved'
df.loc[df['Status on RTDs'] == 'Resolved', 'Type'] = 'resolved'

# Prefix PR values
df.loc[df['PR'] != '', 'PR'] = 'R' + df.loc[df['PR'] != '', 'PR']

# Clear BR values at or below the latest release.
br_numeric = pd.to_numeric(df['BR'], errors='coerce')
df.loc[br_numeric <= float(BR_latest), 'BR'] = ''

# Build Target column: Final BR first, then fill blanks with BR, then PR, then TBD if still blank
df['Final BR'] = df['Final BR'].replace('', np.nan)
df['BR'] = df['BR'].replace('', np.nan)
df['PR'] = df['PR'].replace('', np.nan)
df['BR'] = df['Final BR'].fillna(df['BR']).fillna(df['PR']).fillna('TBD')

# For BR values, if missing ".0", add it to the end of the string
df['BR'] = df['BR'].apply(lambda x: str(x) + '.0' if str(x) != 'TBD' and '.' not in str(x) else str(x))

# Type mapping and sort by (1) domain, (2) table/topic
# df["MappedType"] = df["Type"].apply(map_type)
# df = df[df["MappedType"].notna()]
# df = df.sort_values(by=['BR', 'Domain', 'Table/Topic'])

# Build grouped structure (by domain only)
grouped_by_domain = {}

for _, row in df.iterrows():
    domain = row["Domain"]
    issue_id = row["ID"]
    table = row["Table/Topic"]
    summary_md = row["Text"]
    br = row["BR"]
    status = row["Status on RTDs"]
    is_resolved = status == "Resolved"

    # Convert Markdown → HTML & strip outer <p>
    summary_html = markdown.markdown(
        summary_md,
        extensions=["extra", "sane_lists"]
    )
    summary_html = re.sub(r'^<p>(.*)</p>$', r'\1', summary_html, flags=re.DOTALL)

    grouped_by_domain.setdefault(domain, []).append(
        (issue_id, table, summary_html, br, is_resolved, status)
    )

# Generate known issues and updates tables for internal page
table_configs = [
    ("Issue",
     '<i class="fas fa-bug icon-bug"></i> Known Issues'),
    ("Update",
     '<i class="fa-solid fa-rotate icon-rotate"></i> Updates'),
]

def build_combined_tables():
    # Inline change handling works after MkDocs instant navigation too, without
    # a separate JavaScript file or document-ready initialization.
    filter_handler = """
const container = this.closest('[data-known-issues]');
container.querySelectorAll('[data-known-issue-row][data-resolved="true"]').forEach(row => {
    row.hidden = !this.checked;
});
container.querySelectorAll('[data-known-issue-domain]').forEach(section => {
    section.hidden = !section.querySelector('[data-known-issue-row]:not([hidden])');
});
container.querySelector('[data-known-issues-empty]').hidden =
    !!container.querySelector('[data-known-issue-row]:not([hidden])');
""".strip()
    tables = [
        '<div class="known-issues" data-known-issues markdown="1">',
        # Override theme table-row display rules when a row is hidden.
        '<style>.known-issues [hidden] { display: none !important; }</style>',
        '<p><label><input type="checkbox" autocomplete="off" '
        f'onchange="{html.escape(filter_handler, quote=True)}"> '
        'Show resolved issues</label></p>',
    ]
    has_open_issues = any(
        not row[5] for rows in grouped_by_domain.values() for row in rows
    )
    empty_hidden = " hidden" if has_open_issues else ""
    tables.append(
        f'<p data-known-issues-empty role="status"{empty_hidden}>'
        'No issues or updates match the current filter.</p>'
    )

    for domain in sorted(grouped_by_domain.keys()):
        rows = grouped_by_domain[domain]
        
        # Sort within domain by Target (BR), then type, then Table/Topic
        rows = sorted(rows, key=lambda x: (target_sort_key(x[4]), x[0], x[1]))
        domain_hidden = "" if any(not row[5] for row in rows) else " hidden"
        tables.append(f'<div data-known-issue-domain markdown="1"{domain_hidden}>')
        tables.append(build_table(domain, rows))
        tables.append('</div>')

    tables.append('</div>')
    return "\n\n".join(tables)

# Make table and insert into markdown
combined_tables_html_int = build_combined_tables()
insert_into_markdown(INTERNAL_MD, combined_tables_html_int)





