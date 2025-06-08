# Data Release Workflows & SOPs

### 🚧 Action Items 🚧

See [Basecamp](https://3.basecamp.com/5032058/buckets/35843816/todolists/8733090807) for updates needed for this page.

------------------------

## BR Hot Sheets

Every beta release (BR) of the HDCC data will have a corresponding "BR Hot Sheet" to be completed by the HDCC and sent to Lasso once all items are checked off. This document serves as a central resource for information regarding the release to address the following key areas:

- **Single Point of Truth on date/time**: provides a clear time/date when BRX is ready, and a single point of contact/truth 
- **Checklist/Information**: provides a checklist and information for Lasso and HDCC for when something may have changed that will either make the data sent ‘non-compliant’ (e.g. not all participants represented in the `participant.tsv`) or break loading or downloading of files
- **Sign Off**: provides a clear/thoughtful sign off on what is going into a release and ensure it is properly documented on the internal Docs site

## Lasso Ingestion QA
When data are ingested into Lasso, the following checks are performed:

- Ingestion logs are queried to check for skipped sessions and insertion errors
- Quality Assurance (QA) of the file transfer UI and Globus transfer performed

## Issue Handling
There are 2 bins of issues with separate pipelines for reporting/handling:

#### Bin 1: Internal Findings
These are data issues identified by the workgroups, analysts, or LORIS. These are documented on the Monday board to be discussed/tracked/sorted out internally 

#### Bin 2: Workgroup Findings
These are issues identified during [Lasso ingestion QA](#lasso-ingestion-qa) that need to be addressed by the HDCC. (**TBD:** These issues are documented in a structured format and sent to the HDCC for resolution).

##### Template for reporting issues

> *Issue Name:* {name}        
*Brief name for issue:* {short name}   
*Description:* Explanation of issue - please exclude subject IDs and any other information that can’t be shared publicly - add this under Additional Notes instead. If providing an example filepath/name, use `sub-<label>` and `ses-<label>`      
*Impact on Users:* How this issue affects functionality or user experience      
*Target Release for Fix:* TBD or BR number if known     
*Additional Notes:* For discussion only, not for inclusion in the internal HBCD Docs Known Issues page

