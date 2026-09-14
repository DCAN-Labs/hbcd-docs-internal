import pandas as pd
import html
import os
import markdown
import numpy as np
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))   

XLSX= "latest.xlsx"
resolved_html = f"../docs/changelog/resolved-archive.html"

domain_mapping = {
    "All Data / General": "NA",
    "Behavior & Child-Caregiver Interaction": "MH",
    "Biospecimens & Omics": "BIO",
    "Demographics": "Demo",
    "Neurocognition & Language": "NCL",
    "Novel Tech & Wearable Sensors": "NT",
    "Physical Health": "PH",
    "Pregnancy & Environmental Exposure": "PEX",
    "Social & Environmental Determinants": "SED"
}

# FUNCTIONS
def load_and_filter_xlsx(xlsx_path):
    """
    Load XLSX file, rename columns, filter rows, fill missing values, and strip whitespace.
    """
    df = pd.read_excel(xlsx_path, dtype=str)
    df = df.rename(columns={
    "RTDs": "Type",
    "RTDs Text (markdown format)": "Summary"})

    # Filter - only include items with RTDs_Status == "Archived to BR"
    df = df[df['RTDs_Status'] == 'Archived to BR']

    # Specify columns to keep
    columns_to_keep = ['Domain', 'Table/Topic', 'Type',  'Summary', 'Final BR']
    df = df[columns_to_keep]

    # Map domain values using the domain_mapping dictionary
    df["Domain"] = df["Domain"].replace(domain_mapping)

    # Fill missing values and strip whitespace 
    df = df.fillna('')
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    return df

type_icons = {
    "known_issue": '<i class="fas fa-bug icon-bug"></i>',
    "pending": '<i class="fa-solid fa-rotate icon-rotate"></i>',
}

def build_rows(df):
    """
    Build <tr> markup for each row, sorted with the highest Final BR first.
    """
    rows_html = []
    for br, group in sorted(df.groupby("Final BR", sort=False), key=lambda kv: float(kv[0]), reverse=True):
        rows_html.append(f"<!-- BR{br} -->")
        for _, row in group.iterrows():
            icon = type_icons.get(row["Type"], "")

            summary_html = markdown.markdown(row["Summary"], extensions=["extra", "sane_lists"])
            summary_html = re.sub(r'^<p>(.*)</p>$', r'\1', summary_html, flags=re.DOTALL)

            rows_html.append("<tr>")
            rows_html.append(f"<td>{html.escape(str(row['Domain']))}</td>")
            rows_html.append(f"<td>{html.escape(str(row['Table/Topic']))}</td>")
            rows_html.append(f"<td>{icon} {summary_html}</td>")
            rows_html.append(f"<td>{html.escape(str(br))}</td>")
            rows_html.append("</tr>")
    return "\n".join(rows_html)

def insert_at_top_of_table(html_path, rows_html):
    """
    Insert new rows immediately after the opening <tbody> tag, i.e. at the
    top of the table, since the table is sorted with the highest/most
    recent BR first.
    """
    TBODY_TAG = "<tbody>"

    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    insert_index = content.find(TBODY_TAG) + len(TBODY_TAG)

    new_content = (
        content[:insert_index]
        + "\n\n" + rows_html + "\n"
        + content[insert_index:]
    )
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Resolved archive table successfully updated.")

# WORK
df = load_and_filter_xlsx(XLSX)
# df.to_csv("debug.csv", index=False)

rows_html = build_rows(df)
insert_at_top_of_table(resolved_html, rows_html)

