#  🚧 HDCC Organizational Charts 🚧

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
  layout: elk
---
flowchart TB
    n2["<b>Anders Dale, PhD<br></b>HDCC Co-Director<br>JCVI"] --> jvci["<b>JVCI</b>"]
    E["<b>Damien Fair, PA-C, PhD</b><br>HDCC Co-Director<br>University of Minnesota"] 
    E --> lasso["<b>Lasso</b>"]
    E --> umn["<b>UMN</b>"]
    E --> n7["<b>LORIS</b>"]
    E --> n8["<b>UMD EEG Core</b>"]
    E --> n11["<b>Columbia</b>"]
    lasso --> lasso1["<b>Leigh MacIntyre</b><br>MCIN Assoc Dir, PM"]
    n1["<b>Christopher Smyser, MD<br></b>HDCC Co-Director<br>WashU"] 
    n1 --> n10["<b>WashU</b><br>"] & ripple["<b>Ripple</b>"] & n12["<b>LIBR</b>"] & lasso
    n16["<b>Wesley K.<br>Thompson, PhD</b><br>HDCC Assoc Dir,<br>BioStatistics Chair"] 
    n16 --> n17["<b>Chun Fan, PhD</b><br>Geolocation Chair"]
    n12 --> n16
    n8 --> n19["<b>Nathan Fox, PhD<br></b>HDCC Assoc. Dir."]
    n7 --> n20["<b>Alan Evans</b><br>PI<br><b>Samir Das</b><br>AD Softw Dev"]
    umn --> reed["<b>Reed McEwan, MS</b><br>Sr Research Dev"]
    n10 --> n22["<b>Chad Sylvester, PhD</b><br>Co-Investigator"]
    n11 --> n23(["<b>Novel Tech &amp; Wearables</b>"])
    n23 --> n18["<b>William P. Fifer, PhD</b>, Chair<br><b>Nicolo Pini</b>, Co-I &amp; Dev<br><b>Beth Smith</b>"]
    reed --> n25(["<b>USDTL</b>"]) & n26(["<b>MIDB &amp; MSI</b>"]) & n27(["<b>DCAN Lab</b>"]) & n30(["<b>HST</b>"])
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

## LORIS
```mermaid
---
config:
  layout: elk
---
flowchart TB
    A["<b>Alan Evans</b>, PI"] --- nl["<b>Samir Das</b><br>Assoc Dir Softw Dev"]
    nl --- n9(["<b>Study Coordination</b>"]) & C(["<b>CBRAIN/Computing</b>"])
    C --- n12["<b>Bryan Caron</b><br>Director, CBRAIN<br>&amp; NeuroHub - MCIN<br><br><b>Pierre Rioux</b><br>Sr HPC Dev"]
    n9 --- E["<b>Santiago Torres</b><br>Study Officer"]
    F(["<b>Behavior (BHV)</b>"]) --- I["<b>Regis Ongaro-Carcy</b><br>Lead Dev<br><br><b>Sruthy Matthew</b><br>Sr Backend Dev<br><br><b>George Murad</b>, Jr Dev"]
    G(["<b>MRI</b>"]) --- L["<b>Cecile Madjar</b><br>Lead Dev"]
    H(["<b>EEG/Biosamples</b>"]) --- M["<b>Laetitia Faeselier</b><br>Lead Dev"]
    nl --> G & H & F
    style A stroke:#2962FF,fill:#BBDEFB
    style nl stroke:#2962FF,fill:#BBDEFB
    style n9 stroke:#AA00FF,fill:#E1BEE7
    style C stroke:#AA00FF,fill:#E1BEE7
    style n12 stroke:#2962FF,fill:#BBDEFB
    style E stroke:#2962FF,fill:#BBDEFB
    style F stroke:#AA00FF,fill:#E1BEE7
    style I stroke:#2962FF,fill:#BBDEFB
    style G stroke:#AA00FF,fill:#E1BEE7
    style L stroke:#2962FF,fill:#BBDEFB
    style H stroke:#AA00FF,fill:#E1BEE7
    style M stroke:#2962FF,fill:#BBDEFB
    click A "#evans"
    click nl "#das"
    click E "#torres"
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
#### Overview
```mermaid
---
config:
  layout: elk
