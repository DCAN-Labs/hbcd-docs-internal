#  HDCC Organizational Charts <br> 🚧 UNDER CONSTRUCTION 🚧

## Overview
The larger organizational structure of the HBCD Data Coordinating Center (HDCC) is as follows - ***click on individual groups to be directed to their asssociated organizational charts***. Please visit the [HDCC page](https://hbcdstudy.org/hbcd-data-coordinating-center/) of the HBCD Study website for a full list of all HDCC members.

```mermaid
---
config:
  layout: dagre
---
flowchart TB
    A["<strong>HDCC</strong>"] --> E["<b>Damien Fair, PA-C, PhD</b><br>UMN, HDCC MPI"] & n1["<b>Chris Smyser</b><br>WashU"] & n2["<b>Anders Dale</b><br>UCSD"]
    E --> umn["<b>UMN</b><br>Reed McKewan"] & n7["<b>LORIS</b><br>Alan Evans<br>Samir Das"] & n8["<b>UMD EEG Core</b><br>Nathan Fox<br>Associate HDCC Director"] & n11["<b>Columbia</b><br><b>William P. Fifer</b><br>Novel Tech Work Group Chair"] & n15["<b>Lasso</b><br>Leigh MacIntyre"]
    n1 --> n10["<b>WashU</b><br>Chad Sylvester"] & n12["<b>LIBR</b>"] & n15
    n16@{ label: "<span style=\"--tw-scale-x:\"><b>Wesley K. Thompson<br></b>HDCC Associate Director & BioStatistics Work Group Chair</span><br>" } --> n17@{ label: "<span style=\"color:\"><b>Chun Fan<br></b></span><span style=\"--tw-scale-x:\">Geolocation Work Group Chair</span><br style=\"--tw-scale-x:\">" }
    n12 --> n16
    A@{ shape: rect}
    E@{ shape: rect}
    n1@{ shape: rect}
    n2@{ shape: rect}
    umn@{ shape: rounded}
    n7@{ shape: rounded}
    n8@{ shape: rounded}
    n11@{ shape: rounded}
    n15@{ shape: rounded}
    n10@{ shape: rounded}
    n12@{ shape: rounded}
    n16@{ shape: text}
    n17@{ shape: text}
    style A fill:#FFD600,stroke:#424242
    style E fill:#BBDEFB,stroke:#616161
    style n1 fill:#BBDEFB,stroke:#000000
    style n2 fill:#BBDEFB,stroke:#000000
    style umn fill:#E1BEE7,stroke:#000000
    style n7 fill:#E1BEE7,stroke:#000000
    style n8 fill:#E1BEE7,stroke:#757575
    style n11 fill:#E1BEE7,stroke:#757575
    style n15 fill:#E1BEE7,stroke:#000000
    style n10 fill:#E1BEE7,stroke:#000000
    style n12 fill:#E1BEE7,stroke:#000000
    style n16 fill:#BBDEFB
    style n17 fill:#BBDEFB
    click n2 "#ucsd"
    click umn "#university-of-minnesota"
    click n7 "#loris"
    click n8 "#umd-eeg-core"
    click n11 "#columbia"
    click n15 "#lasso"
    click n10 "#washu"
```

## Alt overview option

```mermaid
flowchart TB
    E["<b>Damien Fair, PA-C, PhD</b><br>HDCC Co-Director<br>University of Minnesota"] --> lasso["<b>Lasso</b>"] & umn["UMN"] & n7["<b>LORIS</b>"] & n8["<b>UMD EEG Core</b>"] & n11["<b>Columbia</b>"]
    lasso --> lasso1["<b>Leigh MacIntyre</b><br>Assoc. Dir, PM - MCIN"]
    n1["<b>Christopher Smyser, MD<br></b>HDCC Co-Director<br>WashU"] --> n10["<b>WashU</b><br>"] & n12["<b>LIBR</b>"] & lasso
    n16@{ label: "<span style=\"--tw-scale-x:\"><b>Wesley K. Thompson, PhD<br></b>HDCC Assoc. Dir.<br>&amp; BioStatistics Chair</span><br>" } --> n17@{ label: "<span style=\"color:\"><b>Chun Fan, PhD<br></b></span><span style=\"--tw-scale-x:\">Geolocation Chair</span><br style=\"--tw-scale-x:\">" }
    n12 --> n16
    n11 --> n18@{ label: "<b>William P. Fifer, PhD<br></b><span style=\"--tw-scale-x:\">Novel Tech Chair</span>" }
    n8 --> n19["<b>Nathan Fox, PhD<br></b>HDCC Assoc. Dir."]
    n7 --> n20@{ label: "<b><span style=\"color:\">Alan Evans</span><br style=\"--tw-scale-x:\"></b><span style=\"--tw-scale-x:\">PI</span><br style=\"--tw-scale-x:\"><b><span style=\"color:\">Samir Das</span><br style=\"--tw-scale-x:\"></b><span style=\"--tw-scale-x:\">AD Softw Dev</span>" }
    umn --> reed["<b>Reed McKewan, MS</b><br>Sr Research Dev"]
    n10 --> n22@{ label: "<b><span style=\"color:\">Chad Sylvester, PhD</span><br style=\"--tw-scale-x:\"></b><span style=\"--tw-scale-x:\">Co-Investigator</span>" }
    n23["<h3>HDCC</h3>"] --> n1 & n2["<b>Anders Dale, PhD<br></b>HDCC Co-Director<br>UCSD"] & E

    E@{ shape: rect}
    lasso@{ shape: rounded}
    umn@{ shape: rounded}
    n7@{ shape: rounded}
    n8@{ shape: rounded}
    n11@{ shape: rounded}
    lasso1@{ shape: text}
    n1@{ shape: rect}
    n10@{ shape: rounded}
    n12@{ shape: rounded}
    n16@{ shape: text}
    n17@{ shape: text}
    n18@{ shape: text}
    n19@{ shape: text}
    n20@{ shape: text}
    reed@{ shape: text}
    n22@{ shape: text}
    n23@{ shape: rounded}
    n2@{ shape: rect}
    style E fill:#BBDEFB,stroke:#757575
    style lasso fill:#E1BEE7,stroke:#000000
    style umn fill:#E1BEE7,stroke:#000000
    style n7 fill:#E1BEE7,stroke:#000000
    style n8 fill:#E1BEE7,stroke:#000000
    style n11 fill:#E1BEE7,stroke:#000000
    style lasso1 fill:#BBDEFB
    style n1 fill:#BBDEFB,stroke:#757575
    style n10 fill:#E1BEE7,stroke:#000000
    style n12 fill:#E1BEE7,stroke:#000000
    style n16 fill:#BBDEFB
    style n17 fill:#BBDEFB
    style n18 fill:#BBDEFB
    style n19 fill:#BBDEFB
    style n20 fill:#BBDEFB
    style reed fill:#BBDEFB
    style n22 fill:#BBDEFB
    style n23 stroke:#000000,fill:#E1BEE7,color:#000000
    style n2 fill:#BBDEFB,stroke:#757575
    click lasso "#lasso"
    click umn "#university-of-minnesota"
    click n7 "#loris"
    click n8 "#umd-eeg-core"
    click n11 "#columbia"
    click n10 "#washu"
    click n2 "#ucsd"
```

## HBCD Working Groups
<div id="columbia" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Columbia (Novel Technologies & Wearables Work Group)</span>
  <a class="anchor-link" href="#columbia" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<br>
<b>Leadership</b><br>
William P. Fifer, <i>Co-chair</i><br>
Dimo Amso, <i>Co-Investigator</i><br>
Nicolo Pini, <i>Co-Investigator & Pipeline Developer</i><br>
<br>
<b>Research Team</b><br>
Liana Eisler, <i>Technician</i><br>
<br>
</div>

<div id="umd-eeg-core" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">UMD EEG Core</span>
  <a class="anchor-link" href="#umd-eeg-core" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="table-arrow">▸</span>
</div>
<div class="closed-collapsible-content">
<br>
<b>Leadership</b><br>
Nathan Fox, <i>Associate Director, Data Core</i><br>
Santiago Morales, <i>Co-Investigator</i><br>
Jamie Listokin, <i>EEG Core Research Coordinator</i><br>
<br>
<b>Research Team</b><br>
Marco McSweeney: <i>Pre-processing & Derivatives</i><br>
Whitney Kasenetz: <i>EEG pre-processing in CBRAIN</i><br>
Savannah McNair: <i>QC, EEG training, & troubleshooting</i><br>
Jessica Norris: <i>QC, EEG training, & troubleshooting</i><br>
<br>
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
    click I "#ongaro-carcy"
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

<div id="ongaro-carcy" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Regis Ongaro-Carcy, Lead BHV Developer</span>
  <a class="anchor-link" href="#ongaro-carcy" title="Copy link">
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


## Lasso
```mermaid
---
config:
  theme: redux
---
flowchart TD
    A@{ label: "<b>Leigh MacIntyre</b><br>Associate Director, Project Management- MCIN" } --> B["Jennifer Zink"]
    B --> C["<b>Aarushi Chadhury</b><br>LORIS Project Coordinator"] & D["Jordan Stirling"] & n1["Fraser Glen"]
    A@{ shape: text}
    B@{ shape: text}
    C@{ shape: text}
    D@{ shape: text}
    n1@{ shape: text}
    style A fill:#BBDEFB
    style B fill:#BBDEFB
    style C fill:#BBDEFB
    style D fill:#BBDEFB
    style n1 fill:#BBDEFB
```

## University of Minnesota
UMN has three main cores that support the HBCD study: 

<div style="width: 80%; margin: 0 auto;">
```mermaid
---
config:
  theme: redux
  layout: dagre
---
flowchart TB
    A1["<b>Damien Fair</b><br>HDCC MPI<br>
    <b>Reed McKewan</b><br>HDCC Architect &amp; Data Manager"] --> HST["<b>Health Sciences Technology (HST)</b><br>"]
    A1 --> MIDB["<b>MIDB Informatics Hub & Minnesota Supercomputing Institute (MSI)</b><br>"] & DCAN["<b>Developmental Cognition and Neuroimaging Lab (DCAN)</b>"]
    A1@{ shape: text}
    HST@{ shape: rounded}
    MIDB@{ shape: rounded}
    DCAN@{ shape: rounded}
    style A1 fill:#BBDEFB
    style HST fill:#E1BEE7
    style MIDB fill:#E1BEE7
    style DCAN fill:#E1BEE7
    click HST "#health-sciences-technology-hst"
    click MIDB "#masonic-institute-for-the-developing-brain-midb-informatics-hub"
    click DCAN "#dcan-lab"
```
</div>

### Health Sciences Technology
[HST](https://hst.umn.edu/) at UMN is responsible for: *Data shelter*, *PHI*, *Ripple Interface*, *Overall Data Management*, *QC Dashboards*, *Ancillary Studies*, and *Third Party Integration*.
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
    L["<b>Thomas Pengo</b><br>Co-Director, Informatics Group"] --> M(["<b>Project Management</b>"]) & N(["<b>System Operations</b>"]) & O(["<b>Informatics &amp; Processing</b>"]) & P(["<b>Data Management</b>"])
    N --> Q["<b>Jesse Erdman</b><br>Senior SysOps<br>"]
    O --> n4["<b>Timothy Hendrickson</b><br>Neuroimaging Lead<br>
    <b>Erik Lee</b><br>Pipeline Lead<br>
    <b>Monalisa Biles</b><br>Analyst"]
    M --> n6@{ label: "<span style=\"--tw-scale-x:\"><b>Maren Macgregor-Hannah</b><br>HDCC PM</span><br style=\"--tw-scale-x:\">" }
    P --> n7["<b>Kimberleigh Breen</b><br>Data Manager<br>
    <b>Borgne Raasch</b><br>Data Steward<br>
    <b>Naomi Hospodarsky-Sutherland</b><br>Security/Compliance"]
    L@{ shape: text}
    Q@{ shape: text}
    n4@{ shape: text}
    n6@{ shape: text}
    n7@{ shape: text}
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
<div style="width: 80%; margin: 0 auto;">
```mermaid
---
config:
  layout: dagre
---
flowchart TB
    D["<b>Damien Fair, PA-C, PhD</b><br>Professor UMN<br>HDCC MPI"] --> S["<b>Eric Feczko, PhD</b><br>Neuroscience/Informatics<br>Software Engineer"] & t1["<b>Kim Weldon, PhD</b><br>Data Acquisition Seimens Engineer"] & n1["<b>Lucille A. Moore, PhD</b><br>Software Engineer"]
    D@{ shape: text}
    S@{ shape: text}
    t1@{ shape: text}
    n1@{ shape: text}
    style D stroke:#000000,fill:#BBDEFB
    style S stroke:#000000,fill:#BBDEFB
    style t1 fill:#BBDEFB
    style n1 fill:#BBDEFB
```
</div>

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

## WashU
The Washington University in St. Louis (WashU) group has oversight of: *Neurology*, *Electronic Health Records (EHR)*, *Ripple*, *Ambra*, *AirTable*, and *HCAC coordination*.

```mermaid
---
config:
  layout: dagre
---
flowchart TB
    A["<b>Chris Smyser</b><br>Principal Investigator<br>
    <b>Chad Sylvester</b><br>Co-Investigator"] --> neurology(["<b>Neurology</b>"]) & C(["<b>EHR</b><br>"]) & B["<b>Sauren Ravencroft</b><br>Project Manager"]
    neurology --> n1["<b>Bob McKinstry</b><br><b>Josh Shimony</b><br>Co-Investigators &amp; Study Neuroradiologists"]
    n1 --> n2["<b>Dimitrios (Jim) Alexopoulos</b>
    Data Manager, Ambra"]
    C --> n3["<b>Philip Payne</b><br><b>Albert Lai</b>
    Co-Investigators"]
    n3 --> n4["<b>Nicole Venteris</b><br>Project Manager"]
    B --> n5(["<b>Ripple</b>"]) & n6(["<b>AirTable &amp; Ancillary Studies</b>"])
    n5 --> n8["<b>Liliana Mueller</b>
    Programming &amp; Management"]
    n6 --> n9["<b>Lynn Menchaca</b>
    AirTable Management<br>"] & n10["<b>Madison Gardner</b>
    U01 Site Piloting"]
    A@{ shape: text}
    B@{ shape: text}
    n1@{ shape: text}
    n2@{ shape: text}
    n3@{ shape: text}
    n4@{ shape: text}
    n8@{ shape: text}
    n9@{ shape: text}
    n10@{ shape: text}
    style A fill:#BBDEFB
    style neurology fill:#E1BEE7,stroke:#000000
    style C stroke:#000000,fill:#E1BEE7
    style B fill:#BBDEFB
    style n1 fill:#BBDEFB
    style n2 fill:#BBDEFB
    style n3 fill:#BBDEFB
    style n4 fill:#BBDEFB
    style n5 fill:#E1BEE7,stroke:#000000
    style n6 fill:#E1BEE7,stroke:#000000
    style n8 fill:#BBDEFB,stroke:none
    style n9 fill:#BBDEFB
    style n10 fill:#BBDEFB
```

