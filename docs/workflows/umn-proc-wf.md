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
  <span class="table-text"><i class="fa-solid fa-1" style="margin-right: 6px; color: blue;"></i> Creation of Release Candidate IDs for Anonymization</span>
  <a class="anchor-link" href="#1" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>
<strong>Goal:</strong> Maintain an up-to-date mapping of identifiers for de-identification workflows.<br>
<strong>Contacts:</strong> Reed McEwan, Dan Duhon<br>
<strong>Frequency:</strong> Daily (&lt;1 hour)<br>
<strong>Inputs:</strong> N/A<br>
<strong>Outputs:</strong> <code>s3://midb-hbcd-main-pr-deidentification-list/release_identifiers.csv</code><br>
<strong>Notes:</strong> Phantom data may not yet be included.</p>
</div>

<div id="2" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-2" style="margin-right: 6px; color: blue;"></i> Raw BIDS De-identification</span>
  <a class="anchor-link" href="#2" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal:</strong> De-identify and upload raw BIDS sessions</p><br>
<p><b>Criteria for De-identification:</b></p><br>
<ul>
  <li>Subject is listed in the release ID mapping</li>
  <li>No existing session files in the de-ID bucket</li>
  <li>Session files are available in the LORIS bucket and are ≥1 day old</li>
</ul>
<br>
<p><strong>De-identification Procedure Overview:</strong></p>
<ul>
  <li>De-identify and upload all supported session files to the de-ID bucket</li>
  <li>Update session metadata (<code>sessions.&lt;tsv|json&gt;</code>) in de-ID bucket</li>
  <li>Tag each file with its <code>loris-versionid</code> (corresponds to <code>VersionId</code> in original LORIS files) for traceability</li>
</ul>
<br><br>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
  <td><i>REMOVED/RETAINED IDENTIFIERS:</i></td>
</tr>
<tr>
  <td><strong>Removed</strong>: PSCIDs, DCCIDs, and Site IDs & manually populated fields (prone to typos) that commonly contain these identifiers</td>
</tr>
<tr>
  <td><strong>Retained</strong>: Jittered patient age at acquisition, Acquisition dates/times, and & Acquisition device serial numbers </td>
</tr>
</tbody>
</table>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; padding-top; 0; margin-top: 0;">
<tbody>
<tr>
  <td><i>FILE COVERAGE:</i></td>
</tr>
<tr>
  <td><b>BIDS metadata</b> (<code>scans</code>/<code>session</code> tsv & JSONs)<br>
      <ul>
      <li>Remove <code>PatientName</code> and <code>PatientBirthDate</code> from JSONs</li>
      <li>Replace site info with anonymized site IDs via mapping file</li>
      <li>Remove <code>InstitutionAddress</code>, <code>InstitutionalDepartmentName</code>, and <code>InstitutionName</code></li>
    </ul>
  </td>
</tr>
<tr>
<td><b>EEG</b><br>
  <ul>
  <li><b>sourcedata</b> (<code>eventlogs.txt</code>): Anonymize entries for <code>DataFile.Basename</code>, <code>DCCID</code>, and <code>Subject</code> columns</li>
  <li><b>.set files:</b> Replace <b>(1)</b> All DCCIDs/PSCIDs with Release Candidate IDs & <b>(2)</b> Unapproved manual entries with “Anonymized”</li>
  </ul>
</td>
</tr>
<tr>
  <td><b>MRS NIfTI files:</b><br><ul><li>Remove <code>InstitutionName</code>, <code>InstitutionAddress</code>, <code>PatientSex</code>, and <code>PatientWeight</code> using <code>spec2nii</code></li></ul></td>
</tr>
</tbody>
</table>
<p><strong>Contacts:</strong> Sriharshitha Anuganti, Erik Lee<br>
<strong>Frequency:</strong> Daily (PM CST; ensure completion within 24 hours)<br>
<strong>Inputs:</strong> <code>s3://midb-hbcd-main-pr/assembly_bids</code> (raw BIDS data with DCCIDs)<br>
<strong>Outputs:</strong> <code>s3://midb-hbcd-main-deid/assembly_bids</code> (with Release Candidate IDs)<br>
<strong>Notes:</strong> EEG sourcedata files <code>eventlogs.edat3</code> and <code>eeg_flags.json</code> are not yet supported.</p>
</div>

