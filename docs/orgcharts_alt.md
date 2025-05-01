# HBCD Data Coordinating Center (HDCC) Organizational Charts

## LORIS
<p>
<div class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text">Tip: Click on names to be directed to information on responsibilities</span>
</div>
</p>

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
![](https://www.mermaidchart.com/raw/3d9fad4e-04e4-4be5-9450-5fb3c34f68a4?theme=light&version=v0.1&format=svg)


## LIBR
### Organizational Chart
[ADD ORG CHART]

### Roles and Responsibilities


## Columbia
### Organizational Chart
(ADD ORG CHART DIAGRAM HERE)

### Roles and Responsibilities
