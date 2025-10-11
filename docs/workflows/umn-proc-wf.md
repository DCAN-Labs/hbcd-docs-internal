<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

# UMN De-Identification & Pipeline Processing

## Overview

This documentation describes how UMN handles imaging data after it has been curated by LORIS into BIDS format. At a high level, UMN’s manipulations of the BIDS data mostly involves de-identification of the data and post-processing with containerized pipelines (such as Nibabies). The workflow is largely designed in 8 independent components that rely on the actions or outputs of one another to curate processing. Briefly, these workflows are as follows:

1. Creation of Release Candidate IDs that will be used for anonymization  
2. De-identification routines for the raw BIDS data  
3. ‘Registration’ of subjects from the raw BIDS data into CBRAIN  
4. Post-processing of de-identified data  
5. Saving stdout/stderr files for failed CBRAIN processing tasks to S3  
6. Clean-up routines that remove raw and derived data when the LORIS and BIDS data become out of sync.  
7. Routines that re-insert DCCIDs into the outputs of post-processing derivatives so that they can be ingested and viewed in LORIS   
8. Clean-up routines that remove out-of-sync post-processing derivatives from LORIS’ bucket  

**These workflows operate together to facilitate a processing system with the following desired functionalities and constraints:**

* Only anonymized data using Release Candidate IDs is allowed for public release  
* Release Candidate IDs and DCCIDs/PSCIDs should never be found in the same data structure. However if they ever are found in the same structure, it is better for this to be in an internal facing data store.  
* The raw BIDS data curated by LORIS will be periodically updated. These updates include changes to BIDS metadata, which may or may not impact processing pipelines. They also include changes to the data files themselves and changes to QC values.  
* The derived processing outputs released to the public must be from the same processing stream that internal HBCD investigators use for QC purposes.  
* LORIS must have access to derived data outputs for creating tabulated versions of imaging derived phenotypes, and for facilitating internal QC for the consortium.  
* Data should be re-processed as infrequently as possible while still maintaining integrity between inputs/outputs. For example, if ses-V03 becomes available for a given subject, this should not initiate re-processing of data from ses-V02. However if new files or updated QC becomes available for ses-V02 then ses-V02 reprocessing should occur.

### General limitations of current workflows

The incoming data elements from a session, ranging from MRI (initial scans along with any rescans), EEG, Axivity, GABI, and manual QC ratings may come into the LORIS assembly_bids structure over the course of a few weeks. Processing of any pipeline will not become stable until the last data element of a session comes in. Therefore, certain processing workflows that are intended for automated QC will be slowed down while other data elements are coming in.


## Individual Workflows

<div id="1" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Creation of Release Candidate IDs used for anonymization</span>
  <a class="anchor-link" href="#1" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal of workflow:</strong> Upload new versions of the release identifier mapping spreadsheet as the study progresses, so that new subjects can be included in de-identified processing workflows.<br><strong>Relevant contacts:</strong> Reed McEwan, Dan Duhon<br><strong>Frequency:</strong> Runs daily (takes less than one hour to complete)<br><strong>Inputs:</strong> N/A<br><strong>Outputs:</strong> <code>s3://midb-hbcd-main-pr-deidentification-list/release_identifiers.csv</code><br><strong>Caveats / Notes:</strong> Phantom data is (probably) not currently included in the output file.</p>
</div>

<div id="2" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">De-identification routines for the raw BIDS data</span>
  <a class="anchor-link" href="#2" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal of workflow:</strong><br>Identify and process imaging sessions that meet the following conditions:</p>
<ul>
<li>Session belongs to a subject listed in the identifier mapping file  </li>
<li>Session does <em>not</em> have existing files in the de-id bucket  </li>
<li>Session <em>does</em> have files in the LORIS bucket, with all files at least one day old  </li>
</ul>
<br>
<p>When these conditions are met:</p>
<ul>
<li>All supported files under the session prefix are de-identified and added to the de-id bucket  </li>
<li>The subject’s <code>sessions.tsv</code> and <code>sessions.json</code> files are updated in the de-id bucket  </li>
<li>De-identified outputs include metadata for tracking synchronization with LORIS: Each file includes the S3 metadata field <code>loris-versionid</code>, which corresponds to the <code>VersionId</code> of the original LORIS file prior to de-identification</li>
</ul>
<p><strong>Relevant contacts:</strong> Sriharshitha Anuganti, Erik Lee<br><strong>Frequency:</strong> Runs daily at 11 PM CST, processes may need to be put into place to ensure workflow ends within 24 hours<br><strong>Inputs:</strong> <code>s3://midb-hbcd-main-pr/assembly_bids</code> (raw BIDS data, contain DCCIDs and other identifying information)<br><strong>Outputs:</strong> <code>s3://midb-hbcd-main-deid/assembly_bids</code> (contains Release Candidate IDs)<br><strong>Caveats / Notes:</strong>  </p>
<ul>
<li>Additional details about file-specific de-identification procedures (file type specific details, types of information that is removed) are provided in the <strong>De-Identification Details</strong> section.  </li>
<li>Certain rare or lower-priority EEG files are not currently included in the de-id routines.</li>
</ul>
</div>

