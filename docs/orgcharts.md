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

## LORIS
<div style="width: 90%; margin: 0 auto;">
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
```
</div>
<br>

<div id="loris" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">Roles & Responsibilities</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
    <thead>
      <tr>
        <th style="width: 20%;">Name</th>
        <th style="width: 30%;">Title</th>
        <th style="width: 50%;">Role on HDCC</th>
      </tr>
    </thead>
    <tbody>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Alan Evans</td>
        <td style="word-wrap: break-word; white-space: normal;">Principal Investigator</td>
        <td style="word-wrap: break-word; white-space: normal;">Oversight and management of MCIN and LORIS operations</td>
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
        <td style="word-wrap: break-word; white-space: normal;">Lead BioSamples/EEG Developer</td>
        <td style="word-wrap: break-word; white-space: normal;">Development and implementation of LORIS BioSample/EEG features, including data ingestion, quality control, tracking systems, and Dashboard innovations</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Regis Ongaro-Carcy</td>
        <td style="word-wrap: break-word; white-space: normal;">Lead Behavior (BHV) Developer</td>
        <td style="word-wrap: break-word; white-space: normal;">Development of LORIS BHV features, including integration with external platforms (e.g. REDCap, Ripple, MSI), streamlining data collection, and enhancing system functionality through interoperability and workflow improvements</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">Sruthy Matthew</td>
        <td style="word-wrap: break-word; white-space: normal;">Senior Backend Developer</td>
        <td style="word-wrap: break-word; white-space: normal;">Development of LORIS LaunchPad and Backend features</td>
    </tr>
    <tr>
        <td style="word-wrap: break-word; white-space: normal;">George Murad</td>
        <td style="word-wrap: break-word; white-space: normal;">Junior Behavior (BHV) Developer</td>
        <td style="word-wrap: break-word; white-space: normal;">Development of LORIS BHV features, including instrument coding, automated QC queries, and API/Endpoint implementation</td>
    </tr>
</tbody>
</table>
</div>

## Lasso
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
    A["<b>Leigh MacIntyre</b>, CEO<br>MCIN Assoc. Dir., PM"] --> B(["<b>Pre-Release Training<br>Scheduling<br></b>"]) & n1(["<b>Ancillary<br>Studies</b>"]) & n2(["<a href="https://hbcdstudy.org/workgroups-and-committees/"><b>Workgroup</a> Data QC</b>"]) & n3(["<b>Technical</b>"]) & n4(["<b>Data<br>Loading</b>"]) & s1
    B --> n5["<b>Ellise Elamparo</b><br>Exec Admin"]
    n1 --> n6["<b>Aarushi Chaudhry<br></b>Study Success<br>Manager"]
    n2 --> n7["<b>Jen Zink<br></b>Director,<br>Partnerships &amp; Grant<br>Funding<br><br><b>Marion Fechino</b><br>Data Analyst"]
    n3 --> n8["<b>Fraser Glen<br></b>CTO<br><br><b>Jordan<br>Sterling<br></b>Lead Dev"]
    n4 --> n9["<b>Laetitia Fesselier<br></b>Sr. Dev<br><b><br>Edson Silva</b><br><b>Mateus Andre<br></b>Dev"]
    n23 --> n24["<b>Francisco Soto</b><br>Dev/SysOps Manager<br><b>Alexandre Meyer</b><br>DevOps<br><b>Nataliya Korniyenko<br></b>Sys Admin<br><br><b>Mark Walker<br></b>Software Architect<br><b>Daniel Patularu</b><br><b>Oksana Bodnariuk<br>Jonas Vinson<br></b>Developers"]
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
    style s1 fill:transparent,stroke:#000000
    style n5 fill:#BBDEFB,stroke:#2962FF
    style n6 fill:#BBDEFB,stroke:#2962FF
    style n7 fill:#BBDEFB,stroke:#2962FF
    style n8 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    style n24 fill:#BBDEFB,stroke:#2962FF
    style n26 fill:#BBDEFB,stroke:#2962FF
    style n27 fill:#BBDEFB,stroke:#2962FF
```

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
<div style="width: 90%; margin: 0 auto;">
```mermaid
---
config:
  layout: elk
---
flowchart TB
    A["<b>Anders Dale, PhD</b><br>PI/Director"] --- n1(["<b>Fiona</b>"]) & n2(["<b>MRI QC</b>"]) & n3(["<b>MRI</b>"]) & n6(["<b>REDCap</b>"]) & n15(["<b>Dashboard</b>"])
    n1 --- n8["<b>Rongguang Yang, PhD</b><br>Fiona Lead"]
    n2 --- n9["<b>Donald Hagler, PhD</b><br>MRI QC Lead<br>"]
    n3 --- n10["<b>Josh Kuperman</b><br>MRI Lead"]
    n6 --- n4["<b>Janosch Linkersdörfer, PhD</b><br>REDCap/Data Science Lead"]
    n9 --- n13["<b>Tyler Berkness</b><br>Protocol Violations<br><b>Sejal Shanbhag</b><br>Issue Handling"]
    n15 --- n4
    n4 --- n12["<b>Joseph Baligh</b><br>Server Admin<br><b>Erika Bolden</b> &amp; <b>Laura Ziemer</b><br>Dev/Admin"] & n17["<b>Biplabendu Das</b><br>Backend Dev<br><b>Olivier Celhay</b><br>Frontend Dev"]
    n15 --> n17
    n6 --> n12
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
    A["<b>Chris Smyser, MD</b>, PI<br><b>Chad Sylvester, PhD</b>, Co-I"] --- neurology(["<b>Neurology</b>"]) & C(["<b>EHR</b><br>"]) & n11(["<b>OMOR</b>"])
    neurology --- n1["<b>Bob McKinstry</b><br><b>Josh Shimony</b><br>Co-Investigators &amp; Study Neuroradiologists"]
    n1 --- n2["<b>Dimitrios (Jim) Alexopoulos</b><br>Data Manager, Ambra"]
    C --- n3["<b>Philip Payne</b><br><b>Albert Lai</b><br>Co-Investigators"]
    n3 --- n4["<b>Nicole Venteris</b><br>Project Manager"]
    n12["<b>UMN HST</b><br><i>Click to see org chart</i>"] --> C
    n5(["<b>Ripple</b>"]) --- B["<b>Sauren Ravencroft</b><br>Project Manager"]
    A --> n5 & n6(["<b>AirTable &amp; Ancillary Studies</b>"])
    B --> n8["<b>Lynn Menchaca</b><br>AirTable Management<br><b>Madison Gardner</b><br>U01 Site Piloting"] & n9["<b>Liliana Mueller</b><br>Programming<br>&amp; Management"]
    n6 --- B
    style A fill:#BBDEFB,stroke:#2962FF
    style neurology fill:#E1BEE7,stroke:#AA00FF
    style C fill:#E1BEE7,stroke:#AA00FF
    style n11 fill:#E1BEE7,stroke:#AA00FF
    style n1 fill:#BBDEFB,stroke:#2962FF
    style n2 fill:#BBDEFB,stroke:#2962FF
    style n3 fill:#BBDEFB,stroke:#2962FF
    style n4 fill:#BBDEFB,stroke:#2962FF
    style n12 fill:#E1BEE7,stroke:#AA00FF
    style n5 fill:#E1BEE7,stroke:#AA00FF
    style B fill:#BBDEFB,stroke:#2962FF
    style n6 fill:#E1BEE7,stroke:#AA00FF
    style n8 fill:#BBDEFB,stroke:#2962FF
    style n9 fill:#BBDEFB,stroke:#2962FF
    click n12 "#health-sciences-technology"
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