---
flowchart TB
    A["<b>Leigh MacIntyre</b>, CEO<br>MCIN Assoc. Dir., PM"] --> B(["<b>Pre-Release Training<br>Scheduling<br></b>"])
    A --> n1(["<b>Ancillary<br>Studies</b>"]) & n2(["<b>WorkGroup<br>Data QC</b>"]) & n3(["<b>Technical</b>"]) & n4(["<b>Data<br>Loading</b>"])
    A --> n18(["<b><u>Internal</u><br></b>(<i>Click for Details</i>)"])
    B --> n5["<b>Ellise Elamparo</b><br>Exec Admin"]
    n1 --> n6["<b>Aarushi Chaudhry<br></b>Study Success<br>Manager"]
    n2 --> n7["<b>Jen Zink<br></b>Director,<br>Partnerships &amp; Grant<br>Funding<br><br><b>Marion Fechino</b><br>Data Analyst"]
    n3 --> n8["<b>Fraser Glen<br></b>CTO<br><br><b>Jordan<br>Sterling<br></b>Lead Dev"]
    n4 --> n9["<b>Laetitia Fesselier<br></b>Sr. Dev<br><b><br>Edson Silva</b><br><b>Mateus Andre<br></b>Dev"]
    style A fill:#BBDEFB,stroke:#2962FF
    style B fill:#E1BEE7,stroke:#AA00FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#E1BEE7,stroke:#AA00FF
    style n4 fill:#E1BEE7,stroke:#AA00FF
    style n18 fill:#E1BEE7,stroke:#AA00FF
    style n5 fill:#BBDEFB,stroke:#2962FF
    style n6 fill:#BBDEFB,stroke:#2962FF
    style n7 fill:#BBDEFB,stroke:#2962FF
    style n8 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    click n18 "#internal-non-consortium-facing"
```
<br>

#### Internal / Non-Consortium-Facing

<div style="width: 80%; margin: 0 auto;">
```mermaid
---
config:
  layout: elk
---
flowchart TB
    B(["<b>Development</b>"]) --> n5["<b>Mark Walker<br></b>Software Architect<br><br><b>Daniel Patularu</b><br><b>Oksana Bodnariuk<br>Jonas Vinson<br></b>Developers"]
    n1(["<b>QA</b>"]) --> n6["<b>Vandana Sriram</b><br><b>Anjali Raj Katuri<br></b>QA Engineers"]
    n3(["<b>Dev Ops/Sys Ops</b>"]) --> n8["<b>Francisco Soto</b><br>Manager<br><br><b>Alexandre Meyer</b><br>DevOps Engineer<br><br><b>Nataliya Korniyenko<br></b>Sys Admin"]
    n4(["<b>UI/UX</b>"]) --> n9["<b>Andrew Sawaya</b><br>Lead Designer<br><br><b>Mehrafarin Ekhlaspour</b><br>Visual Design"]
    n10["<b>Leigh MacIntyre</b>, CEO<br>MCIN Assoc. Dir., PM"] --> B & n1 & n3 & n4
    style B fill:#E1BEE7,stroke:#AA00FF
    style n5 fill:#BBDEFB,stroke:#2962FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n6 fill:#BBDEFB,stroke:#2962FF
    style n3 fill:#E1BEE7,stroke:#AA00FF
    style n8 fill:#BBDEFB,stroke:#2962FF
    style n4 fill:#E1BEE7,stroke:#AA00FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n10 fill:#BBDEFB,stroke:#2962FF
