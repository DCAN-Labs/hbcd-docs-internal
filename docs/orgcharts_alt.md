## Test1

---
config:
  layout: elk
---
flowchart TB
    lasso1(["<div class='tooltip'>MCIN Assoc Dir<span class='tooltiptext'>Montreal Consortium for Innovation in Neuroinformatics</span></div><br><b>Leigh MacIntyre</b><br>Lasso CEO"])


## Test3 - remove init

```mermaid
flowchart TB
    lasso1(["<div class='tooltip'>MCIN Assoc Dir<span class='tooltiptext'>Montreal Consortium for Innovation in Neuroinformatics</span></div><br><b>Leigh MacIntyre</b><br>Lasso CEO"])
```

## test6 - elk format

```mermaid
---
config:
  layout: elk
---
flowchart TB
    mc(["<div class='diagram-tooltip'>MCIN Assoc Dir<span class='diagram-tooltiptext'>Montreal Consortium for Innovation in Neuroinformatics</span></div><br><b>Leigh MacIntyre</b><br>Lasso CEO"])
```


## PMs

```mermaid
flowchart TB
    n6(["<b>MIDB &amp; MSI</b>"]) --> A1["<b>Maren Macgregor-Hannah</b>"]
    n9(["<b>WashU</b>"]) --> n8["<b>Sauren Ravencroft</b>"] & n12(["<b>EHR</b>"])
    n7(["<b>HST</b>"]) --> B["<b>Karen Athy-Penrose</b>"]
    n11(["<b>UMN</b>"]) --> n6 & n7 & n12
    n12 --> n13["<b>Nicole Venteris</b>"]
    style n6 fill:#E1BEE7,stroke:#AA00FF
    style A1 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#E1BEE7
    style n8 fill:#BBDEFB
    style n12 fill:#E1BEE7
    style n7 fill:#E1BEE7
    style B fill:#BBDEFB
    style n11 fill:#E1BEE7
    style n13 fill:#BBDEFB
```


## Orig Overview w/out BAH listed under UMN
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
    style n2 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style jvci fill:#E1BEE7,stroke:#AA00FF
    style E fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style lasso fill:#E1BEE7,stroke:#AA00FF
    style umn fill:#E1BEE7,stroke:#AA00FF
    style n7 fill:#E1BEE7,stroke:#AA00FF
    style n8 fill:#E1BEE7,stroke:#AA00FF
    style n11 fill:#E1BEE7,stroke:#AA00FF
    style lasso1 fill:#BBDEFB,stroke:#2962FF
    style n1 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style n10 fill:#E1BEE7,stroke:#AA00FF
    style ripple fill:#E1BEE7,stroke:#AA00FF
    style n12 fill:#E1BEE7,stroke:#AA00FF
    style n16 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style n17 fill:#BBDEFB,stroke:#2962FF
    style n19 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style n20 fill:#BBDEFB,stroke:#2962FF
    style reed fill:#BBDEFB,stroke:#2962FF
    style n22 fill:#BBDEFB,stroke:#2962FF
    style n23 fill:#E1BEE7,stroke:#AA00FF
    style n18 fill:#BBDEFB,stroke:#2962FF
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

## Overview alt

