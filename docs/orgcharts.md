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
    A["<strong>HDCC</strong>"] --> E["<b>LORIS</b><br>Alan Evans<br>Samir Das"] & F["<b>UMN</b><br>Damien Fair<br>Reed McKewan"] & G["<b>UCSD</b><br>Anders Dale"] & H["<b>LIBR</b><br>"] & n1["<b>Columbia</b><br>William P. Fifer"] & n16["<b>University of Maryland</b>"] & washu["<b>WashU</b><br>Chris Smyser<br>Chad Sylvester"]
    F --> n6["<b>Health Sciences Technology (HST)</b><br>Reed McKewan"] & n7["<b>MIDB Informatics Hub</b><br>Jim Wilgenbusch<br>Thomas Pengo"] & n8["<b>DCAN Lab</b><br>Eric Feczko &amp; Steven Nelson"]
    H --> n14["<b>Biostatistics Workgroup</b><br>Wesley K. Thompson"] & n15["<b>Geolocation Workgroup</b><br>Chun Chieh Fan"]
    n16 --> n17["<b>EEG Core</b><br>Nathan Fox"]
    A@{ shape: rect}
    E@{ shape: rounded}
    F@{ shape: rounded}
    G@{ shape: rounded}
    H@{ shape: rounded}
    n1@{ shape: rounded}
    n16@{ shape: rounded}
    washu@{ shape: rounded}
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
    style washu fill:#e6e6fa,stroke:#616161
    style n6 fill:#dcdcdc,stroke:#757575
    style n7 fill:#dcdcdc,stroke:#757575
    style n8 fill:#dcdcdc,stroke:#757575
    style n14 fill:#dcdcdc,stroke:#757575
    style n15 fill:#dcdcdc,stroke:#757575
    style n17 fill:#dcdcdc,stroke:#757575
    click E "#loris"
    click F "#university-of-minnesota-umn"
    click G "#ucsd"
    click H "#libr"
    click n1 "#columbia-university"
    click washu "#washu"
    click n6 "#health-sciences-technology-hst"
    click n7 "#midb-informatics-hub-msi"
    click n8 "#dcan-lab"
    click n17 "#umd-eeg-core"
    click n14 "#thompson"
    click n15 "#fan"
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
    nl --> n9(["<b>Study Coordination</b>"]) & C(["<b>CBRAIN/Computing</b><br>"]) & B(["<b>Development</b>"])
    C --> D["<b>Pierre Rioux</b><br>Senior HPC developer"]
    n9 --> E["<b>Santiago Torres</b><br>Study Officer"]
    B --> F["<b>BHV/Database</b>"] & H["<b>EEG/Biosamples</b>"] & G["<b>MRI</b>"]
    F --> I["<b>Regis Ongaro-Carcy</b><br>Lead Developer"] & n10["<b>Sruthy Matthew</b><br>Sr. Backend Dev"]
    G --> L["<b>Cecile Madjar</b><br>Lead developer"]
    H --> M["<b>Laetitia Faeselier</b><br>Lead Developer"]
    n10 --> n11["<b>George Murad</b>, Jr. Dev"]
    I --> n11
    A@{ shape: text}
    nl@{ shape: text}
    D@{ shape: text}
    E@{ shape: text}
    F@{ shape: rounded}
    H@{ shape: rounded}
    G@{ shape: rounded}
    I@{ shape: text}
    n10@{ shape: text}
    L@{ shape: text}
    M@{ shape: text}
    n11@{ shape: text}
    style A stroke:#000000,fill:#BBDEFB
    style nl stroke:#000000,fill:#BBDEFB
    style n9 stroke:#000000,fill:#E1BEE7,stroke-width:2px,stroke-dasharray: 0
    style C stroke:#333,fill:#E1BEE7
    style B stroke:#333,fill:#E1BEE7
    style D stroke:#333,fill:#BBDEFB
    style E stroke:#333,fill:#BBDEFB
    style F stroke:#333,fill:#E1BEE7
    style H stroke:#333,fill:#E1BEE7
    style G stroke:#333,fill:#E1BEE7
    style I stroke:#333,fill:#BBDEFB
    style n10 fill:#BBDEFB
    style L stroke:#000000,fill:#BBDEFB
    style M fill:#BBDEFB,stroke:#000000
    style n11 fill:#BBDEFB
    click A "#evans"
    click nl "#das"
    click D "#rioux"
    click E "#torres"
    click n10 "#matthew"
    click I "#ontaro-carcy"
    click n11 "#murad"
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

