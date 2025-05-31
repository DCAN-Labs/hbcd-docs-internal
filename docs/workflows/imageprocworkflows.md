# Image Processing Workflows

<object type="image/svg+xml" data="../procWF.drawio.svg" width="100%" height="600px"></object>



### with tooltip

<object type="image/svg+xml" data="../procWF_tooltip.drawio.svg" width="100%" height="600px"></object>

### test
<object type="image/svg+xml" data="../test.drawio.svg" width="100%" height="600px"></object>




### S3 Bucket Definitions
**S3DEID**: `s3://midb-hbcd-main-deid` - S3 Bucket with de-identified data 

### De-Identification Details

De-identification is run daily to update `s3://midb-hbcd-main-deid/assembly_bids` from `s3://midb-hbcd-main-pr/assembly_bids`. In the process of de-identification, any DCCIDs/PSCIDs/Site IDs are removed or replaced with Release Candidate IDs and/or Anonymized Site IDs, where applicable. In addition to de-identifying new sessions, existing sessions are also updated.

### CBRAIN Processing

Processing pipelines are run in CBRAIN and outputs are stored in session-specific folders on `s3://midb-hbcd-main-deid/derivatives`. When processing is launched, a record of which files were used for processing is stored under `s3://midb-hbcd-main-deid/derivatives/ses-<label>/cbrain_misc`. In the future, this will likely be replaced with a simple database in the S3 bucket that keeps track of these (and other) details more centrally.

### Re-Identification Details

Following CBRAIN processing, processing records are queried for new derivative outputs ready to be re-identified. Re-identificated replaces instances of release candidate ID's in processing outputs with DCCIDs. The `s3://midb-hbcd-main-deid/derivatives` folder is copied to `s3://midb-hbcd-main-pr/derivatives` and re-identified in the process of duplication. 

The purpose of this new copy of the data is for LORIS to be able to (1) maintain QC dashboards for HBCD users based on processing outputs (mostly important for EEG) and (2) prepare tabulated summary outputs that will eventually get sent to LASSO.

Prior to performing re-identification, `s3://midb-hbcd-main-pr/derivatives` is first queried to find and delete any data that does not have associated files in `s3://midb-hbcd-main-deid/derivatives`. When there is a newer copy of derivative data available, delete and repopulate any data in `s3://midb-hbcd-main-pr/derivatives`. Finally, new derivative data that has never existed in the LORIS bucket is copied over.

#### LORIS Ingestion Post- Re-Identification
LORIS updates their databased using `s3://midb-hbcd-main-pr/derivatives` by:

1. Removing any database entries related to derivative outputs that no longer exist
2. Looking for cases where there are newer derivative outputs than what exists in LORIS records and replacing the old records with the new data
3. Adding in records for any new subjects/sessions

### Potentially Add Post-CBRAIN Procesing: 

Erik queries previous processing records and `s3://midb-hbcd-main-deid/assembly_bids` to check if processing is still up to date with the current BIDS data

For any cases where the derivative data has become out of sync with the assembly_bids data - (1) impacted derivative data is deleted, (2) impacted CBRAIN processing task objects are deleted

Following these deletions, the next time Erik's scripts look for new subjects to process, the processing will be re-initiated

### Copying Data to Release Staging Bucket
This involves (1) finding release ready subject/sessions, (2) making edits to the assembly_bids structure such as (a) removing low-QC images/files that were not used for attempted processing, (b) reconstructing the scans.tsv file to only have rows for files that are included in the release, (c) reconstructing the sessions.tsv file to only include sessions from the release, (3) squashing the derivatives folders across imaging sessions so that there is one common derivatives folder for all imaging sessions, (4) placing the resulting assembly_bids data at s`3://midb-hbcd-lasso-staging/<release_identifier>/hbcd/rawdata/`, (5) placing the resulting derivatives data at `s3://midb-hbcd-lasso-staging/<release_identifier>/hbcd/derivatives`