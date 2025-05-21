#  🚧 HDCC Organizational Charts 🚧

## Overview
The larger organizational structure of the HBCD Data Coordinating Center (HDCC) is as follows, with the HDCC Co-Directors listed at the top and the institutions/organizations listed below- ***click on individual teams to be directed to their organizational charts***. Please visit the [HDCC page](https://hbcdstudy.org/hbcd-data-coordinating-center/) of the HBCD Study website for a full list of all HDCC members. 

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
    n2["<b>Anders Dale, PhD<br></b>HDCC Co-Director<br>JCVI"] --- jcvi["<b>JCVI</b> <i class="fa-solid fa-link" style="color: blue;"></i>"]
    E["<b>Damien Fair, PA-C, PhD</b><br>HDCC Co-Director<br>University of Minnesota"] --- lasso["<b>Lasso</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & umn["<b>UMN</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & n7["<b>LORIS</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & n8["<b>UMD EEG Core</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & n11["<b>Columbia</b>"]
    lasso --- lasso1["<b>Leigh MacIntyre</b><br>Lasso CEO"]
    n1["<b>Christopher Smyser, MD<br></b>HDCC Co-Director<br>WashU"] --- n10["<b>WashU</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & n12["<b>LIBR</b>"] & lasso
    n16["<b>Wesley K.<br>Thompson, PhD</b><br>HDCC Assoc Dir,<br>BioStatistics Chair"] --- n17["<b>Chun Fan, PhD</b><br>Geolocation Chair"]
    n12 --- n16
    n8 --- n19["<b>Nathan Fox, PhD<br></b>HDCC Assoc Dir"]
    n7 --- n20["<b>Alan Evans</b>, PI<br><b>Samir Das</b><br><a href="https://mcin.ca/about-mcin/" target="_blank">MCIN</a> Assoc Dir"]
    umn --- reed["<b>Reed McEwan, MS</b><br>Sr Research Dev"]
    n10 --- n22["<b>Chad Sylvester, PhD</b><br>Co-Investigator"]
    n11 --- n18["<b>William P. Fifer, PhD</b><br>Novel Tech &<br>Wearables Co-Chair"]
    reed --- n25["<b>MIDB &amp; MSI</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & n27["<b>HST</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & n28["<b>CDNI</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & n29["<b>USDTL<br>Biospecimens<br>Genomics</b>"]
    n25 --- n30["<b>Maren Macgregor-Hannah</b><br>Program Manager"]
    n27 --- n31["<b>Karen Athy-Penrose</b><br>Project Manager"]
    n22 --- n32["<b>Sauren Ravencroft<br>Nicole Venteris</b><br>Project Managers"]
    n20 --- n33["<b>Santiago Torres</b><br>Study Officer"]
    style n2 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style jcvi fill:#E1BEE7,stroke:#AA00FF
    style E fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style lasso fill:#E1BEE7,stroke:#AA00FF
    style umn fill:#E1BEE7,stroke:#AA00FF
    style n7 fill:#E1BEE7,stroke:#AA00FF
    style n8 fill:#E1BEE7,stroke:#AA00FF
    style n11 fill:#E1BEE7,stroke:#AA00FF
    style lasso1 fill:#BBDEFB,stroke:#2962FF
    style n1 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style n10 fill:#E1BEE7,stroke:#AA00FF
    style n12 fill:#E1BEE7,stroke:#AA00FF
    style n16 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style n17 fill:#BBDEFB,stroke:#2962FF
    style n19 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style n20 fill:#BBDEFB,stroke:#2962FF
    style reed fill:#BBDEFB,stroke:#2962FF
    style n22 fill:#BBDEFB,stroke:#2962FF
    style n18 fill:#BBDEFB,stroke:#2962FF
    style n25 fill:#E1BEE7,stroke:#AA00FF
    style n27 fill:#E1BEE7,stroke:#AA00FF
    style n28 fill:#E1BEE7,stroke:#AA00FF
    style n29 fill:#E1BEE7,stroke:#AA00FF
    style n30 fill:#C8E6C9,stroke:#00C853
    style n31 fill:#C8E6C9,stroke:#00C853
    style n32 fill:#C8E6C9,stroke:#00C853
    style n33 fill:#C8E6C9,stroke:#00C853
    click jcvi "#j-craig-venter-institute"
    click lasso "#lasso"
    click umn "#university-of-minnesota"
    click n7 "#loris"
    click n8 "#university-of-maryland-eeg-core"
    click n10 "#washu"
    click n25 "#midb-informatics-hub-msi"
    click n27 "#health-sciences-technology"
    click n28 "#center-for-developmental-neuroimaging"
```

## Overview - Alternate 

```mermaid
---
config:
  layout: elk
---
flowchart TB
    n2["<b>Anders Dale, PhD<br></b>HDCC Co-Director<br>JCVI"] --- jcvi["<b>JCVI</b> <i class="fa-solid fa-link" style="color: blue;"></i>"]
    E["<b>Damien Fair, PA-C, PhD</b><br>HDCC Co-Director<br>University of Minnesota"] --- lasso["<b>Lasso</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & umn["<b>UMN</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & n7["<b>LORIS</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & n8["<b>UMD EEG Core</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & n11["<b>Columbia</b>"]
    lasso --- lasso1["<b>Leigh MacIntyre</b><br>Lasso CEO"]
    n1["<b>Christopher Smyser, MD<br></b>HDCC Co-Director<br>WashU"] --- n10["<b>WashU</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & n12["<b>LIBR</b>"] & lasso
    n16["<b>Wesley K.<br>Thompson, PhD</b><br>HDCC Assoc Dir,<br>BioStatistics Chair"] --- n17["<b>Chun Fan, PhD</b><br>Geolocation Chair"]
    n12 --- n16
    n8 --- n19["<b>Nathan Fox, PhD<br></b>HDCC Assoc Dir"]
    n7 --- n20["<b>Alan Evans</b>, PI<br><b>Samir Das</b><br><a href="https://mcin.ca/about-mcin/" target="_blank">MCIN</a> Assoc Dir"]
    umn --- reed["<b>Reed McEwan, MS</b><br>Sr Research Dev"]
    n10 --- n22["<b>Chad Sylvester, PhD</b><br>Co-Investigator"]
    n11 --- n18["<b>William P. Fifer, PhD</b><br>Novel Tech &<br>Wearables Co-Chair"]
    reed --- n30["<b>Maren Macgregor-Hannah</b><br>Program Manager"]
    n30 --- n25["<b>MIDB &amp; MSI</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & n27["<b>HST</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & n28["<b>CDNI</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & n29["<b>USDTL<br>Biospecimens<br>Genomics</b>"]
    n27 --- n31["<b>Karen Athy-Penrose</b><br>Project Manager"]
    n22 --- n32["<b>Sauren Ravencroft<br>Nicole Venteris</b><br>Project Managers"]
    n20 --- n33["<b>Santiago Torres</b><br>Study Officer"]
    style n2 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style jcvi fill:#E1BEE7,stroke:#AA00FF
    style E fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style lasso fill:#E1BEE7,stroke:#AA00FF
    style umn fill:#E1BEE7,stroke:#AA00FF
    style n7 fill:#E1BEE7,stroke:#AA00FF
    style n8 fill:#E1BEE7,stroke:#AA00FF
    style n11 fill:#E1BEE7,stroke:#AA00FF
    style lasso1 fill:#BBDEFB,stroke:#2962FF
    style n1 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style n10 fill:#E1BEE7,stroke:#AA00FF
    style n12 fill:#E1BEE7,stroke:#AA00FF
    style n16 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style n17 fill:#BBDEFB,stroke:#2962FF
    style n19 fill:#BBDEFB,stroke:#2962FF,stroke-width:4px
    style n20 fill:#BBDEFB,stroke:#2962FF
    style reed fill:#BBDEFB,stroke:#2962FF
    style n22 fill:#BBDEFB,stroke:#2962FF
    style n18 fill:#BBDEFB,stroke:#2962FF
    style n25 fill:#E1BEE7,stroke:#AA00FF
    style n27 fill:#E1BEE7,stroke:#AA00FF
    style n28 fill:#E1BEE7,stroke:#AA00FF
    style n29 fill:#E1BEE7,stroke:#AA00FF
    style n30 fill:#C8E6C9,stroke:#00C853
    style n31 fill:#C8E6C9,stroke:#00C853
    style n32 fill:#C8E6C9,stroke:#00C853
    style n33 fill:#C8E6C9,stroke:#00C853
    click jcvi "#j-craig-venter-institute"
    click lasso "#lasso"
    click umn "#university-of-minnesota"
    click n7 "#loris"
    click n8 "#university-of-maryland-eeg-core"
    click n10 "#washu"
    click n25 "#midb-informatics-hub-msi"
    click n27 "#health-sciences-technology"
    click n28 "#center-for-developmental-neuroimaging"
```

## J. Craig Venter Institute 
The [J. Craig Venter Institute](https://www.jcvi.org/) (JCVI) is responsible for MRI quality control, REDCap, FIONA, and the QC Dashboard.

<div style="width: 90%; margin: 0 auto;">
```mermaid
---
config:
  layout: elk
---
flowchart TB
    A["<b>Anders Dale, PhD</b>, PI/Director"] --- z(["<a href="#fiona"><b>FIONA</b></a>"])
    A --- n2(["<b>Raw MRI Quality Control</b>"])
    A --- n3(["<b>MRI Phantom Quality Control</b>"])
    A --- n6(["<a href="#redcap"><b>REDCap</b></a><br><b>Data Science</b><br><a href="#deap"><b>DEAP</b></a>"])
    n2 --- n9["<b>Donald Hagler, PhD</b><br>Raw MRI QC Lead<br><br><b>Tyler Berkness</b><br>Protocol Violations<br><br><b>Sejal Shanbhag</b><br>Issue Handling"]
    n3 --- n10["<b>Josh Kuperman</b><br>MRI Phantom QC Lead"]
    n6 --- n4["<b>Janosch Linkersdörfer, PhD</b><br>Team Lead<br>
    <b>Asef-Joseph Baligh</b><br>REDCap Server Admin<br>
    <b>Erika Bolden<br>Laura Ziemer</b><br>REDCap Dev/Admin<b><br>
    Biplabendu Das</b><br>Dashboard Backend<br><br><b>Olivier Celhay</b><br>Dashboard Frontend"]
    z --- n8["<b>Rongguang Yang, PhD</b><br>FIONA Lead"]
    style A fill:#BBDEFB,stroke:#2962FF
    style z fill:#E1BEE7,stroke:#AA00FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#E1BEE7,stroke:#AA00FF
    style n6 fill:#E1BEE7,stroke:#AA00FF
    style n8 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n10 fill:#BBDEFB,stroke:#2962FF
    style n4 fill:#BBDEFB,stroke:#2962FF
```
</div>

### Subcontractor Details

#### DEAP 🚧 **UPDATE FOLLOWING DESCRIPTION** 🚧
The Data Exploration and Analysis Portal (DEAP) is a cloud-based platform developed to facilitate secure, efficient, and user-friendly access to large-scale, multimodal research datasets. Originally designed for the Adolescent Brain Cognitive Development (ABCD) Study, DEAP supports visual exploration of NBDC data dictionaries as well as data download.

#### FIONA 🚧 **UPDATE FOLLOWING DESCRIPTION** 🚧
FIONA (Flexible Image Open Network Appliance) is a high-performance data transfer node (DTN) developed by the Energy Sciences Network (ESnet), designed to move large scientific datasets quickly and securely across research networks. It's typically used in research settings to support efficient, reliable, and high-throughput data transfers between institutions, especially for projects that generate or share large volumes of data. For the HBCD Study, FIONA plays a critical role in the infrastructure that supports data management and secure sharing, specifically for neuroimaging and other high-throughput data types collected across the many study sites.

#### REDCap 🚧 **UPDATE FOLLOWING DESCRIPTION** 🚧
[REDCap](https://projectredcap.org/) (Research Electronic Data Capture) is a secure, widely used web-based application designed to support data capture for research studies, particularly in academic and clinical environments. In the HBCD Study, REDCap serves as a central tool for managing behavioral, clinical, and demographic data across the multiple participating sites. While neuroimaging and biosensor data flow through pipelines involving systems like FIONA, REDCap is used for more structured, form-based data collected during assessments and visits.

## Lasso
[Lasso](https://www.lassoinformatics.com/) is a lightweight RESTful API framework developed to integrate external tools and pipelines with LORIS. Lasso offers a user-friendly, (NIST) 800-171-compliant data management platform particularly suited for large-scale multi-modal data. Lasso serves several core functions in HDCC, including developing dashboards for ongoing workgroup data QC and being the official public data release platform for the HBCD Study.

```mermaid
---
config:
  layout: elk
---
flowchart TB
    B(["<b>Admin</b>"]) --- n5["<b>Ellise Elamparo</b><br>Training Scheduling<br>(pre-release)"]
    n1(["<b>Ancillary Studies</b>"]) --- n6["<b>Aarushi Chaudhry<br></b>Study Success<br>Manager"]
    n2(["<b>Data QC</b>"]) --- n7["<b>Jen Zink<br></b>Dir Partnerships<br>&amp; Grant Funding<br><br><b>Marion Fechino</b><br>Data Analyst"]
    n4(["<b>Data Loading</b>"]) --- n9["<b><i>INTERNAL TO LASSO:</i></b><br><b>Laetitia Fesselier</b><br>Sr Developer<br>
    <b>Edson Silva</b><br><b>Mateus Andre</b><br>Developers"]
    n23(["<b>Dev/SysOps</b>"]) --- n24["<b><i>INTERNAL TO LASSO:</i><br>Francisco Soto</b><br>Manager<br>
    <b>Alexandre Meyer</b><br>DevOps Engineer<br><br><b>Nataliya Korniyenko<br></b>Systems Administrator"]
    n22(["<b>Development</b>"]) --- n26["<b>Fraser Glen<br></b>CTO<br><b>Jordan Sterling<br></b>Lead Developer
    -------------------------------
    <b><i>INTERNAL TO LASSO:</i>
    Mark Walker</b><br>Software Architect<br>
    <b>Daniel Patularu</b><br><b>Oksana Bodnariuk<br>Jonas Vinson<br></b>Developers"]
    A["<b>Leigh MacIntyre</b>, CEO"] --- n22 & n23 & n2 & B & n4 & n1
    A --- n27(["<b>QA</b>"]) & n29(["<b>UI/UX</b>"])
    n27 --- n28["<b><i>INTERNAL TO LASSO:</i></b>
    <b>Vandana Sriram</b><br><b>Anjali Raj Katuri<br></b>QA Engineers"]
    n29 --- n30["<b><i>INTERNAL TO LASSO:</i></b>
    <b>Andrew Sawaya</b><br>Lead Designer<br>
    <b>Mehrafarin Ekhlaspour</b><br>Visual Design"]
    style B fill:#E1BEE7,stroke:#AA00FF
    style n5 fill:#BBDEFB,stroke:#2962FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n6 fill:#BBDEFB,stroke:#2962FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n7 fill:#BBDEFB,stroke:#2962FF
    style n4 fill:#E1BEE7,stroke:#AA00FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n23 fill:#E1BEE7,stroke:#AA00FF
    style n24 fill:#BBDEFB,stroke:#2962FF
    style n22 fill:#E1BEE7,stroke:#AA00FF
    style n26 fill:#BBDEFB,stroke:#2962FF
    style A fill:#BBDEFB,stroke:#2962FF
    style n27 fill:#E1BEE7,stroke:#AA00FF
    style n29 fill:#E1BEE7,stroke:#AA00FF
    style n28 fill:#BBDEFB,stroke:#2962FF
    style n30 fill:#BBDEFB,stroke:#2962FF
```

## LORIS
🚧 **UPDATE FOLLOWING DESCRIPTION** 🚧      
[LORIS](https://mcin.ca/technology/loris/) (Longitudinal Online Research and Imaging System), developed and maintained by research teams within the McGill Centre for Integrative Neuroscience ([MCIN](https://mcin.ca/)), is the core data management system for the HBCD Study. It is a web-based data management system designed for large-scale, multi-site neuroscience research. It supports the collection, curation, and sharing of diverse data types, including neuroimaging, behavioral, and clinical data. LORIS emphasizes data standardization, quality control, and longitudinal tracking across participants and timepoints.

```mermaid
---
config:
  layout: elk
---
flowchart TB
    nl["<b>Santiago Torres</b><br>Study Officer"] --- C(["<b>CBRAIN</b>"]) & G(["<b>MRI BIDS Conversion &amp; Database Management</b>"]) & H(["<b>EEG &amp; Biospecimens</b>"]) & F(["<b>Systems Operations</b>"])
    C --- n12["<b>Bryan Caron</b><br>Director, CBRAIN<br>&amp; MCIN NeuroHub<br><br><b>Pierre Rioux</b><br>Lead Developer"]
    F --- I["<b>Dave McFarlane</b><br>Lead Developer<br><br><b>Sruthy Matthew</b><br>Sr Backend Developer<br><br><b>Regis Ongaro-Carcy<br>George Murad<br>Moshood Abiola</b><br>Developers"]
    G --- L["<b>Cecile Madjar</b><br>Lead Developer"]
    H --- M["<b>Laetitia Faeselier</b><br>Lead Developer"]
    n13["<b>Alan Evans</b>, PI<br><b>Samir Das</b>, MCIN Assoc Dir"] --- nl
    style nl stroke:#00C853,fill:#C8E6C9
    style C stroke:#AA00FF,fill:#E1BEE7
    style G stroke:#AA00FF,fill:#E1BEE7
    style H stroke:#AA00FF,fill:#E1BEE7
    style F stroke:#AA00FF,fill:#E1BEE7
    style n12 stroke:#2962FF,fill:#BBDEFB
    style I stroke:#2962FF,fill:#BBDEFB
    style L stroke:#2962FF,fill:#BBDEFB
    style M stroke:#2962FF,fill:#BBDEFB
    style n13 stroke:#2962FF,fill:#BBDEFB
```
<p>
<div id="loris-rr" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Roles & Responsibilities</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
    <thead>
      <tr>
        <th style="width: 25%;">Name</th>
        <th style="width: 30%;">Title</th>
        <th style="width: 50%;">Role on HDCC</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Alan Evans</td>
        <td style="word-wrap: break-word; white-space: normal;">Principal Investigator</td>
        <td style="word-wrap: break-word; white-space: normal;">Oversight and management of <a href="https://mcin.ca/about-mcin/" target="_blank">MCIN</a> and LORIS operations</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Samir Das</td>
        <td style="word-wrap: break-word; white-space: normal;">Associate Director of Software Development</td>
        <td style="word-wrap: break-word; white-space: normal;">Administration and oversight of LORIS operations for the HBCD Study</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Pierre Rioux</td>
        <td style="word-wrap: break-word; white-space: normal;">Senior CBRAIN Developer</td>
        <td style="word-wrap: break-word; white-space: normal;">CBRAIN configuration, tool containerization, design computing and analysis workflows, system interoperability</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Santiago Torres</td>
        <td style="word-wrap: break-word; white-space: normal;">Study Officer (Research Admin)</td>
        <td style="word-wrap: break-word; white-space: normal;">Project coordinator and liaison, ensuring timely implementation of study tasks and alignment with Workgroup requirements through oversight, testing, and data validation activities</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Cecile Madjar</td>
        <td style="word-wrap: break-word; white-space: normal;">Lead MRI developer</td>
        <td style="word-wrap: break-word; white-space: normal;">Development and deployment of LORIS MRI features, including ingestion and error handling</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Laetitia Faeselier</td>
        <td style="word-wrap: break-word; white-space: normal;">Lead Biospecimens & EEG Developer</td>
        <td style="word-wrap: break-word; white-space: normal;">Development and implementation of LORIS Biospecimens & EEG features, including data ingestion, quality control, tracking systems, and Dashboard innovations</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Regis Ongaro-Carcy</td>
        <td style="word-wrap: break-word; white-space: normal;">Lead Developer</td>
        <td style="word-wrap: break-word; white-space: normal;">Development of LORIS features for behavior (questionnaire/survey responses), including integration with external platforms (e.g. REDCap, Ripple, MSI), streamlining data collection, and enhancing system interoperability and workflows</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Sruthy Matthew</td>
        <td style="word-wrap: break-word; white-space: normal;">Senior Backend Developer</td>
        <td style="word-wrap: break-word; white-space: normal;">Development of LORIS LaunchPad and Backend features</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">George Murad</td>
        <td style="word-wrap: break-word; white-space: normal;">Junior Developer</td>
        <td style="word-wrap: break-word; white-space: normal;">Development of LORIS features for behavior (questionnaire/survey responses), including instrument coding, automated QC queries, and API/Endpoint implementation</td>
    </tr>
</tbody>
</table>
</div>
</p>

## University of Maryland EEG Core
<div style="width: 80%; margin: 0 auto;">
```mermaid
---
config:
  layout: elk
---
flowchart TB
    n17(["<b>EEG Pre-processing &amp; Derivatives</b>"]) --- n19["<b>Marco McSweeney, PhD</b>
    <b>Dylan Gilbreath</b>
    <b>Trisha Maheshwari</b>
    <b>Kira Ashton</b>"]
    n18(["<b>CBRAIN Processing</b>"]) --- n20["<b>Whitney Kasenetz</b>"]
    n21(["<b>QC, Training, &amp; Troubleshooting</b>"]) --- n22["<b>Savannah McNair<br>Jessica Norris</b>"]
    n16["<b>Nathan Fox</b>, Assoc Dir<br><b>Santiago Morales</b>, Co-I"] --- n21 & n17 & n18
    style n17 fill:#E1BEE7,stroke:#AA00FF
    style n19 fill:#BBDEFB,stroke:#2962FF
    style n18 fill:#E1BEE7,stroke:#AA00FF
    style n20 fill:#BBDEFB,stroke:#2962FF
    style n21 fill:#E1BEE7,stroke:#AA00FF
    style n22 fill:#BBDEFB,stroke:#2962FF
    style n16 fill:#BBDEFB,stroke:#2962FF
```
</div>

## University of Minnesota
🚧 **UPDATE FOLLOWING DESCRIPTION** 🚧      
There are several groups that fall under the oversight of UMN. The US Drug Testing Laboratories ([USDTL](https://www.usdtl.com/)) handles toxicology. The remaining groups are described in greater detail below.  

<div style="width: 80%; margin: 0 auto;">
```mermaid
---
config:
  layout: elk
---
flowchart LR
    A1["<b>Damien Fair</b><br>HDCC Co-Director<br><br><b>Reed McEwan</b><br>HDCC Architect &amp; Data Manager"] 
    A1 --- HST["<b>Health Sciences Technology (HST)</b> <i class="fa-solid fa-link" style="color: blue;"></i>"]
    A1 --- MIDB["<b>MIDB Informatics Hub &amp; MSI</b> <i class="fa-solid fa-link" style="color: blue;"></i>"]
    A1 --- CDNI["<b>Center for Developmental NeuroImaging (CDNI)</b> <i class="fa-solid fa-link" style="color: blue;"></i>"] & n6["<b>USDTL<br>Biospecimens<br>Genomics</b>"]
    style A1 fill:#BBDEFB,stroke:#2962FF
    style HST fill:#E1BEE7,stroke:#AA00FF
    style MIDB fill:#E1BEE7,stroke:#AA00FF
    style CDNI fill:#E1BEE7,stroke:#AA00FF
    style n6 fill:#E1BEE7,stroke:#AA00FF
    click HST "#health-sciences-technology-hst"
    click MIDB "#midb-informatics-hub-msi"
    click CDNI "#center-for-developmental-neuroimaging"
```
</div>

### Center for Developmental NeuroImaging
🚧 **UPDATE FOLLOWING DESCRIPTION** 🚧      
The Center for Developmental NeuroImaging ([CDNI](https://cdni.umn.edu/)) at UMN is responsible for: *Processing*, *Software Development*, and *Deployment* of imaging data. 

<div style="width: 80%; margin: 0 auto;">
```mermaid
---
config:
  layout: elk
---
flowchart LR
    CDNI["<b>Damien Fair</b><br>HDCC Co-Director"] --- n2(["<b>MRI Acquisition</b>"]) & n5(["<b>Processed MRI Quality Control</b>"])
    n2 --- n4["<b>Kimberly Weldon, PhD</b><br>Seimens Engineer"]
    n5 --- n6["<b>Eric Feczko, PhD</b><br>QC Lead<br><br><b>Lucille A. Moore, PhD</b><br>Neuroinformatics<br>
    <b>Michael Anderson</b><br>Analyst"]
    style CDNI fill:#E1BEE7,stroke:#AA00FF
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n5 fill:#E1BEE7,stroke:#AA00FF
    style n4 fill:#BBDEFB,stroke:#2962FF
    style n6 fill:#BBDEFB,stroke:#2962FF
```
</div>

### Health Sciences Technology
🚧 **UPDATE FOLLOWING DESCRIPTION** 🚧      
[HST](https://hst.umn.edu/) at UMN is responsible for: *Data shelter*, *PHI*, *Electronic Health Records (EHR)*, *Ripple Interface*, *Overall Data Management*, *QC Dashboards*, *Ancillary Studies*, and *Third Party Integration*.

<div style="width: 90%; margin: 0 auto;">
```mermaid
---
config:
  layout: elk
---
flowchart TB
    B["<b>Karen Athy-Penrose</b><br>Project Manager"] --- n2(["<b>Development Operations</b>"])
    B --- n3(["<b>MRI Quality Control Dashboard</b>"]) & n4(["<b>Electronic Health Records</b>"])
    n2 --- F["<b>Dan Duhon<br>Derek Thompson<br>Saranya Subramanian<br>Brett Weaver</b>"]
    n3 --- G["<b>Haley Hutala</b><br>Tableau Engineer<br><br><b>Sanjana Madakshire</b><br>Quality Control"]
    E["<b>Reed McEwan</b><br>HDCC Architect &amp; Data Manager"] --- B
    H["<b>Steve Johnson</b><br>Dir Informatics Innovation<br><br><b>Tim Meyer</b><br>Informatics Engineer"] --- n5["<b>WashU EMR Data Core<br></b><i>Click to view org chart</i>"]
    n4 --- H
    style B fill:#C8E6C9,stroke:#00C853
    style n2 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#E1BEE7,stroke:#AA00FF
    style n4 fill:#E1BEE7,stroke:#AA00FF
    style F fill:#BBDEFB,stroke:#2962FF
    style G fill:#BBDEFB,stroke:#2962FF
    style E fill:#BBDEFB,stroke:#2962FF
    style H fill:#BBDEFB,stroke:#2962FF
    style n5 fill:#E1BEE7,stroke:#AA00FF
    click n5 "#washu"
```
</div>

### MIDB Informatics Hub & MSI
🚧 **UPDATE FOLLOWING DESCRIPTION** 🚧      
The [Masonic Institute for the Developing Brain (MIDB) Informatics Hub](https://midb.umn.edu/research/informatics) and [Minnesota Supercomputing Institute (MSI)](https://msi.umn.edu/) at UMN provide the following services to the HBCD study: *System Administration*, *Loris Hosting*, *Computing*, *Processing*, and *Data Sharing*.

```mermaid
---
config:
  layout: elk
---
flowchart TB
    L["<b>Maren Macgregor-Hannah</b><br>HDCC Program Manager"] --- N(["<b>Advanced System Operations</b>"]) & O(["<b>Informatics &amp; Processing</b>"]) & P(["<b>Data Steward</b>"]) 
    L --- n8(["<b>Security &amp Compliance</b>"])
    N --- Q["<b>Jesse Erdmann</b><br>Senior SysOps<br><br><b>Kimberleigh Breen</b><br>Data Manager<br><br><b>Sriharshitha Anuganti<br>Alyssa Oksa</b><br>DevOps"]
    O --- n4["<b>Timothy Hendrickson</b><br>Neuroimaging Lead<br><br><b>Erik Lee</b><br>Pipeline Lead<br><br><b>Monalisa Biles</b><br>Analyst"]
    P --- n7["<b>Jeff Shi</b><br>Informatics Consultant<br><br><b>Borgne Raasch</b><br>Data Steward"]
    n8 --- n9["<b>Naomi Hospodarsky-Sutherland</b>"]
    n10["<b>Thomas Pengo, PhD</b><br>Co-Director, Informatics Group"] --- L
    style L fill:#C8E6C9,stroke:#00C853
    style N fill:#E1BEE7,stroke:#AA00FF
    style O fill:#E1BEE7,stroke:#AA00FF
    style P fill:#E1BEE7,stroke:#AA00FF
    style n8 fill:#E1BEE7,stroke:#AA00FF
    style Q fill:#BBDEFB,stroke:#2962FF
    style n4 fill:#BBDEFB,stroke:#2962FF
    style n7 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n10 fill:#BBDEFB,stroke:#2962FF
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
        <th style="width: 30%;">Title</th>
        <th style="width: 45%;">Role on HDCC</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Thomas Pengo, PhD</td>
        <td style="word-wrap: break-word; white-space: normal;">Co-Director, MIDB Informatics Group</td>
        <td style="word-wrap: break-word; white-space: normal;">IG Lead</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Maren Macgregor-Hannah</td>
        <td style="word-wrap: break-word; white-space: normal;">Program Manager</td>
        <td style="word-wrap: break-word; white-space: normal;">HDCC Program Manager</td>
    </tr>
    <tr>
    <td>Jesse Erdmann</td>
    <td>Systems Operations</td>
    <td style="word-wrap: break-word; white-space: normal;">Advanced System Operations (ASO) oversight</td>
    </tr>
    <tr>
    <td>Devin Willis</td>
    <td>DevOps Engineer</td>
    <td>Dev Ops</td>
    </tr>
    <tr>
    <td>Jesus Garcia</td>
    <td>DevOps Engineer</td>
    <td>Dev Ops</td>
    </tr>
    <tr>
    <td>Timothy Hendrickson</td>
    <td style="word-wrap: break-word; white-space: normal;">MIDB-IG Neuroimaging Informatics Manager</td>
    <td>Neuroimaging lead</td>
    </tr>
    <tr>
    <td>Erik Lee</td>
    <td>Neuroimaging Analyst</td>
    <td>Pipeline lead</td>
    </tr>
    <tr>
    <td>Monalisa Biles</td>
    <td>&nbsp;</td>
    <td>Analyst</td>
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
  <td>Research Security and Compliance Analyst</td>
  <td>Security/Compliance</td>
  </tr>
</tbody>
</table>
</div>


## WashU
🚧 **UPDATE FOLLOWING DESCRIPTION** 🚧      
The Washington University in St. Louis (WashU) group has oversight of: *Electronic Medical Records (EMR)*, *Ripple*, *Ambra*, *AirTable*, and *HBCD Study Administrative Core (HCAC) coordination*.

<div style="width: 60%; margin: 0 auto;">
```mermaid
---
config:
  layout: elk
---
flowchart TB
    A["<b>Sauren Ravencroft</b><br>Project Manager"] --- ambra(["<a href="#ambra"><b>Ambra</b></a>"])
    A --- n5
    n13["<b>Nicole Venteris</b><br>EMR Project Manager"] --- C["<b>EMR Data Core</b><br>"]
    n5(["<a href="#airtable"><b>AirTable</b></a> & <a href="#ripple"><b>Ripple</b></a>"]) --- n9["<b>Liliana Mueller</b><br>Ripple Admin<br><br><b>Kevine Ngalula</b><br>Ripple<br><br><b>Lynn Menchaca</b><br>AirTable Admin"]
    ambra --- n1["<b>Bob McKinstry</b><br><b>Josh Shimony</b><br>Co-Is &amp; Neuroradiologists<br><br><b>Dimitrios ('Jim') Alexopoulos</b><br>Data Manager"]
    n14["<b>Chris Smyser, MD</b>, PI<br><b>Chad Sylvester, PhD</b>, Co-I"] --- A & n13
    style A fill:#C8E6C9,stroke:#00C853
    style C fill:#E1BEE7,stroke:#AA00FF
    style n13 fill:#C8E6C9,stroke:#00C853
    style n5 fill:#E1BEE7,stroke:#AA00FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n1 fill:#BBDEFB,stroke:#2962FF
    style n14 fill:#BBDEFB,stroke:#2962FF
    style ambra fill:#E1BEE7,stroke:#AA00FF
    linkStyle 3 stroke:#000000,fill:none
    linkStyle 4 stroke:#000000,fill:none
    linkStyle 5 stroke:#000000,fill:none
```
</div>

### Subcontractor Details

#### AirTable 🚧 **UPDATE FOLLOWING DESCRIPTION** 🚧
AirTable is a cloud-based collaborative platform and database service that combines the features of a database and a spreadsheet. It allows users to organize, track, and collaborate on structured data using customizable tables, forms, views, and automation. In the HBCD Study, Airtable is widely used as a centralized project management and tracking tool, including study coordination and oversight, neuroimaging workflow tracking, cross-team communication, and quality control and reporting.

#### Ambra 🚧 **UPDATE FOLLOWING DESCRIPTION** 🚧
Ambra is a cloud-based gateway that allows the direct transmission of medical images between participating institutions. Ambra supports secure data transfer, DICOM standard compliance, de-identification tools, and access control, making it suitable for large-scale, multi-site research studies. For the HBCD Study, Ambra is used as the centralized platform for uploading, storing, and sharing neuroimaging data from participating research sites.
 
#### Ripple 🚧 **UPDATE FOLLOWING DESCRIPTION** 🚧
[Ripple Science](https://www.ripplescience.com/) is a digital clinical trial software deployed at all HBCD Study sites for participant recruitment and retention. See details of Ripple's role in the study [here](https://www.ripplescience.com/ripple-science-supports-nih-funded-healthy-brain-and-child-development-study/).




