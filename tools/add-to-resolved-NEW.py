import pandas as pd
import html
import os
import markdown
import numpy as np
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))   

XLSX= "data/latest.xlsx"
# Populate resolved html page
resolved_html = f"../docs/changelog/resolved-archive.html"

# Parse text describing issue from google sheet
sheet_id = "1P6QFJaZjb-F5roWkzQXkoGFW1E95t9rge6RfNmmKozc"
sheet_gid = "0"

domain_mapping = {
    "Administrative": "ADM",
    "All Data / General": "All/NA",
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
def load_and_filter_xlsx(xlsx_path, sheet_id, sheet_gid):
    """
    Load XLSX file, rename columns, filter rows, fill missing values, and strip whitespace.
    """
    # df_monday = pd.read_excel(xlsx_path, dtype=str, usecols=['PR', 'BR', 'Domain', 'Type', 'RTDs', 'Table/Topic', 'Autoparsed?', 'ID'])
    df_monday = pd.read_excel(xlsx_path, dtype=str)
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_gid}"
    df_gsheet = pd.read_csv(url, usecols=['ID', 'Text']) 

    df = pd.merge(df_monday, df_gsheet, on='ID', how='left')  

    # Filter - only include items with RTDs == "Add to Archive"
    df = df[df['RTDs'] == 'Add to Archive']

    # Specify columns to keep
    columns_to_keep = ['ID', 'Text', 'Final BR', 'Domain', 'Table/Topic', 'Type']
    df = df[columns_to_keep]

    # Map domain values using the domain_mapping dictionary
    df["Domain"] = df["Domain"].replace(domain_mapping)

    # Fill missing values and strip whitespace 
    df = df.fillna('')
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    df.to_csv(f"data/test.csv", index=False)  

    return df

type_icons = {
    "known_issue": '<i class="fas fa-bug icon-bug"></i>',
    "pending": '<i class="fa-solid fa-rotate icon-rotate"></i>',
}

def normalize_text(text):
    """
    Strip HTML tags/entities and collapse whitespace so rendered summaries
    can be compared as plain text regardless of markup differences.
    """
    text = re.sub(r'<[^>]+>', '', text)
    text = html.unescape(text)
    return re.sub(r'\s+', ' ', text).strip().lower()

def get_existing_summaries(html_path):
    """
    Pull the plain-text Summary content already present in the resolved
    archive table (3rd <td> of each row) so we can skip re-adding items.
    """
    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    summaries = set()
    for row in re.findall(r'<tr>(.*?)</tr>', content, flags=re.DOTALL):
        cells = re.findall(r'<td>(.*?)</td>', row, flags=re.DOTALL)
        if len(cells) >= 3:
            summaries.add(normalize_text(cells[2]))
    return summaries

def build_rows(df, existing_summaries):
    """
    Build <tr> markup for each row not already present in the archive,
    sorted with the highest Final BR first.
    """
    rows_html = []
    for br, group in sorted(df.groupby("Final BR", sort=False), key=lambda kv: float(kv[0]), reverse=True):
        br_rows = []
        for _, row in group.iterrows():
            icon = type_icons.get(row["Type"], "")

            summary_html = markdown.markdown(row["Summary"], extensions=["extra", "sane_lists"])
            summary_html = re.sub(r'^<p>(.*)</p>$', r'\1', summary_html, flags=re.DOTALL)

            if normalize_text(summary_html) in existing_summaries:
                print(f"Skipping already-added item ({row['Domain']} / {row['Table/Topic']}): {row['Summary']}")
                continue

            br_rows.append("<tr>")
            br_rows.append(f"<td>{html.escape(str(row['Domain']))}</td>")
            br_rows.append(f"<td>{html.escape(str(row['Table/Topic']))}</td>")
            br_rows.append(f"<td>{icon} {summary_html}</td>")
            br_rows.append(f"<td>{html.escape(str(br))}</td>")
            br_rows.append("</tr>")

        if br_rows:
            rows_html.append(f"<!-- BR{br} -->")
            rows_html.extend(br_rows)
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
df = load_and_filter_xlsx(XLSX, sheet_id, sheet_gid)
# df.to_csv("debug.csv", index=False)

# existing_summaries = get_existing_summaries(resolved_html)
# rows_html = build_rows(df, existing_summaries)

# if rows_html:
#     insert_at_top_of_table(resolved_html, rows_html)
# else:
#     print("No new items to add - all filtered items are already in the resolved archive.")

