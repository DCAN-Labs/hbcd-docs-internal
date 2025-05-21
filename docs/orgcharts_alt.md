# Lasso alt

## Alt 1
### Code

```mermaid
---
config:
  layout: elk
---
flowchart TB
 subgraph s1["<b>INTERNAL TO LASSO</b>"]
        n23(["<b>Dev/SysOps</b>"])
        n24["<b>Francisco Soto</b><br>Manager<br>
    <b>Alexandre Meyer</b><br>DevOps Engineer<br><br><b>Nataliya Korniyenko<br></b>Systems Administrator"]
        n4(["<b>Data Loading</b>"])
        n9["<b>Laetitia Fesselier</b><br>Sr Developer<br>
    <b>Edson Silva</b><br><b>Mateus Andre</b><br>Developers"]
        n29(["<b>UI/UX</b>"])
        n30["<b>Andrew Sawaya</b><br>Lead Designer<br>
    <b>Mehrafarin Ekhlaspour</b><br>Visual Design"]
        n27(["<b>QA</b>"])
        n28["<b>Vandana Sriram</b><br><b>Anjali Raj Katuri<br></b>QA Engineers"]
  end
 subgraph s2["<b>CONSORTIUM-FACING<br>(<i>Unless Specified Otherwise</i>)</b>"]
        B(["<b>Admin</b>"])
        n5["<b>Ellise Elamparo</b><br>Training Scheduling<br>(pre-release)"]
        n1(["<b>Ancillary Studies</b>"])
        n6["<b>Aarushi Chaudhry<br></b>Study Success<br>Manager"]
        n2(["<b>Data QC</b>"])
        n7["<b>Jen Zink<br></b>Dir Partnerships<br>&amp; Grant Funding<br><br><b>Marion Fechino</b><br>Data Analyst"]
        n22(["<b>Development</b>"])
        n26["<b>Fraser Glen<br></b>CTO<br><b>Jordan Sterling<br></b>Lead Developer
    -------------------------------
    <b><i>INTERNAL TO LASSO:</i>
    Mark Walker</b><br>Software Architect<br>
    <b>Daniel Patularu</b><br><b>Oksana Bodnariuk<br>Jonas Vinson<br></b>Developers"]
  end
    B --- n5
    n1 --- n6
    n2 --- n7
    n4 --- n9
    n23 --- n24
    n22 --- n26
    n27 --- n28
    n29 --- n30
    A["<b>Leigh MacIntyre</b>, CEO"] --- s2 & s1
    style n23 fill:#E1BEE7,stroke:#AA00FF
    style n24 fill:#BBDEFB,stroke:#2962FF
    style n4 fill:#E1BEE7,stroke:#AA00FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n29 fill:#E1BEE7,stroke:#AA00FF
    style n30 fill:#BBDEFB,stroke:#2962FF
    style n27 fill:#E1BEE7,stroke:#AA00FF
    style n28 fill:#BBDEFB,stroke:#2962FF
    style B fill:#E1BEE7,stroke:#AA00FF
    style n5 fill:#BBDEFB,stroke:#2962FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n6 fill:#BBDEFB,stroke:#2962FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n7 fill:#BBDEFB,stroke:#2962FF
    style n22 fill:#E1BEE7,stroke:#AA00FF
    style n26 fill:#BBDEFB,stroke:#2962FF
    style A fill:#BBDEFB,stroke:#2962FF
    style s2 fill:#FFFFFF,stroke:#000000
    style s1 fill:#FFFFFF,stroke:#000000
```
### svg

![](lasso.svg)

