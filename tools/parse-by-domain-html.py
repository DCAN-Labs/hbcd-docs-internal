import pandas as pd
import html
import os
import markdown
import numpy as np
import re

os.chdir(os.path.dirname(os.path.abspath(__file__)))

XLSX= "latest.xlsx"
knownissues_html = f"../docs/changelog/knownissues.html"

# Same domain abbreviations used in add-to-resolved.py, so the Domain column
# reads the same way here as it does on the resolved archive page.
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

ROWS_PLACEHOLDER = "__KNOWN_ISSUES_ROWS__"

# Page/table structure mirrors resolved-archive.html (single sortable/filterable
# table with archive-controls, Domain as its own column).
PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Known Issues & Pending Updates</title>
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="../css/custom.css">
  <link rel="stylesheet" href="../css/tables.css">
  <style>
    body {
      margin: 3rem;
      font-family: sans-serif;
    }
    .compact-table-no-vertical-lines th:nth-child(4),
    .compact-table-no-vertical-lines td:nth-child(4) {
    text-align: center;
    }
    .br-pill {
      display: inline-block;
      padding: 2px 8px;
      font-size: 0.75em;
      font-weight: 600;
      border-radius: 999px;
      line-height: 1.4;
      white-space: nowrap;
      background-color: #e6f0ff;
      color: #1a4fb3;
    }
    .pr-pill {
      display: inline-block;
      padding: 2px 8px;
      font-size: 0.75em;
      font-weight: 600;
      border-radius: 999px;
      line-height: 1.4;
      white-space: nowrap;
      background-color: #f89781af;
    }
    .tbd-pill {
      display: inline-block;
      padding: 2px 8px;
      font-size: 0.75em;
      font-weight: 600;
      border-radius: 999px;
      line-height: 1.4;
      white-space: nowrap;
      background-color: #f1f3f5;
      color: #666;
      font-style: italic;
    }
    /* Archive controls */
    .archive-controls {
      margin: 1.5rem 0 0.75rem;
      padding: 1rem 1.1rem;
      border: 1px solid #ddd;
      border-radius: 8px;
      background: #f8f9fa;
    }

    .archive-controls-row {
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      align-items: center;
    }

    .archive-search {
      flex: 1 1 280px;
      min-width: 220px;
    }

    .archive-controls input,
    .archive-controls select,
    .archive-controls button {
      box-sizing: border-box;
      height: 38px;
      border: 1px solid #cfd4da;
      border-radius: 5px;
      background: white;
      padding: 0 0.75rem;
      font: inherit;
      font-size: 0.9rem;
    }

    .archive-controls input:focus,
    .archive-controls select:focus,
    .archive-controls button:focus {
      outline: 2px solid rgba(25, 155, 214, 0.25);
      border-color: #199bd6;
    }

    .archive-controls button {
      cursor: pointer;
      font-weight: 600;
    }

    .archive-controls button:hover {
      background: #f1f3f5;
    }

    .archive-status {
      margin-top: 0.65rem;
      font-size: 0.85rem;
      color: #666;
    }

    .archive-sort {
      cursor: pointer;
      user-select: none;
      white-space: nowrap;
    }

    .archive-sort:hover {
      text-decoration: underline;
    }

    .archive-sort::after {
      content: " ↕";
      color: #999;
      font-size: 0.8em;
    }

    .archive-sort.sorted-asc::after {
      content: " ↑";
      color: #199bd6;
    }

    .archive-sort.sorted-desc::after {
      content: " ↓";
      color: #199bd6;
    }

    .archive-empty {
      display: none;
      padding: 2rem 1rem;
      text-align: center;
      color: #777;
      font-size: 0.95rem;
    }

    .archive-highlight {
      background: #fff3cd;
      border-radius: 2px;
    }

    @media (max-width: 700px) {
      .archive-controls-row {
        align-items: stretch;
      }

      .archive-controls input,
      .archive-controls select,
      .archive-controls button {
        width: 100%;
      }

      .archive-search {
        flex-basis: 100%;
      }
    }
  </style>
</head>
<body>
  <h2>Known Issues & Pending Updates</h2>

<p>This page lists ACTIVE issues/pending updates either targeted for upcoming BRs or still pending final Workgroup/SME sign-off. Items are not considered resolved until final review and approval by Workgroup/SME. Note that items addressed in a BR are not reflected as resolved in the <a href="https://docs.hbcdstudy.org/latest/changelog/issues-updates/">public release documentation</a> until the corresponding PR is released.</p>
<div style="margin: 1.25rem 0;"> <a href="resolved-archive.html" class="archive-return-button"> <i class="fa-solid fa-clock-rotate-left"></i> View Resolved Issues Archive </a> </div>

