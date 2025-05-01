# HBCD Data Coordinating Center (HDCC) Organizational Charts

## Overview
The larger organizational structure of the HDCC is as follows - ***click on individual groups to be directed to their asssociated organizational charts***.

```mermaid
---
config:
  theme: redux
  layout: dagre
---
flowchart LR
    A["<b>HDCC</b>"] --> E["<b>LORIS</b><br>Alan Evans, <i>PI</i><br>Samir Das, <i>AD Software Dev</i>"] & F["<b>UMN</b><br>Damien Fair, <i>HBCD DCC MPI</i><br>Reed McKewan, <i>HDCC Architect &amp; Data Manager</i>"] & G["<b>UCSD</b><br>Anders Dale, <i>PI/Director</i>"] & H["<b>LIBR</b><br>"] & n1["<b>Columbia</b><br>William P. Fifer,  <i>PI</i>"] & n16["<b>University of Maryland</b><br>Nathan Fox, <i>AD Data Core</i>"]
    F --> n6["<b>Health Sciences Technology (HST)</b><br>Reed McKewan"] & n7["<b>MIDB Informatics Hub</b><br>Jim Wilgenbusch, <i>Research Computing</i><br>Thomas Pengo, <i>Co-Director Research Informatics</i>"] & n8["<b>DCAN Lab</b><br>Eric Feczko &amp; Steven Nelson, <i>PIs</i>"]
    H --> n14["<b>Biostatistics Workgroup</b><br>Wesley K. Thompson, <i>Associate Director</i>"] & n15["<b>Geolocation Workgroup</b><br>Chun Chieh Fan, <i>Co-PI</i>"]
    A@{ shape: rect}
    E@{ shape: rounded}
    F@{ shape: rounded}
    G@{ shape: rounded}
    H@{ shape: rounded}
    n1@{ shape: rounded}
    n16@{ shape: rounded}
    n6@{ shape: rounded}
    n7@{ shape: rounded}
    n8@{ shape: rounded}
    n14@{ shape: rounded}
    n15@{ shape: rounded}
    style A fill:transparent,color:#000000
    style E fill:#FFCDD2
    style F fill:#E1BEE7
    style G fill:#FFF9C4
    style H fill:#C8E6C9
    style n1 fill:#BBDEFB
    style n16 fill:#FFE0B2
    style n6 fill:#E1BEE7,stroke:none
    style n7 fill:#E1BEE7,stroke:none
    style n8 fill:#E1BEE7,stroke:none
    style n14 fill:#C8E6C9,stroke:none
    style n15 fill:#C8E6C9,stroke:none
    click E "#loris"
```

## Vertial option
```mermaid
---
config:
  theme: redux
  layout: dagre
---
flowchart TD
    A["<b>HDCC</b>"] --> E["<b>LORIS</b><br>Alan Evans, <i>PI</i><br>Samir Das, <i>AD Software Dev</i>"] & F["<b>UMN</b><br>Damien Fair, <i>HBCD DCC MPI</i><br>Reed McKewan, <i>HDCC Architect &amp; Data Manager</i>"] & G["<b>UCSD</b><br>Anders Dale, <i>PI/Director</i>"] & H["<b>LIBR</b><br>"] & n1["<b>Columbia</b><br>William P. Fifer,  <i>PI</i>"] & n16["<b>University of Maryland</b><br>Nathan Fox, <i>AD Data Core</i>"]
    F --> n6["<b>Health Sciences Technology (HST)</b><br>Reed McKewan"] & n7["<b>MIDB Informatics Hub</b><br>Jim Wilgenbusch, <i>Research Computing</i><br>Thomas Pengo, <i>Co-Director Research Informatics</i>"] & n8["<b>DCAN Lab</b><br>Eric Feczko &amp; Steven Nelson, <i>PIs</i>"]
    H --> n14["<b>Biostatistics Workgroup</b><br>Wesley K. Thompson, <i>Associate Director</i>"] & n15["<b>Geolocation Workgroup</b><br>Chun Chieh Fan, <i>Co-PI</i>"]
    A@{ shape: rect}
    E@{ shape: rounded}
    F@{ shape: rounded}
    G@{ shape: rounded}
    H@{ shape: rounded}
    n1@{ shape: rounded}
    n16@{ shape: rounded}
    n6@{ shape: rounded}
    n7@{ shape: rounded}
    n8@{ shape: rounded}
    n14@{ shape: rounded}
    n15@{ shape: rounded}
    style A fill:transparent,color:#000000
    style E fill:#FFCDD2
    style F fill:#E1BEE7
    style G fill:#FFF9C4
    style H fill:#C8E6C9
    style n1 fill:#BBDEFB
    style n16 fill:#FFE0B2
    style n6 fill:#E1BEE7,stroke:none
    style n7 fill:#E1BEE7,stroke:none
    style n8 fill:#E1BEE7,stroke:none
    style n14 fill:#C8E6C9,stroke:none
    style n15 fill:#C8E6C9,stroke:none
    click E "#loris"
```

