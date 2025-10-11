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

The incoming data elements from a session, ranging from MRI (initial scans along with any rescans), EEG, Axivity, GABI, and manual QC ratings may come into the LORIS assembly\_bids structure over the course of a few weeks. Processing of any pipeline will not become stable until the last data element of a session comes in. Therefore, certain processing workflows that are intended for automated QC will be slowed down while other data elements are coming in.


## Individual Workflows

### Creation of Release Candidate IDs that will be used for anonymization

**Goal of workflow:** Upload new versions of the release identifier mapping spreadsheet as the study progresses, so that new subjects can be included in de-identified processing workflows.    
**Relevant contacts:** Reed McEwan, Dan Duhon           
**Frequency:** Runs daily (takes less than one hour to complete)            
**Inputs:** N/A             
**Outputs:** `s3://midb-hbcd-main-pr-deidentification-list/release_identifiers.csv`         
**Caveats / Notes:** Phantom data is (probably) not currently included in the output file.

### De-identification routines for the raw BIDS data

**Goal of workflow:**  
Identify and process imaging sessions that meet the following conditions:

- Session belongs to a subject listed in the identifier mapping file  
- Session does *not* have existing files in the de-id bucket  
- Session *does* have files in the LORIS bucket, with all files at least one day old  

When these conditions are met:

1. All supported files under the session prefix are de-identified and added to the de-id bucket  
2. The subject’s `sessions.tsv` and `sessions.json` files are updated in the de-id bucket  
3. De-identified outputs include metadata for tracking synchronization with LORIS: Each file includes the S3 metadata field `loris-versionid`, which corresponds to the `VersionId` of the original LORIS file prior to de-identification

**Relevant contacts:** Sriharshitha Anuganti, Erik Lee          
**Frequency:** Runs daily at **11:00 PM CST**, Workflow should complete within 24 hours         
**Inputs:** `s3://midb-hbcd-main-pr/assembly_bids` (contains DCCIDs and other identifying information)      
**Outputs:** `s3://midb-hbcd-main-deid/assembly_bids` (contains Release Candidate IDs)      
**Caveats / Notes:**  
- Additional details about file-specific de-identification procedures are provided in the **De-Identification Details** section.  
- Certain rare or lower-priority EEG files are not currently included in the de-id routines.

### Registration of Subjects from Raw BIDS Data into CBRAIN

**Goal of workflow:** Make CBRAIN aware of subjects available for processing.       
**Relevant contacts:** Monalisa Bilas, Erik Lee         
**Frequency:** Runs daily (takes less than one hour to complete)        
**Inputs:** `s3://midb-hbcd-main-deid/assembly_bids`        
**Outputs:** Internal records in CBRAIN indicating subject folder existence within the BIDS directory       
**Caveats / Notes:**  Each subject has a single CBRAIN *BidsSubject File Collection* linking all sessions, though each session is processed independently.

### Post-processing of De-identified Data

**Goal of workflow:** Initiate processing of de-identified BIDS data through post-processing BIDS Apps in CBRAIN (e.g., `nibabies`, `bibsnet`, `qsiprep`) to produce derivatives.

**Workflow Steps:**

1. Identify available subjects and sessions in the BIDS directory and CBRAIN  
2. Check for existing outputs or prior processing attempts  
3. Verify that required files exist and pass QC (from `scans.tsv`)  
4. Select files for processing based on modality-specific rules  
   - *Example:* Use only the best T1w image or all fMRI images passing QC  
5. Confirm dependencies between pipelines (e.g., `bibsnet` outputs required by `nibabies`)  
6. Launch CBRAIN processing tasks using predefined settings  
7. Upload successful outputs to S3 and record tasks in CBRAIN  

**Relevant contacts:** Erik Lee, Monalisa Bilas         
**Frequency:** Runs daily (initial routine <1 hour; processing jobs may take ~1 day)        
**Inputs:** `s3://midb-hbcd-main-deid/assembly_bids`        
**Outputs:** `s3://midb-hbcd-main-deid/derivatives/ses-<label>`  