<div id="3" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Registration of Subjects from Raw BIDS Data into CBRAIN</span>
  <a class="anchor-link" href="#3" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal of workflow:</strong> Make CBRAIN aware of subjects available for processing.<br><strong>Relevant contacts:</strong> Monalisa Bilas, Erik Lee<br><strong>Frequency:</strong> Runs daily (takes less than one hour to complete)<br><strong>Inputs:</strong> <code>s3://midb-hbcd-main-deid/assembly_bids</code><br><strong>Outputs:</strong> Internal records in CBRAIN indicating subject folder existence within the BIDS directory<br><strong>Caveats / Notes:</strong>  Each subject has a single CBRAIN <em>BidsSubject File Collection</em> linking all sessions, though each session is processed independently.</p>
</div>

<div id="4" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Post-processing of De-identified Data</span>
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
<strong>Relevant contacts:</strong> Erik Lee, Monalisa Bilas<br>
<strong>Frequency:</strong> Runs daily (initial routine &lt;1 hour; processing jobs may take ~1 day)<br>        
<strong>Inputs:</strong> Raw BIDS data under s3://midb-hbcd-main-deid/assembly_bids<br>
<strong>Outputs:</strong> Derivative BIDS data (post-processing outputs) located in session specific folders under s3://midb-hbcd-main-deid/derivatives/ses-{V0X}<br>
<strong>Caveats / Notes:</strong> The code that manages processing is available in this <a href="https://github.com/erikglee/HBCD_CBRAIN_PROCESSING">GitHub Repository</a> and <a href="https://hbcd-cbrain-processing.readthedocs.io/latest/index.html#">ReadTheDocs Documentation</a></p>
</ul>
</div>

<div id="5" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Saving stdout/stderr Files for Failed CBRAIN Processing Tasks</span>
  <a class="anchor-link" href="#5" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<p><strong>Goal of workflow:</strong> Ensure permanent records of all CBRAIN processing logs. Since jobs are deleted a few weeks after completion, this preserves failure records.</p>
<p><strong>Relevant contacts:</strong> Monalisa Bilas, Erik Lee<br><strong>Frequency:</strong> Runs daily (takes less than one hour)<br><strong>Inputs:</strong> CBRAIN task directories stored at <code>/scratch.global</code> (MSI)<br><strong>Outputs:</strong> <code>s3://midb-hbcd-main-deid/cbrain_std_logs/</code> (Files named <code>&lt;CBRAIN_Task_ID&gt;.out</code> and <code>&lt;CBRAIN_Task_ID&gt;.err</code>)</p>
<p><strong>Caveats / Notes:</strong>  </p>
<ul>
<li>CBRAIN task IDs are unique—duplicates pose no issue.  </li>
<li>Saving logs is only necessary when processing fails: successful ones already include <code>.cbrain</code> logs in their output directories. CBRAIN only sends processing outputs to S3 when processing is successful. </li>
</ul>
</div>

<div id="6" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Clean-up routines for out-of-sync raw BIDS data between LORIS and de-id buckets</span>
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
<p><strong>Relevant contacts:</strong> Erik Lee, Monalisa Bilas<br>
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
  <span class="table-text">Re-insertion of DCCIDs into Derivatives for LORIS Ingestion </span>
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
<li>Download the de-id derivatives and replace Release Candidate IDs with DCCIDs (in both file names and file contents, with specific routines for specific file types). Also replace anonymized with real site IDs</li>
<li>Upload resulting files to <code>s3://midb-hbcd-main-pr/reid_derivatives</code> with the metadata field <code>cbrain-timestamp</code> (from original file’s <code>LastModified</code> time)</li>
</ul>
<p><strong>Relevant contacts:</strong> Sriharshitha Anuganti, Erik Lee<br>
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
  <span class="table-text">Clean-up Routines for Out-of-sync Derivatives in LORIS Bucket</span>
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
<p><strong>Relevant contacts:</strong> Sriharshitha Anuganti, Monalisa Bilas, Erik Lee<br>
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

* bibsnet  
* bme_x  
* hbcd_motion  
* made  
* mriqc  
* mrsqc  
* nibabies  
* osprey  
* qmri_postproc  
* qsiprep  
* qsirecon-DIPYDKI  
* qsirecon-DSIStudio  
* qsirecon-TORTOISE_model-MAPMRI  
* asirecon-TORTOISE_model-tensor  
* symri  
* xcp_d

These pipelines are present in the *s3://midb-hbcd-main-deid/derivatives* bucket, which contains de-identified data. Specifically, this bucket uses *release candidate IDs* as subject labels. At a high level, the re-identification routines replace these release candidate IDs with the corresponding *candidate IDs (DCCIDs)*.

The re-identification routines process two types of files:

1. **Standard text-based files** (.csv, .html, .json, .txt, .toml, .tsv, .log): In these files, all occurrences of release candidate IDs are replaced with the corresponding DCCIDs.  
2. **EEG .set files** (with .set and .mat extensions): These routines recursively search through nested fields within the file structure to identify and replace release candidate IDs with DCCIDs.

