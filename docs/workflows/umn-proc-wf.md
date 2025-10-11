<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

# UMN De-Identification & Pipeline Processing

## Overview

This documentation outlines how UMN processes imaging data after it has been curated by LORIS into BIDS format.  
The workflow consists of **eight interdependent components** that handle de-identification, pipeline processing, synchronization, and cleanup of imaging data.

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

### Primary Goals

- Ensure only anonymized data (using Release Candidate IDs) is released publicly  
- Prevent overlap of Release Candidate IDs and DCCIDs/PSCIDs within the same dataset  
- The raw BIDS data curated by LORIS will be periodically updated. These updates also include updates to BIDS metadata and QC (which may impact processing pipelines).
- The derived processing outputs released to the public must be from the same processing stream that internal HBCD investigators use for QC purposes.  
- Provide LORIS with access to derived outputs for facilitating internal QC with Workgroups and for tabulation of derivatives  
- Limit unnecessary reprocessing while still maintaining integrity between inputs/outputs. For example, if ses-V03 becomes available for a given subject, this should not initiate re-processing of ses-V02 data. However if new files or updated QC becomes available for ses-V02 then ses-V02 reprocessing should occur.   

### General Limitations
Incoming session data (MRI including initial scans and rescans, EEG, Axivity, GABI, and manual QC ratings) often arrive over several weeks. Automated QC and processing routines may be delayed until all expected elements for a session are available.

---

## Individual Workflows

<div id="1" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-gears" style="margin-right: 6px; color: blue;"></i> Creation of Release Candidate IDs for Anonymization</span>
  <a class="anchor-link" href="#1" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>
<strong>Goal of workflow:</strong> Maintain an up-to-date mapping of identifiers for de-identification workflows.<br>
<strong>Contacts:</strong> Reed McEwan, Dan Duhon<br>
<strong>Frequency:</strong> Daily (&lt;1 hour)<br>
<strong>Inputs:</strong> N/A<br>
<strong>Outputs:</strong> <code>s3://midb-hbcd-main-pr-deidentification-list/release_identifiers.csv</code><br>
<strong>Caveats / Notes:</strong> Phantom data may not yet be included.</p>
</div>


<div id="2" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-gears" style="margin-right: 6px; color: blue;"></i> Raw BIDS Data De-identification</span>
  <a class="anchor-link" href="#2" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal of workflow:</strong><br>Identify and process imaging sessions that meet the following conditions:</p>
<ul>
<li>Subject listed in the release ID mapping  </li>
<li>No existing session files in the de-ID bucket  </li>
<li>Session files exist in the LORIS bucket and are ≥1 day old </li>
</ul>
<br>
<p>When these conditions are met:</p>
<ul>
<li>De-identify and upload all supported session files to the de-id bucket </li>
<li>Update session-level metadata (<code>sessions.tsv</code> and <code>sessions.json</code>) in the de-id bucket  </li>
<li>For traceability, tag each file with <code>loris-versionid</code>, which corresponds to the <code>VersionId</code> of the original LORIS file prior to de-identification</li>
</ul>
<p><strong>Contacts:</strong> Sriharshitha Anuganti, Erik Lee<br>
<strong>Frequency:</strong> Daily at PM CST (processes may need to be put into place to ensure workflow ends within 24 hours)<br>
<strong>Inputs:</strong> <code>s3://midb-hbcd-main-pr/assembly_bids</code> (raw BIDS data, contain DCCIDs and other identifying information)<br>
<strong>Outputs:</strong> <code>s3://midb-hbcd-main-deid/assembly_bids</code> (contains Release Candidate IDs)<br>
<strong>Caveats / Notes:</strong>  </p>
<ul>
<li>Additional details about file-specific de-identification procedures (file type specific details, types of information that is removed) are provided in the <strong>De-Identification Details</strong> section.  </li>
<li>Certain rare or low-priority EEG files are currently excluded.</li>
</ul>
</div>

<div id="3" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-gears" style="margin-right: 6px; color: blue;"></i> Registration of Subjects from Raw BIDS Data into CBRAIN</span>
  <a class="anchor-link" href="#3" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal of workflow:</strong> Make CBRAIN aware of subjects available for processing.<br><strong>Contacts:</strong> Monalisa Bilas, Erik Lee<br><strong>Frequency:</strong> Runs daily (takes less than one hour to complete)<br><strong>Inputs:</strong> <code>s3://midb-hbcd-main-deid/assembly_bids</code><br><strong>Outputs:</strong> Internal records in CBRAIN indicating subject folder existence within the BIDS directory<br><strong>Caveats / Notes:</strong>  Each subject has a single CBRAIN <em>BidsSubject File Collection</em> linking all sessions, though each session is processed independently.</p>
</div>

<div id="4" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-gears" style="margin-right: 6px; color: blue;"></i> Post-processing of De-identified Data</span>
  <a class="anchor-link" href="#4" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>
