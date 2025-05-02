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
    click n6 "#health-sciences-technology-hst"
    click n7 "#masonic-institute-for-the-developing-brain-midb-informatics-hub"
    click n8 "#dcan-lab"
```
</div>


## LORIS
```mermaid
---
config:
  layout: dagre
---
flowchart TB
    A["<b>Alan Evans</b><br>Principal Investigator"] --> nl["<b>Samir Das</b><br>Associate Director of Software Development"]
    nl --> n9(["<b>Study Coordination</b>"]) & C(["<b>CBRAIN/Computing</b>"]) & B(["<b>Development</b>"])
    C --> D["<b>Pierre Rioux</b><br>Senior HPC developer"]
    n9 --> E["<b>Santiago Torres</b><br>Study Officer (Research Administration)"]
    B --> F["<b>BHV/Database</b>"] & H["<b>EEG/Biosamples</b>"] & G["<b>MRI</b>"]
    F --> I["<b>Regis Ongaro-Carcy</b><br>Lead BHV Developer<br>
    <b>Sruthy Matthew</b><br>Senior Backend Developer"]
    I --> K["<b>George Murad</b><br>Junior BHV Developer"]
    G --> L["<b>Cecile Madjar</b><br>Lead MRI developer"]
    H --> M["<b>Laetitia Faeselier</b><br>Lead BioSamples/EEG Developer"]
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
    click A "#evans"
    click nl "#das"
    click D "#rioux"
    click E "#torres"
    click I "#bhv-database"
    click K "#bhv-database"
    click L "#madjar"
    click M "#faeselier"
```
<br>

### Roles & Responsibilities

<div id="evans" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Alan Evans, Principal Investigator</span>
  <a class="anchor-link" href="#evans" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<p>Oversight and management of MCIN and LORIS operations:</p>
<ul>
<li>Ensure regulatory compliance between LORIS, McGill and affiliated institutions.</li>
<li>Engage with stakeholders to ensure the study's relevance and applicability.</li>
<li>Secure funding and resources for the study.</li>
</ul>
</div>

<div id="das" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Samir Das, Associate Director of Software Development</span>
  <a class="anchor-link" href="#das" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<p>General planning and oversight of LORIS operations for the HBCD study:</p>
<ul>
<li>Administration of LORIS operations.</li>
<li>Overseeing and managing allocated study budget.</li>
<li>Provide guidance, and mentorship to the research and development team.</li>
<li>Conceptualization, establishment and planning of standardized workflow procedures and experimental protocols with the aim of maintaining data consistency and integrity across study.</li>
<li>Establish project plans, outlining tasks, timelines, and dependencies for the development of the HBCD project.</li>
<li>Attend workgroup meetings with SMEs and workgroup leads to gather requirements and periodic feedback crucial for aligning project outcomes with expectations throughout the project duration.</li>
<li>General oversight of structural functionality and new features and tools in LORIS.</li>
</ul>
</div>

<div id="rioux" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Pierre Rioux, Senior CBRAIN Developer</span>
  <a class="anchor-link" href="#rioux" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<p>CBRAIN:</p>
<ul>
<li>Configure clusters to handle all tools and pipelines for HBCD</li>
<li>Help containerize tools</li>
<li>Design efficient workflows for computing and analysis</li>
<li>Configure CBRAIN to handle all workflows and tools in HBCD</li>
<li>Interoperability with each system linking to HPCs</li>
<li>Data release design aspects as it pertains to HPCs</li>
</ul>
</div>

<div id="torres" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Santiago Torres, Study Officer (Research Administration)</span>
  <a class="anchor-link" href="#torres" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<p>Review the completeness and accuracy of project tasks, including:</p>
<ul>
<li>Attend workgroup meetings with SMEs and workgroup leads to gather requirements and periodic feedback crucial for aligning project outcomes with expectations throughout the project duration.</li>
<li>Acting as an initial liaison for sites to aid in troubleshooting, bug resolutions and provide assistance related to LORIS functionality.</li>
<li>Identify and assign roles and responsibilities for completion of established tasks.</li>
<li>Oversight of tasks for on time implementation and delivery of requested instruments, instrument edits, bug fixes and other study requests, including the creation, coordination, testing and follow-up of task </li>
<li>Check collection of relevant data through the various data collection streams such as surveys, questionnaires, BioSamples or 3rd party sources.</li>
<li>Conduct interoperability testing via data exchange simulations with external systems or platforms to ensure seamless integration and compatibility.</li>
</ul>
</div>

<div id="bhv-database" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">BHV/Database Team</span>
  <a class="anchor-link" href="#bhv-database" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<br>
<b>Regis Ongaro-Carcy, Lead BHV Developer</b>
<ul>
<i>Development of LORIS BHV features for HBCD:</i>
<li>Integrate data exchange protocols to enable interoperability between LORIS software and collaborating external platforms (e.g. REDCap, Ripple, MSI).</li>
<li>Establishment and overview of the various data collection streams such as surveys, questionnaires or 3rd party sources.</li>
<li>Conduct interoperability testing via data exchange simulations with external systems or platforms to ensure seamless integration and compatibility.</li>
<li>Implementation of CRF alert and escalation procedures and notification system.</li>
<li>Conception and design of alternative processing pathways to optimize current code functionalities in LORIS and improve system functionality and user satisfaction.</li>
<li>Implementation of new features and functionalities to maintain database integrity across LORIS.</li>
</ul>

<b>Sruthy Matthew, Senior Backend Developer</b>
<ul>
<i>Development of LORIS LaunchPad and Backend features for HBCD:</i>
<li>Set up and oversight of deployment procedures for execution and implementation of LORIS updates.</li>
<li>Formulation and execution of database upkeep and maintenance requests.</li>
<li>Design and implement new LaunchPad features to enhance user experience.</li>
<li>Monitor the quality and integrity of data collected, ensuring adherence to the study protocol.</li>
<li>Ensure proper data storage, confidentiality, and security measures are in place across the database.</li>
<li>Implementation of new features and functionalities to maintain database integrity across LORIS.</li>
</ul>

<b>George Murad, Junior BHV Developer</b>
<ul>
<i>Development of LORIS BHV features specific to HBCD:</i>
<li>Coding of new instruments and their corresponding scoring algorithms.</li>
<li>Creation of automated queries for study progression and quality control monitoring..</li>
<li>Development and implementation of new Endpoint and APIs for HBCD.</li>
</ul>
</div>

<div id="madjar" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Cecile Madjar, Lead MRI developer</span>
  <a class="anchor-link" href="#madjar" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<p>Development of LORIS MRI features specific to HBCD:</p>
<ul>
<li>Ingestion of raw data (DICOMs, conversion to BIDS, import of MRS data)</li>
<li>Ingestion of MRI QC data</li>
<li>Ingestion of derivatives (OSPREY, NiBabies, XCP-D, QSIPrep, etc…)</li>
<li>Notification system for missing MRI data; incorrect scan log entries or pipeline ingestion errors</li>
<li>MRI data fixes (Deletion of data, correction of incorrect conversion, recreation of the BIDS data post-DICOM updates…)</li>
<li>Responsible for the deployment process on the MRI side of HBCD</li>
</ul>
</div>

<div id="faeselier" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Laetitia Faeselier, Lead BioSamples/EEG Developer</span>
  <a class="anchor-link" href="#faeselier" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<p>Development of LORIS BioSample/EEG features specific to HBCD: </p>
<ul>
<li>Ingestion of EEG data (Import of raw EEG files, Conversion to EEG BIDS) and EEG derivative data.</li>
<li>Ingestion of EKG data.</li>
<li>Creation of EEG QC and EEG QC equipment reports and output values</li>
<li>Establish data tracking protocols for EEG and BioSample data.</li>
<li>Implementation of processing requests for EEG and BioSample Data.</li>
<li>Establishment of BioSamples dashboard for display and navigation of BioSample processing and stage progression tracking.</li>
<li>Implementation of new features and innovations for BioSample Dashboard, shipping manifests and tracking systems.</li>
<li>Review of EEG and BioSample data, including conversion outputs, code tracking, kits registrations and other related data fixes.</li>
<li>Monitoring of radiological reports.</li>
</ul>
</div>




## University of Minnesota (UMN)
```mermaid
---
config:
  theme: redux
  layout: dagre
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
    <b>Naomi Hospodarsky-Sutherland</b><br>Security Compliance"] & M4["<b>Jesse Erdman</b><br>Sr. SysOps<br>
    <b>Devin Willis</b><br>DevOps<br>
    <b>Jesus Garcia</b><br>DevOps"] & M5["<b>Timothy Hendrickson</b>
    MR/EEG/Biosensor Informatics Lead<br>
    <b>Erik Lee</b><br>Pipelines/Processing<br>
    <b>Monalisa Biles</b><br>Analyst"]
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
    style D1 fill:#FFE0B2
    style D2 fill:#FFE0B2
    style D2a fill:#FFE0B2
    style D2b fill:#FFE0B2
```
### Health Sciences Technology (HST)
```mermaid
---
config:
  layout: dagre
---
flowchart TB
    A["<b>Health Sciences Technology</b><br>Data shelter, PHI, Ripple interface, Overall Data Management, QC Dashboards, Ancillary Studies, Third party integration"] --o B["<b>Reed McKewan</b><br>HDCC Architect &amp; Data Manager"]
    B --o E["<b>Karen Athy-Penrose</b><br>Data Shelter PM"] & F["<b>Dan Duhon</b><br>DevOps/ETl"] & G["<b>Haley Hutala</b><br>Tableau Engineer/QC Dashboards"] & H["<b>Constantine Aliferis</b><br>Director Insitute Health Informatics"]
    H --o I["<b>Steve Johnson</b><br>Director Informatics Innovation"] & J["<b>Tim Meyers</b><br>Senior Informatics Engineer/EHR"]
    A@{ shape: rounded}
    B@{ shape: text}
    E@{ shape: text}
    F@{ shape: text}
    G@{ shape: text}
    H@{ shape: text}
    I@{ shape: text}
    J@{ shape: text}
    style A fill:#C8E6C9,stroke:#000000
    style B fill:#C8E6C9,stroke-width:2px,stroke-dasharray: 0,stroke:none
    style E fill:#C8E6C9
    style F fill:#C8E6C9
    style G fill:#C8E6C9
    style H fill:#C8E6C9
    style I fill:#C8E6C9
    style J fill:#C8E6C9
```

### Masonic Institute for the Developing Brain (MIDB) Informatics Hub
```mermaid
---
config:
  layout: dagre
---
flowchart TB
    C["<b>MIDB Informatics Hub</b><br><i>Minnesota Supercomputing Institute (MSI)</i><br>System Administration, Loris Hosting, Computing, Processing, Data sharing"] --> K["<b>Jim Wilgenbusch</b><br>Research Computing"]
    K --> L["<b>Thomas Pengo</b><br>Co-Director Research Informatics"]
    L --> M(["<b>Project Management</b>"]) & N(["<b>System Operations</b>"]) & O(["<b>Informatics &amp; Processing</b>"]) & P(["<b>Data Management</b>"])
    N --> Q["<b>Jesse Erdman</b><br>Senior System Operations<br>
    <b>Devin Willis</b><br>DevOps Engineer<br>
    <b>Jesus Garcia</b><br>DevOps Engineer"]
    O --> n4["<b>Timothy Hendrickson</b><br>Neuroimaging/EEG/MRS/Biosensor Informatics Lead<br>
    <b>Erik Lee</b><br>Pipeline Integration/Processing<br>
    <b>Monalisa Biles</b><br>Analysis Data Processing"]
    M --> n6@{ label: "<span style=\"--tw-scale-x:\"><b>Maren Macgregor-Hannah</b><br>HDCC PM</span><br style=\"--tw-scale-x:\">" }
    P --> n7["<b>Kimberleigh Breen</b><br>Data Manager/Version Control<br>
    <b>Borgne Raasch</b><br>Data Steward/Access Controls<br>
    <b>Naomi Hospodarsky-Sutherland</b><br>Security Compliance"]
    C@{ shape: rounded}
    K@{ shape: text}
    L@{ shape: text}
    Q@{ shape: text}
    n4@{ shape: text}
    n6@{ shape: text}
    n7@{ shape: text}
    style C stroke:#000000,fill:#FFF9C4
    style K fill:#FFF9C4
    style L fill:#FFF9C4
    style M fill:#FFD600,stroke:#000000
    style N fill:#FFD600,stroke:#000000
    style O color:#000000,fill:#FFD600,stroke:#000000
    style P fill:#FFD600,stroke:#000000
    style Q fill:#FFF9C4
    style n4 fill:#FFF9C4
    style n6 fill:#FFF9C4
    style n7 fill:#FFF9C4
```

### DCAN Lab
```mermaid
---
config:
  layout: dagre
---
flowchart LR
    D["<b>DCAN Lab</b><br>Processing, Software Development &amp; Deployment"] --> S["<b>Eric Feczko</b><br>Neuroscience/Informatics<br>Software Engineer"] & T["<b>Steve Nelson</b><br>Director Neuroimaging Hub MIDB/CMRR"]
    S --> s1["<b>Lucille Moore</b><br>PM &amp; Software Engineer<br>
    <b>Mathias Goncalves</b><br>Software Engineer (Infant fMRIPrep)"]
    T --> t1["<b>Kim Weldon</b><br>PM, Data Acquisition Seimens Engineer"]
    t1 --> t2["<b>Thomas Madison</b><br>Software Engineer<br>
    <b>Matthew Cieslack</b><br>Software Engineer (QSIPrep/Diffusion)"]
    D@{ shape: rounded}
    S@{ shape: text}
    T@{ shape: text}
    s1@{ shape: text}
    t1@{ shape: text}
    t2@{ shape: text}
    style D stroke:#000000,fill:#FFE0B2
    style S stroke:#000000,fill:#FFE0B2
    style T stroke:#000000,fill:#FFE0B2
    style s1 fill:#FFE0B2
    style t1 fill:#FFE0B2
    style t2 fill:#FFE0B2
```

## UCSD
(ADD ORG CHART DIAGRAM HERE)

### Roles and Responsibilities

## LIBR
(ADD ORG CHART DIAGRAM HERE)

### Roles and Responsibilities


## Columbia University
NOTE: org chart is small, perhaps can just be integrated into larger org chart?

## University of Maryland
(ADD ORG CHART DIAGRAM HERE)

### Roles and Responsibilities