## Alt 2
### Code
<div style="width: 80%; margin: 0 auto;">
```mermaid
---
config:
  layout: elk
---
flowchart TB
 subgraph s1["<b>INTERNAL TO LASSO</b>"]
        n23(["<b>Dev/SysOps</b>"])
        n24["<b>Francisco Soto</b><br>Manager<br>
    <b>Alexandre Meyer</b><br>DevOps Engineer<br><br><b>Nataliya Korniyenko<br></b>Systems Administrator"]
        n4(["<b>Data Loading</b>"])
        n9["<b>Laetitia Fesselier</b><br>Sr Developer<br>
    <b>Edson Silva</b><br><b>Mateus Andre</b><br>Developers"]
        n29(["<b>UI/UX</b>"])
        n30["<b>Andrew Sawaya</b><br>Lead Designer<br>
    <b>Mehrafarin Ekhlaspour</b><br>Visual Design"]
        n27(["<b>QA</b>"])
        n28["<b>Vandana Sriram</b><br><b>Anjali Raj Katuri<br></b>QA Engineers"]
        n31["<b>Mark Walker</b>
        Software Architect<br>
        <b>Daniel Patularu
        Oksana Bodnariuk
        Jonas Vinson</b>
        Developers"]
        n32(["<b>Development</b>"])
  end
 subgraph s2["<b>CONSORTIUM-FACING</b>"]
        B(["<b>Admin</b>"])
        n5["<b>Ellise Elamparo</b><br>Training Scheduling<br>(pre-release)"]
        n1(["<b>Ancillary Studies</b>"])
        n6["<b>Aarushi Chaudhry<br></b>Study Success<br>Manager"]
        n2(["<b>Data QC</b>"])
        n7["<b>Jen Zink<br></b>Dir Partnerships<br>&amp; Grant Funding<br><br><b>Marion Fechino</b><br>Data Analyst"]
        n22(["<b>Development</b>"])
        n26["<b>Fraser Glen<br></b>CTO<br><b>Jordan Sterling<br></b>Lead Develope"]
  end
    B --- n5
    n1 --- n6
    n2 --- n7
    n4 --- n9
    n23 --- n24
    n22 --- n26
    n27 --- n28
    n29 --- n30
    A["<b>Leigh MacIntyre</b>, CEO"] --- s2 & s1
    n32 --- n31
    n26 --- n32
    style n23 fill:#E1BEE7,stroke:#AA00FF
    style n24 fill:#BBDEFB,stroke:#2962FF
    style n4 fill:#E1BEE7,stroke:#AA00FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n29 fill:#E1BEE7,stroke:#AA00FF
    style n30 fill:#BBDEFB,stroke:#2962FF
    style n27 fill:#E1BEE7,stroke:#AA00FF
    style n28 fill:#BBDEFB,stroke:#2962FF
    style n31 fill:#BBDEFB,stroke:#2962FF
    style n32 fill:#E1BEE7,stroke:#AA00FF
    style B fill:#E1BEE7,stroke:#AA00FF
    style n5 fill:#BBDEFB,stroke:#2962FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n6 fill:#BBDEFB,stroke:#2962FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n7 fill:#BBDEFB,stroke:#2962FF
    style n22 fill:#E1BEE7,stroke:#AA00FF
    style n26 fill:#BBDEFB,stroke:#2962FF
    style A fill:#BBDEFB,stroke:#2962FF
    style s2 fill:#FFFFFF,stroke:#000000
    style s1 fill:#FFFFFF,stroke:#000000
```
</div>


### svg

<div style="text-align: center;">
  <img src="../lasso2.svg" alt="Lasso" width="80%" />
</div>



# Tests for hover boxes

## Test1

%%{ init: {
  "flowchart": {
    "htmlLabels": true
  }
} }%%
flowchart TB
    lasso1(["<div title='Montreal Consortium for Innovation in Neuroinformatics'>MCIN Assoc Dir</div><br><b>Leigh MacIntyre</b><br>Lasso CEO"])



## test2

```mermaid
%%{ init: {
  "flowchart": {
    "htmlLabels": true
  }
} }%%
flowchart TB
    lasso1(["<div title='Montreal Consortium for Innovation in Neuroinformatics'>MCIN Assoc Dir</div><br><b>Leigh MacIntyre</b><br>Lasso CEO"])
```

## test3

```mermaid
flowchart TB
    lasso1(["<div class='tooltip'>MCIN Assoc Dir<span class='tooltiptext'>Montreal Consortium for Innovation in Neuroinformatics</span></div><br><b>Leigh MacIntyre</b><br>Lasso CEO"])
```


## test with mermaid tool tip

```mermaid
flowchart TB
    lasso1["Leigh MacIntyre<br>Lasso CEO<br>MCIN Assoc Dir"]
    click lasso1 "https://mcin.ca/about-mcin/" "Montreal Consortium for Innovation in Neuroinformatics"
```

## vesion fix

```mermaid
%%{ init: { "flowchart": { "htmlLabels": true } } }%%
flowchart TB
    lasso1(["<div title='Montreal Consortium for Innovation in Neuroinformatics'>Leigh MacIntyre<br>Lasso CEO<br>MCIN Assoc Dir</div>"])
```

```mermaid
flowchart TB
    lasso1(["<div title='Montreal Consortium for Innovation in Neuroinformatics'>Leigh MacIntyre<br>Lasso CEO<br>MCIN Assoc Dir</div>"])
```


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