```mermaid
---
config:
  layout: elk
---
flowchart TB
    n2["<b>Anders Dale, PhD<br></b>HDCC Co-Director<br>JCVI"] --> jvci["<b>JVCI</b>"]
    E["<b>Damien Fair, PA-C, PhD</b><br>HDCC Co-Director<br>University of Minnesota"] --> lasso["<b>Lasso</b>"] & umn["<b>UMN</b>"] & n7["<b>LORIS</b>"] & n8["<b>UMD EEG Core</b>"] & n11["<b>Columbia</b>"]
    lasso --> lasso1["<b>Leigh MacIntyre</b><br>MCIN Assoc Dir, PM"]
    n1["<b>Christopher Smyser, MD<br></b>HDCC Co-Director<br>WashU"] --> n10["<b>WashU</b><br>"] & ripple["<b>Ripple</b>"] & n12["<b>LIBR</b>"] & lasso
    n16["<b>Wesley K.<br>Thompson, PhD</b><br>HDCC Assoc Dir,<br>BioStatistics Chair"] --> n17["<b>Chun Fan, PhD</b><br>Geolocation Chair"]
    n12 --> n16
    n8 --> n19["<b>Nathan Fox, PhD<br></b>HDCC Assoc. Dir."]
    n7 --> n20["<b>Alan Evans</b><br>PI<br><b>Samir Das</b><br>AD Softw Dev"]
    umn --> reed["<b>Reed McEwan, MS</b><br>Sr Research Dev"]
    n10 --> n22["<b>Chad Sylvester, PhD</b><br>Co-Investigator"]
    n11 --> n23(["<b>Novel Tech<br>&amp; Wearables</b>"])
    n23 --> n18["<b>William P. Fifer, PhD<br></b>Chair<br><b>Nicolo Pini<br></b>Co-I &amp; Dev<br><b>Beth Smith</b>"]
    reed --> n25(["<b>USDTL</b>"]) & n26(["<b>MIDB/MSI</b>"]) & n27(["<b>DCAN Lab</b>"]) & bio(["<b>BAH</b>"]) & n30(["<b>HST</b>"])
    style n2 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style jvci fill:#E1BEE7,stroke:#AA00FF
    style E fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style lasso fill:#E1BEE7,stroke:#AA00FF
    style umn fill:#E1BEE7,stroke:#AA00FF
    style n7 fill:#E1BEE7,stroke:#AA00FF
    style n8 fill:#E1BEE7,stroke:#AA00FF
    style n11 fill:#E1BEE7,stroke:#AA00FF
    style lasso1 fill:#BBDEFB,stroke:#2962FF
    style n1 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style n10 fill:#E1BEE7,stroke:#AA00FF
    style ripple fill:#E1BEE7,stroke:#AA00FF
    style n12 fill:#E1BEE7,stroke:#AA00FF
    style n16 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style n17 fill:#BBDEFB,stroke:#2962FF
    style n19 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style n20 fill:#BBDEFB,stroke:#2962FF
    style reed fill:#BBDEFB,stroke:#2962FF
    style n22 fill:#BBDEFB,stroke:#2962FF
    style n23 fill:#E1BEE7,stroke:#AA00FF
    style n18 fill:#BBDEFB,stroke:#2962FF
    style n25 fill:#E1BEE7,stroke:#AA00FF
    style n26 fill:#E1BEE7,stroke:#AA00FF
    style n27 fill:#E1BEE7,stroke:#AA00FF
    style bio fill:#E1BEE7,stroke:#AA00FF
    style n30 fill:#E1BEE7,stroke:#AA00FF
    click jvci "#j-craig-venter-institute"
    click lasso "#lasso"
    click umn "#university-of-minnesota"
    click n7 "#loris"
    click n8 "#umd-eeg-core"
    click n10 "#washu"
```

## JCVI ALT

```mermaid
---
config:
  layout: elk
---
flowchart TB
    A["<b>Anders Dale, PhD</b><br>PI/Director"] --- n1(["<b>Fiona</b>"]) & n2(["<b>MRI QC</b>"]) & n3(["<b>MRI</b>"]) & n6(["<b>REDCap</b>"]) & n15(["<b>Dashboard</b>"])
    n1 --- n8["<b>Rongguang Yang, PhD</b><br>Fiona Lead<br>"]
    n2 --- n9["<b>Donald Hagler, PhD</b><br>QC Lead<br>"]
    n3 --- n10["<b>Josh Kuperman</b><br>MRI Lead"]
    n9 --- n13["<b>Tyler Berkness</b><br>Protocol Violations<br><br><b>Sejal Shanbhag</b><br>Issue Handling"]
    n4["<b>Janosch Linkersdörfer, PhD</b><br>Data Science Lead"] --- n12["<b>Joseph Baligh</b><br>Server Admin<br><b>Erika Bolden</b> &amp; <b>Laura Ziemer</b><br>Dev/Admin"] & n18["<b>Amanda Li, MS</b><br>Biostats Support"] & n17["<b>Biplabendu Das</b><br>Backend Dev<br><b>Olivier Celhay</b><br>Frontend Dev"]
    n6 --> n12
    n15 --> n17
    A --> n4
    style A fill:#BBDEFB,stroke:#2962FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#E1BEE7,stroke:#AA00FF
    style n6 fill:#E1BEE7,stroke:#AA00FF
    style n15 fill:#E1BEE7,stroke:#AA00FF
    style n8 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n10 fill:#BBDEFB,stroke:#2962FF
    style n13 fill:#BBDEFB,stroke:#2962FF
    style n4 fill:#BBDEFB,stroke:#2962FF
    style n12 fill:#BBDEFB,stroke:#2962FF
    style n18 fill:#BBDEFB,stroke:#2962FF
    style n17 fill:#BBDEFB,stroke:#2962FF
```

