# Lasso

## Lasso1
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
 subgraph s2["<b>CONSORTIUM-FACING</b> (<i>Unless Specified Otherwise</i>)"]
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
![](../lasso.svg)

## Lasso2
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
  <img src="../../lasso2.svg" alt="Lasso" width="90%" />
</div>


## Lasso3
### Code
```mermaid
---
config:
  layout: dagre
---
flowchart TB
    A["<b>Leigh MacIntyre</b>, CEO"] --- n1(["<b>Data QC</b>"]) & n3(["<b>Admin</b>"]) & n5(["<b>Ancillary Studies</b>"]) & n7(["<b>Development</b>"]) & n9(["<b>Data Loading</b>"]) & n11(["<b>Dev/SysOps</b>"]) & n13(["<b>QA</b>"]) & n15(["<b>UI/UX</b>"])
    n1 --- n2["<b>Jen Zink<br></b>Dir Partnerships<br>&amp; Grant Funding<br><br><b>Marion Fechino</b><br>Data Analyst"]
    n3 --- n4["<b>Ellise Elamparo</b><br>Training Scheduling<br>(pre-release)"]
    n5 --- n6["<b>Aarushi Chaudhry<br></b>Study Success Manager"]
    n7 --- n8["<b>Fraser Glen<br></b>CTO<br><b>Jordan Sterling<br></b>Lead Developer
    -------------------------------
    <b><i>INTERNAL TO LASSO:</i>
    Mark Walker</b><br>Software Architect<br>
    <b>Daniel Patularu</b><br><b>Oksana Bodnariuk<br>Jonas Vinson<br></b>Developers"]
    n9 --- n10["<b><i>INTERNAL TO LASSO:</i></b><br><b>Laetitia Fesselier</b><br>Sr Developer<br>
    <b>Edson Silva</b><br><b>Mateus Andre</b><br>Developers"]
    n11 --- n12["<b><i>INTERNAL TO LASSO:</i><br>Francisco Soto</b><br>Manager<br>
    <b>Alexandre Meyer</b><br>DevOps Engineer<br><br><b>Nataliya Korniyenko<br></b>Systems Administrator"]
    n13 --- n14["<b><i>INTERNAL TO LASSO:</i></b>
    <b>Vandana Sriram</b><br><b>Anjali Raj Katuri<br></b>QA Engineers"]
    n15 --- n16["<b><i>INTERNAL TO LASSO:</i></b>
    <b>Andrew Sawaya</b><br>Lead Designer<br>
    <b>Mehrafarin Ekhlaspour</b><br>Visual Design"]
    style A fill:#BBDEFB,stroke:#2962FF
    style n1 fill:#E1BEE7,stroke:#AA00FF
    style n3 fill:#E1BEE7,stroke:#AA00FF
    style n5 fill:#E1BEE7,stroke:#AA00FF
    style n7 fill:#E1BEE7,stroke:#AA00FF
    style n9 fill:#E1BEE7,stroke:#AA00FF
    style n11 fill:#E1BEE7,stroke:#AA00FF
    style n13 fill:#E1BEE7,stroke:#AA00FF
    style n15 fill:#E1BEE7,stroke:#AA00FF
    style n2 fill:#BBDEFB,stroke:#2962FF
    style n4 fill:#BBDEFB,stroke:#2962FF
    style n6 fill:#BBDEFB,stroke:#2962FF
    style n8 fill:#BBDEFB,stroke:#2962FF
    style n10 fill:#BBDEFB,stroke:#2962FF
    style n12 fill:#BBDEFB,stroke:#2962FF
    style n14 fill:#BBDEFB,stroke:#2962FF
    style n16 fill:#BBDEFB,stroke:#2962FF
```

### SVG

![](../lasso3.svg)