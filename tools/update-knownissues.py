import html
import os
import markdown
import numpy as np
import re
from utils import load_and_filter
from utils import map_type

# NEW VERSION OF parse-by-domains.py that parses text documenting issues from a separate google sheet and matches issue based on ID#
os.chdir(os.path.dirname(os.path.abspath(__file__)))   

XLSX= "data/latest.xlsx"
INTERNAL_MD = "../docs/changelog/knownissues-alt.md"

# FUNCTIONS

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

    table_parts.append(f"<h3>{html.escape(domain)}</h3>")
    table_parts.append("""
<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>
""")

    for issue_type, issue_id, table, summary_html, br, is_resolved in rows:
        # Keep resolved rows in the page so readers can reveal them.
        row_attrs = ' data-known-issue-row data-resolved="true" hidden' if is_resolved else ' data-known-issue-row data-resolved="false"'
        table_parts.append(f"<tr{row_attrs}>")
        if is_resolved:
            type_label = '<i class="fa-solid fa-circle-check" style="color: #2e7d32;" title="Resolved"></i>'
        elif issue_type == "Issue":
            type_label = '<i class="fas fa-bug icon-bug"></i>'
        else:
            type_label = '<i class="fa-solid fa-rotate icon-rotate"></i>'
        table_parts.append(f"<td>{type_label} {html.escape(str(issue_id))}</td>")
        table_parts.append(f"<td>{html.escape(str(table))}</td>")
        table_parts.append(f"<td>{summary_html}</td>")
        table_parts.append(
            f"<td style='text-align: center;'><span class='pill'>{html.escape(str(br))}</span></td>"
        )
        table_parts.append("</tr>")
    table_parts.append("</tbody></table>")

    return "\n".join(table_parts)

# WORK
df = load_and_filter(XLSX)

# Remove rows archived to BR - already documented in resolved issues page.
# ARCHIVE rows are included but hidden by default; the page filter reveals them.
df['Autoparsed?'] = df['Autoparsed?'].fillna('').astype(str).str.strip().str.upper()
df = df[df['Autoparsed?'] != 'ARCHIVED']

# Prefix PR values
df.loc[df['PR'] != '', 'PR'] = 'R' + df.loc[df['PR'] != '', 'PR']

# Build Target column: Final BR first, then fill blanks with BR, then PR, then TBD
df['Final BR'] = df['Final BR'].replace('', np.nan)
df['BR'] = df['BR'].replace('', np.nan)
df['PR'] = df['PR'].replace('', np.nan)
df['BR'] = df['Final BR'].fillna(df['BR']).fillna(df['PR']).fillna('TBD')

# For BR values, if missing ".0", add it to the end of the string
df['BR'] = df['BR'].apply(lambda x: str(x) + '.0' if str(x) != 'TBD' and '.' not in str(x) else str(x))

# Type mapping and sort by (1) domain, (2) table/topic
df["MappedType"] = df["Type"].apply(map_type)
df = df[df["MappedType"].notna()]
df = df.sort_values(by=['BR', 'Domain', 'Table/Topic'])

# Build grouped structure (by domain only)
grouped_by_domain = {}

for _, row in df.iterrows():
    domain = row["Domain"]
    issue_type = row["MappedType"]
    issue_id = row["ID"]
    table = row["Table/Topic"]
    summary_md = row["Text"]
    br = row["BR"]
    is_resolved = row["Autoparsed?"] == "ARCHIVE"

    # Convert Markdown → HTML & strip outer <p>
    summary_html = markdown.markdown(
        summary_md,
        extensions=["extra", "sane_lists"]
    )
    summary_html = re.sub(r'^<p>(.*)</p>$', r'\1', summary_html, flags=re.DOTALL)

    grouped_by_domain.setdefault(domain, []).append(
        (issue_type, issue_id, table, summary_html, br, is_resolved)
    )

# Generate known issues and pending tables for internal page
table_configs = [
    ("Issue",
     '<i class="fas fa-bug icon-bug"></i> Known Issues'),
    ("Pending Update",
     '<i class="fa-solid fa-rotate icon-rotate"></i> Pending Updates'),
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
        'No issues or pending updates match the current filter.</p>'
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


# df.to_csv("debug.tsv", sep='\t', index=False)


