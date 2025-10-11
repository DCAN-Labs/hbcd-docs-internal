<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧</p>


<div id="2" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
    <span class="table-text">
      <i class="fa-solid fa-2" style="margin-right: 6px; color: blue;"></i>
      Raw BIDS De-identification
    </span>
    <a class="anchor-link" href="#2" title="Copy link">
      <i class="fa-solid fa-link"></i>
    </a>
  </span>
  <span class="arrow">▸</span>
</div>

<div class="table-collapsible-content">






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


# Further Details on De-Id Routines

The de-identification procedures of raw BIDS data largely covers the following groups of files:

* Standard BIDS metadata text sources such as `scans.tsv`, `session.tsv`, JSON files  
    * In motion files, any JSON fields with `PatientName` or `PatientBirthDate` are deleted  
    * In scans/sessions tsv/json files, the site information is replaced with anonymized site IDs based on a site mapping file.  
    * All other JSON files known to contain site IDs have `InstitutionAddress`, `InstitutionalDepartmentName`, and `InstitutionName` deleted  
* EEG `eventlogs.txt` sourcedata files: Custom routines anonymize entries for `DataFile.Basename`, `DCCID`, and `Subject` columns  
* EEG .set files  
    * Custom routines recursively search through nested fields and replaces DCCIDs/PSCIDs with Release Candidate IDs  
    * Certain fields likely to contain manually entered information such as DCCID/PSCID have their text replaced with ‘Anonymized’  
    * Other fields likely to contain manually entered information have values outside of a pre-approved list of strings replaced with ‘Anonymized’  
* **MRS Nifti files:** Fields `InstitutionName`, `InstitutionAddress`, `PatientSex`, and `PatientWeight` are removed from nifti headers using spec2nii


Some files are not currently supported by de-identification routines and have thus far not been copied to any of the de-identified data stores. This includes files from the EEG sourcedata directory (i.e. `sub-{ID}/ses-{V0X}/eeg/sourcedata`): `eventlogs.edat3` and `eeg_flags.json` files