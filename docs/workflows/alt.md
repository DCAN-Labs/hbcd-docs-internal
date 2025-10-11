<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧</p>


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