## JCVI ALT2

```mermaid
---
config:
  layout: elk
---
flowchart TB
    A["<b>Anders Dale, PhD</b><br>PI/Director"] --- n3(["<b>MRI</b>"])
    n3 --- n10["<b>Josh Kuperman</b><br>MRI Lead"]
    n6(["<b>REDCap</b>"]) --> n12["<b>Joseph Baligh</b><br>Server Admin<br><b>Erika Bolden</b> &amp; <b>Laura Ziemer</b><br>Dev/Admin"]
    n15(["<b>Dashboard</b>"]) --> n17["<b>Biplabendu Das</b><br>Backend Dev<br><b>Olivier Celhay</b><br>Frontend Dev"]
    A --> n4["<b>Janosch Linkersdörfer, PhD</b><br>Data Science Lead"] & n8["<b>Rongguang Yang, PhD</b><br>Supervisor (Informatics)<br>"] & n9["<b>Donald Hagler, PhD</b><br>QC Lead<br>"]
    n8 --> n1(["<b>Fiona</b>"])
    n9 --> n2(["<b>MRI QC</b>"])
    n2 --> n13["<b>Tyler Berkness</b><br>Protocol Violations<br><br><b>Sejal Shanbhag</b><br>Issue Handling"]
    n4 --> n15 & n6
    style A fill:#BBDEFB,stroke:#2962FF
    style n3 fill:#E1BEE7,stroke:#AA00FF
    style n10 fill:#BBDEFB,stroke:#2962FF
    style n4 fill:#BBDEFB,stroke:#2962FF
    style n6 fill:#E1BEE7,stroke:#AA00FF
    style n12 fill:#BBDEFB,stroke:#2962FF
    style n15 fill:#E1BEE7,stroke:#AA00FF
    style n17 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n13 fill:#BBDEFB,stroke:#2962FF
```

## LORIS OLD- Roles & Responsibilities
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


# Lasso Alt diagrams
## lasso alt

```mermaid
---
config:
  layout: elk
---
flowchart TB
    A["<b>Leigh MacIntyre</b>, CEO<br>MCIN Assoc. Dir., PM"] --> B(["<b>Pre-Release Training<br>Scheduling<br></b>"]) & n1(["<b>Ancillary<br>Studies</b>"]) & n2(["<b>WorkGroup<br>Data QC</b>"]) & n3(["<b>Technical</b>"]) & n4(["<b>Data<br>Loading</b>"]) & n19(["<b>Internal</b>"])
    B --> n5["<b>Ellise Elamparo</b><br>Exec Admin"]
    n1 --> n6["<b>Aarushi Chaudhry<br></b>Study Success<br>Manager"]
    n2 --> n7["<b>Jen Zink<br></b>Director,<br>Partnerships &amp; Grant<br>Funding<br><br><b>Marion Fechino</b><br>Data Analyst"]
    n3 --> n8["<b>Fraser Glen<br></b>CTO<br><br><b>Jordan<br>Sterling<br></b>Lead Dev"]
    n4 --> n9["<b>Laetitia Fesselier<br></b>Sr. Dev<br><b><br>Edson Silva</b><br><b>Mateus Andre<br></b>Dev"]
    n19 --> n21(["<b>QA</b>"]) & n22(["<b>UI/UX</b>"]) & n23(["Dev &amp; Operations"])
    n23 --> n24["<b>Francisco Soto</b><br>Dev/SysOps Manager<br><b>Alexandre Meyer</b><br>DevOps<br><b>Nataliya Korniyenko<br></b>Sys Admin"] & n25["<b>Mark Walker<br></b>Software Architect<br><b>Daniel Patularu</b><br><b>Oksana Bodnariuk<br>Jonas Vinson<br></b>Developers"]
    n22 --> n26["<b>Andrew Sawaya</b><br>Lead Designer<br><b>Mehrafarin Ekhlaspour</b><br>Visual Design"]
    n21 --> n27["<b>Vandana Sriram</b><br><b>Anjali Raj Katuri<br></b>QA Engineers"]
    style A fill:#BBDEFB,stroke:#2962FF
    style B fill:#E1BEE7,stroke:#AA00FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#E1BEE7,stroke:#AA00FF
    style n4 fill:#E1BEE7,stroke:#AA00FF
    style n19 fill:#E1BEE7,stroke:#AA00FF
    style n5 fill:#BBDEFB,stroke:#2962FF
    style n6 fill:#BBDEFB,stroke:#2962FF
    style n7 fill:#BBDEFB,stroke:#2962FF
    style n8 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n21 fill:#E1BEE7,stroke:#AA00FF
    style n22 fill:#E1BEE7,stroke:#AA00FF
    style n23 fill:#E1BEE7,stroke:#AA00FF
    style n24 fill:#BBDEFB,stroke:#2962FF
    style n25 fill:#BBDEFB,stroke:#2962FF
    style n26 fill:#BBDEFB,stroke:#2962FF
    style n27 fill:#BBDEFB,stroke:#2962FF
```