<div id="ongary-carcy" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Regis Ongaro-Carcy, Lead BHV Developer</span>
  <a class="anchor-link" href="#ongary-carcy" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<ul>
<i>Development of LORIS BHV features for HBCD:</i>
<li>Integrate data exchange protocols to enable interoperability between LORIS software and collaborating external platforms (e.g. REDCap, Ripple, MSI).</li>
<li>Establishment and overview of the various data collection streams such as surveys, questionnaires or 3rd party sources.</li>
<li>Conduct interoperability testing via data exchange simulations with external systems or platforms to ensure seamless integration and compatibility.</li>
<li>Implementation of CRF alert and escalation procedures and notification system.</li>
<li>Conception and design of alternative processing pathways to optimize current code functionalities in LORIS and improve system functionality and user satisfaction.</li>
<li>Implementation of new features and functionalities to maintain database integrity across LORIS.</li>
</ul>
</div>

<div id="matthew" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Sruthy Matthew, Senior Backend Developer</span>
  <a class="anchor-link" href="#matthew" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<ul>
<i>Development of LORIS LaunchPad and Backend features for HBCD:</i>
<li>Set up and oversight of deployment procedures for execution and implementation of LORIS updates.</li>
<li>Formulation and execution of database upkeep and maintenance requests.</li>
<li>Design and implement new LaunchPad features to enhance user experience.</li>
<li>Monitor the quality and integrity of data collected, ensuring adherence to the study protocol.</li>
<li>Ensure proper data storage, confidentiality, and security measures are in place across the database.</li>
<li>Implementation of new features and functionalities to maintain database integrity across LORIS.</li>
</ul>
</div>

<div id="murad" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">George Murad, Junior BHV Developer</span>
  <a class="anchor-link" href="#murad" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
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
    A1 --> HST["<b>Health Sciences Technology</b><br>Data shelter, PHI, Ripple interface, Overall Data Management, QC Dashboards, Ancillary Studies, Third party integration"] & MIDB["<b>MIDB Informatics Hub</b> & <b>Minnesota Supercomputing Institute (MSI)</b><br>System Administration, Loris Hosting, Computing, Processing, Data sharing"] & DCAN["<b>DCAN Lab</b><br>Processing, Software Development &amp; Deployment"]
    A@{ shape: text}
    A1@{ shape: text}
    HST@{ shape: rounded}
    MIDB@{ shape: rounded}
    DCAN@{ shape: rounded}
    style A fill:#BBDEFB
    style A1 fill:#BBDEFB
    style HST fill:#E1BEE7
    style MIDB fill:#E1BEE7
    style DCAN fill:#E1BEE7
    click HST "#health-sciences-technology-hst"
    click MIDB "#midb-informatics-hub-msi"
    click DCAN "#dcan-lab"
```
### Health Sciences Technology (HST)
[HST](https://hst.umn.edu/) at UMN is responsible for: *Data shelter*, *PHI*, *Ripple Interface*, *Overall Data Management*, *QC Dashboards*, *Ancillary Studies*, and *Third Party Integration*
```mermaid
---
config:
  layout: dagre
---
flowchart TB
    B["<b>Reed McKewan</b><br>HDCC Architect &amp; Data Manager"] --> E["<b>Karen Athy-Penrose</b><br>Data Shelter PM"] & F["<b>Dan Duhon</b><br>DevOps/ETl"] & G["<b>Haley Hutala</b><br>Tableau Engineer/QC Dashboards"] & H["<b>Constantine Aliferis</b><br>Director Insitute Health Informatics"]
    H --> I["<b>Steve Johnson</b><br>Director Informatics Innovation"] & J["<b>Tim Meyer</b><br>Senior Informatics Engineer/EHR"]
    B@{ shape: text}
    E@{ shape: text}
    F@{ shape: text}
    G@{ shape: text}
    H@{ shape: text}
    I@{ shape: text}
    J@{ shape: text}
    style B fill:#BBDEFB,stroke-width:2px,stroke-dasharray: 0,stroke:none
    style E fill:#BBDEFB
    style F fill:#BBDEFB
    style G fill:#BBDEFB
    style H fill:#BBDEFB
    style I fill:#BBDEFB
    style J fill:#BBDEFB
