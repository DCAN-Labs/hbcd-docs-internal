<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧</p>

# UMN De-Identification & Pipeline Processing

## Overview

This documentation outlines how UMN processes imaging data after it has been curated by LORIS into BIDS format.  
The workflow consists of **eight interdependent components** that handle de-identification, post-processing, synchronization, and cleanup of imaging data.

### Primary Goals
- Ensure only anonymized data (using Release Candidate IDs) is released publicly  
- Prevent overlap of Release Candidate IDs and DCCIDs/PSCIDs within the same dataset  
- Maintain data integrity and consistency between LORIS and post-processing outputs  
- Limit unnecessary reprocessing while ensuring updates are reflected appropriately  
- Provide LORIS with access to derived outputs for internal QC and phenotype tabulation  

### General Limitations
Incoming session data (MRI, EEG, Axivity, GABI, and manual QC ratings) often arrive over several weeks.  
Automated QC and processing routines may be delayed until all expected elements for a session are available.

---

## Workflow Summary

| # | Workflow | Core Function | Frequency |
|---|-----------|----------------|------------|
| 1 | **Release Candidate ID Creation** | Uploads updated release ID mappings for new subjects | Daily |
| 2 | **Raw BIDS De-Identification** | Removes identifiers and uploads anonymized data to de-ID bucket | Daily |
| 3 | **CBRAIN Subject Registration** | Registers de-identified subjects in CBRAIN for processing | Daily |
| 4 | **Post-Processing of De-ID Data** | Runs pipelines (e.g., Nibabies, QSIPrep) on de-identified BIDS | Daily |
| 5 | **CBRAIN Log Preservation** | Archives failed task logs for permanent tracking | Daily |
| 6 | **Raw BIDS Sync Cleanup** | Removes outdated data when LORIS and de-ID buckets diverge | Daily |
| 7 | **Re-ID for LORIS** | Replaces Release Candidate IDs with DCCIDs for LORIS ingestion | Daily |
| 8 | **Derivative Sync Cleanup** | Removes outdated re-ID derivatives from LORIS bucket | Daily |

---

## Detailed Workflows

Each section below summarizes goals, inputs, outputs, and key notes.

---

### 1. Creation of Release Candidate IDs
**Goal:** Maintain an up-to-date mapping of identifiers for de-identification workflows.  
**Frequency:** Daily (<1 hour)  
**Inputs:** N/A  
**Outputs:** `s3://midb-hbcd-main-pr-deidentification-list/release_identifiers.csv`  
**Contacts:** Reed McEwan, Dan Duhon  
**Notes:** Phantom data may not yet be included.

---

### 2. De-Identification of Raw BIDS Data
**Goal:** Identify sessions eligible for anonymization and upload de-identified versions.  
**Conditions:**
- Subject listed in the release ID mapping  
- No existing files in the de-ID bucket  
- Files exist in the LORIS bucket and are ≥1 day old  

**Actions:**
- De-identify and upload all supported session files to `s3://midb-hbcd-main-deid/assembly_bids`  
- Update session-level metadata (`sessions.tsv` / `sessions.json`)  
- Tag each file with `loris-versionid` metadata for traceability  

**Contacts:** Sriharshitha Anuganti, Erik Lee  
**Frequency:** Daily at 11 PM CST (completion within 24 hrs)  
**Inputs:** `s3://midb-hbcd-main-pr/assembly_bids`  
**Outputs:** `s3://midb-hbcd-main-deid/assembly_bids`  
**Notes:**
- See [De-Identification Details](#further-details-on-de-id-routines) for file-specific info.  
- Some rare EEG files are currently excluded.

---

### 3. CBRAIN Subject Registration
**Goal:** Register de-identified subjects for processing within CBRAIN.  
**Frequency:** Daily (<1 hour)  
**Inputs:** `s3://midb-hbcd-main-deid/assembly_bids`  
**Outputs:** Internal CBRAIN records linking subject sessions  
**Contacts:** Monalisa Bilas, Erik Lee  
**Notes:** Each subject has a single CBRAIN *BidsSubject File Collection*, though sessions process independently.

---

### 4. Post-Processing of De-Identified Data
**Goal:** Run containerized post-processing (e.g., `Nibabies`, `BIBSNet`, `QSIPrep`) to generate derivatives.  
**Steps:**
1. Detect available sessions in CBRAIN  
2. Check for existing outputs  
3. Verify required inputs pass QC  
4. Select files by modality rules (e.g., best T1w, all fMRI passing QC)  
5. Ensure dependencies between pipelines (e.g., `BIBSNet` → `Nibabies`)  
6. Launch CBRAIN jobs with predefined configurations  

**Outputs:** `s3://midb-hbcd-main-deid/derivatives/ses-{V0X}`  
**Contacts:** Erik Lee, Monalisa Bilas  
**Frequency:** Daily (jobs may take ~1 day)  
**Code:** [GitHub Repo](https://github.com/erikglee/HBCD_CBRAIN_PROCESSING) • [Docs](https://hbcd-cbrain-processing.readthedocs.io/latest/index.html)  
**Notes:** CBRAIN logs and file collections are stored internally for traceability.

---

### 5. Saving CBRAIN stdout/stderr Logs
**Goal:** Preserve failure logs from CBRAIN before job deletion.  
**Frequency:** Daily (<1 hour)  
**Inputs:** `/scratch.global` (MSI)  
**Outputs:** `s3://midb-hbcd-main-deid/cbrain_std_logs/`  
**Contacts:** Monalisa Bilas, Erik Lee  
**Notes:**
- Only failed jobs require log preservation (successful ones already archived).  
- Filenames follow `<CBRAIN_Task_ID>.out` / `.err` format.

---

### 6. Cleanup for Out-of-Sync Raw Data
**Goal:** Detect and remove sessions where LORIS and de-ID data diverge.  
**Process:**
1. Compare file counts and `loris-versionid` metadata  
2. If mismatched, delete all related derivatives, CBRAIN task records, and raw data  

**Inputs:**
- `s3://midb-hbcd-main-deid/assembly_bids`  
- `s3://midb-hbcd-main-pr/assembly_bids`  
- `s3://midb-hbcd-main-deid/derivatives`  
- CBRAIN task metadata  

**Contacts:** Erik Lee, Monalisa Bilas  
**Frequency:** Daily (runtime varies)  
**Notes:** Cleanup enables the next de-ID workflow to rerun cleanly for that session.

---

