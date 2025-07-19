# Data Release Workflows & SOPs

### Stage 1: Determine Measures to Include in Release

The HCAC PM (Stephanie Averill) collaborates with HDCC to generate a full list of **potential** measures for the data release.

 - Leadership and OG approve, along with Workgroups  
 - The full list of potential measures is circulated to all Workgroups and subject matter experts, who update [this form](https://docs.google.com/spreadsheets/d/171oj0PLLtVgp5OSReBD5J6Ir4U56QQrWEwu92ZwttrM/edit?usp=sharing) to mark “INCLUDE” or “NOT INCLUDED” *at the variable level* for each potential measure

## Stage 2: Integrate Planned Measures in Beta Releases

The HDCC works to implement the items indicated as “INCLUDE” by the Workgroups and subject matter experts and the first versioned beta release begins 1-2 months after the data freeze. The Beta Release (BR) Sprint Cycle includes: 

*Under development: Adapt SOP to account for scenarios where a Workgroup selects “INCLUDE,” but HDCC is unable to implement at this stage.*

1. Known issues or new features are prioritized
2. Versioned BRs are released on the 4th Friday of every month
    - Every BR of the HDCC has  a corresponding "BR Hot Sheet" to be completed by the HDCC. This document serves as a central resource for information regarding the release to address the following key areas:
        - **Single Point of Truth on date/time**: provides a clear time/date when BRX is ready, and a single point of contact/truth 
        - **Checklist/Information**: provides a checklist and information for Lasso and HDCC for when something may have changed that will either make the data sent ‘non-compliant’ (e.g. not all participants represented in the `participant.tsv`) or break loading or downloading of files
        - **Sign Off**: responsible parties provide a clear/thoughtful sign off on what is going into a release and ensure it is properly documented on the internal Docs site.   
    - When the “BR Hot Sheet” is completed and all items are checked off, it is sent to Lasso to initiate BR ingestion. When data are ingested into Lasso, the following checks are performed:
        - Ingestion logs are queried to check for skipped sessions and insertion errors  
        - Quality Assurance (QA) of the file transfer UI and Globus transfer performed  
3. Once Lasso ingestion of BR data is complete, HDCC liaison (Jen Zink) communicates this back out to the WGs to QC their data in the Lasso system  

## Stage 3: Data Quality Issue Identification, Reporting, and Handling  

There are 2 bins of issues with separate pipelines for reporting/handling:

#### Bin 1: Internal Findings

These are issues identified during [Lasso ingestion QA](qc.md#pre-release-pheno) that need to be addressed by the HDCC; these are documented on the Monday board to be discussed/tracked/addressed internally. 

#### Bin 2: Workgroup Findings (reported in collaboration with HDCC Liaison)

These are data issues identified by the workgroups, analysts, or LORIS. (These issues are communicated to Jen and documented in a structured format for BR sprint planning and ultimate  resolution by HDCC).

*Once Bin 2 issues are added to an upcoming BR sprint and the corrections appear in a versioned BR in Lasso, Jen communicates to original reporter that the known issue is addressed and to verify the correction is implemented as expected in the Lasso system*

**WG Template for reporting issues**

> *Issue Category:* {Data Error, Data Improvement, Data Dictionary Request)       
*Data Element/Instrument Affected:* {element/instrument name}          
*Description:* Explanation of issue         
*Explanation for how to address the issue*: Description of fix	      
*Reporter*: SME/analyst name and contact information 	