<strong>Goal of workflow:</strong> Initiate processing of de-identified BIDS data through post-processing BIDS Apps in CBRAIN (e.g., <code>Nibabies</code>, <code>BIBSNet</code>, <code>QSIPrep</code>, etc.) to produce derivatives.</p>
<p><strong>Workflow Steps:</strong></p>
<ul>
<li>Identify available subjects and sessions in the BIDS directory and CBRAIN  </li>
<li>Check for existing outputs or prior processing attempts  </li>
<li>For sessions without outputs or attempted processing, verify that required prerequisite files exist and pass QC (from <code>scans.tsv</code>)  </li>
<li>Select files for processing based on modality-specific rules. <em>Example:</em> Use only the best T1w image or all fMRI images passing QC</li>
<li>For sessions with requisite files present for processing, confirm dependencies between pipelines (e.g., BIBSNet outputs are required by Nibabies)</li>
<li>Launch CBRAIN processing tasks using predefined settings and including only files selected for processing  </li>
<li>CBRAIN uploads outputs from successful jobs to S3 and stores internal records of the processing ‘task’ and the created ‘file collections’ stemming from processing.</li>
</ul>
<p>
<strong>Contacts:</strong> Erik Lee, Monalisa Bilas<br>
<strong>Frequency:</strong> Runs daily (initial routine &lt;1 hour; processing jobs may take ~1 day)<br>        
<strong>Inputs:</strong> Raw BIDS data under s3://midb-hbcd-main-deid/assembly_bids<br>
<strong>Outputs:</strong> Derivative BIDS data (post-processing outputs) located in session specific folders under s3://midb-hbcd-main-deid/derivatives/ses-{V0X}<br>
<strong>Caveats / Notes:</strong> The code that manages processing is available in this <a href="https://github.com/erikglee/HBCD_CBRAIN_PROCESSING">GitHub Repository</a> and <a href="https://hbcd-cbrain-processing.readthedocs.io/latest/index.html#">ReadTheDocs Documentation</a></p>
</ul>
</div>

<div id="5" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-gears" style="margin-right: 6px; color: blue;"></i> Saving stdout/stderr Files for Failed CBRAIN Processing Tasks</span>
  <a class="anchor-link" href="#5" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal of workflow:</strong> Ensure permanent records of all CBRAIN processing logs. Since jobs are deleted a few weeks after completion, this preserves failure records.</p>
<p><strong>Contacts:</strong> Monalisa Bilas, Erik Lee<br><strong>Frequency:</strong> Runs daily (takes less than one hour)<br><strong>Inputs:</strong> CBRAIN task directories stored at <code>/scratch.global</code> (MSI)<br><strong>Outputs:</strong> <code>s3://midb-hbcd-main-deid/cbrain_std_logs/</code> (Files named <code>&lt;CBRAIN_Task_ID&gt;.out</code> and <code>&lt;CBRAIN_Task_ID&gt;.err</code>)</p>
<p><strong>Caveats / Notes:</strong>  </p>
<ul>
<li>CBRAIN task IDs are unique—duplicates pose no issue.  </li>
<li>Saving logs is only necessary when processing fails: successful ones already include <code>.cbrain</code> logs in their output directories. CBRAIN only sends processing outputs to S3 when processing is successful. </li>
</ul>
</div>

<div id="6" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-gears" style="margin-right: 6px; color: blue;"></i> Clean-up routines for out-of-sync raw BIDS data between LORIS and de-id buckets</span>
  <a class="anchor-link" href="#6" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal of workflow:</strong> Detect and clean up raw BIDS data when the LORIS and de-id buckets become out of sync, followed by cleanup of various data elements to set the stage for updated data.</p>
<p><strong>Process:</strong></p>
<ol>
<li>Compare file counts between de-id and LORIS session folders</li>
<li>If files counts are the same, compare the loris-version id of the de-id files to ensure they match</li>
<li>If counts differ or <code>loris-versionid</code> mismatches, delete: all derivative files for that session, CBRAIN task processing record, and associated raw BIDS</li>
</ol>
<p><strong>Contacts:</strong> Erik Lee, Monalisa Bilas<br>
<strong>Frequency:</strong> Runs daily. Unclear what the worst case performance is for how long the job will take to run.Runs daily (runtime varies by data volume)<br>
<strong>Inputs:</strong>  </p>
<ul>
<li>Raw BIDS data: <code>s3://midb-hbcd-main-deid/assembly_bids</code> and <code>s3://midb-hbcd-main-pr/assembly_bids</code>  </li>
<li>Derivatives: <code>s3://midb-hbcd-main-deid/derivatives</code>  </li>
<li>CBRAIN records of userfiles and tasks  </li>
</ul>
<p><strong>Outputs:</strong> N/A<br>
<strong>Caveats / Notes:</strong> Following the completion of this workflow, any raw BIDS data from sessions with ‘out of sync’ files will be removed. This sets the stage for the de-id routines to be rerun for the given session.</p>
</div>

