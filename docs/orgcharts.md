#  HDCC Organizational Charts <br> 🚧 UNDER CONSTRUCTION 🚧

## Overview
The larger organizational structure of the HBCD Data Coordinating Center (HDCC) is as follows, with the HDCC Co-Directors listed at the top and the institutions/organizations listed below- ***click on individual institutions to be directed to their organizational charts***. Please visit the [HDCC page](https://hbcdstudy.org/hbcd-data-coordinating-center/) of the HBCD Study website for a full list of all HDCC members. 

<div id="faq-subids" class="notification-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
    <span class="text"><b>NOTE:</b> These org charts emphasize functional structure within the context of HDCC, not reporting line details of individual organizations.</span>
</div>
<br>

```mermaid
---
config:
  layout: dagre
---
flowchart TB
    n2["<b>Anders Dale, PhD<br></b>HDCC Co-Director<br>JCVI"] --> jvci["<b>JVCI</b>"]
    E["<b>Damien Fair, PA-C, PhD</b><br>HDCC Co-Director<br>University of Minnesota"] --> lasso["<b>Lasso</b>"] & umn["<b>UMN</b>"] & n7["<b>LORIS</b>"] & n8["<b>UMD EEG Core</b>"] & n11["<b>Columbia</b>"]
    lasso --> lasso1["<b>Leigh MacIntyre</b><br>MCIN Assoc Dir, PM"]
    n1["<b>Christopher Smyser, MD<br></b>HDCC Co-Director<br>WashU"] --> n10["<b>WashU</b><br>"] & ripple["<b>Ripple</b>"] & n12["<b>LIBR</b>"] & lasso
    n16["<b>Wesley K.<br>Thompson, PhD</b><br>HDCC Assoc Dir,<br>BioStatistics Chair"] --> n17@{ label: "<span style=\"color:\"><b>Chun Fan, PhD<br></b></span><span style=\"--tw-scale-x:\">Geolocation Chair</span><br style=\"--tw-scale-x:\">" }
    n12 --> n16
    n8 --> n19["<b>Nathan Fox, PhD<br></b>HDCC Assoc. Dir."]
    n7 --> n20@{ label: "<b><span style=\"color:\">Alan Evans</span><br style=\"--tw-scale-x:\"></b><span style=\"--tw-scale-x:\">PI</span><br style=\"--tw-scale-x:\"><b><span style=\"color:\">Samir Das</span><br style=\"--tw-scale-x:\"></b><span style=\"--tw-scale-x:\">AD Softw Dev</span>" }
    umn --> reed["<b>Reed McEwan, MS</b><br>Sr Research Dev"]
    n10 --> n22@{ label: "<b><span style=\"color:\">Chad<br>Sylvester, PhD</span><br style=\"--tw-scale-x:\"></b><span style=\"--tw-scale-x:\">Co-Investigator</span>" }
    n11 --> n23(["<b>Novel Tech &amp; Wearables</b>"])
    n23 --> n18["<b>William P. Fifer, PhD</b>, Chair<br><b>Nicolo Pini</b>, Co-I &amp; Dev<br><b>Beth Smith</b>"]
    reed --> n25@{ label: "<span style=\"--tw-scale-x:\"><b>USDTL</b></span>" } & n26(["<b>MIDB &amp; MSI</b>"]) & n27(["<b>DCAN Lab</b>"]) & n30(["<b>HST</b>"])
    n2@{ shape: rect}
    jvci@{ shape: rounded}
    E@{ shape: rect}
    lasso@{ shape: rounded}
    umn@{ shape: rounded}
    n7@{ shape: rounded}
    n8@{ shape: rounded}
    n11@{ shape: rounded}
    lasso1@{ shape: text}
    n1@{ shape: rect}
    n10@{ shape: rounded}
    ripple@{ shape: rounded}
    n12@{ shape: rounded}
    n16@{ shape: rect}
    n17@{ shape: text}
    n19@{ shape: rect}
    n20@{ shape: text}
    reed@{ shape: text}
    n22@{ shape: text}
    n18@{ shape: text}
    n25@{ shape: stadium}
    style n2 fill:#BBDEFB,stroke:#2962FF
    style jvci fill:#E1BEE7,stroke:#AA00FF
    style E fill:#BBDEFB,stroke:#2962FF
    style lasso fill:#E1BEE7,stroke:#AA00FF
    style umn fill:#E1BEE7,stroke:#AA00FF
    style n7 fill:#E1BEE7,stroke:#AA00FF
    style n8 fill:#E1BEE7,stroke:#AA00FF
    style n11 fill:#E1BEE7,stroke:#AA00FF
    style lasso1 fill:#BBDEFB
    style n1 fill:#BBDEFB,stroke:#2962FF
    style n10 fill:#E1BEE7,stroke:#AA00FF
    style ripple fill:#E1BEE7,stroke:#AA00FF
    style n12 fill:#E1BEE7,stroke:#AA00FF
    style n16 fill:#BBDEFB,stroke:#2962FF
    style n17 fill:#BBDEFB
    style n19 fill:#BBDEFB,stroke:#2962FF
    style n20 fill:#BBDEFB
    style reed fill:#BBDEFB
    style n22 fill:#BBDEFB
    style n23 fill:#E1BEE7,stroke:#AA00FF
    style n18 fill:#BBDEFB
    style n25 fill:#E1BEE7,stroke:#AA00FF
    style n26 fill:#E1BEE7,stroke:#AA00FF
    style n27 fill:#E1BEE7,stroke:#AA00FF
    style n30 fill:#E1BEE7,stroke:#AA00FF
    click jvci "#j-craig-venter-institute"
    click lasso "#lasso"
    click umn "#university-of-minnesota"
    click n7 "#loris"
    click n8 "#umd-eeg-core"
    click n10 "#washu"
```

## Overview - Alternative
```mermaid
flowchart TB
    layout: elk
    n2[<b>Anders Dale, PhD<br></b>HDCC Co-Director<br>JCVI] --> jvci[<b>JVCI</b>]
```

## LORIS
```mermaid
---
config:
  layout: dagre
---
flowchart TB
    A["<b>Alan Evans</b><br>Principal Investigator"] --- nl["<b>Samir Das</b><br>Associate Director of Software Development"]
    nl --- n9(["<b>Study Coordination</b>"]) & C(["<b>CBRAIN/Computing</b>"]) & B(["<b>Development</b>"])
    C --- n12["<b>Bryan Caron</b><br>Director, CBRAIN &amp; NeuroHub - MCIN"]
    n9 --- E["<b>Santiago Torres</b><br>Study Officer"]
    B --- F["<b>BHV/Database</b>"] & H["<b>EEG/Biosamples</b>"] & G["<b>MRI</b>"]
    F --- I["<b>Regis Ongaro-Carcy</b><br>Lead Developer"] & n10["<b>Sruthy Matthew</b><br>Sr. Backend Dev"]
    G --- L["<b>Cecile Madjar</b><br>Lead developer"]
    H --- M["<b>Laetitia Faeselier</b><br>Lead Developer"]
    n10 --- n11["<b>George Murad</b>, Jr. Dev"]
    I --- n11
    n12 --- D["<b>Pierre Rioux</b><br>Senior HPC developer"]
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
    style n9 stroke:#000000,fill:#E1BEE7
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
#### Overview
```mermaid
---
config:
  theme: redux
---
flowchart TB
    A["<b>Leigh MacIntyre</b>, CEO<br>MCIN Assoc. Dir., PM"] --> B(["<b>Pre-Release Training<br>Scheduling<br></b>"]) & n1(["<b>Ancillary<br>Studies</b>"]) & n2(["<b>WorkGroup<br>Data QC</b>"]) & n3(["<b>Technical</b>"]) & n4(["<b>Data<br>Loading</b>"]) & n18@{ label: "<b style=\"color:\"><u>Internal</u><br></b>(<i>Click for Details</i>)" }
    B --> n5["<b>Ellise Elamparo</b><br>Exec Admin"]
    n1 --> n6["<b>Aarushi Chaudhry<br></b>Study Success<br>Manager"]
    n2 --> n7["<b>Jen Zink<br></b>Director,<br>Partnerships &amp; Grant<br>Funding<br><br><b>Marion Fechino</b><br>Data Analyst"]
    n3 --> n8["<b>Fraser Glen<br></b>CTO<br><br><b>Jordan<br>Sterling<br></b>Lead Dev"]
    n4 --> n9@{ label: "<span style=\"--tw-scale-x:\"><b>Laetitia Fesselier<br style=\"--tw-scale-x:\"></b></span>Sr. Dev<br><b><br>Edson Silva</b><br><b>Mateus Andre<br></b>Dev" }
    A@{ shape: text}
    n18@{ shape: stadium}
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
<br>

#### Internal / Non-Consortium-Facing

<div style="width: 80%; margin: 0 auto;">
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
    n10["<b>Leigh MacIntyre</b>, CEO<br>MCIN Assoc. Dir., PM"] --> B & n1 & n3 & n4
    n5@{ shape: text}
    n6@{ shape: text}
    n8@{ shape: text}
    n9@{ shape: text}
    n10@{ shape: text}
    style B fill:#E1BEE7
    style n5 fill:#BBDEFB
    style n1 fill:#E1BEE7
    style n6 fill:#BBDEFB
    style n3 fill:#E1BEE7
    style n8 fill:#BBDEFB
    style n4 fill:#E1BEE7
    style n9 fill:#BBDEFB
    style n10 fill:#BBDEFB
```
</div>

## University of Minnesota
There are several groups that fall under the oversight of UMN. The US Drug Testing Laboratories ([USDTL](https://www.usdtl.com/)) handles toxicology. The Developmental Cognition and Neuroimaging Lab ([DCAN](https://innovation.umn.edu/developmental-cognition-and-neuroimaging-lab)) led by Damien Fair at UMN is responsible for: *Processing*, *Software Development*, and *Deployment* of imaging data. The remaining groups are described in greater detail below.  

<div style="width: 90%; margin: 0 auto;">
```mermaid
---
config:
  layout: dagre
---
flowchart TB
    A1["<b>Damien Fair</b><br>HDCC MPI<br>
    <b>Reed McEwan</b><br>HDCC Architect &amp; Data Manager"] --- HST(["<b>Health Sciences Technology (HST)</b><br>"]) & MIDB(["<b>MIDB Informatics Hub &amp; Minnesota Supercomputing Institute (MSI)</b><br>"]) & DCAN(["<b>Developmental Cognition and Neuroimaging Lab (DCAN)</b>"]) & USDTL(["<b>USDTL</b>"])
    DCAN --- n1(["<b>Neuroinformatics</b>"]) & n2(["<b>MRI Acquisition</b>"])
    n1 --- n3["<b>Eric Feczko, PhD</b><br></b><b>Lucille A. Moore, PhD</b>"]
    n2 --- n4["<b>Kimberly Weldon, PhD</b><br>Seimens Engineer"]
    A1@{ shape: text}
    n3@{ shape: text}
    n4@{ shape: text}
    style A1 fill:#BBDEFB
    style HST fill:#E1BEE7,stroke:#AA00FF
    style MIDB fill:#E1BEE7,stroke:#AA00FF
    style DCAN fill:#E1BEE7,stroke:#AA00FF
    style USDTL fill:#E1BEE7,stroke:#AA00FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#BBDEFB
    style n4 fill:#BBDEFB
    click HST "#health-sciences-technology-hst"
    click MIDB "#masonic-institute-for-the-developing-brain-midb-informatics-hub"
```
</div>

### Health Sciences Technology
[HST](https://hst.umn.edu/) at UMN is responsible for: *Data shelter*, *PHI*, *Ripple Interface*, *Overall Data Management*, *QC Dashboards*, *Ancillary Studies*, and *Third Party Integration*.

<div style="width: 80%; margin: 0 auto;">
```mermaid
---
config:
  layout: dagre
---
flowchart TB
    B["<b>Reed McEwan</b><br>HDCC Architect &amp; Data Manager"] --- n1(["<b>Project Management</b>"]) & n2(["<b>DevOps</b>"]) & n3(["<b>MRI Dashboard</b>"]) & n4(["<b>EHR</b>"])
    H["<b>Constantine Aliferis</b><br>Dir. Insitute Health Informatics"] --- I["<b>Steve Johnson</b><br>Director Informatics Innovation<br><b>Tim Meyer</b><br>EHR Informatics Engineer"]
    n1 --- E["<b>Karen Athy-Penrose</b><br>Data Shelter PM"]
    n2 --- F["<b>Dan Duhon</b><br>DevOps/ETL"]
    n3 --- G["<b>Haley Hutala</b><br>Tableau Engineer"]
    n4 --- H
    B@{ shape: text}
    H@{ shape: text}
    I@{ shape: text}
    E@{ shape: text}
    F@{ shape: text}
    G@{ shape: text}
    style B fill:#BBDEFB
    style n1 fill:#E1BEE7,stroke:#000000
    style n2 fill:#E1BEE7,stroke:#000000
    style n3 fill:#E1BEE7,stroke:#000000
    style n4 fill:#E1BEE7,stroke:#000000
    style H fill:#BBDEFB
    style I fill:#BBDEFB
    style E fill:#BBDEFB
    style F fill:#BBDEFB
    style G fill:#BBDEFB
```
</div>

### MIDB Informatics Hub & MSI
The [Masonic Institute for the Developing Brain (MIDB) Informatics Hub](https://midb.umn.edu/research/informatics) and [Minnesota Supercomputing Institute (MSI)](https://msi.umn.edu/) at UMN provide the following services to the HBCD study: *System Administration*, *Loris Hosting*, *Computing*, *Processing*, and *Data Sharing*.

```mermaid
---
config:
  layout: dagre
---
flowchart TB
    L["<b>Thomas Pengo</b><br>Co-Director, Informatics Group"] --- M(["<b>Project<br>Management</b>"]) & N(["<b>Advanced<br>SysOps (ASO)</b>"]) & O(["<b>Informatics<br>&amp; Processing</b>"]) & P(["<b>Data Steward</b>"]) & n8(["<b>Security &amp;<br>Compliance</b>"])
    N --- Q@{ label: "<b style=\"color:\">Jesse Erdman</b><br>Senior SysOps<br><br><b style=\"color:\"><span style=\"--tw-scale-x:\">Kimberleigh Breen</span><br style=\"--tw-scale-x:\"></b>Data Manager<br><br><b>Sriharshitha Anuganti<br></b>DevOps" }
    O --- n4["<b>Timothy Hendrickson</b><br>Neuroimaging Lead<br>
    <b>Erik Lee</b><br>Pipeline Lead<br>
    <b>Monalisa Biles</b><br>Analyst"]
    M --- n6@{ label: "<span style=\"--tw-scale-x:\"><b>Maren Macgregor-Hannah</b><br>HDCC PM</span><br style=\"--tw-scale-x:\">" }
    P --- n7["<b>Borgne Raasch</b><br>"]
    n8 --- n9@{ label: "<span style=\"--tw-scale-x:\"><b>Naomi<br>Hospodarsky-Sutherland</b></span><br style=\"--tw-scale-x:\">" }
    L@{ shape: text}
    Q@{ shape: text}
    n4@{ shape: text}
    n6@{ shape: text}
    n7@{ shape: text}
    n9@{ shape: text}
    style L fill:#BBDEFB
    style M fill:#E1BEE7,stroke:#333
    style N fill:#E1BEE7,stroke:#333
    style O fill:#E1BEE7,stroke:#333
    style P fill:#E1BEE7,stroke:#333
    style n8 fill:#E1BEE7,stroke:#333
    style Q fill:#BBDEFB
    style n4 fill:#BBDEFB
    style n6 fill:#BBDEFB
    style n7 fill:#BBDEFB
    style n9 fill:#BBDEFB
```

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


## J. Craig Venter Institute

The [J. Craig Venter Institute](https://www.jcvi.org/) (JCVI) is responsible for MRI quality control, REDCap, Fiona, and the QC Dashboard.

```mermaid
---
config:
  layout: dagre
---
flowchart TB
    A["<b>Anders Dale, PhD</b><br>PI/Director"] --- n1(["<b>Fiona</b>"]) & n2(["<b>MRI QC</b>"]) & n3(["<b>MRI</b>"]) & n6(["<b>REDCap</b>"]) & n15(["<b>Dashboard</b>"])
    n1 --- n8["<b>Rongguang Yang, PhD</b><br>Fiona Lead<br>"]
    n2 --- n9["<b>Donald Hagler, PhD</b><br>QC Lead<br>"]
    n3 --- n10["<b>Josh Kuperman</b><br>MRI Lead"]
    n6 --- n4["<b>Janosch Linkersdörfer, PhD</b><br>Data Science Lead"]
    n9 --- n13@{ label: "<span style=\"--tw-scale-x:\"><b>Tyler Berkness<br></b></span><span style=\"background-color:\">Protocol Violations<br></span><br><span style=\"--tw-scale-x:\"><span style=\"--tw-scale-x:\"><b>Sejal Shanbhag<br style=\"--tw-scale-x:\"></b></span></span><span style=\"--tw-scale-x:\">Issue Handling</span>" }
    n15 --- n4
    n4 --- n12["<b><b><u>RECap</u></b><br>Joseph Baligh</b><br>Server Admin<br><b>Erika Bolden</b> &amp; <b>Laura Ziemer</b><br>Dev/Admin"] & n18@{ label: "<span style=\"--tw-scale-x:\"><span style=\"--tw-scale-x:\"><b><span style=\"--tw-scale-x:\">Amanda Li, MS</span><br style=\"--tw-scale-x:\"></b></span></span><span style=\"--tw-scale-x:\">Biostats Support</span>" } & n17@{ label: "<span style=\"--tw-scale-x:\"><b><b><u>Dashboard</u></b><br>Biplabendu Das</b><br>Backend Dev<br></span><span style=\"--tw-scale-x:\"><b>Olivier Celhay</b><br></span><span style=\"background-color:\">Frontend Dev</span>" }
    A@{ shape: text}
    n8@{ shape: text}
    n9@{ shape: text}
    n10@{ shape: text}
    n4@{ shape: text}
    n13@{ shape: text}
    n12@{ shape: text}
    n18@{ shape: text}
    n17@{ shape: text}
    style A fill:#BBDEFB
    style n1 fill:#E1BEE7,stroke:#000000
    style n2 stroke:#000000,fill:#E1BEE7
    style n3 stroke:#000000,fill:#E1BEE7
    style n6 stroke:#000000,fill:#E1BEE7
    style n15 fill:#E1BEE7,stroke:#000000
    style n8 fill:#BBDEFB
    style n9 fill:#BBDEFB
    style n10 fill:#BBDEFB
    style n4 fill:#BBDEFB
    style n13 fill:#BBDEFB
    style n12 fill:#BBDEFB
    style n18 fill:#BBDEFB
    style n17 fill:#BBDEFB
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
    <b>Chad Sylvester</b><br>Co-Investigator"] --- neurology(["<b>Neurology</b>"]) & C(["<b>EHR</b><br>"]) & B["<b>Sauren Ravencroft</b><br>Project Manager"] & n11(["<b>OMOR</b>"])
    neurology --- n1["<b>Bob McKinstry</b><br><b>Josh Shimony</b><br>Co-Investigators &amp; Study Neuroradiologists"]
    n1 --- n2["<b>Dimitrios (Jim) Alexopoulos</b>
    Data Manager, Ambra"]
    C --- n3["<b>Philip Payne</b><br><b>Albert Lai</b>
    Co-Investigators"]
    n3 --- n4["<b>Nicole Venteris</b><br>Project Manager"]
    B --- n5(["<b>Ripple</b>"]) & n6(["<b>AirTable &amp; Ancillary Studies</b>"])
    n5 --- n8["<b>Liliana Mueller</b>
    Programming &amp; Management"]
    n6 --- n9["<b>Lynn Menchaca</b>
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
    style n11 stroke:#000000,fill:#E1BEE7
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

## University of Maryland EEG Core
<div style="width: 80%; margin: 0 auto;">
```mermaid
---
config:
  layout: dagre
---
flowchart TB
    n16["<b>Nathan Fox</b><br>Associate Director, Data Core"] --- UMD2["<b>Santiago Morales</b>, Co-Investigator<br>
    <b>Jamie Listokin</b>, EEG Core Research Coordinator"]
    UMD2 --- n17(["<b>EEG Processing</b>"]) & n18(["<b>CBRAIN</b>"]) & n21(["<b>QC, Training, &amp; Troubleshooting</b>"])
    n17 --- n19@{ label: "<span style=\"--tw-scale-x:\"><b>Marco McSweeney</b><br>Pre-processing &amp; Derivatives</span>" }
    n18 --- n20@{ label: "<span style=\"--tw-scale-x:\"><b>Whitney Kasenetz</b></span><br style=\"--tw-scale-x:\">EEG pre-processing in CBRAIN" }
    n21 --- n22@{ label: "<b><span style=\"--tw-scale-x:\">Savannah McNair</span><br style=\"--tw-scale-x:\"><span style=\"--tw-scale-x:\">Jessica Norris</span></b>" }
    n16@{ shape: rounded}
    UMD2@{ shape: text}
    n19@{ shape: text}
    n20@{ shape: text}
    n22@{ shape: text}
    style n16 fill:#BBDEFB,stroke:none
    style UMD2 fill:#BBDEFB
    style n17 fill:#E1BEE7,stroke:#000000
    style n18 fill:#E1BEE7,stroke:#000000
    style n21 fill:#E1BEE7,stroke:#000000
    style n19 fill:#BBDEFB
    style n20 fill:#BBDEFB
    style n22 fill:#BBDEFB
```
</div>