**Caveats / Notes:**  
- Workflow code and documentation:  
  - [GitHub Repository](https://github.com/erikglee/HBCD_CBRAIN_PROCESSING)  
  - [ReadTheDocs Documentation](https://hbcd-cbrain-processing.readthedocs.io/latest/index.html#)

### Saving stdout/stderr Files for Failed CBRAIN Processing Tasks

**Goal of workflow:** Ensure permanent records of all CBRAIN processing logs. Since jobs are deleted a few weeks after completion, this preserves failure records.

**Relevant contacts:** Monalisa Bilas, Erik Lee         
**Frequency:** Runs daily (takes less than one hour)        
**Inputs:** CBRAIN task directories stored at `/scratch.global` (MSI)       
**Outputs:** `s3://midb-hbcd-main-deid/cbrain_std_logs/` (Files named `<CBRAIN_Task_ID>.out` and `<CBRAIN_Task_ID>.err`)

**Caveats / Notes:**  
- CBRAIN task IDs are unique—duplicates pose no issue.  
- Only failed tasks require log saving; successful ones already include `.cbrain` logs in their output directories.  

### Clean-up Routines for Out-of-sync Raw and Derived Data

**Goal of workflow:** Detect and clean up raw and derivative BIDS data when the LORIS and de-id buckets become out of sync.

**Process:**

1. Compare file counts between de-id and LORIS session folders  
2. If counts differ or `loris-versionid` mismatches:  
   - Delete all derivative files for that session  
   - Delete related CBRAIN user files and task records  
   - Delete raw BIDS data for the affected session  

**Relevant contacts:** Erik Lee, Monalisa Bilas         
**Frequency:** Runs daily (runtime varies by data volume)

**Inputs:**  
- Raw data: `s3://midb-hbcd-main-deid/assembly_bids` and `s3://midb-hbcd-main-pr/assembly_bids`  
- Derivatives: `s3://midb-hbcd-main-deid/derivatives`  
- CBRAIN records of userfiles and tasks  

**Outputs:** N/A          
**Caveats / Notes:** After cleanup, sessions with removed data are reprocessed via the de-id routines.

### Re-insertion of DCCIDs into Post-processing Derivatives (for LORIS)

**Goal of workflow:** Make de-identified derivative files available in LORIS by replacing Release Candidate IDs with DCCIDs (“re-iding”).

**Process:**

1. Check for corresponding LORIS folders for each subject/session/pipeline  
2. If LORIS folder is empty:  
   - Download de-id derivatives  
   - Replace Release Candidate IDs and anonymized site IDs with DCCIDs and real site IDs  
   - Upload to `s3://midb-hbcd-main-pr/reid_derivatives`  
   - Include metadata field `cbrain-timestamp` (from original file’s `LastModified` time)

**Relevant contacts:** Sriharshitha Anuganti, Erik Lee          
**Frequency:** Runs daily       
**Inputs:** `s3://midb-hbcd-main-deid/derivatives`      
**Outputs:** `s3://midb-hbcd-main-pr/reid_derivatives`

**Caveats / Notes:**  
- Update routines whenever pipeline filenames change.  
- See “Further Details on Re-ID Routines” for more information.  
- Older documentation referenced `VersionId`; now replaced by `LastModified` due to non-versioned de-id bucket.

### Clean-up Routines for Out-of-sync Post-processing Derivatives (LORIS)

**Goal of workflow:** Remove re-id derivatives from LORIS when they become out of sync with the de-id derivatives.

**Process:**

1. For each subject/session/pipeline:  
   - Compare `LastModified` and `cbrain-timestamp` values between  
     - `s3://midb-hbcd-main-pr/reid_derivatives`  
     - `s3://midb-hbcd-main-deid/derivatives`  
   - If mismatched, delete the corresponding re-id data from LORIS

**Relevant contacts:** Sriharshitha Anuganti, Monalisa Bilas, Erik Lee          
**Frequency:** Runs daily       
**Inputs:** `s3://midb-hbcd-main-pr/reid_derivatives` and `s3://midb-hbcd-main-deid/derivatives`        
**Outputs:** N/A        
**Caveats / Notes:** Ensures only synchronized derivatives remain in LORIS.

## Further Details on De-Id Routines

The de-identification described here covers the procedures used on s3://midb-hbcd-main-pr/assembly\_bids, which is ‘raw BIDS’ and uses DCCID’s as subject labels. During de-identification the following features are removed:

* PSCIDs  
* DCCIDs  
* Site IDs  
* Fields that commonly contain PSCIDs/DCCIDs/Site IDs, that are manually populated and therefore prone to typos

Other features that are of interest but are not removed include:

* Patient age at acquisition (available in jittered form)  
* Acquisition dates/times for different study elements  
* Acquisition device serial numbers

The de-identification procedures of raw BIDS data largely covers the following groups of files:

* Standard BIDS metadata text sources such as scans.tsv, session.tsv, JSON files  
  * In motion files, any JSON fields with PatientName or PatientBirthDate are deleted  
  * In scans/sessions tsv/json files, the site information is replaced with anonymized site IDs based on a site mapping file.  
  * All other JSON files known to contain site IDs have InstitutionAddress, InstitutionalDepartmentName, and InstitutionName deleted  
* EEG eventlogs.txt sourcedata files  
  * Custom routines anonymize entries for DataFile.Basename, DCCID, and Subject columns  
* EEG .set files  
  * Custom routines recursively search through nested fields and replaces DCCIDs/PSCIDs with Release Candidate IDs  
  * Certain fields likely to contain manually entered information such as DCCID/PSCID have their text replaced with ‘Anonymized’  
  * Other fields likely to contain manually entered information have values outside of a pre-approved list of strings replaced with ‘Anonymized’  
* MRS Nifti files:  
  * Fields InstitutionName, InstitutionAddress, PatientSex, and PatientWeight are removed from nifti headers using spec2nii

Some files are not currently supported by de-identification routines and have thus far not been copied to any of the de-identified data stores:

* Files from the EEG sourcedata directory (i.e. sub-\<label\>/ses-\<label\>/eeg/sourcedata)  
  * eventlogs.edat3 files, eeg\_flags.json files

## Further Details on Re-Id Routines

The re-identification procedures described here apply to the following derivatives pipelines:

* bibsnet  
* bme\_x  
* hbcd\_motion  
* made  
* mriqc  
* mrsqc  
* nibabies  
* osprey  
* qmri\_postproc  
* qsiprep  
* qsirecon-DIPYDKI  
* qsirecon-DSIStudio  
* qsirecon-TORTOISE\_model-MAPMRI  
* asirecon-TORTOISE\_model-tensor  
* symri  
* xcp\_d

These pipelines are present in the *s3://midb-hbcd-main-deid/derivatives* bucket, which contains de-identified data. Specifically, this bucket uses *release candidate IDs* as subject labels. At a high level, the re-identification routines replace these release candidate IDs with the corresponding *candidate IDs (DCCIDs)*.

The re-identification routines process two types of files:

1. Standard text-based files(.csv, .html, .json, .txt, .toml, .tsv, .log)  
* In these files, all occurrences of release candidate IDs are replaced with the corresponding DCCIDs.  
2. EEG .set files(with .set and .mat extensions)  
* These routines recursively search through nested fields within the file structure to identify and replace release candidate IDs with DCCIDs.