<div id="7" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-gears" style="margin-right: 6px; color: blue;"></i> Re-insertion of DCCIDs into Derivatives for LORIS Ingestion </span>
  <a class="anchor-link" href="#7" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal of workflow:</strong> Make de-identified derivative files available in LORIS by replacing Release Candidate IDs with DCCIDs (“re-iding”).</p>
<p><strong>Process:</strong></p>
<ul>
<li>Download the de-id derivatives and replace Release Candidate IDs with DCCIDs (in both file names and file contents, with specific routines for specific file types). Also replace anonymized with real site IDs.</li>
<li>Upload resulting files to <code>s3://midb-hbcd-main-pr/reid_derivatives</code> with the metadata field <code>cbrain-timestamp</code> (from original file’s <code>LastModified</code> time)</li>
</ul>
<p><strong>Contacts:</strong> Sriharshitha Anuganti, Erik Lee<br>
<strong>Frequency:</strong> Runs daily<br>
<strong>Inputs:</strong> Derived BIDS data <code>s3://midb-hbcd-main-deid/derivatives</code><br>
<strong>Outputs:</strong> Derived BIDS data <code>s3://midb-hbcd-main-pr/reid_derivatives</code></p><br>
<p><strong>Caveats / Notes:</strong>  </p>
<ul>
<li>Update routines whenever pipeline filenames change.  </li>
<li>See “Further Details on Re-ID Routines” for more information.  </li>
<li>Older documentation referenced <code>VersionId</code>; now replaced by <code>LastModified</code> due to non-versioned de-id bucket.</li>
</ul>
</div>

<div id="8" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-gears" style="margin-right: 6px; color: blue;"></i> Clean-up Routines for Out-of-sync Derivatives in LORIS Bucket</span>
  <a class="anchor-link" href="#8" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal of workflow:</strong> Remove re-id derivatives from LORIS when they become out of sync with the de-id derivatives.</p>
<p><strong>Process:</strong> For each subject/session/pipeline:  </p>
<ul>
<li>Compare <code>LastModified</code> and <code>cbrain-timestamp</code> values between <code>s3://midb-hbcd-main-pr/reid_derivatives</code> and <code>s3://midb-hbcd-main-deid/derivatives</code>  </li>
<li>If number of files or timestamp fields are mismatched, delete the corresponding re-id data from LORIS (<code>s3://midb-hbcd-main-pr</code>)</li>
</ul>
<p><strong>Contacts:</strong> Sriharshitha Anuganti, Monalisa Bilas, Erik Lee<br>
<strong>Frequency:</strong> Runs daily<br>
<strong>Inputs:</strong> Derived BIDS data located at <code>s3://midb-hbcd-main-pr/reid_derivatives</code> and <code>s3://midb-hbcd-main-deid/derivatives</code><br>
<strong>Outputs:</strong> N/A<br>
<strong>Caveats / Notes:</strong> Ensures only synchronized derivatives remain in LORIS.</p>
</div>

## Further Details on De-Id Routines

The de-identification described here covers the procedures used on s3://midb-hbcd-main-pr/assembly_bids, which is ‘raw BIDS’ and uses DCCIDs as subject labels. During de-identification the following features are removed:

* PSCIDs  
* DCCIDs  
* Site IDs  
* Fields that commonly contain PSCIDs/DCCIDs/Site IDs, that are manually populated and therefore prone to typos

Other features that are of interest but are not removed include:

* Patient age at acquisition (available in jittered form)  
* Acquisition dates/times for different study elements  
* Acquisition device serial numbers

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

## Further Details on Re-Id Routines

The re-identification procedures described here apply to the following derivatives pipelines:

<div id="pipeline" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Pipelines</span>
  <a class="anchor-link" href="#pipelines" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<ul>
<li>bibsnet  </li>
<li>bme_x  </li>
<li>hbcd_motion  </li>
<li>made  </li>
<li>mriqc  </li>
<li>mrsqc  </li>
<li>nibabies  </li>
<li>osprey  </li>
<li>qmri_postproc  </li>
<li>qsiprep  </li>
<li>qsirecon-DIPYDKI  </li>
<li>qsirecon-DSIStudio  </li>
<li>qsirecon-TORTOISE_model-MAPMRI  </li>
<li>asirecon-TORTOISE_model-tensor  </li>
<li>symri  </li>
<li>xcp_d</li>
</ul>
</div>

These pipelines are present in the *s3://midb-hbcd-main-deid/derivatives* bucket, which contains de-identified data. Specifically, this bucket uses *release candidate IDs* as subject labels. At a high level, the re-identification routines replace these release candidate IDs with the corresponding *candidate IDs (DCCIDs)*.

The re-identification routines process two types of files:

1. **Standard text-based files** (.csv, .html, .json, .txt, .toml, .tsv, .log): In these files, all occurrences of release candidate IDs are replaced with the corresponding DCCIDs.  
2. **EEG .set files** (with .set and .mat extensions): These routines recursively search through nested fields within the file structure to identify and replace release candidate IDs with DCCIDs.

