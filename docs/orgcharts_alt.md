## Lasso

```mermaid
---
config:
  theme: redux
---
flowchart TB
    A["<b>Leigh MacIntyre</b><br>CEO<br>MCIN Assoc. Dir., PM"] --> B(["<b>Pre-Release Training<br>Scheduling<br></b>"]) & n1(["<b>Ancillary Studies</b>"]) & n2(["<b>WorkGroup<br>Data QC</b>"]) & n3(["<b>Technical</b>"]) & n4(["<b>Data Loading</b>"]) & n18@{ label: "<b><u>Internal</u><br></b><span style=\"--tw-scale-x:\">Dev<br style=\"--tw-scale-x:\">QA<br style=\"--tw-scale-x:\">Dev/SysOps<br style=\"--tw-scale-x:\">UI/UX</span><b></b>" }
    B --> n5["<b>Ellise Elamparo</b><br>Exec Admin"]
    n1 --> n6["<b>Aarushi Chaudhry<br></b>Study Success Manager"]
    n2 --> n7["<b>Jen Zink<br></b>Director,<br>Partnerships &amp; Grant<br>Funding<br><br><b>Marion Fechino</b><br>Data Analyst"]
    n3 --> n8["<b>Fraser Glen<br></b>CTO<br><br><b>Jordan Sterling<br></b>Lead Developer"]
    n4 --> n9["<b>Edson Silva<br></b>Developer<br><br><b>Laetitia Fesselier<br></b>Sr. Developer<br><br><b>Mateus Andre<br></b>Developer"]
    A@{ shape: text}
    n18@{ shape: rounded}
    n5@{ shape: text}
    n6@{ shape: text}
    n7@{ shape: text}
    n8@{ shape: text}
    n9@{ shape: text}
    style A fill:#BBDEFB
    style B fill:#E1BEE7
    style n1 fill:#E1BEE7
    style n2 fill:#E1BEE7
    style n3 fill:#E1BEE7
    style n4 fill:#E1BEE7
    style n18 fill:#E1BEE7
    style n5 fill:#BBDEFB
    style n6 fill:#BBDEFB
    style n7 fill:#BBDEFB
    style n8 fill:#BBDEFB
    style n9 fill:#BBDEFB
    click n18 "#internal-non-consortium-facing"
```


### Internal (Non-Consortium-Facing)
```mermaid
---
config:
  theme: redux
---
flowchart TB
    B(["<b>Development</b>"]) --> n5["<b>Mark Walker<br></b>Software Architect<br><br><b>Daniel Patularu</b><br><b>Oksana Bodnariuk<br>Jonas Vinson<br></b>Developers"]
    n1(["<b>QA</b>"]) --> n6["<b>Vandana Sriram</b><br><b>Anjali Raj Katuri<br></b>QA Engineers"]
    n3(["<b>Dev Ops/Sys Ops</b>"]) --> n8@{ label: "<b>Francisco Soto<br></b>Manager<br><br><span style=\"--tw-scale-x:\"><b>Alexandre Meyer<br style=\"--tw-scale-x:\"></b></span>DevOps Engineer<br><br><span style=\"--tw-scale-x:\"><b>Nataliya Korniyenko<br style=\"--tw-scale-x:\"></b></span>Sys Admin" }
    n4(["<b>UI/UX</b>"]) --> n9@{ label: "<b>Andrew Sawaya<br></b>Lead Designer<br><br><span style=\"--tw-scale-x:\"><b>Mehrafarin Ekhlaspour<br style=\"--tw-scale-x:\"></b></span>Visual Design" }
    n5@{ shape: text}
    n6@{ shape: text}
    n8@{ shape: text}
    n9@{ shape: text}
    style B fill:#E1BEE7
    style n5 fill:#BBDEFB
    style n1 fill:#E1BEE7
    style n6 fill:#BBDEFB
    style n3 fill:#E1BEE7
    style n8 fill:#BBDEFB
    style n4 fill:#E1BEE7
    style n9 fill:#BBDEFB
```















## MIDB roles & resp table
<div id="midb-msi" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Roles & Responsibilities</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
    <thead>
      <tr>
        <th style="width: 25%;">Name</th>
        <th style="width: 25%;">Role on HDCC</th>
        <th style="width: 50%;">Title</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Jim Wilgenbusch</td>
        <td style="word-wrap: break-word; white-space: normal;">Administration</td>
        <td style="word-wrap: break-word; white-space: normal;">Director of Research Computing in the Research & Innovation Office, UMN</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Thomas Pengo, PhD</td>
        <td style="word-wrap: break-word; white-space: normal;">IG Lead</td>
        <td style="word-wrap: break-word; white-space: normal;">Co-Director, MIDB Informatics Group</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Maren Macgregor-Hannah</td>
        <td style="word-wrap: break-word; white-space: normal;">HDCC Project Manager</td>
        <td style="word-wrap: break-word; white-space: normal;">Project Manager</td>
    </tr>
    <tr>
    <td>Jesse Erdmann</td>
    <td>ASO oversight</td>
    <td>Systems Operations</td>
    </tr>
    <tr>
    <td>Devin Willis</td>
    <td>Dev Ops</td>
    <td>DevOps Engineer</td>
    </tr>
    <tr>
    <td>Jesus Garcia</td>
    <td>Dev Ops</td>
    <td>DevOps Engineer</td>
    </tr>
    <tr>
    <td>Timothy Hendrickson</td>
    <td>Neuroimaging lead</td>
    <td>MIDB-IG Neuroimaging Informatics Manager</td>
    </tr>
    <tr>
    <td>Erik Lee</td>
    <td>Pipeline lead</td>
    <td>Neuroimaging Analyst</td>
    </tr>
    <tr>
    <td>Monalisa Biles</td>
    <td>Analyst</td>
    <td>&nbsp;</td>
    </tr>
    <tr>
    <td>Kimberleigh Breen</td>
    <td>Data Manager</td>
    <td>Data Manager</td>
    </tr>
    <tr>
  <td>Borgne Raasch</td>
  <td>Data Steward</td>
  <td>Data Steward</td>
  </tr>
  <tr>
  <td>Naomi Hospodarsky-Sutherland</td>
  <td>Security/Compliance</td>
  <td>Research Security and Compliance Analyst</td>
  </tr>
</tbody>
</table>
</div>

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