## lasso alt 2
```mermaid
---
config:
  layout: elk
---
flowchart TB
    A["<b>Leigh MacIntyre</b>, CEO<br>MCIN Assoc. Dir., PM"] --> B(["<b>Pre-Release Training<br>Scheduling<br></b>"]) & n1(["<b>Ancillary<br>Studies</b>"]) & n2(["<b>WorkGroup<br>Data QC</b>"]) & n3(["<b>Technical</b>"]) & n4(["<b>Data<br>Loading</b>"]) & n22(["<b>UI/UX</b>"]) & n21(["<b>QA</b>"]) & n23(["<b>Dev &amp; Operations</b>"])
    B --> n5["<b>Ellise Elamparo</b><br>Exec Admin"]
    n1 --> n6["<b>Aarushi Chaudhry<br></b>Study Success<br>Manager"]
    n2 --> n7["<b>Jen Zink<br></b>Director,<br>Partnerships &amp; Grant<br>Funding<br><br><b>Marion Fechino</b><br>Data Analyst"]
    n3 --> n8["<b>Fraser Glen<br></b>CTO<br><br><b>Jordan<br>Sterling<br></b>Lead Dev"]
    n4 --> n9["<b>Laetitia Fesselier<br></b>Sr. Dev<br><b><br>Edson Silva</b><br><b>Mateus Andre<br></b>Dev"]
    n23 --> n24["<b>Francisco Soto</b><br>Dev/SysOps Manager<br><b>Alexandre Meyer</b><br>DevOps<br><b>Nataliya Korniyenko<br></b>Sys Admin<br><br><b>Mark Walker<br></b>Software Architect<br><b>Daniel Patularu</b><br><b>Oksana Bodnariuk<br>Jonas Vinson<br></b>Developers"]
    n22 --> n26["<b>Andrew Sawaya</b><br>Lead Designer<br><b>Mehrafarin Ekhlaspour</b><br>Visual Design"]
    n21 --> n27["<b>Vandana Sriram</b><br><b>Anjali Raj Katuri<br></b>QA Engineers"]
    style A fill:#BBDEFB,stroke:#2962FF
    style B fill:#E1BEE7,stroke:#AA00FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#E1BEE7,stroke:#AA00FF
    style n4 fill:#E1BEE7,stroke:#AA00FF
    style n22 fill:#E1BEE7,stroke:#AA00FF
    style n21 fill:#E1BEE7,stroke:#AA00FF
    style n23 fill:#E1BEE7
    style n5 fill:#BBDEFB,stroke:#2962FF
    style n6 fill:#BBDEFB,stroke:#2962FF
    style n7 fill:#BBDEFB,stroke:#2962FF
    style n8 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n24 fill:#BBDEFB,stroke:#2962FF
    style n26 fill:#BBDEFB,stroke:#2962FF
    style n27 fill:#BBDEFB,stroke:#2962FF
```

