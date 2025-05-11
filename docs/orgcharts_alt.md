
## lasso alt

```mermaid
---
config:
  layout: elk
---
flowchart TB
    A["<b>Leigh MacIntyre</b>, CEO<br>MCIN Assoc. Dir., PM"] --> B(["<b>Pre-Release Training<br>Scheduling<br></b>"]) & n1(["<b>Ancillary<br>Studies</b>"]) & n2(["<b>WorkGroup<br>Data QC</b>"]) & n3(["<b>Technical</b>"]) & n4(["<b>Data<br>Loading</b>"]) & n19(["<b>Internal</b>"])
    B --> n5["<b>Ellise Elamparo</b><br>Exec Admin"]
    n1 --> n6["<b>Aarushi Chaudhry<br></b>Study Success<br>Manager"]
    n2 --> n7["<b>Jen Zink<br></b>Director,<br>Partnerships &amp; Grant<br>Funding<br><br><b>Marion Fechino</b><br>Data Analyst"]
    n3 --> n8["<b>Fraser Glen<br></b>CTO<br><br><b>Jordan<br>Sterling<br></b>Lead Dev"]
    n4 --> n9["<b>Laetitia Fesselier<br></b>Sr. Dev<br><b><br>Edson Silva</b><br><b>Mateus Andre<br></b>Dev"]
    n19 --> n21(["<b>QA</b>"]) & n22(["<b>UI/UX</b>"]) & n23(["Dev &amp; Operations"])
    n23 --> n24["<b>Francisco Soto</b><br>Dev/SysOps Manager<br><b>Alexandre Meyer</b><br>DevOps<br><b>Nataliya Korniyenko<br></b>Sys Admin"] & n25["<b>Mark Walker<br></b>Software Architect<br><b>Daniel Patularu</b><br><b>Oksana Bodnariuk<br>Jonas Vinson<br></b>Developers"]
    n22 --> n26["<b>Andrew Sawaya</b><br>Lead Designer<br><b>Mehrafarin Ekhlaspour</b><br>Visual Design"]
    n21 --> n27["<b>Vandana Sriram</b><br><b>Anjali Raj Katuri<br></b>QA Engineers"]
    style A fill:#BBDEFB,stroke:#2962FF
    style B fill:#E1BEE7,stroke:#AA00FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#E1BEE7,stroke:#AA00FF
    style n4 fill:#E1BEE7,stroke:#AA00FF
    style n19 fill:#E1BEE7,stroke:#AA00FF
    style n5 fill:#BBDEFB,stroke:#2962FF
    style n6 fill:#BBDEFB,stroke:#2962FF
    style n7 fill:#BBDEFB,stroke:#2962FF
    style n8 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n21 fill:#E1BEE7,stroke:#AA00FF
    style n22 fill:#E1BEE7,stroke:#AA00FF
    style n23 fill:#E1BEE7,stroke:#AA00FF
    style n24 fill:#BBDEFB,stroke:#2962FF
    style n25 fill:#BBDEFB,stroke:#2962FF
    style n26 fill:#BBDEFB,stroke:#2962FF
    style n27 fill:#BBDEFB,stroke:#2962FF
```

## lasso alt 2
```mermaid
---
config:
  layout: elk
---
flowchart TB
    A["<b>Leigh MacIntyre</b>, CEO<br>MCIN Assoc. Dir., PM"] --> B(["<b>Pre-Release Training<br>Scheduling<br></b>"]) & n1(["<b>Ancillary<br>Studies</b>"]) & n2(["<b>WorkGroup<br>Data QC</b>"]) & n3(["<b>Technical</b>"]) & n4(["<b>Data<br>Loading</b>"]) & n22(["<b>UI/UX</b>"]) & n21(["<b>QA</b>"]) & n23(["<b>Dev &amp; Operations</b>"])
    B --> n5["<b>Ellise Elamparo</b><br>Exec Admin"]
    n1 --> n6["<b>Aarushi Chaudhry<br></b>Study Success<br>Manager"]
    n2 --> n7["<b>Jen Zink<br></b>Director,<br>Partnerships &amp; Grant<br>Funding<br><br><b>Marion Fechino</b><br>Data Analyst"]
    n3 --> n8["<b>Fraser Glen<br></b>CTO<br><br><b>Jordan<br>Sterling<br></b>Lead Dev"]
    n4 --> n9["<b>Laetitia Fesselier<br></b>Sr. Dev<br><b><br>Edson Silva</b><br><b>Mateus Andre<br></b>Dev"]
    n23 --> n24["<b>Francisco Soto</b><br>Dev/SysOps Manager<br><b>Alexandre Meyer</b><br>DevOps<br><b>Nataliya Korniyenko<br></b>Sys Admin<br><br><b>Mark Walker<br></b>Software Architect<br><b>Daniel Patularu</b><br><b>Oksana Bodnariuk<br>Jonas Vinson<br></b>Developers"]
    n22 --> n26["<b>Andrew Sawaya</b><br>Lead Designer<br><b>Mehrafarin Ekhlaspour</b><br>Visual Design"]
    n21 --> n27["<b>Vandana Sriram</b><br><b>Anjali Raj Katuri<br></b>QA Engineers"]
    style A fill:#BBDEFB,stroke:#2962FF
    style B fill:#E1BEE7,stroke:#AA00FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#E1BEE7,stroke:#AA00FF
    style n4 fill:#E1BEE7,stroke:#AA00FF
    style n22 fill:#E1BEE7,stroke:#AA00FF
    style n21 fill:#E1BEE7,stroke:#AA00FF
    style n23 fill:#E1BEE7
    style n5 fill:#BBDEFB,stroke:#2962FF
    style n6 fill:#BBDEFB,stroke:#2962FF
    style n7 fill:#BBDEFB,stroke:#2962FF
    style n8 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n24 fill:#BBDEFB,stroke:#2962FF
    style n26 fill:#BBDEFB,stroke:#2962FF
    style n27 fill:#BBDEFB,stroke:#2962FF
```

