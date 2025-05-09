#  HDCC Organizational Charts <br> 🚧 UNDER CONSTRUCTION 🚧

## Overview
The larger organizational structure of the HBCD Data Coordinating Center (HDCC) is as follows, with the HDCC Co-Directors listed at the top and the institutions/organizations listed below- ***click on individual institutions to be directed to their organizational charts***. Please visit the [HDCC page](https://hbcdstudy.org/hbcd-data-coordinating-center/) of the HBCD Study website for a full list of all HDCC members. 

<div id="faq-subids" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text"><b>NOTE:</b> These org charts emphasize functional structure, not reporting lines details.</span>
</div>
<br>

```mermaid
flowchart TB
    n2["<b>Anders Dale, PhD<br></b>HDCC Co-Director<br>UCSD"] --> ucsd["<b>UCSD</b>"]
    E["<b>Damien Fair, PA-C, PhD</b><br>HDCC Co-Director<br>University of Minnesota"] --> lasso["<b>Lasso</b>"] & umn["<b>UMN</b>"] & n7["<b>LORIS</b>"] & n8["<b>UMD EEG Core</b>"] & n11["<b>Columbia</b>"]
    lasso --> lasso1["<b>Leigh MacIntyre</b><br>Assoc Dir, PM - MCIN"]
    n1["<b>Christopher Smyser, MD<br></b>HDCC Co-Director<br>WashU"] --> n10["<b>WashU</b><br>"] & n12["<b>LIBR</b>"] & lasso
    n16@{ label: "<span style=\"--tw-scale-x:\"><b>Wesley K.<br>Thompson, PhD<br></b>HDCC Assoc Dir,<br>BioStatistics Chair</span><br>" } --> n17@{ label: "<span style=\"color:\"><b>Chun Fan, PhD<br></b></span><span style=\"--tw-scale-x:\">Geolocation Chair</span><br style=\"--tw-scale-x:\">" }
    n12 --> n16
    n11 --> n18@{ label: "<b>William P. Fifer, PhD<br></b><span style=\"--tw-scale-x:\">Novel Tech Chair</span>" }
    n8 --> n19["<b>Nathan Fox, PhD<br></b>HDCC Assoc. Dir."]
    n7 --> n20@{ label: "<b><span style=\"color:\">Alan Evans</span><br style=\"--tw-scale-x:\"></b><span style=\"--tw-scale-x:\">PI</span><br style=\"--tw-scale-x:\"><b><span style=\"color:\">Samir Das</span><br style=\"--tw-scale-x:\"></b><span style=\"--tw-scale-x:\">AD Softw Dev</span>" }
    umn --> reed["<b>Reed McKewan, MS</b><br>Sr Research Dev"]
    n10 --> n22@{ label: "<b><span style=\"color:\">Chad Sylvester, PhD</span><br style=\"--tw-scale-x:\"></b><span style=\"--tw-scale-x:\">Co-Investigator</span>" }

    n1@{ shape: rect}
    E@{ shape: rect}
    n2@{ shape: rect}
    ucsd@{ shape: rounded}
    lasso@{ shape: rounded}
    umn@{ shape: rounded}
    n7@{ shape: rounded}
    n8@{ shape: rounded}
    n11@{ shape: rounded}
    lasso1@{ shape: text}
    n10@{ shape: rounded}
    n12@{ shape: rounded}
    n16@{ shape: text}
    n17@{ shape: text}
    n18@{ shape: text}
    n19@{ shape: text}
    n20@{ shape: text}
    reed@{ shape: text}
    n22@{ shape: text}
    style n1 fill:#BBDEFB,stroke:#2962FF
    style E fill:#BBDEFB,stroke:#2962FF
    style n2 fill:#BBDEFB,stroke:#2962FF
    style ucsd fill:#E1BEE7,stroke:#AA00FF
    style lasso fill:#E1BEE7,stroke:#AA00FF
    style umn fill:#E1BEE7,stroke:#AA00FF
    style n7 fill:#E1BEE7,stroke:#AA00FF
    style n8 fill:#E1BEE7,stroke:#AA00FF
    style n11 fill:#E1BEE7,stroke:#AA00FF
    style lasso1 fill:#BBDEFB
    style n10 fill:#E1BEE7,stroke:#AA00FF
    style n12 fill:#E1BEE7,stroke:#AA00FF
    style n16 fill:#BBDEFB
    style n17 fill:#BBDEFB
    style n18 fill:#BBDEFB
    style n19 fill:#BBDEFB
    style n20 fill:#BBDEFB
    style reed fill:#BBDEFB
    style n22 fill:#BBDEFB
    click ucsd "#ucsd"
    click lasso "#lasso"
    click umn "#university-of-minnesota"
    click n7 "#loris"
    click n8 "#umd-eeg-core"
    click n11 "#columbia"
    click n10 "#washu"
```

## LORIS
```mermaid
---
config:
  layout: dagre
---
flowchart TB
    A["<b>Alan Evans</b><br>Principal Investigator"] --> nl["<b>Samir Das</b><br>Associate Director of Software Development"]
    nl --> n9(["<b>Study Coordination</b>"]) & C(["<b>CBRAIN/Computing</b><br>"]) & B(["<b>Development</b>"])
    C --> n12["<b>Bryan Caron</b><br>Director, CBRAIN &amp; NeuroHub - MCIN"]
    n9 --> E["<b>Santiago Torres</b><br>Study Officer"]
    B --> F["<b>BHV/Database</b>"] & H["<b>EEG/Biosamples</b>"] & G["<b>MRI</b>"]
    F --> I["<b>Regis Ongaro-Carcy</b><br>Lead Developer"] & n10["<b>Sruthy Matthew</b><br>Sr. Backend Dev"]
    G --> L["<b>Cecile Madjar</b><br>Lead developer"]
    H --> M["<b>Laetitia Faeselier</b><br>Lead Developer"]
    n10 --> n11["<b>George Murad</b>, Jr. Dev"]
    I --> n11
    n12 --> D["<b>Pierre Rioux</b><br>Senior HPC developer"]
    A@{ shape: text}
    nl@{ shape: text}
    n12@{ shape: text}
    E@{ shape: text}
    F@{ shape: rounded}
    H@{ shape: rounded}
    G@{ shape: rounded}
    I@{ shape: text}
    n10@{ shape: text}
    L@{ shape: text}
    M@{ shape: text}
    n11@{ shape: text}
    D@{ shape: text}
    style A stroke:#000000,fill:#BBDEFB
    style nl stroke:#000000,fill:#BBDEFB
    style n9 stroke:#000000,fill:#E1BEE7,stroke-width:2px,stroke-dasharray: 0
    style C stroke:#333,fill:#E1BEE7
    style B stroke:#333,fill:#E1BEE7
    style n12 fill:#BBDEFB
    style E stroke:#333,fill:#BBDEFB
    style F stroke:#333,fill:#E1BEE7
    style H stroke:#333,fill:#E1BEE7
    style G stroke:#333,fill:#E1BEE7
    style I stroke:#333,fill:#BBDEFB
    style n10 fill:#BBDEFB
    style L stroke:#000000,fill:#BBDEFB
    style M fill:#BBDEFB,stroke:#000000
    style n11 fill:#BBDEFB
    style D stroke:#333,fill:#BBDEFB
    click A "#evans"
    click nl "#das"
    click E "#torres"
    click I "#ongaro-carcy"
    click n10 "#matthew"
    click L "#madjar"
    click M "#faeselier"
    click n11 "#murad"
    click D "#rioux"
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
  layout: dagre
---
flowchart TB
    A1["<b>Damien Fair</b><br>HDCC MPI<br>
    <b>Reed McEwan</b><br>HDCC Architect &amp; Data Manager"] --> HST(["<b>Health Sciences Technology (HST)</b><br>"]) & MIDB(["<b>MIDB Informatics Hub &amp; Minnesota Supercomputing Institute (MSI)</b><br>"]) & DCAN(["<b>Developmental Cognition and Neuroimaging Lab (DCAN)</b>"]) & USDTL(["<b>USDTL</b>"])
    A1@{ shape: text}
    style A1 fill:#BBDEFB
    style HST fill:#E1BEE7,stroke:#AA00FF
    style MIDB fill:#E1BEE7,stroke:#AA00FF
    style DCAN fill:#E1BEE7,stroke:#AA00FF
    style USDTL fill:#E1BEE7,stroke:#AA00FF
    click HST "#health-sciences-technology-hst"
    click MIDB "#masonic-institute-for-the-developing-brain-midb-informatics-hub"
    click DCAN "#dcan-lab"
```
</div>

### Health Sciences Technology
[HST](https://hst.umn.edu/) at UMN is responsible for: *Data shelter*, *PHI*, *Ripple Interface*, *Overall Data Management*, *QC Dashboards*, *Ancillary Studies*, and *Third Party Integration*.

![](https://www.mermaidchart.com/raw/16bb04e3-f6e3-4058-a217-877ae8343c57?theme=light&version=v0.1&format=svg)

### MIDB Informatics Hub & MSI
The [Masonic Institute for the Developing Brain (MIDB) Informatics Hub](https://midb.umn.edu/research/informatics) and [Minnesota Supercomputing Institute (MSI)](https://msi.umn.edu/) at UMN provide the following services to the HBCD study: *System Administration*, *Loris Hosting*, *Computing*, *Processing*, and *Data Sharing*.

![](https://www.mermaidchart.com/raw/fa8b14a3-8b42-4ed6-9167-b3872f2d9855?theme=light&version=v0.1&format=svg)

### DCAN Lab
The Developmental Cognition and Neuroimaging Lab ([DCAN](https://innovation.umn.edu/developmental-cognition-and-neuroimaging-lab)) at UMN is responsible for: *Processing*, *Software Development*, and *Deployment* of imaging data. 

<img src="https://www.mermaidchart.com/raw/deb324cd-c386-477d-8b46-f842362da3c8?theme=light&version=v0.1&format=svg" width="80%" height="auto" class="center">

## J. Craig Venter Institute

The [J. Craig Venter Institute](https://www.jcvi.org/) (JCVI) is responsible for MRI quality control, REDCap, Fiona, and the QC Dashboard.

![](https://www.mermaidchart.com/raw/cd632b85-d99d-48e5-82b1-553d346b8f2a?theme=light&version=v0.1&format=svg)


## WashU
The Washington University in St. Louis (WashU) group has oversight of: *Neurology*, *Electronic Health Records (EHR)*, *Ripple*, *Ambra*, *AirTable*, and *HCAC coordination*.

![](https://www.mermaidchart.com/raw/1a26c247-6f63-4ac1-83c9-3607e79beb4a?theme=light&version=v0.1&format=svg)

## Columbia University
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

## University of Maryland EEG Core
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