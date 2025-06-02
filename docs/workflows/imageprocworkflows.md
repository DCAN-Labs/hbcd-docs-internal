# Image Processing Workflows
<p>
    Below is the full image processing workflow for the HBCD data processing, including data capture from HBCD study sites, quality control, BIDS conversion, LORIS ingestion, de- and re-identification procedures at various stages, CBRAIN processing, and lastly Lasso ingestion. Further details for certain steps are provided in the sections below (as indicated by the note <span class="blue-text">ⓘ <i>Click for Details</i>).</span>
</p>

The organization responsible for each step is indicated in the lower left-hand corner of each box. Click on the organization name to be directed to its correponding section on the [Org Charts](../orgcharts.md) page for more information about the organization, team members, and its role in the HBCD Study.

### *TO DO*
- Add in MRS QC: performed by UCSD (does UCSD source from UMN post-BIDS conversion?) is it sent to loris separate from QC?
- Add: what is automated and what is not
- Add missing s3 bucket names and server names: CDNI BrainSwipes Bucket
- Clarify final de-ID steps

<object type="image/svg+xml" data="../WF.svg" width="100%"></object>

<p>
<div id="s3-paths" class="table-banner" onclick="toggleCollapse(this)">
  <span class="table-text">S3 Bucket Paths Key</span>
  <span class="notification-arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
    <thead>
      <tr>
        <th style="width: 25%;">S3 Location Short Name Used in Diagram</th>
        <th style="width: 75%;">S3 URL</th>
      </tr>
    </thead>
    <tbody>
        <tr>
        <td>BrainSwipes</td>
        <td><code> </code></td>
        </tr>
        <tr>
        <td>De-ID &gt; BrainSwipes</td>
        <td><code>s3://midb-hbcd-main-deid/brainswipes</code></td>
        </tr>
        <tr>
        <td>De-ID &gt; Derivatives</td>
        <td><code>s3://midb-hbcd-main-deid/derivatives/</code></td>
        </tr>
        <tr>
        <td>De-ID &gt; Raw BIDS</td>
        <td><code>s3://midb-hbcd-main-deid/assembly_bids/</code></td>
        </tr>
        <tr>
        <td>Lasso Staging</td>
        <td><code>s3://midb-hbcd-lasso-staging/</code></td>
        </tr>
        <tr>
        <td>Lasso Release</td>
        <td><code>s3://midb-hbcd-lasso-release/</code></td>
        </tr>
        <tr>
        <td>Main &gt; BrainSwipes</td>
        <td><code>s3://midb-hbcd-main-pr/reid_brainswipes/</code></td>
        </tr>
        <tr>
        <td>Main &gt; Derivatives</td>
        <td><code>s3://midb-hbcd-main-pr/derivatives/</code></td>
        </tr>
        <tr>
        <td>Main &gt; De-ID Lists</td>
        <td><code>s3://midb-hbcd-main-pr/deidentification-lists/</code></td>
        </tr>
        <tr>
        <td>Main &gt; Raw BIDS</td>
        <td><code>s3://midb-hbcd-main-pr/assembly_bids/</code></td>
        </tr>
        <tr>
        <td>UCSD DICOMs</td>
        <td><code>s3://midb-hbcd-ucsd-main-pr-dicoms/</code></td>
        </tr>
    </tbody>
    </table>
</div>
</p>

## De-Identification
De-identification is run daily to update `s3://midb-hbcd-main-deid/assembly_bids` from `s3://midb-hbcd-main-pr/assembly_bids`. In the process of de-identification, any DCCIDs/PSCIDs/Site IDs are removed or replaced with Release Candidate IDs and/or Anonymized Site IDs, where applicable. In addition to de-identifying new sessions, existing sessions are also updated.

## CBRAIN Processing
Processing pipelines are run in CBRAIN and outputs are stored in session-specific folders on `s3://midb-hbcd-main-deid/derivatives`. When processing is launched, a record of which files were used for processing is stored under `s3://midb-hbcd-main-deid/derivatives/ses-<label>/cbrain_misc`. In the future, this will likely be replaced with a simple database in the S3 bucket that keeps track of these (and other) details more centrally.

### Record Query & Derivatives Cleanup
After CBRAIN processing, previous processing records are queried against the contents of `s3://midb-hbcd-main-deid/assembly_bids` to ensure that processing is still up-to-date with the current BIDS data. For any cases where the derivative data has become out of sync with the assembly_bids data, the impacted derivative data along with CBRAIN processing task objects are deleted. The next time the query scripts are run that look for new subjects to process, the processing will be re-initiated for these subjects.

## Re-Identification
Following CBRAIN processing, processing records are queried for new derivative outputs ready to be re-identified. Re-identification involves replacing all release candidate IDs with DCCIDs in processing outputs and occurs in the process of copying the data from the source (`s3://midb-hbcd-main-deid/derivatives/`) to destination (`s3://midb-hbcd-main-pr/derivatives`) S3 paths.

Duplicating the derivatives enables LORIS to (1) maintain QC dashboards for HBCD users based on processing outputs (primarily important for EEG) and (2) prepare tabulated summary outputs for Lasso ingestion.

Prior to re-identification, `s3://midb-hbcd-main-pr/derivatives` is first queried to find and delete any data that either does not have associated files in `s3://midb-hbcd-main-deid/derivatives`. When there is a newer copy of derivative data available from the source bucket, these are deleted and repopulated. Finally, new derivative data that has never existed in the LORIS bucket is copied over.

### LORIS Ingestion of Re-Identified Derivatives
LORIS updates their database from `s3://midb-hbcd-main-pr/derivatives` by:

1. Removing any database entries related to derivative outputs that no longer exist
2. Looking for cases where there are newer derivative outputs than what exists in LORIS records and replacing the old records with the new data
3. Adding in records for any new subjects/sessions

## Copying Release Data to Staging Bucket
The details of this process are as follows:

1. Find release-ready subject/sessions
2. Edit assembly_bids structure like so:
    - Remove low-QC images/files that were not used for attempted processing
    - Reconstruct `scans.tsv` files to only include entries for files included in the release
    - Reconstruct `sessions.tsv` files to only include sessions from the release
3. Squash the derivatives folders across imaging sessions so that there is one common derivatives folder for all imaging sessions
4. Place the resulting assembly_bids data in `s3://midb-hbcd-lasso-staging/<release_identifier>/hbcd/rawdata/`
5. Place the resulting derivatives data in `s3://midb-hbcd-lasso-staging/<release_identifier>/hbcd/derivatives`