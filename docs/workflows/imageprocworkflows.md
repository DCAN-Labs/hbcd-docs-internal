# Image Processing Workflows

<object type="image/svg+xml" data="../WF.drawio.svg" width="100%"></object>

## TO DO
Add in MRS QC: performed by UCSD (does UCSD source from UMN post-BIDS conversion?) is it sent to loris separate from QC?

## De-Identification
De-identification is run daily to update `s3://midb-hbcd-main-deid/assembly_bids` from `s3://midb-hbcd-main-pr/assembly_bids`. In the process of de-identification, any DCCIDs/PSCIDs/Site IDs are removed or replaced with Release Candidate IDs and/or Anonymized Site IDs, where applicable. In addition to de-identifying new sessions, existing sessions are also updated.

## CBRAIN Processing
Processing pipelines are run in CBRAIN and outputs are stored in session-specific folders on `s3://midb-hbcd-main-deid/derivatives`. When processing is launched, a record of which files were used for processing is stored under `s3://midb-hbcd-main-deid/derivatives/ses-<label>/cbrain_misc`. In the future, this will likely be replaced with a simple database in the S3 bucket that keeps track of these (and other) details more centrally.

## Re-Identification

Following CBRAIN processing, processing records are queried for new derivative outputs ready to be re-identified. Re-identification involves replacing all release candidate IDs with DCCIDs in processing outputs and occurs in the process of copying the data from the source (`s3://midb-hbcd-main-deid/derivatives/`) to destination (`s3://midb-hbcd-main-pr/derivatives`) S3 paths.

Duplicating the derivatives enables LORIS to (1) maintain QC dashboards for HBCD users based on processing outputs (primarily important for EEG) and (2) prepare tabulated summary outputs for Lasso ingestion.

Prior to re-identification, `s3://midb-hbcd-main-pr/derivatives` is first queried to find and delete any data that either does not have associated files in `s3://midb-hbcd-main-deid/derivatives`. When there is a newer copy of derivative data available from the source bucket, these are deleted and repopulated. Finally, new derivative data that has never existed in the LORIS bucket is copied over.

### LORIS Ingestion Post- Re-Identification
LORIS updates their databased using `s3://midb-hbcd-main-pr/derivatives` by:

1. Removing any database entries related to derivative outputs that no longer exist
2. Looking for cases where there are newer derivative outputs than what exists in LORIS records and replacing the old records with the new data
3. Adding in records for any new subjects/sessions

## Potentially Add Post-CBRAIN Procesing: 

Erik queries previous processing records and `s3://midb-hbcd-main-deid/assembly_bids` to check if processing is still up to date with the current BIDS data

For any cases where the derivative data has become out of sync with the assembly_bids data - (1) impacted derivative data is deleted, (2) impacted CBRAIN processing task objects are deleted

Following these deletions, the next time Erik's scripts look for new subjects to process, the processing will be re-initiated

## Copying Data to Release Staging Bucket
This involves (1) finding release ready subject/sessions, (2) making edits to the assembly_bids structure such as (a) removing low-QC images/files that were not used for attempted processing, (b) reconstructing the scans.tsv file to only have rows for files that are included in the release, (c) reconstructing the sessions.tsv file to only include sessions from the release, (3) squashing the derivatives folders across imaging sessions so that there is one common derivatives folder for all imaging sessions, (4) placing the resulting assembly_bids data at s`3://midb-hbcd-lasso-staging/<release_identifier>/hbcd/rawdata/`, (5) placing the resulting derivatives data at `s3://midb-hbcd-lasso-staging/<release_identifier>/hbcd/derivatives`