## LORIS
```mermaid
---
config:
  layout: dagre
---
flowchart TB
    A["<b>Alan Evans</b><br>Principal Investigator"] --o nl["<b>Samir Das</b><br>Associate Director of Software Development"]
    nl --o n9(["<b>Study Coordination</b>"]) & C(["<b>CBRAIN/Computing</b>"]) & B(["<b>Development</b>"])
    C --o D["<b>Pierre Rioux</b><br>Senior HPC developer"]
    n9 --o E["<b>Santiago Torres</b><br>Study Officer (Research Administration)"]
    B --o F["<b>BHV/Database</b>"] & H["<b>EEG/Biosamples</b>"] & G["<b>MRI</b>"]
    F --o I["<b>Regis Ongaro-Carcy</b><br>Lead BHV Developer"] & J["<b>Sruthy Matthew</b><br>Senior Backend Developer"]
    I --o K["<b>George Murad</b><br>Junior BHV Developer"]
    J --o K
    G --o L["<b>Cecile Madjar</b><br>Lead MRI developer"]
    H --o M["<b>Laetitia Faeselier</b><br>Lead BioSamples/EEG Developer"]
    A@{ shape: text}
    nl@{ shape: text}
    D@{ shape: text}
    E@{ shape: text}
    F@{ shape: rounded}
    H@{ shape: rounded}
    G@{ shape: rounded}
    I@{ shape: text}
    J@{ shape: text}
    K@{ shape: text}
    L@{ shape: text}
    M@{ shape: text}
    style A stroke:#000000,fill:#BBDEFB
    style nl stroke:#000000,fill:#BBDEFB
    style n9 stroke:#000000,fill:#E1BEE7,stroke-width:1px,stroke-dasharray: 0
    style C stroke:#333,fill:#E1BEE7
    style B stroke:#333,fill:#E1BEE7
    style D stroke:#333,fill:#BBDEFB
    style E stroke:#333,fill:#BBDEFB
    style F stroke:#333,fill:#C8E6C9
    style H stroke:#333,fill:#FFE0B2
    style G stroke:#333,fill:#FFF9C4
    style I stroke:#333,fill:#C8E6C9
    style J stroke:#333,fill:#C8E6C9
    style K stroke:#333,fill:#C8E6C9
    style L stroke:#000000,fill:#FFF9C4
    style M fill:#FFE0B2,stroke:#000000
    click A "#alan-evans-principal-investigator"
    click nl "#samir-das-associate-director-of-software-development"
```

### Roles & Responsibilities

##### Alan Evans, Principal Investigator
<p style="margin: 0;"><i>Oversight and management of MCIN and LORIS operations:</i></p>
- Ensure regulatory compliance between LORIS, McGill and affiliated institutions.
- Engage with stakeholders to ensure the study's relevance and applicability.
- Secure funding and resources for the study.

##### Samir Das, Associate Director of Software Development
<p style="margin: 0;"><i>General planning and oversight of LORIS operations for the HBCD study including:</i></p>
- Administration of LORIS operations.
- Overseeing and managing allocated study budget.
- Provide guidance, and mentorship to the research and development team.
- Conceptualization, establishment and planning of standardized workflow procedures and experimental protocols with the aim of maintaining data consistency and integrity across study.
- Establish project plans, outlining tasks, timelines, and dependencies for the development of the HBCD project.
- Attend workgroup meetings with SMEs and workgroup leads to gather requirements and periodic feedback crucial for aligning project outcomes with expectations throughout the project duration.
- General oversight of structural functionality and new features and tools in LORIS.

## University of Minnesota (UMN)
(ADD ORG CHART DIAGRAM HERE)

### Roles and Responsibilities
***Alternative format - list info in table:***

<div id="table-banner" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Responsibilities</span>
  <span class="arrow">▸</span>
</div>
<div class="table-open-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
    <thead>
      <tr>
        <th style="width: 15%; border: 1px solid #ddd; padding: 5px; text-align: center;">Name</th>
        <th style="width: 70%; border: 1px solid #ddd; padding: 5px; text-align: center;">Responsibilities</th>
    </thead>
    <tbody>
</tbody>
</table>
</div>

## LIBR
(ADD ORG CHART DIAGRAM HERE)

### Roles and Responsibilities


## Columbia
(ADD ORG CHART DIAGRAM HERE)

### Roles and Responsibilities