## lasso with subgraph
```mermaid
---
config:
  layout: elk
---
flowchart TB
 subgraph s1["<b>Internal</b>"]
        n21(["<b>QA</b>"])
        n22(["<b>UI/UX</b>"])
        n23(["Dev &amp; Operations"])
        n24["<b>Francisco Soto</b><br>Dev/SysOps Manager<br><b>Alexandre Meyer</b><br>DevOps<br><b>Nataliya Korniyenko<br></b>Sys Admin<br><br><b>Mark Walker<br></b>Software Architect<br><b>Daniel Patularu</b><br><b>Oksana Bodnariuk<br>Jonas Vinson<br></b>Developers"]
        n26["<b>Andrew Sawaya</b><br>Lead Designer<br><b>Mehrafarin Ekhlaspour</b><br>Visual Design"]
        n27["<b>Vandana Sriram</b><br><b>Anjali Raj Katuri<br></b>QA Engineers"]
  end
    A["<b>Leigh MacIntyre</b>, CEO<br>MCIN Assoc. Dir., PM"] --> B(["<b>Pre-Release Training<br>Scheduling<br></b>"]) & n1(["<b>Ancillary<br>Studies</b>"]) & n2(["<b>WorkGroup<br>Data QC</b>"]) & n3(["<b>Technical</b>"]) & n4(["<b>Data<br>Loading</b>"]) & s1
    B --> n5["<b>Ellise Elamparo</b><br>Exec Admin"]
    n1 --> n6["<b>Aarushi Chaudhry<br></b>Study Success<br>Manager"]
    n2 --> n7["<b>Jen Zink<br></b>Director,<br>Partnerships &amp; Grant<br>Funding<br><br><b>Marion Fechino</b><br>Data Analyst"]
    n3 --> n8["<b>Fraser Glen<br></b>CTO<br><br><b>Jordan<br>Sterling<br></b>Lead Dev"]
    n4 --> n9["<b>Laetitia Fesselier<br></b>Sr. Dev<br><b><br>Edson Silva</b><br><b>Mateus Andre<br></b>Dev"]
    n23 --> n24
    n22 --> n26
    n21 --> n27
    style n21 fill:#E1BEE7,stroke:#AA00FF
    style n22 fill:#E1BEE7,stroke:#AA00FF
    style n23 fill:#E1BEE7,stroke:#AA00FF
    style n24 fill:#BBDEFB,stroke:#2962FF
    style n26 fill:#BBDEFB,stroke:#2962FF
    style n27 fill:#BBDEFB,stroke:#2962FF
    style A fill:#BBDEFB,stroke:#2962FF
    style B fill:#E1BEE7,stroke:#AA00FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#E1BEE7,stroke:#AA00FF
    style n4 fill:#E1BEE7,stroke:#AA00FF
    style s1 stroke:#000000
    style n5 fill:#BBDEFB,stroke:#2962FF
    style n6 fill:#BBDEFB,stroke:#2962FF
    style n7 fill:#BBDEFB,stroke:#2962FF
    style n8 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
```


## Columbia University

```mermaid
---
config:
  theme: redux
---
flowchart TD
    A["<b>William P. Fifer</b>
    Co-chair of Novel Technologies/Wearables Working Group (Subaward PI)"] --> n1["<b>Nicolo Pini</b><br>Co-Investigator"] & n2["<b>Liana Eisler</b>
    Technician Research Assistant"]
    C["<b>Dima Amso</b>
    Co-Investigator"]
    A@{ shape: rounded}
    n1@{ shape: rounded}
    n2@{ shape: rounded}
    C@{ shape: rounded}
```


## LIBR

<div id="table-banner" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Data Dictionary Column Definitions</span>
  <span class="arrow">▸</span>
</div>
<div class="table-open-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
    <thead>
      <tr>
        <th style="width: 15%; border: 1px solid #ddd; padding: 5px; text-align: center;">Name</th>
        <th style="width: 5%; border: 1px solid #ddd; padding: 5px; text-align: center;">Title</th>
        <th style="width: 30%; border: 1px solid #ddd; padding: 5px; text-align: center;">Role on HDCC</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Jim Wilgenbusch</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Director of Research Computing in the Research & Innovation Office, UMN</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Administration</td>
    </tr>
</tbody>
</table>
</div>

