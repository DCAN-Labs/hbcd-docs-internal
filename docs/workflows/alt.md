<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧</p>


## Detailed Workflows

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