<div id="3" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-3" style="margin-right: 6px; color: blue;"></i> Registration of Subjects from Raw BIDS Data into CBRAIN</span><a class="anchor-link" href="#3" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal:</strong> Make CBRAIN aware of subjects available for processing.<br>
<strong>Contacts:</strong> Monalisa Bilas, Erik Lee<br>
<strong>Frequency:</strong> Daily (&lt;1 hour)<br>
<strong>Inputs:</strong> <code>s3://midb-hbcd-main-deid/assembly_bids</code><br>
<strong>Outputs:</strong> Internal CBRAIN records indicating existence of subject folder within BIDS directory<br>
<strong>Notes:</strong>  Each subject has a single CBRAIN <em>BidsSubject File Collection</em> linking all sessions, though sessions are processed independently.</p>
</div>

<div id="4" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-4" style="margin-right: 6px; color: blue;"></i> Pipeline processing of De-identified Data</span>
  <a class="anchor-link" href="#4" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p>
<strong>Goal:</strong> Run de-identified BIDS data through BIDS App pipelines in CBRAIN (e.g., `Nibabies`, `BIBSNet`, `QSIPrep`) to generate derivatives.</p>
<p><strong>Workflow Steps:</strong></p>
<ol>
<li>Detect available sessions sessions in the BIDS directory and CBRAIN  </li>
<li>Check for existing outputs or prior processing attempts  </li>
<li>For sessions without outputs or attempted processing, verify that required prerequisite files exist and pass QC (from <code>scans.tsv</code>)  </li>
<li>Select files for processing based on modality-specific rules (e.g., best T1w image only, all fMRI images passing QC)</li>
<li>Confirm dependencies between pipelines (e.g., BIBSNet outputs are required by Nibabies)</li>
<li>Launch CBRAIN processing tasks using predefined settings and including only files selected for processing  </li>
<li>CBRAIN uploads successful job outputs to session-specific folders on S3 and records the corresponding processing tasks and generated file collections internally.</li>
</ol>
<p>
<strong>Contacts:</strong> Erik Lee, Monalisa Bilas<br>
<strong>Frequency:</strong> Daily (initial routine &lt;1 hour; processing jobs may take ~1 day)<br>        
<strong>Inputs:</strong> <code>s3://midb-hbcd-main-deid/assembly_bids</code> (raw BIDS data)<br>
<strong>Outputs:</strong> <code>s3://midb-hbcd-main-deid/derivatives/ses-{V0X}</code> (session-specific subject folders with Release Candidate IDs)<br>
<strong>Notes:</strong> See the <a href="https://github.com/erikglee/HBCD_CBRAIN_PROCESSING">GitHub repository</a> and <a href="https://hbcd-cbrain-processing.readthedocs.io/latest/index.html#">Documentation</a> for the code that manages processing. CBRAIN logs and file collections are stored internally for traceability.</p>
</ul>
</div>

<div id="5" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-5" style="margin-right: 6px; color: blue;"></i>Saving stdout/stderr Logs for Failed CBRAIN Processing Tasks</span>
  <a class="anchor-link" href="#5" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal:</strong> Preserve CBRAIN processing logs for failed tasks before the jobs are deleted (a few weeks after completion). Logs from successful jobs are already archived in the <code>.cbrain</code> logs included with the S3 outputs. Note that CBRAIN only transfers outputs to S3 for successful jobs.<br>
<strong>Contacts:</strong> Monalisa Bilas, Erik Lee<br>
<strong>Frequency:</strong> Daily (&lt;1 hour)<br>
<strong>Inputs:</strong> CBRAIN task directories stored on MSI under <code>/scratch.global</code><br>
<strong>Outputs:</strong> <code>s3://midb-hbcd-main-deid/cbrain_std_logs/</code> (Files named <code>{CBRAIN_Task_ID}.&lt;out|err&gt;.out</code>)<br>
<strong>Notes:</strong> CBRAIN task IDs are unique, so duplicates pose no issue.
</div>

<div id="6" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-6" style="margin-right: 6px; color: blue;"></i> Cleanup for Out-of-Sync Raw BIDS Data (between LORIS & de-id buckets)</span>
  <a class="anchor-link" href="#6" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal:</strong> Detect and remove sessions where LORIS and de-ID data diverge.</p>
<ol>
<strong>Process:</strong>
<li>Compare file counts between de-id and LORIS session folders</li>
<li>If files counts are the same, compare the <code>loris-versionid</code> of the de-id files to ensure they match</li>
<li>If session counts or <code>loris-versionid</code> mismatch, delete all associated derivatives, CBRAIN task records, and raw BIDS data</li>
</ol>
<p><strong>Contacts:</strong> Erik Lee, Monalisa Bilas<br>
<strong>Frequency:</strong> Daily (runtime varies by data volume)<br>
<ul>
<strong>Inputs:</strong>
<li>Raw BIDS data: <code>s3://midb-hbcd-main-deid/assembly_bids</code> and <code>s3://midb-hbcd-main-pr/assembly_bids</code>  </li>
<li>Derivatives: <code>s3://midb-hbcd-main-deid/derivatives</code>  </li>
<li>CBRAIN records of userfiles and tasks  </li>
</ul>
<p><strong>Outputs:</strong> N/A<br>
<strong>Notes:</strong> Cleanup enables the next de-ID workflow to rerun cleanly for that session.</p>
</div>

