<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧</p>


## Detailed Workflows


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

