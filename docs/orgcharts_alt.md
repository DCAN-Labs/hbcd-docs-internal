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
```mermaid
---
config:
  theme: redux
  layout: fixed
---
flowchart TB
    A["<b>Damien Fair</b><br>Professor UMN<br>HBCD DCC MPI"] --> A1["<b>Reed McKewan</b><br>HDCC Architect &amp; Data Manager"]
    A1 --> HST["<b>Health Sciences Technology</b><br>Data shelter, PHI, Ripple interface, Overall Data Management, QC Dashboards, Ancillary Studies, Third party integration"] & MIDB["<b>MIDB Informatics Hub</b><br><i>Minnesota Supercomputing Institute (MSI)</i><br>System Administration, Loris Hosting, Computing, Processing, Data sharing"] & DCAN["<b>DCAN Lab</b><br>Processing, Software Development &amp; Deployment"]
    HST --> HST1["<b>Karen Athy-Penrose</b><br>Data Shelter PM<br>
        <b>Dan Duhon</b><br>DevOps/ETL<br>
        <b>Haley Hutala</b><br>Tableau Engineer/QC Dashboards"] & HST2["<b>Constantine Aliferis</b><br>Director Insitute Health Informatics"]
    HST2 --> HST2a["<b>Steve Johnson</b><br>Director Informatics Innovation"]
    HST2a --> HST2b["<b>Tim Meyers</b><br>Senior Informatics Engineer/EHR"]
    MIDB --> M1["<b>Jim Wilgenbusch</b><br>Research Computing"]
    M1 --> M2["<b>Thomas Pengo</b><br>Co-Director Research Informatics"]
    M2 --> M3["<b>Maren Macgregor-Hannah</b><br>HDCC PM<br>
    <b>Kimberleigh Breen</b><br>Data Manager/Version Control<br>
    <b>Borgne Raasch</b><br>Data Steward/Access Controls<br>
    <b>Naomi Hospodarsky-Sutherland</b><br>Security Compliance"] & M4["<b>Jesse Erdman</b><br>Senior System Operations"] & M5["<b>Timothy Hendrickson</b><br>Neuroimaging/EEG/MRS/Biosensor Informatics Lead"]
    M4 --> M4a["<b>Devin Willis</b><br>DevOps Engineer<br>
    <b>Jesus Garcia</b><br>DevOps Engineer"]
    M5 --> M5a["<b>Erik Lee</b><br>Pipeline Integration/Processing"]
    M5a --> M5b["<b>Monalisa Biles</b><br>Analysis Data Processing"]
    DCAN --> D1["<b>Eric Feczko</b><br>Neuroscience/Informatics<br>Software Engineer<br>
    <b>Lucille Moore</b><br>PM &amp; Software Engineer<br>
    <b>Mathias Goncalves</b><br>Software Engineer (Infant fMRIPrep)"] & D2["<b>Steve Nelson</b><br>Director Neuroimaging Hub MIDB/CMRR"]
    D2 --> D2a["<b>Kim Weldon</b><br>PM, Data Acquisition Seimens Engineer"]
    D2a --> D2b["<b>Thomas Madison</b><br>Software Engineer<br>
    <b>Matthew Cieslack</b><br>Software Engineer (QSIPrep/Diffusion)"]
    A@{ shape: text}
    A1@{ shape: text}
    HST@{ shape: rounded}
    MIDB@{ shape: rounded}
    DCAN@{ shape: rounded}
    HST2@{ shape: text}
    HST2a@{ shape: text}
    HST2b@{ shape: text}
    M1@{ shape: text}
    M2@{ shape: text}
    M3@{ shape: text}
    M4@{ shape: text}
    M5@{ shape: text}
    M4a@{ shape: text}
    M5a@{ shape: text}
    M5b@{ shape: text}
    D1@{ shape: text}
    D2@{ shape: text}
    D2a@{ shape: text}
    D2b@{ shape: text}
    style A fill:#BBDEFB
    style A1 fill:#C8E6C9
    style HST fill:#C8E6C9
    style MIDB fill:#FFF9C4
    style DCAN fill:#FFE0B2
    style HST1 fill:#C8E6C9,stroke:none
    style HST2 fill:#C8E6C9
    style HST2a stroke:#C8E6C9,fill:#C8E6C9
    style HST2b fill:#C8E6C9
    style M1 fill:#FFF9C4
    style M2 fill:#FFF9C4
    style M3 fill:#FFF9C4
    style M4 fill:#FFF9C4
    style M5 fill:#FFF9C4
    style M4a fill:#FFF9C4
    style M5a fill:#FFF9C4
    style M5b fill:#FFF9C4
    style D1 fill:#FFE0B2
    style D2 fill:#FFE0B2
    style D2a fill:#FFE0B2
    style D2b fill:#FFE0B2
```

## LIBR
### Organizational Chart
(ADD ORG CHART DIAGRAM HERE)

### Roles and Responsibilities


## Columbia
### Organizational Chart
(ADD ORG CHART DIAGRAM HERE)

### Roles and Responsibilities
