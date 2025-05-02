# HBCD Data Coordinating Center (HDCC) Organizational Charts

## Overview
The larger organizational structure of the HDCC is as follows - ***click on individual groups to be directed to their asssociated organizational charts***.

<div style="width: 450px;">
```mermaid
---
config:
  layout: dagre
---
flowchart LR
    A["<strong>HDCC</strong>"] --> E["<b>LORIS</b><br>Alan Evans<br>Samir Das"] & F["<b>UMN</b><br>Damien Fair<br>Reed McKewan"] & G["<b>UCSD</b><br>Anders Dale"] & H["<b>LIBR</b><br>"] & n1["<b>Columbia</b><br>William P. Fifer"] & n16["<b>University of Maryland</b><br>Nathan Fox"]
    F --> n6["<b>Health Sciences Technology (HST)</b><br>Reed McKewan"] & n7["<b>MIDB Informatics Hub</b><br>Jim Wilgenbusch<br>Thomas Pengo"] & n8["<b>DCAN Lab</b><br>Eric Feczko &amp; Steven Nelson"]
    H --> n14["<b>Biostatistics Workgroup</b><br>Wesley K. Thompson"] & n15["<b>Geolocation Workgroup</b><br>Chun Chieh Fan"]
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
    style A fill:#e6e6fa,stroke:#424242
    style E fill:#e6e6fa,stroke:#616161
    style F fill:#e6e6fa,stroke:#616161
    style G fill:#e6e6fa,stroke:#616161
    style H fill:#e6e6fa,stroke:#616161
    style n1 fill:#e6e6fa,stroke:#616161
    style n16 fill:#e6e6fa,stroke:#616161
    style n6 fill:#dcdcdc,stroke:#757575
    style n7 fill:#dcdcdc,stroke:#757575
    style n8 fill:#dcdcdc,stroke:#757575
    style n14 fill:#dcdcdc,stroke:#757575
    style n15 fill:#dcdcdc,stroke:#757575
    click E "#loris"
    click F "#university-of-minnesota-umn"
    click G "#ucsd"
    click H "#libr"
    click n1 "#columbia"
    click n16 "#university-of-maryland"
```
</div>


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
    F --o I["<b>Regis Ongaro-Carcy</b><br>Lead BHV Developer<br>
    <b>Sruthy Matthew</b><br>Senior Backend Developer"]
    I --o K["<b>George Murad</b><br>Junior BHV Developer"]
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
    style K stroke:#333,fill:#C8E6C9
    style L stroke:#000000,fill:#FFF9C4
    style M fill:#FFE0B2,stroke:#000000
    click A "#alan-evans-principal-investigator"
    click nl "#samir-das-associate-director-of-software-development"
```
<br>

```mermaid
---
config:
  layout: dagre
---
flowchart LR
    A["<b>Alan Evans</b><br>Principal Investigator"] --o nl["<b>Samir Das</b><br>Associate Director of Software Development"]
    nl --o n9(["<b>Study Coordination</b>"]) & C(["<b>CBRAIN/Computing</b>"]) & B(["<b>Development</b>"])
    C --o D["<b>Pierre Rioux</b><br>Senior HPC developer"]
    n9 --o E["<b>Santiago Torres</b><br>Study Officer (Research Administration)"]
    B --o F["<b>BHV/Database</b>"] & H["<b>EEG/Biosamples</b>"] & G["<b>MRI</b>"]
    F --o I["<b>Regis Ongaro-Carcy</b><br>Lead BHV Developer<br>
    <b>Sruthy Matthew</b><br>Senior Backend Developer<br>
     ↓ <br>
     <b>George Murad</b><br>Junior BHV Developer"]
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

## UCSD
(ADD ORG CHART DIAGRAM HERE)

### Roles and Responsibilities

## LIBR
(ADD ORG CHART DIAGRAM HERE)

### Roles and Responsibilities


## Columbia
(ADD ORG CHART DIAGRAM HERE)

### Roles and Responsibilities

## University of Maryland
(ADD ORG CHART DIAGRAM HERE)

### Roles and Responsibilities
