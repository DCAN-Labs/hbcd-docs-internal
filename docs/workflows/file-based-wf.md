# File Based Data Processing Workflow

![](images/capture.svg)



S3 - MRS BIDS: `s3://midb-hbcd-main-pr-mrs/`        
S3 JCVI DICOMs: `s3://midb-hbcd-ucsd-main-pr-dicoms/`       
S3 MAIN PR: `s3://midb-hbcd-main-pr/assembly_bids/`


```mermaid
---
config:
  layout: elk
  look: neo
  theme: redux
---
flowchart LR
 subgraph Sites_Capture["Sites Capture [FIONA]"]
        FIONA_KSI[/"KSI MRI (DCM)"/]
        LORIS_ACM[/"MRS"/]
        n15[/"K-Space"/]
  end
 subgraph Capture_JCVI["Capture & BIDS Conversion [JCVI]"]
        UMN["UMN SCE [HST]"]
        JCVI["Convert to BIDS"]
        n1@{ label: "<span style=\"color:\">s3://midb-hbcd-main-pr-mrs/</span>" }
  end
 subgraph Capture_HST["Capture & BIDS Conversion [HST]"]
        n6["HBCD Central"]
        n9["QC Raw MRI"]
        n10@{ label: "<br><span style=\"color:\">s3://midb-hbcd-ucsd-main-pr-dicoms/</span>" }
        n11["Convert to BIDS"]
  end
 subgraph Capture_LORIS["Sites Capture [LORIS]"]
        n12[/"EEG BIDSWizard"/]
        n13[/"Axtivity"/]
        n14[/"GABI"/]
  end
    LORIS_ACM --> UMN
    UMN --> JCVI
    JCVI --> n1
    n1 --> RAW_BIDS@{ label: "<b>S3 - Main PR<br><span style=\"color:\">s3://midb-hbcd-main-pr/assembly_bids/</span></b><br>" }
    n6 --> n9 & n10
    n9 --> n10
    n10 --> n11
    n11 --> RAW_BIDS
    n12 --> RAW_BIDS
    n13 --> RAW_BIDS
    n14 --> RAW_BIDS
    n15 --> UMN
    FIONA_KSI --> n6
    UMN@{ shape: disk}
    JCVI@{ shape: rect}
    n1@{ shape: disk}
    n6@{ shape: disk}
    n9@{ shape: rect}
    n10@{ shape: disk}
    n11@{ shape: rect}
    RAW_BIDS@{ shape: disk}
    style FIONA_KSI fill:#FFD600
    style LORIS_ACM fill:#FFD600
    style n15 fill:#FFD600
    style UMN fill:#C8E6C9
    style JCVI fill:#2962FF,color:#FFFFFF
    style n1 fill:#C8E6C9
    style n6 fill:#C8E6C9,color:#000000
    style n9 fill:#2962FF,color:#FFFFFF
    style n10 fill:#C8E6C9,color:#FFFFFF
    style n11 fill:#2962FF,color:#FFFFFF
    style n12 fill:#FFD600
    style n13 fill:#FFD600
    style n14 fill:#FFD600
    style RAW_BIDS fill:#C8E6C9
    style Capture_LORIS fill:#FFF9C4
    style Sites_Capture fill:#FFF9C4
    style Capture_JCVI fill:#BBDEFB
    style Capture_HST fill:#BBDEFB
```