```
</div>

## University of Minnesota
There are several groups that fall under the oversight of UMN. The US Drug Testing Laboratories ([USDTL](https://www.usdtl.com/)) handles toxicology. The Developmental Cognition and Neuroimaging Lab ([DCAN](https://innovation.umn.edu/developmental-cognition-and-neuroimaging-lab)) led by Damien Fair at UMN is responsible for: *Processing*, *Software Development*, and *Deployment* of imaging data. The remaining groups are described in greater detail below.  

<div style="width: 90%; margin: 0 auto;">
```mermaid
---
config:
  layout: elk
---
flowchart TB
    A1["<b>Damien Fair</b><br>HDCC Co-Director<br>
    <b>Reed McEwan</b><br>HDCC Architect &amp; Data Manager"] --- HST(["<b>Health Sciences Technology (HST)</b><br>"]) & MIDB(["<b>MIDB Informatics Hub &amp; MSI</b><br>"]) & DCAN(["<b>DCAN Lab</b>"]) & USDTL(["<b>USDTL</b>"])
    DCAN --- n1(["<b>Neuroinformatics</b>"]) & n2(["<b>MRI Acquisition</b>"])
    n1 --- n3["<b>Eric Feczko, PhD</b><br><b>Lucille A. Moore, PhD</b>"]
    n2 --- n4["<b>Kimberly Weldon, PhD</b><br>Seimens Engineer"]
    style A1 fill:#BBDEFB,stroke:#2962FF
    style HST fill:#E1BEE7,stroke:#AA00FF
    style MIDB fill:#E1BEE7,stroke:#AA00FF
    style DCAN fill:#E1BEE7,stroke:#AA00FF
    style USDTL fill:#E1BEE7,stroke:#AA00FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#BBDEFB,stroke:#2962FF
    style n4 fill:#BBDEFB,stroke:#2962FF
    click HST "#health-sciences-technology-hst"
    click MIDB "#masonic-institute-for-the-developing-brain-midb-informatics-hub"
    click DCAN "https://innovation.umn.edu/developmental-cognition-and-neuroimaging-lab"
    click USDTL "https://www.usdtl.com/"
```
</div>

### Health Sciences Technology
[HST](https://hst.umn.edu/) at UMN is responsible for: *Data shelter*, *PHI*, *Ripple Interface*, *Overall Data Management*, *QC Dashboards*, *Ancillary Studies*, and *Third Party Integration*.

<div style="width: 80%; margin: 0 auto;">
```mermaid
---
config:
  layout: elk
---
flowchart TB
    B["<b>Reed McEwan</b><br>HDCC Architect &amp; Data Manager"]
    B --- n1(["<b>Project Management</b>"]) & n2(["<b>DevOps</b>"]) & n3(["<b>MRI Dashboard</b>"]) & n4(["<b>EHR</b>"])
    H["<b>Constantine Aliferis</b><br>Dir. Insitute Health Informatics"] 
    --- I["<b>Steve Johnson</b><br>Dir Informatics Innovation<br><b>Tim Meyer</b><br>EHR Informatics Engineer"]
    n1 --- E["<b>Karen Athy-Penrose</b><br>Data Shelter PM"]
    n2 --- F["<b>Dan Duhon</b><br>DevOps/ETL"]
    n3 --- G["<b>Haley Hutala</b><br>Tableau Engineer"]
    n4 --- H
    style B fill:#BBDEFB,stroke:#2962FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#E1BEE7,stroke:#AA00FF
    style n4 fill:#E1BEE7,stroke:#AA00FF
    style H fill:#BBDEFB,stroke:#2962FF
    style I fill:#BBDEFB,stroke:#2962FF
    style E fill:#BBDEFB,stroke:#2962FF
    style F fill:#BBDEFB,stroke:#2962FF
    style G fill:#BBDEFB,stroke:#2962FF
```
</div>

### MIDB Informatics Hub & MSI
The [Masonic Institute for the Developing Brain (MIDB) Informatics Hub](https://midb.umn.edu/research/informatics) and [Minnesota Supercomputing Institute (MSI)](https://msi.umn.edu/) at UMN provide the following services to the HBCD study: *System Administration*, *Loris Hosting*, *Computing*, *Processing*, and *Data Sharing*.

```mermaid
---
config:
  layout: elk
---
flowchart TB
    L["<b>Thomas Pengo</b><br>Co-Director, Informatics Group"] 
    --- M(["<b>Project<br>Management</b>"]) & N(["<b>Advanced<br>SysOps (ASO)</b>"])
    L --- O(["<b>Informatics<br>&amp; Processing</b>"]) & P(["<b>Data Steward</b>"]) & n8(["<b>Security &amp;<br>Compliance</b>"])
    N --- Q["<b>Jesse Erdman</b><br>Senior SysOps<br><br><b>Kimberleigh Breen</b><br>Data Manager<br><br><b>Sriharshitha Anuganti</b><br>DevOps"]
    O --- n4["<b>Timothy Hendrickson</b><br>Neuroimaging Lead<br><br><b>Erik Lee</b><br>Pipeline Lead<br><br><b>Monalisa Biles</b><br>Analyst"]
    M --- n6["<b>Maren Macgregor-Hannah</b><br>HDCC PM"]
    P --- n7["<b>Borgne Raasch</b>"]
    n8 --- n9["<b>Naomi<br>Hospodarsky-Sutherland</b>"]
    style L fill:#BBDEFB,stroke:#2962FF
    style M fill:#E1BEE7,stroke:#AA00FF
    style N fill:#E1BEE7,stroke:#AA00FF
    style O fill:#E1BEE7,stroke:#AA00FF
    style P fill:#E1BEE7,stroke:#AA00FF
    style n8 fill:#E1BEE7,stroke:#AA00FF
    style Q fill:#BBDEFB,stroke:#2962FF
    style n4 fill:#BBDEFB,stroke:#2962FF
    style n6 fill:#BBDEFB,stroke:#2962FF
    style n7 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
```
<br>

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
<div style="width: 80%; margin: 0 auto;">
```mermaid
---
config:
  layout: elk
---
flowchart TB
    A["<b>Anders Dale, PhD</b><br>PI/Director"] 
    --- n1(["<b>Fiona</b>"]) & n2(["<b>MRI QC</b>"]) & n3(["<b>MRI</b>"]) & n6(["<b>REDCap</b>"]) & n15(["<b>Dashboard</b>"])
    n1 --- n8["<b>Rongguang Yang, PhD</b><br>Fiona Lead<br>"]
    n2 --- n9["<b>Donald Hagler, PhD</b><br>QC Lead<br>"]
    n3 --- n10["<b>Josh Kuperman</b><br>MRI Lead"]
    n6 --- n4["<b>Janosch Linkersdörfer, PhD</b><br>Data Science Lead"]
    n9 --- n13["<b>Tyler Berkness</b><br>Protocol Violations<br><br><b>Sejal Shanbhag</b><br>Issue Handling"]
    n15 --- n4
    n4 --- n12["<b><b><u>RECap</u></b><br>Joseph Baligh</b><br>Server Admin<br><b>Erika Bolden</b> &amp; <b>Laura Ziemer</b><br>Dev/Admin"]
    n4 --- n18["<b>Amanda Li, MS</b><br>Biostats Support"] 
    n4 --- n17["<b><u>Dashboard</u></b><br><b>Biplabendu Das</b><br>Backend Dev<br><b>Olivier Celhay</b><br>Frontend Dev"]
    style A fill:#BBDEFB,stroke:#2962FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#E1BEE7,stroke:#AA00FF
    style n6 fill:#E1BEE7,stroke:#AA00FF
    style n15 fill:#E1BEE7,stroke:#AA00FF
    style n8 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n10 fill:#BBDEFB,stroke:#2962FF
    style n4 fill:#BBDEFB,stroke:#2962FF
    style n13 fill:#BBDEFB,stroke:#2962FF
    style n12 fill:#BBDEFB,stroke:#2962FF
    style n18 fill:#BBDEFB,stroke:#2962FF
    style n17 fill:#BBDEFB,stroke:#2962FF
```
</div>

## WashU
The Washington University in St. Louis (WashU) group has oversight of: *Neurology*, *Electronic Health Records (EHR)*, *Ripple*, *Ambra*, *AirTable*, and *HCAC coordination*.

```mermaid
---
config:
  layout: elk
---
flowchart TB
    A["<b>Chris Smyser</b><br>Principal Investigator<br>
    <b>Chad Sylvester</b><br>Co-Investigator"] --- neurology(["<b>Neurology</b>"]) & C(["<b>EHR</b><br>"]) & B["<b>Sauren Ravencroft</b><br>Project Manager"] & n11(["<b>OMOR</b>"])
    neurology --- n1["<b>Bob McKinstry</b><br><b>Josh Shimony</b><br>Co-Investigators &amp; Study Neuroradiologists"]
    n1 --- n2["<b>Dimitrios (Jim) Alexopoulos</b><br>Data Manager, Ambra"]
    C --- n3["<b>Philip Payne</b><br><b>Albert Lai</b><br>Co-Investigators"]
    n3 --- n4["<b>Nicole Venteris</b><br>Project Manager"]
    B --- n5(["<b>Ripple</b>"]) & n6(["<b>AirTable &amp; Ancillary Studies</b>"])
    n5 --- n8["<b>Liliana Mueller</b><br>Programming &amp; Management"]
    n6 --- n9["<b>Lynn Menchaca</b><br>AirTable Management<br>"] & n10["<b>Madison Gardner</b><br>U01 Site Piloting"]
    style A fill:#BBDEFB,stroke:#2962FF
    style neurology fill:#E1BEE7,stroke:#AA00FF
    style C fill:#E1BEE7,stroke:#AA00FF
    style B fill:#BBDEFB,stroke:#2962FF
    style n11 fill:#E1BEE7,stroke:#AA00FF
    style n1 fill:#BBDEFB,stroke:#2962FF
    style n2 fill:#BBDEFB,stroke:#2962FF
    style n3 fill:#BBDEFB,stroke:#2962FF
    style n4 fill:#BBDEFB,stroke:#2962FF
    style n5 fill:#E1BEE7,stroke:#AA00FF
    style n6 fill:#E1BEE7,stroke:#AA00FF
    style n8 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n10 fill:#BBDEFB,stroke:#2962FF
```

## University of Maryland EEG Core
<div style="width: 80%; margin: 0 auto;">
```mermaid
---
config:
  layout: elk
---
flowchart TB
    n16["<b>Nathan Fox</b><br>Associate Director, Data Core"]
    --- UMD2["<b>Santiago Morales</b>, Co-I<br><br><b>Jamie Listokin</b>, EEG Core Research Coordinator"]
    UMD2 --- n17(["<b>EEG Processing</b>"]) & n18(["<b>CBRAIN</b>"]) & n21(["<b>QC, Training, &amp; Troubleshooting</b>"])
    n17 --- n19["<b>Marco McSweeney</b><br>Pre-processing &amp; Derivatives"]
    n18 --- n20["<b>Whitney Kasenetz</b><br>EEG pre-processing in CBRAIN"]
    n21 --- n22["<b>Savannah McNair<br>Jessica Norris</b>"]
    style n16 fill:#BBDEFB,stroke:#2962FF
    style UMD2 fill:#BBDEFB,stroke:#2962FF
    style n17 fill:#E1BEE7,stroke:#AA00FF
    style n18 fill:#E1BEE7,stroke:#AA00FF
    style n21 fill:#E1BEE7,stroke:#AA00FF
    style n19 fill:#BBDEFB,stroke:#2962FF
    style n20 fill:#BBDEFB,stroke:#2962FF
    style n22 fill:#BBDEFB,stroke:#2962FF
```
</div>