```

### MIDB Informatics Hub & MSI
The [Masonic Institute for the Developing Brain (MIDB) Informatics Hub](https://midb.umn.edu/research/informatics) and [Minnesota Supercomputing Institute (MSI)](https://msi.umn.edu/) at UMN provide the following services to the HBCD study: *System Administration*, *Loris Hosting*, *Computing*, *Processing*, and *Data Sharing*.

```mermaid
---
config:
  layout: dagre
---
flowchart TB
    K["<b>Jim Wilgenbusch</b><br>Director of Research Computing"] --> L["<b>Thomas Pengo</b><br>Co-Director of MIDB Informatics Group"]
    L --> M(["<b>Project Management</b>"]) & N(["<b>System Operations</b>"]) & O(["<b>Informatics &amp; Processing</b>"]) & P(["<b>Data Management</b>"])
    N --> Q["<b>Jesse Erdman</b><br>Sr. SysOps<br>
    <b>Devin Willis</b>
    <b>Jesus Garcia</b><br>DevOps Engineers"]
    O --> n4["<b>Timothy Hendrickson</b><br>Neuroimaging Lead<br>
    <b>Erik Lee</b><br>Pipeline Lead<br>
    <b>Monalisa Biles</b><br>Analyst"]
    M --> n6@{ label: "<span style=\"--tw-scale-x:\"><b>Maren Macgregor-Hannah</b><br>HDCC PM</span><br style=\"--tw-scale-x:\">" }
    P --> n7["<b>Kimberleigh Breen</b><br>Data Manager<br>
    <b>Borgne Raasch</b><br>Data Steward<br>
    <b>Naomi Hospodarsky-Sutherland</b><br>Security/Compliance"]
    K@{ shape: text}
    L@{ shape: text}
    Q@{ shape: text}
    n4@{ shape: text}
    n6@{ shape: text}
    n7@{ shape: text}
    style K fill:#BBDEFB
    style L fill:#BBDEFB
    style M fill:#E1BEE7,stroke:#000000
    style N fill:#E1BEE7,stroke:#000000
    style O color:#000000,fill:#E1BEE7,stroke:#000000
    style P fill:#E1BEE7,stroke:#000000
    style Q fill:#BBDEFB
    style n4 fill:#BBDEFB
    style n6 fill:#BBDEFB
    style n7 fill:#BBDEFB
```

### DCAN Lab
The Developmental Cognition and Neuroimaging Lab ([DCAN](https://innovation.umn.edu/developmental-cognition-and-neuroimaging-lab)) at UMN is responsible for: *Processing*, *Software Development*, and *Deployment* of imaging data. 
```mermaid
---
config:
  layout: dagre
---
flowchart LR
    D["<b>Damien Fair, PA-C, PhD</b><br>Professor UMN<br>HBCD DCC MPI"] --> S["<b>Eric Feczko, PhD</b><br>Neuroscience/Informatics<br>Software Engineer<br>
    <b>Lucille A. Moore, PhD</b><br>PM &amp; Software Engineer<br>
    <b>Mathias Goncalves</b><br>Software Engineer (Infant fMRIPrep)"] & T["<b>Steve Nelson, PhD</b><br>Director Neuroimaging Hub MIDB/CMRR"]
    T --> t1["<b>Kim Weldon, PhD</b><br>PM, Data Acquisition Seimens Engineer"]
    t1 --> t2["<b>Thomas Madison</b><br>Software Engineer<br>
    <b>Matthew Cieslack, PhD</b><br>Software Engineer (QSIPrep/Diffusion)"]
    D@{ shape: text}
    S@{ shape: text}
    T@{ shape: text}
    t1@{ shape: text}
    t2@{ shape: text}
    style D stroke:#000000,fill:#BBDEFB
    style S stroke:#000000,fill:#BBDEFB
    style T stroke:#000000,fill:#BBDEFB
    style t1 fill:#BBDEFB
    style t2 fill:#BBDEFB
```

## UCSD
```mermaid
---
config:
  layout: dagre
---
flowchart TB
    A["<b>Anders Dale</b><br>PI/Director"] --> n1(["<b>Informatics</b>"]) & n2(["<b>MR Capture/QC</b>"]) & n3(["<b>Imaging</b>"]) & n4["<b>Janosch Linkersdörfer</b><br>Supervisor"]
    n4 --> n5(["<b>Data Science</b>"]) & n6(["<b>REDCap</b>"]) & n7["<b>Amanda (Lin) Li</b><br>Biostats Support<br>
    <b>Wenjie Zheng</b><br>DEAP Development"]
    n1 --> n8["<b>Rongguang Yang</b><br>Supervisor<br>
    <b>Chris Blazej</b>
    Fiona Software Dev"]
    n2 --> n9["<b>Donald Hagler</b><br>Supervisor<br>
    <b>Amanda Plesa</b>
    Tracking
    <b>David Zimmermann</b>
    <b>Tyler Berkness</b>
    Protocol Violations
    <b>Sejal Shanbhag</b>
    Issue Handling"]
    n3 --> n10["<b>Josh Kuperman</b><br>R&amp;D Engineer"]
    n5 --> n11["<b>Biplabendu Das</b><br>Dashboard Backend<br>
    <b>Olivier Celhay</b>
    Dashboard Frontend"]
    n6 --> n12["<b>Joseph Baligh</b><br>Server Admin<br>
    <b>Erika Bolden</b>
    <b>Laura Ziemer</b>
    Form Development"]
    A@{ shape: text}
    n4@{ shape: text}
    n7@{ shape: text}
    n8@{ shape: text}
    n9@{ shape: text}
    n10@{ shape: text}
    n11@{ shape: text}
    n12@{ shape: text}
    style A fill:#BBDEFB
    style n1 fill:#E1BEE7,stroke:#000000
    style n2 stroke:#000000,fill:#E1BEE7
    style n3 stroke:#000000,fill:#E1BEE7
    style n4 fill:#BBDEFB
    style n5 stroke:#000000,fill:#E1BEE7
    style n6 stroke:#000000,fill:#E1BEE7
    style n7 stroke:#000000,fill:#BBDEFB
    style n8 fill:#BBDEFB
    style n9 fill:#BBDEFB
    style n10 fill:#BBDEFB
    style n11 fill:#BBDEFB
    style n12 fill:#BBDEFB
```

## LIBR
<div id="thompson" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Wesley K. Thompson, HDCC Associate Director & BioStatistics Work Group Chair</span>
  <a class="anchor-link" href="#thompson" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<p>Provides guidance on statistical analysis, study design, novel methods development, for large, longitudinal, multi-site studies, including:</p>
<ul>
<li>Direction of statistical analyses for HBCD design and assessments.</li>
<li>Co-supervise and lead the development and maintenance of the statistical aspects of the Data Exploration and Analysis Portal 2.0 (DEAP 2.0).</li>
<li>Assist in the geolocation of residences of HBCD participants, and linking these geolocated addresses with external databases.</li>
</ul>
</div>

<div id="fan" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Chun Chieh Fan, Co-Investigator & Geolocation Work Group Chair</span>
  <a class="anchor-link" href="#fan" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<ul>
<li>Guide curation and analysis of imaging, genomic, and geolocation exposure data.</li>
<li>Co-supervise expanding DEAP 2.0 to include exploration and analysis of high-dimensional genomic, imaging, and exposure data, and to develop DEAP 2.0 tools to harmonize HBCD data and analyses with external studies, including the creation of a probabilistic ontology to compare measures across studies.</li>
</ul>
</div>

## Columbia University
<div style="width: 450px;">
```mermaid
---
config:
  layout: dagre
---
flowchart LR
    columbia["<b>William P. Fifer</b><br>Subaward Principal Investigator"] --> columbia2["<b>Nicolo Pini</b><br>Co-Investigator"]
    columbia2 --> n3["<b>Liana Eisler</b>
    Technician Research Assistant"]
    n1["<b>Dima Amso</b>
    Co-Investigator<br>"]
    columbia@{ shape: text}
    columbia2@{ shape: text}
    n3@{ shape: text}
    n1@{ shape: text}
    style columbia fill:#BBDEFB,stroke:#424242
    style columbia2 fill:#BBDEFB
    style n3 fill:#BBDEFB
    style n1 fill:#BBDEFB
    click columbia "#fifer"
    click columbia2 "#pini"
    click n1 "#amso"
    click n3 "#eisler"
```
</div>

### Roles & Responsibilities

<div id="fifer" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">William P. Fifer, Co-chair: Novel Technologies/Wearables</span>
  <a class="anchor-link" href="#fifer" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<ul>
<li>Overall management.</li>
<li>Supervise automation of sleep stage scoring and data analysis.</li> 
<li>Data analytics, writing, and review of manuscripts.</li>
</ul>
</div>

<div id="amso" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Dimo Amso, Co-Investigator</span>
  <a class="anchor-link" href="#amso" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<ul>
<li>Lead development of best practices, particularly the adapted Family Culture Matters (FCM) task.</li>
<li>Ensure coding is minimally evaluative to support unbiased measurement and minimize errors of inference.</li> 
</ul>
</div>

<div id="pini" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Nicolo Pini, Co-Investigator</span>
  <a class="anchor-link" href="#pini" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<ul>
<li>Serve as a leading member of the Novel Technologies/Wearables Workgroup.</li>
<li>Develop pipelines necessary for extraction of derivatives, data upload, storage, and maintenance of the EKG data collected during EEG and the heart rate wearable sensor data.</li>
<li>Coordinate the recurring training at the HBCD sites in these two modalities.</li> 
<li>Supervise quality control performed by Research Technician.</li>
</ul>
</div>

<div id="eisler" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Liana Eisler, Technician Research Assistant</span>
  <a class="anchor-link" href="#eisler" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<p>Quality control of outputs produced by automated pipelines.</p>
</div>

## UMD EEG Core
```mermaid
---
config:
  layout: dagre
---
flowchart LR
    n16["<b>Nathan Fox</b><br>Associate Director, Data Core"] --> UMD2["<b>Santiago Morales</b><br>Co-Investigator<br>
    <b>Jamie Listokin</b><br>EEG Core Research Coordinator"]
    UMD2 --> UMD3["<b>Marco McSweeney</b><br>Pre-processing &amp; Derivatives<br>
    <b>Whitney Kasenetz</b><br>EEG pre-processing in CBRAIN<br>
    <b>Savannah McNair</b><br><b>Jessica Norris</b><br>QC, EEG training, &amp; troubleshooting"]
    n16@{ shape: rounded}
    UMD2@{ shape: text}
    UMD3@{ shape: text}
    style n16 fill:#BBDEFB,stroke:none
    style UMD2 fill:#BBDEFB
    style UMD3 fill:#BBDEFB
```

## WashU

The Washington University in St. Louis (WashU) group has oversight of: *EHR*, *Ripple*, *Ambra*, *AirTable*, and *HCAC coordination*.

```mermaid
---
config:
  layout: dagre
---
flowchart LR
    A["<b>Chris Smyser</b><br>Principal Investigator<br>
    <b>Chad Sylvester</b><br>Co-Investigator"] --> neurology(["<b>Neurology</b>"]) & C(["<b>EHR</b><br>"]) & B["<b>Sauren Ravencroft</b><br><i>Project Manager</i>
    Oversight of WashU activities including Ripple, Ambra, AirTable, HCAC coordination"]
    neurology --> n1["<b>Bob McKinstry</b><br><b>Josh Shimony</b><br>Co-Investigators &amp; Study Neuroradiologists"]
    n1 --> n2["<b>Dimitrios Alexopoulos</b>
    Data Manager, Ambra"]
    C --> n3["<b>Philip Payne</b><br><b>Albert Lai</b>
    Co-Investigators, EHR oversight"]
    n3 --> n4["<b>Nicole Venteris</b><br>Project Manager, EHR"]
    B --> n5["<b>Lily Mueller</b>
    <i>Programmer</i>
    Ripple programming/ form management<br>
    <b>Lynn Menchaca</b>
    <i>Data Analyst</i>
    Ancillary studies, AirTable management<br>
    <b>Madison Gardner</b>
    <i>Research Assistant</i>
    U01 site beta testing/piloting"]
    A@{ shape: text}
    B@{ shape: text}
    n1@{ shape: text}
    n2@{ shape: text}
    n3@{ shape: text}
    n4@{ shape: text}
    n5@{ shape: text}
    style A fill:#BBDEFB
    style neurology fill:#E1BEE7,stroke:#000000
    style C stroke:#000000,fill:#E1BEE7
    style B fill:#BBDEFB
    style n1 fill:#BBDEFB
    style n2 fill:#BBDEFB
    style n3 fill:#BBDEFB
    style n4 fill:#BBDEFB
    style n5 fill:#BBDEFB
```