## lasso with subgraph
```mermaid
---
config:
  layout: elk
---
flowchart TB
 subgraph s1["<b>INTERNAL</b>"]
        n21(["<b>QA</b>"])
        n22(["<b>UI/UX</b>"])
        n23(["<b>Dev &amp; Operations</b>"])
  end
    A["<b>Leigh MacIntyre</b>, CEO<br>MCIN Assoc. Dir., PM"] --> B(["<b>Pre-Release Training<br>Scheduling<br></b>"]) & n1(["<b>Ancillary<br>Studies</b>"]) & n2(["<b>WorkGroup<br>Data QC</b>"]) & n3(["<b>Technical</b>"]) & n4(["<b>Data<br>Loading</b>"]) & s1
    B --> n5["<b>Ellise Elamparo</b><br>Exec Admin"]
    n1 --> n6["<b>Aarushi Chaudhry<br></b>Study Success<br>Manager"]
    n2 --> n7["<b>Jen Zink<br></b>Director,<br>Partnerships &amp; Grant<br>Funding<br><br><b>Marion Fechino</b><br>Data Analyst"]
    n3 --> n8["<b>Fraser Glen<br></b>CTO<br><br><b>Jordan<br>Sterling<br></b>Lead Dev"]
    n4 --> n9["<b>Laetitia Fesselier<br></b>Sr. Dev<br><b><br>Edson Silva</b><br><b>Mateus Andre<br></b>Dev"]
    n23 --> n24["<b>Francisco Soto</b><br>Dev/SysOps Manager<br><b>Alexandre Meyer</b><br>DevOps<br><b>Nataliya Korniyenko<br></b>Sys Admin"] & n25["<b>Mark Walker<br></b>Software Architect<br><b>Daniel Patularu</b><br><b>Oksana Bodnariuk<br>Jonas Vinson<br></b>Developers"]
    n22 --> n26["<b>Andrew Sawaya</b><br>Lead Designer<br><b>Mehrafarin Ekhlaspour</b><br>Visual Design"]
    n21 --> n27["<b>Vandana Sriram</b><br><b>Anjali Raj Katuri<br></b>QA Engineers"]
    style n21 fill:#E1BEE7,stroke:#AA00FF
    style n22 fill:#E1BEE7,stroke:#AA00FF
    style n23 fill:#E1BEE7,stroke:#AA00FF
    style A fill:#BBDEFB,stroke:#2962FF
    style B fill:#E1BEE7,stroke:#AA00FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#E1BEE7,stroke:#AA00FF
    style n4 fill:#E1BEE7,stroke:#AA00FF
    style s1 stroke:#000000
    style n5 fill:#BBDEFB,stroke:#2962FF
    style n6 fill:#BBDEFB,stroke:#2962FF
    style n7 fill:#BBDEFB,stroke:#2962FF
    style n8 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n24 fill:#BBDEFB,stroke:#2962FF
    style n25 fill:#BBDEFB,stroke:#2962FF
    style n26 fill:#BBDEFB,stroke:#2962FF
    style n27 fill:#BBDEFB,stroke:#2962FF
```


## Columbia University

```mermaid
---
config:
  layout: elk
---
flowchart TD
    A["<b>William P. Fifer</b>
    Co-chair of Novel Technologies/Wearables Working Group (Subaward PI)"] --> n1["<b>Nicolo Pini</b><br>Co-Investigator"] & n2["<b>Liana Eisler</b>
    Technician Research Assistant"]
    C["<b>Dima Amso</b>
    Co-Investigator"]
```


## LIBR

<div id="table-banner" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Data Dictionary Column Definitions</span>
  <span class="arrow">▸</span>
</div>
<div class="table-open-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 13px;">
    <thead>
      <tr>
        <th style="width: 15%; border: 1px solid #ddd; padding: 5px; text-align: center;">Name</th>
        <th style="width: 5%; border: 1px solid #ddd; padding: 5px; text-align: center;">Title</th>
        <th style="width: 30%; border: 1px solid #ddd; padding: 5px; text-align: center;">Role on HDCC</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Jim Wilgenbusch</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Director of Research Computing in the Research & Innovation Office, UMN</td>
        <td style="border: 1px solid #ddd; padding: 4px; word-wrap: break-word; white-space: normal;">Administration</td>
    </tr>
</tbody>
</table>
</div>