<div class="archive-controls" aria-label="Known issues filters">
  <div class="archive-controls-row">
    <input
      id="archive-search"
      class="archive-search"
      type="search"
      placeholder="Search domain, table, or summary..."
      aria-label="Search known issues"
    >

    <select id="archive-domain" aria-label="Filter by domain">
      <option value="">All domains</option>
    </select>

    <select id="archive-br" aria-label="Filter by target">
      <option value="">All targets</option>
    </select>

    <select id="archive-type" aria-label="Filter by type">
      <option value="">All types</option>
      <option value="issue">Known Issues</option>
      <option value="update">Pending Updates</option>
    </select>
    <button id="archive-reset" type="button">Clear filters</button>
  </div>
  <div id="archive-status" class="archive-status" aria-live="polite"></div>
</div>

<p style="color: #555; text-align: center;">
<i class="fas fa-bug" style="color: #f97316;"></i> = Known Issue &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-rotate" style="color: #199bd6; font-size: 1em;"></i> = Pending Update</p>

<!-- TABLE -->
<table id="archive-table" class="compact-table-no-vertical-lines">
<thead>
<tr>
<th class="archive-sort" data-sort="domain" width="5%">Domain</th>
<th class="archive-sort" data-sort="topic" width="10%">Table/Topic</th>
<th class="archive-sort" data-sort="summary" width="70%">Summary</th>
<th class="archive-sort" data-sort="br" width="5%">Target</th></tr>
</thead>
<tbody>
""" + ROWS_PLACEHOLDER + """
</tbody>
</table>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const table = document.getElementById("archive-table");
  const tbody = table.querySelector("tbody");
  const rows = Array.from(tbody.querySelectorAll("tr"));

  const searchInput = document.getElementById("archive-search");
  const domainSelect = document.getElementById("archive-domain");
  const brSelect = document.getElementById("archive-br");
  const typeSelect = document.getElementById("archive-type");
  const resetButton = document.getElementById("archive-reset");
  const status = document.getElementById("archive-status");

  // Build filter options from the existing table.
  const domains = [...new Set(rows.map(row => row.cells[0]?.textContent.trim()).filter(Boolean))]
    .sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));

  const releases = [...new Set(rows.map(row => row.cells[3]?.textContent.trim()).filter(Boolean))]
    .sort((a, b) => b.localeCompare(a, undefined, { numeric: true }));

  domains.forEach(value => {
    domainSelect.add(new Option(value, value));
  });

  releases.forEach(value => {
    brSelect.add(new Option(value, value));
  });

  let sortColumn = null;
  let sortDirection = "asc";

  function normalize(value) {
    return value.toLowerCase().replace(/\\s+/g, " ").trim();
  }

  function applyFilters() {
    const search = normalize(searchInput.value);
    const domain = domainSelect.value;
    const br = brSelect.value;
    const type = typeSelect.value;

    let visible = 0;

    rows.forEach(row => {
      const domainValue = row.cells[0]?.textContent.trim() || "";
      const topicValue = row.cells[1]?.textContent.trim() || "";
      const summaryValue = row.cells[2]?.textContent.trim() || "";
      const brValue = row.cells[3]?.textContent.trim() || "";

      const matchesSearch =
        !search ||
        normalize(domainValue).includes(search) ||
        normalize(topicValue).includes(search) ||
        normalize(summaryValue).includes(search);

      const matchesDomain = !domain || domainValue === domain;
      const matchesBr = !br || brValue === br;
      const matchesType = !type || row.dataset.type === type;

      const show = matchesSearch && matchesDomain && matchesBr && matchesType;

      row.style.display = show ? "" : "none";
      if (show) visible++;
    });

    status.textContent =
      `Showing ${visible} of ${rows.length} record${rows.length === 1 ? "" : "s"}.`;
  }

  function sortRows(column) {
    if (sortColumn === column) {
      sortDirection = sortDirection === "asc" ? "desc" : "asc";
    } else {
      sortColumn = column;
      sortDirection = "asc";
    }

    const index = {
      domain: 0,
      topic: 1,
      summary: 2,
      br: 3
    }[column];

    rows.sort((a, b) => {
      const aValue = a.cells[index]?.textContent.trim() || "";
      const bValue = b.cells[index]?.textContent.trim() || "";

      // Numeric-aware sorting works well for releases such as 30.0, 30.1, 30.2.
      const aNum = parseFloat(aValue);
      const bNum = parseFloat(bValue);

      let comparison;
      if (column === "br" && !Number.isNaN(aNum) && !Number.isNaN(bNum)) {
        comparison = aNum - bNum;
      } else {
        comparison = aValue.localeCompare(bValue, undefined, {
          numeric: true,
          sensitivity: "base"
        });
      }

      return sortDirection === "asc" ? comparison : -comparison;
    });

    rows.forEach(row => tbody.appendChild(row));

    document.querySelectorAll(".archive-sort").forEach(header => {
      header.classList.remove("sorted-asc", "sorted-desc");
    });

    const activeHeader = document.querySelector(
      `.archive-sort[data-sort="${column}"]`
    );

    if (activeHeader) {
      activeHeader.classList.add(
        sortDirection === "asc" ? "sorted-asc" : "sorted-desc"
      );
    }

    applyFilters();
  }

  [searchInput, domainSelect, brSelect, typeSelect].forEach(control => {
    control.addEventListener("input", applyFilters);
    control.addEventListener("change", applyFilters);
  });

  resetButton.addEventListener("click", function () {
    searchInput.value = "";
    domainSelect.value = "";
    brSelect.value = "";
    typeSelect.value = "";
    applyFilters();
  });

  document.querySelectorAll(".archive-sort").forEach(header => {
    header.addEventListener("click", function () {
      sortRows(header.dataset.sort);
    });
    header.setAttribute("role", "button");
    header.setAttribute("tabindex", "0");
    header.addEventListener("keydown", function (event) {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        sortRows(header.dataset.sort);
      }
    });
  });

  // Domain order first by default, matching the prior grouped-by-domain layout.
  sortRows("domain");
});
</script>

