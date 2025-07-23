# HBCD Data Processing Workflows

<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

This section outlines the full HBCD processing workflows for [tabulated data](#tabulated-data) and [file-based data](#file-based-data), detailing each step from data capture at study sites to final ingestion into Lasso. Each subsection of the workflow diagram includes the name of the responsible organization in the lower left-hand corner. Clicking on an organization name directs you to its corresponding section on the [Org Charts](../orgcharts.md) page, where you can find more information about that organization's role in the HBCD Study and its team members. 


<div id="og-wf-fb" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">
    Tabulated vs. File-Based Data
  </span>
  <a class="anchor-link" href="#og-wf-fb" title="Copy link">
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
        <td>DCCID/PSCID</td>
        <td style="word-wrap: break-word; white-space: normal;">These participant IDs are primarily used by LORIS and study sites, with PSCID being more commonly used by sites during the data collection and debugging process. The DCCID specifically is the original BIDS participant ID prior to de-identification (e.g. <code>sub-1234</code> where <code>1234</code> is the DCCID).</td>
        </tr>
        <tr>
        <td>SCE</td>
        <td style="word-wrap: break-word; white-space: normal;">Secure computing environment at the UMN <a href="../../orgcharts/#health-sciences-technology">Health Sciences Technology</a> Office</td>
        </tr>
    </tbody>
    </table>
</div>
</p>

## Tabulated Data 

<object type="image/svg+xml" data="../images/tab-proc-wf.svg" width="100%"></object>
<small><b>NOTE</b>: <i>Genetics capture currently occurs via Sampled and BAH, but will be changed to only Sampled in the future.</i></small>

<div id="og-wf-tab" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Original WF Diagram</span>
  <a class="anchor-link" href="#og-wf-tab" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<object type="image/svg+xml" data="../images/tabulated-proc-WF.svg" width="100%"></object>
<span class="blue-text"><b>**</b></span> <span><i>Third party includes: ERICA, CDI, Bayley, Vineland, NIH BTB, and BISQR.</i></span>
</div>

<table class="compact-table">
<b><i>S3 Bucket Key</i></b>
    <thead>
      <tr>
        <th style="width: 5%;">Name</th>
        <th style="width: 10%;">S3 URL</th>
        <th style="width: 30%;">Description</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <td>LORIS Production</td>
      <td><code>????</code></td>
      <td style="word-wrap: break-word; white-space: normal;">LORIS Bucket that receives all tabulated data prior to staging and ingestion</td>
    </tr>
    <tr>
      <td>Lasso Staging</td>
      <td><code>s3://midb-hbcd-lasso-staging/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">Where LORIS deposits data after running data release script for each BR</td>
    </tr>
    <tr>
      <td>Lasso Prerelease</td>
      <td><code>s3://midb-hbcd-lasso-data-prerelease/</code></td>
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

<object type="image/svg+xml" data="../images/fb-wf.svg" style="width: 100%; height: auto;">
  Your browser does not support SVG
</object>

<table class="compact-table">
<b><i>S3 Bucket Key</i></b>
    <thead>
    <thead>
      <tr>
        <th style="width: 20%;">Name</th>
        <th style="width: 40%;">S3 URL</th>
        <th style="width: 30%;">Description</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <td>JCVI DICOMs</td>
      <td><code>s3://midb-hbcd-ucsd-main-pr-dicoms/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">JCVI DICOMs and raw data QC results</td>
    </tr>
    <tr>
      <td>MRS BIDS</td>
      <td><code>s3://midb-hbcd-main-pr-mrs/</code></td>
      <td>MRS data post-BIDS conversion</td>
    </tr>
    <tr>
      <td>De-ID</td>
      <td><code>s3://midb-hbcd-main-deid/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">De-identified raw BIDS, derivatives, and BrainSwipes data</td>
    </tr>
    <tr>
      <td>Main PR</td>
      <td><code>s3://midb-hbcd-main-pr/</code></td>
      <td>Contains LORIS-curated BIDS data for the full HBCD study, including:<br>
       • De-identfied: <span class="tooltip">raw BIDS<span class="tooltiptext"><i>assembly_bids/</i></span></span> and <span class="tooltip">participant lists<span class="tooltiptext"><i>deidentification-lists/</i></span></span><br>
       • Re-identfied: <span class="tooltip">derivatives<span class="tooltiptext"><i>derivatives/</i></span></span> and <span class="tooltip">BrainSwipes data<span class="tooltiptext"><i>reid_brainswipes/</i></span></span>
      </td>
    </tr>
    <tr>
      <td>De-ID Lists</td>
      <td><code>s3://midb-hbcd-main-pr-deidentification-list</code></td>
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
        <th style="width: 40%;">S3 URL</th>
        <th style="width: 30%;">Description</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <td>De-ID</td>
      <td><code>s3://midb-hbcd-main-deid/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">De-identified raw BIDS, derivatives, and BrainSwipes data</td>
    </tr>
    <tr>
      <td>Main PR</td>
      <td><code>s3://midb-hbcd-main-pr/</code></td>
      <td>Contains LORIS-curated BIDS data for the full HBCD study, including:<br>
       • De-identfied: <span class="tooltip">raw BIDS<span class="tooltiptext"><i>assembly_bids/</i></span></span> and <span class="tooltip">participant lists<span class="tooltiptext"><i>deidentification-lists/</i></span></span><br>
       • Re-identfied: <span class="tooltip">derivatives<span class="tooltiptext"><i>derivatives/</i></span></span> and <span class="tooltip">BrainSwipes data<span class="tooltiptext"><i>reid_brainswipes/</i></span></span>
      </td>
    </tr>
    <tr>
      <td>Lasso Prerelease</td>
      <td><code>s3://midb-hbcd-lasso-data-prerelease/br{BETA RELEASE#}/hbcd/</code></td>
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
<li>Find release-ready subject/sessions in <code>s3://midb-hbcd-main-deid/</code></li>
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

<br>

