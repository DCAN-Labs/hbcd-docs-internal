<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

# HBCD Data Processing Workflows

<div class="pill-center">
  <a href="../../#clear-objectives-and-scope" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip"><i class="fa-solid fa-bullseye" style="color: #6300d3;"></i><span class="tooltiptext">Clear objectives & scope<br><i>Click to learn more</i></span></span>
    </span>
  </a>
  <a href="../../#data-quality-checks" target="_blank" class="pill-link-wrapper">
      <span class="pill-link">
        <span class="tooltip">
          <i class="fa-solid fa-clipboard-check" style="color: #6300d3;"></i>
          <span class="tooltiptext">Data quality checks<br><i>Click to learn more</i></span>
        </span>
      </span>
  </a>
  <a href="../../#reproducibility" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip">
        <i class="fa-solid fa-code-compare" style="color: #6300d3;"></i>
        <span class="tooltiptext">Reproducibility<br><i>Click to learn more</i></span>
      </span>
    </span>
  </a>
</div>

This section outlines the full HBCD processing workflows for [tabulated data](#tabulated-data) and [file-based data](#file-based-data), detailing each step from data capture at study sites to final ingestion into Lasso. Each subsection of the workflow diagram includes the name of the responsible organization in the lower left-hand corner. Clicking on an organization name directs you to its corresponding section on the [HDCC Structure & Organizational Charts](../orgcharts.md) page, where you can find more information about that organization's role in the HBCD Study and its team members. 

<div id="fb-vs-tab" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">Tabulated vs. File-Based Data</span>
  <a class="anchor-link" href="#fb-vs-tab" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
</div>
<div class="notification-static-content">
<p>HBCD Study data includes both <strong>tabulated data</strong> and <strong>file-based data</strong> (see <a href="https://docs.hbcdstudy.org/latest/datacuration/overview/">overview of data structure</a>):</p>
<ul>
<li><strong>Tabulated data</strong> are in table format and include behavior, demographics, visit data, toxicology results, and tabulated data associated with brain imaging and other file-based data (<a href="https://docs.hbcdstudy.org/latest/datacuration/phenotypes/">see details</a>). </li>
<li><strong>File-based data</strong> are in BIDS format and include both <span><i class="fas fa-hammer"></i> <b>Raw BIDS</b></span> (<a href="https://docs.hbcdstudy.org/latest/datacuration/rawbids/">details</a>) and processed <span><i class="fas fa-cog"></i> <b>Derivatives</b></span> (<a href="https://docs.hbcdstudy.org/latest/datacuration/derivatives/">details</a>) for MRI, MRS, EEG, and motion/accelerometry. </li>
</ul>
</div>

<p>
<div id="def-terms" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Definition of Terms</span>
  <a class="anchor-link" href="#def-terms" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
    <thead>
      <tr>
        <th style="width: 10%;">Term</th>
        <th style="width: 90%;">Definition</th>
      </tr>
    </thead>
    <tbody>
        <tr>
        <td>Release Candidate ID</td>
        <td style="word-wrap: break-word; white-space: normal;">The anonymized ID that will be used as the BIDS subject label in any public releases.</td>
        </tr>
        <tr>
        <td>DCCID and/or Candidate ID</td>
        <td style="word-wrap: break-word; white-space: normal;">The original BIDS participant ID prior to de-identification (e.g. <code>sub-1234</code> where <code>1234</code> is the DCCID) in LORIS and other internal data sources.</td>
        </tr>
        <tr>
        <td>PSCID</td>
        <td style="word-wrap: break-word; white-space: normal;">An additional ID that is used in LORIS and during data collection. This ID will have begin with a five character sequence where the first two characters indicate participant status and the last three characters indicate the recruitment site.</td>
        </tr>
        <tr>
        <td>de-identification/de-id</td>
        <td style="word-wrap: break-word; white-space: normal;">The process/outputs associated with replacing DCCIDs/PSCIDs with Release Candidate IDs.</td>
        </tr>
        <tr>
        <td>re-identification/re-id</td>
        <td style="word-wrap: break-word; white-space: normal;">The process/outputs associated with replacing Release Candidate IDs with DCCIDs</td>
        </tr>
        <tr>
        <td>SCE</td>
        <td style="word-wrap: break-word; white-space: normal;">Secure computing environment at the UMN <a href="../../orgcharts/#health-sciences-technology">Health Sciences Technology</a> Office</td>
        </tr>
        <tr>
        <td>Third party</td>
        <td style="word-wrap: break-word; white-space: normal;">Refers to external organizations or companies that provide proprietary assessments, scoring tools, or data systems used to collect standardized behavioral, cognitive, and developmental data across study sites</td>
        </tr>
    </tbody>
    </table>
</div>
</p>

## Tabulated Data 

Data is collected from sites and ultimately transferred to the central LORIS Production S3 bucket, where it is subsequently de-identified and staged for ingestion into Lasso. The tabulated data processing workflow is outlined in the diagram below, showing the specific workflows for different data types and identifying the HDCC organization responsible for each processing step. These steps include data capture, de-identification, staging, and ingestion into Lasso.

<object type="image/svg+xml" data="../images/tab-proc-wf.svg" width="100%"></object>
<small><b>NOTE</b>: <i>Genetics capture currently occurs via Sampled and BAH, but will be changed to only Sampled in the future.</i></small>

<table class="compact-table">
<b><i>S3 Bucket Key</i></b>
    <thead>
      <tr>
        <th style="width: 5%;">Name</th>
        <th style="width: 15%;">S3 URL <code>s3://midb-hbcd-</code></th>
        <th style="width: 30%;">Description</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <td>LORIS Production</td>
      <td><code>main-pr/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">LORIS Bucket that receives all tabulated data prior to staging and ingestion</td>
    </tr>
    <tr>
      <td>LORIS Sandbox</td>
      <td><code>main-sb/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">LORIS Bucket for non-production system to test data flows on pilot data</td>
    </tr>
    <tr>
      <td>De-ID</td>
      <td><code>main-deid/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">De-identified raw BIDS, derivatives, and BrainSwipes data</td>
    </tr>
    <tr>
      <td>De-ID List</td>
      <td><code>main-pr-deidentification-list/</code></td>
      <td>Contains de-identified participant list information used for de-identification step.</td>
    </tr>
    <tr>
      <td>Lasso Staging</td>
      <td><code>lasso-staging/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">Where LORIS deposits data after running data release script for each BR</td>
    </tr>
    <tr>
      <td>Lasso Prerelease</td>
      <td><code>lasso-data-prerelease/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">Contains release version-specific data housed under <code>br{BETA RELEASE#}/hbcd/</code> to be ingested into Lasso</td>
    </tr>
</tbody>
</table>

##### Additional Details Linked to in Diagram:

<div id="third-party" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Third Party Tools</span>
  <a class="anchor-link" href="#third-party" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<thead>
  <th>Tool</th>
  <th>Description</th>
</thead>
<tbody>
<tr>
<td><b>ERICA</b></td>
<td style="word-wrap: break-word; white-space: normal;">Early Regulation in Context Assessment</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;"><b>CDI</b></td>
<td style="word-wrap: break-word; white-space: normal;">The <strong>MacArthur-Bates Communicative Development Inventories</strong>, a widely used tool for assessing early language</td>
</tr>
<tr>
<td><b>Bayley</b></td>
<td style="word-wrap: break-word; white-space: normal;">The <strong>Bayley Scales of Infant and Toddler Development</strong> (licensed via <strong>Pearson</strong>), used to assess cognitive, motor, and language development</td>
</tr>
<tr>
<td><b>Vineland</b></td>
<td style="word-wrap: break-word; white-space: normal;">The <strong>Vineland Adaptive Behavior Scales</strong> (licensed via <strong>Pearson</strong>), used to measure adaptive behaviors and daily functioning</td>
</tr>
<tr>
<td><b>NIH BTB</b></td>
<td style="word-wrap: break-word; white-space: normal;">NIH Baby Toolbox</td>
</tr>
<tr>
<td><b>BISQ-R</b></td>
<td style="word-wrap: break-word; white-space: normal;">The <strong>Brief Infant Sleep Questionnaire - Revised</strong>, a validated parent-report sleep instrument</td>
</tr>
</tbody>
</table>
</div>

## File-Based Data

### Site Capture, BIDS Conversion, & De-Identification

Data is collected from sites into LORIS (EEG, Axivity, and GABI) or FIONA (for MRI and MRS). LORIS data is subsequently transferred directly into the central S3 main PR bucket, which subsequently is sourced for CBRAIN processing. MRI and MRS must first be converted to BIDS format and MRI data also undergoes extensive raw data QC ([see details](https://docs.hbcdstudy.org/latest/instruments/mri/qc/#raw-mr-data-qc)).

<object type="image/svg+xml" data="../images/fb-proc-wf.svg" style="width: 100%; height: auto;">
  Your browser does not support SVG
</object>

<table class="compact-table">
<b><i>S3 Bucket Key</i></b>
    <thead>
    <thead>
      <tr>
        <th style="width: 20%;">Name</th>
        <th style="width: 40%;">S3 URL <code>s3://midb-hbcd-</code></th>
        <th style="width: 30%;">Description</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <td>JCVI DICOMs</td>
      <td><code>ucsd-main-pr-dicoms/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">JCVI DICOMs and raw data QC results</td>
    </tr>
    <tr>
      <td>MRS BIDS</td>
      <td><code>main-pr-mrs/</code></td>
      <td>MRS data post-BIDS conversion</td>
    </tr>
    <tr>
      <td>De-ID</td>
      <td><code>main-deid/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">De-identified raw BIDS, derivatives, and BrainSwipes data</td>
    </tr>
    <tr>
      <td>Main PR</td>
      <td><code>main-pr/</code></td>
      <td>Contains LORIS-curated BIDS data for the full HBCD study, including:<br>
       • De-identfied: <span class="tooltip">raw BIDS<span class="tooltiptext"><i>assembly_bids/</i></span></span> and <span class="tooltip">participant lists<span class="tooltiptext"><i>deidentification-lists/</i></span></span><br>
       • Re-identfied: <span class="tooltip">derivatives<span class="tooltiptext"><i>derivatives/</i></span></span> and <span class="tooltip">BrainSwipes data<span class="tooltiptext"><i>reid_brainswipes/</i></span></span>
      </td>
    </tr>
    <tr>
      <td>De-ID List</td>
      <td><code>main-pr-deidentification-list/</code></td>
      <td>Contains de-identified participant list information used for de-identification step.</td>
    </tr>
</tbody>
</table>

### CBRAIN Processing, Re-Identification, & Lasso Ingestion

Processing pipelines are run in CBRAIN and outputs are stored in session-specific folders on `s3://midb-hbcd-main-deid/derivatives`. When processing is launched, a record of which files were used for processing is stored under `s3://midb-hbcd-main-deid/derivatives/ses-<label>/cbrain_misc`. In the future, this will likely be replaced with a simple database in the S3 bucket that keeps track of these (and other) details more centrally.

<object type="image/svg+xml" data="../images/fb-wf-part2.svg" style="width: 100%; height: auto;">
  Your browser does not support SVG
</object>
<small><b>NOTE</b>: <i>Currently, for release staging, the data is first copied to a separate staging bucket prior to being copied to the Lasso Prerelease bucket, but will soon be cut out to transfer directly to the Lasso Prerelease bucket as displayed in the diagram.</i></small>

<div id="og-wf-fb" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Original WF Diagram</span>
  <a class="anchor-link" href="#og-wf-fb" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<i>Note: Select <span class="blue-text">ⓘ <i>Click for Details</i></span> for a given step to be linked to the relevant section on this page with additional details.</i>
<object type="image/svg+xml" data="../images/fb-proc-wf2.svg" width="100%"></object>
</div>

<table class="compact-table">
<b><i>S3 Bucket Key</i></b>
    <thead>
    <thead>
      <tr>
        <th style="width: 20%;">Name</th>
        <th style="width: 40%;">S3 URL <code>s3://midb-hbcd-</code></th>
        <th style="width: 30%;">Description</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <td>De-ID</td>
      <td><code>main-deid/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">De-identified raw BIDS, derivatives, and BrainSwipes data</td>
    </tr>
    <tr>
      <td>Main PR</td>
      <td><code>main-pr/</code></td>
      <td>Contains LORIS-curated BIDS data for the full HBCD study, including:<br>
       • De-identfied: <span class="tooltip">raw BIDS<span class="tooltiptext"><i>assembly_bids/</i></span></span> and <span class="tooltip">participant lists<span class="tooltiptext"><i>deidentification-lists/</i></span></span><br>
       • Re-identfied: <span class="tooltip">derivatives<span class="tooltiptext"><i>derivatives/</i></span></span> and <span class="tooltip">BrainSwipes data<span class="tooltiptext"><i>reid_brainswipes/</i></span></span>
      </td>
    </tr>
    <tr>
      <td>Lasso Prerelease</td>
      <td><code>lasso-data-prerelease/br{BETA RELEASE#}/hbcd/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">Contains release version-specific data, including participant list to be included in the release (<code>rawdata/participants.tsv</code>). This is the final repository after de-identification and prior to Lasso ingestion.</td>
    </tr>
</tbody>
</table>

##### Additional Details Linked to in Diagram:

<div id="record-query" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Record Query Details</span>
  <a class="anchor-link" href="#record-query" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>After CBRAIN processing, previous processing records are queried against the contents of s3://midb-hbcd-main-deid/assembly_bids to ensure that processing is still up-to-date with the current BIDS data. For any cases where the derivative data has become out of sync with the assembly_bids data, the impacted derivative data along with CBRAIN processing task objects are deleted. The next time the query scripts are run that look for new subjects to process, the processing will be re-initiated for these subjects.</p>
</div>

<div id="copy-to-release" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Copying Release Data to Prerelease Bucket</span>
  <a class="anchor-link" href="#copy-to-release" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>The details of this process are as follows:</p>
<ol>
<li>Find release-ready subject/sessions (i.e. participants listed in the LORIS <code>par_visit_data</code> file) in <code>s3://midb-hbcd-main-deid/</code></li>
<li>Edit <code>assembly_bids/</code> structure like so:<ul>
<li>Remove low-QC images/files that were not used for attempted processing</li>
<li>Reconstruct <code>scans.tsv</code> files to only include entries for files included in the release</li>
<li>Reconstruct <code>sessions.tsv</code> files to only include sessions from the release</li>
</ul>
</li>
<li>Squash the derivatives folders across imaging sessions so that there is one common derivatives folder for all imaging sessions</li>
<li>Copy the resulting assembly_bids and derivatives data to <code>rawdata/</code> and <code>derivatives/</code>, respectively, under:<br><code>s3://midb-hbcd-lasso-data-release-staging/&lt;release_identifier&gt;/hbcd/</code> </li>
</ol>
</div>

<div id="brainswipes" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">BrainSwipes</span>
  <a class="anchor-link" href="#brainswipes" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>The workflow for BrainSwipes is unique compared to other data due to the fact that the quality control (QC) is performed post-CBRAIN processing and therefore must go through additional steps. Some details to note:</p>
<ul>
<li>After transfer of the visual reports used for QC to the Prerelease Derivatives S3 URL (<code>s3://midb-hbcd-prerelease-bids/derivatives/ses-V02/xcp_d/{{SUBJECT}}/figures/{{FILENAME}}.png</code>), a query is run to identify outputs that are out of date and either remove or archive records related to out-of-date files</li>
<li><strong>TBD</strong>: Participant sessions that fail structural QC (based on XCP-D derivative visual reports) are flagged to perform manual corrections on the corresponding BIBSNet brain segmentations. The corrected segmentations will not be fed back into the main processing workflows, but are instead integrated into the training set for future BIBSNet models.</li>
</ul>
</div>

<div id="re-id" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Re-Identification</span>
  <a class="anchor-link" href="#re-id" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>Following CBRAIN processing, processing records are queried for new derivative outputs ready to be re-identified. Re-identification involves replacing all release candidate IDs with DCCIDs in processing outputs and occurs in the process of copying the data from the source (<code>s3://midb-hbcd-main-deid/derivatives/</code>) to destination (<code>s3://midb-hbcd-main-pr/derivatives</code>) S3 paths.</p>
<p>Duplicating the derivatives enables LORIS to (1) maintain QC dashboards for HBCD users based on processing outputs (primarily important for EEG) and (2) prepare tabulated summary outputs for Lasso ingestion.</p>
<p>Prior to re-identification, <code>s3://midb-hbcd-main-pr/derivatives</code> is first queried to find and delete any data that either does not have associated files in <code>s3://midb-hbcd-main-deid/derivatives</code>. When there is a newer copy of derivative data available from the source bucket, these are deleted and repopulated. Finally, new derivative data that has never existed in the LORIS bucket is copied over.</p>
</div>

<div id="loris-ingestion" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">LORIS Ingestion of Re-Identified Derivatives</span>
  <a class="anchor-link" href="#loris-ingestion" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>LORIS updates their database from <code>s3://midb-hbcd-main-pr/derivatives</code> by:</p>
<ol>
<li>Removing any database entries related to derivative outputs that no longer exist</li>
<li>Looking for cases where there are newer derivative outputs than what exists in LORIS records and replacing the old records with the new data</li>
<li>Adding in records for any new subjects/sessions</li>
</ol>
</div>

## Clinical Data Validation Procedure

<div class="pill-center">
  <a href="../../#data-quality-checks" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip">
        <i class="fa-solid fa-clipboard-check" style="color: #6300d3;"></i>
        <span class="tooltiptext">Data quality checks<br><i>Click to learn more</i></span>
      </span>
    </span>
  </a>
  <a href="../../#project-management" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip">
        <i class="fa-solid fa-diagram-project" style="color: #6300d3;"></i>
        <span class="tooltiptext">Project Management<br><i>Click to learn more</i></span>
      </span>
    </span>
  </a>
  <a href="../../#reproducibility" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip">
        <i class="fa-solid fa-code-compare" style="color: #6300d3;"></i>
        <span class="tooltiptext">Reproducibility<br><i>Click to learn more</i></span>
      </span>
    </span>
  </a>
</div>
<p></p>

*Validation procedures for Electronic Health Records (EHR) data are performed as follows:*

<img src="../images/EHR-wf.png">

1. Load EHR data from the site into the Landing Zone within the Secure Computing Environment  
2. Run a script to validate that the Landing Zone data was loaded correctly that checks for the following issues and coordinate with the site to correct these issues:  
    - Dates only sent when expecting date / time  
    - Time only sent when expecting date / time  
    - Date / time format was unknown to import script so it was imported as a varchar (requires changes to import script)  
    - Headers not sent so the column names are based on the first row of the data  
    - Rows are all NULL values because the file had rows with no data  
3. Run the Landing Zone to OMOP mapping scripts for each site  
    - Correct any known site-specific issues that can be automatically corrected in the scripts  
    - Let the site know of any issues with their data preventing mapping of their data  
    - Move data that passes QA into the central HBCD Clinical Data Repository (versioned for each year)  
4. Generate two reports back to each site  
    [1] EHR data received by participant study ID  
    [2] Summary Table 1 for the site


<div id="table1" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Example Table 1 Summary (Birth Parent)</span>
  <a class="anchor-link" href="#table1" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
    <thead>
      <tr>
        <th style="width: 5%;">Characteristic</th>
        <th style="width: 5%;">Total</th>
      </tr>
    </thead>
    <tbody>
      <tr>
      <td><b>N</b></td>
      <td>870</td>
      </tr>
      <tr>
      <td><b>Demographics</b></td>
      <td>&nbsp;</td>
      </tr>
      <tr>
      <td>Mean age (&plusmn; SD)</td>
      <td>31.69 (5.69)</td>
      </tr>
      <tr>
      <td>Sex|FEMALE</td>
      <td>870 (100.0)</td>
      </tr>
      <tr>
      <td>Sex|MALE</td>
      <td>0 (0.0)</td>
      </tr>
      <tr>
      <td>Sex|No matching concept</td>
      <td>0 (0.0)</td>
      </tr>
      <tr>
      <td>Race|American Indian or Alaska Native</td>
      <td>10 (1.1)</td>
      </tr>
      <tr>
      <td>Race|Asian</td>
      <td>39 (4.5)</td>
      </tr>
      <tr>
      <td>Race|Black or African American</td>
      <td>197 (22.6)</td>
      </tr>
      <tr>
      <td>Race|Native Hawaiian or Other Pacific Islander</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Race|No matching concept</td>
      <td>105 (12.1)</td>
      </tr>
      <tr>
      <td>Race|White</td>
      <td>517 (59.4)</td>
      </tr>
      <tr>
      <td>Ethnicity|Hispanic or Latino</td>
      <td>122 (14.0)</td>
      </tr>
      <tr>
      <td>Ethnicity|Not Hispanic or Latino</td>
      <td>748 (86.0)</td>
      </tr>
      <tr>
      <td>Ethnicity|No Matching Concept</td>
      <td>0 (0.0)</td>
      </tr>
      <tr>
      <td><b>Conditions</b></td>
      <td>&nbsp;</td>
      </tr>
      <tr>
      <td>Major depression, single episode</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Second trimester pregnancy</td>
      <td>127 (14.6)</td>
      </tr>
      <tr>
      <td>Third trimester pregnancy</td>
      <td>117 (13.4)</td>
      </tr>
      <tr>
      <td>First trimester pregnancy</td>
      <td>88 (10.1)</td>
      </tr>
      <tr>
      <td>Disorder of pregnancy</td>
      <td>87 (10.0)</td>
      </tr>
      <tr>
      <td>Complication occurring during pregnancy</td>
      <td>66 (7.6)</td>
      </tr>
      <tr>
      <td>Anxiety disorder</td>
      <td>66 (7.6)</td>
      </tr>
      <tr>
      <td>Depressive disorder</td>
      <td>64 (7.4)</td>
      </tr>
      <tr>
      <td>Fetal condition affecting obstetrical care of mother</td>
      <td>52 (6.0)</td>
      </tr>
      <tr>
      <td>Gestation period, 36 weeks</td>
      <td>50 (5.7)</td>
      </tr>
      <tr>
      <td>Anemia of pregnancy</td>
      <td>47 (5.4)</td>
      </tr>
      <tr>
      <td>Mental disorders during pregnancy, childbirth and the puerperium</td>
      <td>46 (5.3)</td>
      </tr>
      <tr>
      <td>Finding related to pregnancy</td>
      <td>34 (3.9)</td>
      </tr>
      <tr>
      <td>Uncomplicated asthma</td>
      <td>28 (3.2)</td>
      </tr>
      <tr>
      <td>Disease of the respiratory system complicating pregnancy, childbirth and/or the puerperium</td>
      <td>28 (3.2)</td>
      </tr>
      <tr>
      <td>Poor fetal growth affecting management</td>
      <td>27 (3.1)</td>
      </tr>
      <tr>
      <td>Maternal obesity complicating pregnancy, childbirth and the puerperium, antepartum</td>
      <td>24 (2.8)</td>
      </tr>
      <tr>
      <td>Generalized anxiety disorder</td>
      <td>18 (2.1)</td>
      </tr>
      <tr>
      <td>Posttraumatic stress disorder</td>
      <td>14 (1.6)</td>
      </tr>
      <tr>
      <td>High risk pregnancy</td>
      <td>11 (1.3)</td>
      </tr>
      <tr>
      <td><b>Lab Results</b></td>
      <td>&nbsp;</td>
      </tr>
      <tr>
      <td>Body temperature (degree Celsius)</td>
      <td>36.69 (0.18)</td>
      </tr>
      <tr>
      <td>Systolic blood pressure (millimeter mercury column)</td>
      <td>119.48 (9.42)</td>
      </tr>
      <tr>
      <td>Diastolic blood pressure (millimeter mercury column)</td>
      <td>72.49 (5.62)</td>
      </tr>
      <tr>
      <td>Heart rate (counts per minute)</td>
      <td>91.58 (8.91)</td>
      </tr>
      <tr>
      <td>No matching concept (nanogram per milliliter)</td>
      <td>358.33 (1243.37)</td>
      </tr>
      <tr>
      <td>Pain severity - 0-10 verbal numeric rating [Score] - Reported</td>
      <td>1.77 (1.01)</td>
      </tr>
      <tr>
      <td>Hematocrit [Volume Fraction] of Blood by Automated count (percent)</td>
      <td>34.81 (3.19)</td>
      </tr>
      <tr>
      <td>MCV [Entitic volume] by Automated count (femtoliter)</td>
      <td>88.14 (6.84)</td>
      </tr>
      <tr>
      <td>MCH [Entitic mass] by Automated count (picogram)</td>
      <td>29.53 (2.52)</td>
      </tr>
      <tr>
      <td>Erythrocyte distribution width [Ratio] by Automated count (percent)</td>
      <td>13.65 (1.58)</td>
      </tr>
      <tr>
      <td>Respiratory rate (counts per minute)</td>
      <td>17.35 (0.54)</td>
      </tr>
      <tr>
      <td>Platelet mean volume [Entitic volume] in Blood by Automated count (femtoliter)</td>
      <td>10.52 (1.09)</td>
      </tr>
      <tr>
      <td>Body temperature (degree Fahrenheit)</td>
      <td>97.87 (0.26)</td>
      </tr>
      <tr>
      <td>Erythrocyte distribution width [Entitic volume] by Automated count (femtoliter)</td>
      <td>43.61 (8.49)</td>
      </tr>
      <tr>
      <td>No matching concept (milligram per deciliter)</td>
      <td>98.85 (122.08)</td>
      </tr>
      <tr>
      <td>Hemoglobin [Mass/volume] in Blood (gram per deciliter)</td>
      <td>11.64 (1.14)</td>
      </tr>
      <tr>
      <td>Oxygen saturation in Arterial blood by Pulse oximetry (percent)</td>
      <td>97.99 (1.05)</td>
      </tr>
      <tr>
      <td>Body weight (kilogram)</td>
      <td>83.74 (25.21)</td>
      </tr>
      <tr>
      <td>Body height (centimeter)</td>
      <td>163.48 (6.62)</td>
      </tr>
      <tr>
      <td><b>Procedures</b></td>
      <td>&nbsp;</td>
      </tr>
      <tr>
      <td>Ultrasound scan for fetal growth</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Antenatal screening</td>
      <td>12 (1.4)</td>
      </tr>
      <tr>
      <td>Monitoring of Products of Conception, Cardiac Rate, External Approach</td>
      <td>10 (1.1)</td>
      </tr>
      <tr>
      <td>Fetal biophysical profile</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Ultrasonography for antepartum monitoring of fetus</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Ultrasound scan - obstetric</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Ultrasound scan for fetal nuchal translucency</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Ultrasonography in first trimester</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Delivery of Products of Conception, External Approach</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Ultrasonography of Third Trimester, Single Fetus</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>X-ray of chest anteroposterior view</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Extraction of Products of Conception, Low, Open Approach</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Drainage of Amniotic Fluid, Therapeutic from Products of Conception, Via Natural or Artificial Opening</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Ultrasonography of Second Trimester, Single Fetus</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Diagnostic radiography of chest, combined PA and lateral</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Counseling</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Ultrasonography of cervix uteri</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Insertion of Other Device into Products of Conception, Via Natural or Artificial Opening</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td>Repair Perineum Muscle, Open Approach</td>
      <td>&lt; 10</td>
      </tr>
      <tr>
      <td><b>Medications</b></td>
      <td>&nbsp;</td>
      </tr>
      <tr>
      <td>sodium chloride</td>
      <td>142 (16.3)</td>
      </tr>
      <tr>
      <td>ibuprofen</td>
      <td>132 (15.2)</td>
      </tr>
      <tr>
      <td>potassium chloride</td>
      <td>125 (14.4)</td>
      </tr>
      <tr>
      <td>calcium chloride</td>
      <td>124 (14.3)</td>
      </tr>
      <tr>
      <td>lactate</td>
      <td>124 (14.3)</td>
      </tr>
      <tr>
      <td>acetaminophen</td>
      <td>85 (9.8)</td>
      </tr>
      <tr>
      <td>ondansetron</td>
      <td>79 (9.1)</td>
      </tr>
      <tr>
      <td>sennosides, USP</td>
      <td>63 (7.2)</td>
      </tr>
      <tr>
      <td>oxycodone</td>
      <td>62 (7.1)</td>
      </tr>
      <tr>
      <td>folic acid</td>
      <td>60 (6.9)</td>
      </tr>
      <tr>
      <td>docusate</td>
      <td>57 (6.6)</td>
      </tr>
      <tr>
      <td>ketorolac</td>
      <td>54 (6.2)</td>
      </tr>
      <tr>
      <td>glucose</td>
      <td>53 (6.1)</td>
      </tr>
      <tr>
      <td>oxytocin</td>
      <td>47 (5.4)</td>
      </tr>
      <tr>
      <td>famotidine</td>
      <td>45 (5.2)</td>
      </tr>
      <tr>
      <td>simethicone</td>
      <td>43 (4.9)</td>
      </tr>
      <tr>
      <td>gabapentin</td>
      <td>25 (2.9)</td>
      </tr>
      <tr>
      <td>buprenorphine</td>
      <td>11 (1.3)</td>
      </tr>
</tbody>
</table>
</div>

<br>