<div id="7" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-7" style="margin-right: 6px; color: blue;"></i> Re-identification of Derivatives (i.e. re-insertion of DCCIDs) for LORIS</span>
  <a class="anchor-link" href="#7" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal:</strong> Re-identify de-identified derivatives by replacing Release Candidate IDs with DCCIDs, enabling upload to LORIS. <i>Ensures derivatives are accurately linked back to participant DCCIDs to facilitate internal QC with Workgroups and tabulation of derivatives.</i></p>
<p><strong>Process:</strong></p>
<ul>
  <li>Download de-identified derivatives from <code>s3://midb-hbcd-main-deid/derivatives</code>.</li>
  <li>Replace all Release Candidate IDs with corresponding DCCIDs in both filenames and file contents (using file type–specific routines) for <b>(1)text-based files</b> (<code>.csv</code>, <code>.html</code>, <code>.json</code>, <code>.txt</code>, <code>.toml</code>, <code>.tsv</code>, <code>.log</code>) and <b>(2) EEG .set files</b> (<code>.set</code>, <code>.mat</code>)</li>
  <li>Replace anonymized site IDs with real site IDs.</li>
  <li>Upload re-identified files to <code>s3://midb-hbcd-main-pr/reid_derivatives</code> and set the metadata field <code>cbrain-timestamp</code> based on the original file’s <code>LastModified</code> value.</li>
</ul>
<p><i>Re-identification is performed on derivatives for the following pipelines:</i></p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
<tbody>
<tr>
<td>bibsnet<br>bme_x<br>hbcd_motion<br></td>
<td>made<br>mriqc<br>mrsqc</td>
<td>nibabies<br>osprey<br>qmri_postproc</td>
<td>qsiprep<br>qsirecon-DIPYDKI<br>qsirecon-DSIStudio</td>
<td>qsirecon-TORTOISE_model-&lt;MAPMRI|tensor&gt;<br>symri<br>xcp_d</td>
</tr>
</tbody>
</table>
<p><strong>Contacts:</strong> Sriharshitha Anuganti, Erik Lee<br>
<strong>Frequency:</strong> Runs daily<br>
<strong>Inputs:</strong> <code>s3://midb-hbcd-main-deid/derivatives</code> (de-identified derivatives)<br>
<strong>Outputs:</strong> <code>s3://midb-hbcd-main-pr/reid_derivatives</code> (re-identified derivatives)</p>
<ul>
<strong>Notes:</strong>
  <li>Update re-ID routines whenever pipeline filenames or formats change.</li>
  <li>Previous documentation referenced <code>VersionId</code> metadata; this has been replaced with <code>LastModified</code> since the de-ID bucket is non-versioned.</li>
</ul>
</div>

<div id="8" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-8" style="margin-right: 6px; color: blue;"></i> Cleanup for Out-of-Sync Derivatives in LORIS Bucket</span>
  <a class="anchor-link" href="#8" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal:</strong> Remove re-identified derivatives from LORIS when they become out of sync with corresponding de-identified derivatives.</p>
<p><strong>Process:</strong></p>
<ul>
  <li>For each subject/session/pipeline, compare <code>LastModified</code> (de-ID) and <code>cbrain-timestamp</code> (re-ID) values between:
    <ul>
      <li><code>s3://midb-hbcd-main-deid/derivatives</code></li>
      <li><code>s3://midb-hbcd-main-pr/reid_derivatives</code></li>
    </ul>
  </li>
  <li>If the number of files or timestamps differ, delete the corresponding re-identified data from <code>s3://midb-hbcd-main-pr</code>.</li>
</ul>
<p><strong>Contacts:</strong> Sriharshitha Anuganti, Monalisa Bilas, Erik Lee<br>
<strong>Frequency:</strong> Daily<br>
<strong>Inputs:</strong> <code>s3://midb-hbcd-main-pr/reid_derivatives</code> and <code>s3://midb-hbcd-main-deid/derivatives</code><br>
<strong>Outputs:</strong> N/A<br>
<strong>Notes:</strong> Ensures only synchronized derivatives remain in LORIS and prevents outdated or mismatched data from being used.</p>
</div>
<br>