</body>
</html>
"""

# FUNCTIONS

def load_and_filter_xlsx(xlsx_path):
    """
    Load XLSX file, rename columns, filter rows, fill missing values, and strip whitespace.
    """
    df = pd.read_excel(xlsx_path, dtype=str)
    df = df.rename(columns={
    "RTDs": "Type",
    "RTDs Text (markdown format)": "Text"})

    # Filter - only include items marked for autoparsing
    df = df[df['Autoparsed?'].str.contains('Yes')]

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

def write_html_page(html_path, rows_html):
    page = PAGE_TEMPLATE.replace(ROWS_PLACEHOLDER, rows_html)
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(page)
    print("Known issues page successfully generated.")

# Build a single flat, sortable/filterable table of rows (domain, type, table, summary, target)
def build_rows(records):
    row_parts = []

    for domain, issue_type, table, summary_html, br in records:
        data_type = "issue" if issue_type == "Issue" else "update"

        if issue_type == "Issue":
            type_icon = '<i class="fas fa-bug icon-bug"></i>'
        else:
            type_icon = '<i class="fa-solid fa-rotate icon-rotate"></i>'

        if str(br).upper() == "TBD":
            pill_class = "tbd-pill"
        elif "R" in str(br).upper():
            pill_class = "pr-pill"
        else:
            pill_class = "br-pill"

        row_parts.append(f'<tr data-type="{data_type}">')
        row_parts.append(f"<td>{html.escape(str(domain))}</td>")
        row_parts.append(f"<td>{html.escape(str(table))}</td>")
        row_parts.append(f"<td>{type_icon} {summary_html}</td>")
        row_parts.append(
            f"<td><span class='{pill_class}'>{html.escape(str(br))}</span></td>"
        )
        row_parts.append("</tr>")

    return "\n".join(row_parts)

# WORK
df = load_and_filter_xlsx(XLSX)

# Drop unecessary columns (for troubleshooting purposes)
df = df.drop(['Name'], axis=1)
df = df.drop(['Status'], axis=1)

# Extra steps for internal documentation
## Remove rows archived to BR - already documented in resolved issues page
df = df[~(df['RTDs_Status'] == 'Archived to BR')]

# Map domain values using the same abbreviations as the resolved archive page
df["Domain"] = df["Domain"].replace(domain_mapping)

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

# Build flat record list (domain, type, table, summary, target)
records = []

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

    records.append((domain, issue_type, table, summary_html, br))

# Build single sortable/filterable table (mirrors resolved-archive.html) and write page
rows_html = build_rows(records)
write_html_page(knownissues_html, rows_html)


# df.to_csv("debug.tsv", sep='\t', index=False)
