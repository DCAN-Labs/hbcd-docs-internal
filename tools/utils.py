import re
import markdown
import pandas as pd
from datetime import datetime


def load_and_filter(sheet_id, sheet_gid):

    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_gid}"
    df = pd.read_csv(url, dtype=str) 
    
    # Fill missing values and strip whitespace
    df = df.fillna('')
    df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)

    return df

def map_type(value):
    if "issue" in value:
        return "Issue"
    elif "pending" in value:
        return "Pending Update"
    return None

def get_type_icon(issue_type):
    if issue_type == "Issue":
        return '<i class="fas fa-bug icon-bug"></i>'

    return '<i class="fa-solid fa-rotate icon-rotate"></i>'

def markdown_to_html(value):
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

def insert_into_markdown(md_path, table_html):
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