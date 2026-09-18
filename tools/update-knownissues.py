import pandas as pd
import html
import os
import markdown
import numpy as np
import re
from datetime import datetime
from utils import load_and_filter

# NEW VERSION OF parse-by-domains.py that parses text documenting issues from a separate google sheet and matches issue based on ID#
os.chdir(os.path.dirname(os.path.abspath(__file__)))   

XLSX= "data/latest.xlsx"
# Parse text describing issue from google sheet
sheet_id = "1P6QFJaZjb-F5roWkzQXkoGFW1E95t9rge6RfNmmKozc"
sheet_gid = "0"
# Populate known issues page
INTERNAL_MD = "../docs/changelog/knownissues.md"

# FUNCTIONS

def map_type(value):
    if "issue" in value:
        return "Issue"
    elif "pending" in value:
        return "Pending Update"
    return None

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

    table_parts.append(f"\n### {html.escape(domain)}")
    table_parts.append("""
<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>
""")

    for issue_type, table, summary_html, br in rows:
        table_parts.append("<tr>")
        if issue_type == "Issue":
            type_label = '<i class="fas fa-bug icon-bug"></i>'
        else:
            type_label = '<i class="fa-solid fa-rotate icon-rotate"></i>'
        table_parts.append(f"<td>{type_label}</td>")
        table_parts.append(f"<td>{html.escape(str(table))}</td>")
        table_parts.append(f"<td>{summary_html}</td>")
        table_parts.append(
            f"<td style='text-align: center;'><span class='pill'>{html.escape(str(br))}</span></td>"
        )
        table_parts.append("</tr>")
    table_parts.append("</tbody></table>")

    return "\n".join(table_parts)

# WORK
df = load_and_filter(XLSX, sheet_id, sheet_gid)

# Extra steps for internal documentation: Remove rows archived to BR - already documented in resolved issues page
df = df[~(df['RTDs'] == 'Archived to BR')]
df = df[~(df['RTDs'] == 'Add to archive')]

# Prefix PR values
df.loc[df['PR'] != '', 'PR'] = 'R' + df.loc[df['PR'] != '', 'PR']

# Treat empty strings as NaN and fill BR with PR where missing, then fill remaining with TBD
df['BR'] = df['BR'].replace('', np.nan)
df['BR'] = df['BR'].fillna(df['PR'])
df['BR'] = df['BR'].replace('', np.nan)
df['BR'] = df['BR'].fillna('TBD')

# For BR values, if missing "., add it to the end of the string
df['BR'] = df['BR'].apply(lambda x: str(x) + '.0' if str(x) != 'TBD' and '.' not in str(x) else str(x))

# Drop PR column for troubleshooting
df = df.drop(['PR'], axis=1)

# Type mapping and sort by (1) domain, (2) table/topic
df["MappedType"] = df["Type"].apply(map_type)
df = df[df["MappedType"].notna()]
df = df.sort_values(by=['Domain', 'Table/Topic'])

# Build grouped structure (by domain only)
grouped_by_domain = {}

for _, row in df.iterrows():
    domain = row["Domain"]
    issue_type = row["MappedType"]
    table = row["Table/Topic"]
    summary_md = row["Text"]
    br = row["BR"]

    # Convert Markdown → HTML & strip outer <p>
    summary_html = markdown.markdown(
        summary_md,
        extensions=["extra", "sane_lists"]
    )
    summary_html = re.sub(r'^<p>(.*)</p>$', r'\1', summary_html, flags=re.DOTALL)

    grouped_by_domain.setdefault(domain, []).append(
        (issue_type, table, summary_html, br)
    )

# Generate known issues and pending tables for internal page
table_configs = [
    ("Issue",
     '<i class="fas fa-bug icon-bug"></i> Known Issues'),
    ("Pending Update",
     '<i class="fa-solid fa-rotate icon-rotate"></i> Pending Updates'),
]

def build_combined_tables():
    tables = []

    for domain in sorted(grouped_by_domain.keys()):
        rows = grouped_by_domain[domain]
        # Sort within domain by Target (BR), then type, then Table/Topic
        rows = sorted(rows, key=lambda x: (target_sort_key(x[3]), x[0], x[1]))
        tables.append(build_table(domain, rows))

    return "\n\n".join(tables)

# Make table and insert into markdown
combined_tables_html_int = build_combined_tables()
insert_into_markdown(INTERNAL_MD, combined_tables_html_int)


# df.to_csv("debug.tsv", sep='\t', index=False)
