<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

# File-Based Data Processing Workflow

## Part 1: Site Capture & BIDS Conversion

Data is collected from sites into LORIS (EEG, Axivity, and GABI) or FIONA (for MRI and MRS). LORIS data is subsequently transferred directly into the central S3 main PR bucket, which subsequently is sourced for CBRAIN processing. MRI and MRS must first be converted to BIDS format and MRI data also undergoes extensive raw data QC ([see details](https://docs.hbcdstudy.org/latest/instruments/mri/qc/#raw-mr-data-qc)).

<p  align="center">
<object type="image/svg+xml" data="../images/fb-wf-1-alt.svg" style="width: 85%; height: auto;">
  Your browser does not support SVG
</object>
</p>

<div id="s3buckets-fb1" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-key" style="margin-right: 6px; color: blue;"></i> S3 Bucket Key</span>
  <a class="anchor-link" href="#s3buckets-fb1" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table">
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
      <td>JCVI</td>
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
    <tr>
      <td>QC Environment</td>
      <td><code>lasso-hdcc-qc-ongoing-dccid/</code></td>
      <td>Lasso HDCC environment for ongoing QC (<a href="#lasso-hdcc-qc-environment">see details)</td>
    </tr>
</tbody>
</table>
</div>
<div id="lasso-hdcc-qc-environment" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fa-solid fa-clipboard-check" style="margin-right: 6px; color: blue;"></i> Lasso HDCC QC Environment</span>
  <a class="anchor-link" href="#lasso-hdcc-qc-environment" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>The Lasso HDCC QC environment includes:</p>
<ol>
<li>The <strong>Lasso Prerelease</strong> S3 bucket (<code>s3://midb-hbcd-lasso-hdcc-qc-br</code>) containing release version-specific data housed under <code>br{BETA RELEASE#}/hbcd/</code> to be ingested into Lasso</li>
<li>The <strong>Ongoing QC</strong> S3 bucket (<code>s3://midb-hbcd-lasso-hdcc-qc-ongoing-dccid</code>), which mimics of the structure of the release buckets, but excludes the <code>br{BETA RELEASE#}</code> prefix. The data contains DCCIDs/PSCIDs and is updated with both release and non-release main study participant data regularly, including:<ul>
<li>Tabulated data provided by LASSO</li>
<li>Raw BIDS copied from <code>s3://midb-hbcd-main-pr/assembly_bids</code></li>
<li>Derivatives (re-identified) copied from <code>s3://midb-hbcd-main-pr/reid_derivatives</code></li>
</ul>
</li>
</ol>
</div>

## Part 2: De-Identification, CBRAIN Processing, & Lasso Ingestion

Processing pipelines are run in CBRAIN and outputs are stored in session-specific folders on `s3://midb-hbcd-main-deid/derivatives`. When processing is launched, a record of which files were used for processing is stored under `s3://midb-hbcd-main-deid/derivatives/ses-<label>/cbrain_misc`. In the future, this will likely be replaced with a simple database in the S3 bucket that keeps track of these (and other) details more centrally.

<object type="image/svg+xml" data="../images/fb-wf-2-alt.svg" style="width: 100%; height: auto;">
  Your browser does not support SVG
</object>

<div id="s3buckets-fb2" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-key" style="margin-right: 6px; color: blue;"></i> S3 Bucket Key</span>
  <a class="anchor-link" href="#s3buckets-fb2" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <thead>
      <tr>
        <th>Key Name in Diagram</th>
        <th>S3 URL</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <td>De-ID-List</td>
      <td><code>s3://midb-hbcd-main-pr-deidentification-list/</code></td>
    </tr>
    <tr>
      <td>De-ID / BIDS</td>
      <td><code>s3://midb-hbcd-main-deid/assembly_bids/</code></td>
    </tr>
    <tr>
      <td>De-ID / Derivatives</td>
      <td><code>s3://midb-hbcd-main-deid/derivatives/</code></td>
    </tr>
    <tr>
      <td>De-ID / BrainSwipes</td>
      <td><code>s3://midb-hbcd-main-deid/brainswipes/</code></td>
    </tr>
    <tr>
      <td>Main PR / Derivatives</td>
      <td><code>s3://midb-hbcd-main-pr/reid_derivatives/</code></td>
    </tr>
     <tr>
      <td>Main PR / BrainSwipes</td>
      <td><code>s3://midb-hbcd-main-pr/reid_brainswipes/</code></td>
    </tr>
    <tr>
      <td>Lasso PR</td>
      <td><code>s3://midb-hbcd-lasso-hdcc-qc-br/br{BETA RELEASE#}/hbcd/</code></td>
    </tr>
    <tr>
      <td>QC Environment</td>
      <td><code>s3://midb-hbcd-lasso-hdcc-qc-ongoing-dccid/</code></td>
    </tr>
</tbody>
</table>
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
<p>Following CBRAIN processing, processing records are queried for new derivative outputs ready to be re-identified. Re-identification involves replacing all release candidate IDs with DCCIDs in processing outputs and occurs in the process of copying the data from <code>s3://midb-hbcd-main-deid/derivatives/</code> to <code>s3://midb-hbcd-main-pr/reid_derivatives/</code>.</p>
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
      
### Responsibility Assignment Matrices By Modality 

<p style="text-align: center; font-size: 1.3em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

<div id="imaging-raci" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-table" style="margin-right: 6px; color: blue;"></i>Imaging</span>
  <a class="anchor-link" href="#imaging-raci" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table">
<thead>
  <tr>
    <th style="width: 15%; text-align: center">Study Stage</th>
    <th style="width: 20%; text-align: center">Step</th>
    <th style="width: 25%; text-align: center">Location</th>
    <th style="width: 20%; text-align: center">Responsible</th>
    <th style="background-color: #ff00088b; width: 10%; text-align: center">Accountable</th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>C</b><span class="tooltiptext">Consulted</span></span>/<span class="tooltip tooltip-left"><b>I</b><span class="tooltiptext">Informed</span></span></th>
  </tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Collection</td>
<td style="word-wrap: break-word; white-space: normal;">Participant Source Data Acquisition: DCMs, eCRF population (MRI Acquisition Form)</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#fiona" target="_blank">FIONA</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#loris" target="_blank">LORIS</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies by site)</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies by site)</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">QC at Source Data Acquisition: eCRF populated properly, DCM header checks, naming convention checks</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#fiona" target="_blank">FIONA</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies by site)</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies by site)</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">QC at Source: Check acquisition/protocol adherence</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#j-craig-venter-institute" target="_blank">JCVI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Josh Kuperman</td>
<td style="word-wrap: break-word; white-space: normal;">Anders Dale</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">Transfer acquisition/protocol adherence (both DCM acquisition and MRI Acquisition Form) to DCC</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#j-craig-venter-institute" target="_blank">JCVI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Ron Yang, Don Hagler</td>
<td style="word-wrap: break-word; white-space: normal;">Don Hagler</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Collection</td>
<td style="word-wrap: break-word; white-space: normal;">Convert DICOMs to BIDS/NIfTI</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Cecile Madjar</td>
<td style="word-wrap: break-word; white-space: normal;">Cecile Madjar</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">Data Collection</td>
  <td style="word-wrap: break-word; white-space: normal;">Convert MRS data to BIDS</td>
  <td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#health-sciences-technology" target="_blank">UMN HST</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
  <td style="word-wrap: break-word; white-space: normal;">Reed McEwan, Cecile Madjar</td>
  <td style="word-wrap: break-word; white-space: normal;">Reed McEwan</td>
  <td>[<b>C</b>] Helge Zoellner<br>[<b>C</b>] Erik Lee<br>[<b>C</b>] Georg Oeltzschner</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">QC of the DCM ot BIDs Conversion: Correct BIDS errors</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Cecile Madjar</td>
<td style="word-wrap: break-word; white-space: normal;">Cecile Madjar</td>
<td>[<b>C</b>] Erik Lee<br>[<b>C</b>] Lucille Moore<br>[<b>C</b>] Tim Hendrickson</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">Check for protocol deviations (based on BIDS)</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#j-craig-venter-institute" target="_blank">JCVI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">MRI QC Workgroup</td>
<td style="word-wrap: break-word; white-space: normal;">Don Hagler</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Ingestion</td>
<td style="word-wrap: break-word; white-space: normal;">Ingestion and catalogue DICOMs in Lasso</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">QC of ingestion</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#j-craig-venter-institute" target="_blank">JCVI</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#health-sciences-technology" target="_blank">HST</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">Initial QC raw data (e.g. manual, automated)</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#j-craig-venter-institute" target="_blank">JCVI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">MRI QC Workgroup</td>
<td style="word-wrap: break-word; white-space: normal;">Don Hagler</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
</tbody>
</table>
</div>

<div id="eeg-raci" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-table" style="margin-right: 6px; color: blue;"></i>EEG</span>
  <a class="anchor-link" href="#eeg-raci" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table">
<thead>
  <tr>
    <th style="width: 15%; text-align: center">Study Stage Step</th>
    <th style="width: 5%; text-align: center">Location</th>
    <th style="width: 20%; text-align: center">Responsible</th>
    <th style="background-color: #ff00088b; width: 20%; text-align: center">Accountable</th>
    <th style="width: 10%; text-align: center; text-align: center"><span class="tooltip tooltip-left"><b>C</b><span class="tooltiptext">Consulted</span></span>/<span class="tooltip tooltip-left"><b>I</b><span class="tooltiptext">Informed</span></span></th>
  </tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Monthly Net Inventory/Equipment QC</td>
<td>Site</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site), EEG Core, HDCC, LORIS</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site)</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">EEG Acquisition</td>
<td>Site</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site), EEG Core, HDCC, LORIS</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site)</td>
<td>EEG Core</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Populate EEG Acquisition Form</td>
<td>Site</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site), EEG Core, HDCC, LORIS</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site)</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">QC Acquisition form population</td>
<td>Site</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site), EEG Core, HDCC, LORIS</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site)</td>
<td>EEG Core</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">De-Identification &amp; Flags (pre-LORIS)</td>
<td>Site</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site), EEG Core, HDCC, LORIS</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site)</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">BIDs Wizard Population and Execution</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#loris" target="_blank">LORIS</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site), EEG Core, HDCC, LORIS</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site)</td>
<td>[<b>C</b>] Laetitia Fesselier</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Convert EEG data to BIDS</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Laetitia Fesselier</td>
<td style="word-wrap: break-word; white-space: normal;">Laetitia Fesselier</td>
<td style="word-wrap: break-word; white-space: normal;">EEG Core</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Run MADE Pipeline</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Erik Lee</td>
<td style="word-wrap: break-word; white-space: normal;">Erik Lee</td>
<td>EEG Core</td>
</tr>
<tr>
<td>QC pre-processed EEG</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#university-of-maryland" target="_blank">UMD EEG Core</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Kira Ashton, Dylan Gilbreath, Trisha Maheswari, Elise Harris</td>
<td style="word-wrap: break-word; white-space: normal;">Santiago Morales</td>
<td>EEG Core</td>
</tr>
</tbody>
</table>
</div>

<div id="biospec-raci" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-table" style="margin-right: 6px; color: blue;"></i>Biospecimens</span>
  <a class="anchor-link" href="#biospec-raci" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table">
<thead>
  <tr>
    <th style="width: 15%; text-align: center">Study Stage Step</th>
    <th style="width: 5%; text-align: center">Location</th>
    <th style="width: 20%; text-align: center">Responsible</th>
    <th style="background-color: #ff00088b; width: 20%; text-align: center">Accountable</th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>C</b><span class="tooltiptext">Consulted</span></span>/<span class="tooltip tooltip-left"><b>I</b><span class="tooltiptext">Informed</span></span></th>
  </tr>
</thead>
<tbody>
<tr>
  <td>Acquisition of sample</td>
  <td>Site</td>
  <td>Site Staff</td>
  <td>Site Staff</td>
  <td style="text-align: center;">-/-</td>
</tr>
<tr>
  <td>Population of meta data form</td>
  <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#loris" target="_blank">LORIS</a></span></td>
  <td>Site Staff</td>
  <td>Site Coordinator</td>
  <td style="text-align: center;">-/-</td>
</tr>
<tr>
<td>QC of form population</td>
<td><span class="tooltip">OHSU<span class="tooltiptext">Oregon Health and Science University</span></span></td>
<td>WG Co-Chairs</td>
<td>Elinor Sullivan (Co-Chair)</td>
<td style="text-align: center;">-/-</td>
</tr>
<tr>
<td>Shipment of sample</td>
<td>Site</td>
<td>Site Staff</td>
<td>Site Staff</td>
<td style="text-align: center;">-/-</td>
</tr>
<tr>
<td>QC: Ensuring sample was received</td>
<td>Sampled/USDTL</td>
<td>Charles Hevi (Sampled)<br>Priti Soni (USDTL)</td>
<td>Charles Hevi (Sampled)<br>Priti Soni (USDTL)</td>
<td style="text-align: center;">-/-</td>
</tr>
<tr>
<td>QC: deviation code of sample</td>
<td>Sampled/USDTL</td>
<td>Charles Hevi (Sampled)<br>Priti Soni (USDTL)</td>
<td>Charles Hevi (Sampled)<br>Priti Soni (USDTL)</td>
<td style="text-align: center;">-/-</td>
</tr>
<tr>
<td>Analysis of sample</td>
<td>Sampled/USDTL</td>
<td>Charles Hevi (Sampled)<br>Priti Soni (USDTL)</td>
<td>Charles Hevi (Sampled)<br>Priti Soni (USDTL)</td>
<td style="text-align: center;">-/-</td>
</tr>
</tbody>
</table>
</div>

<div id="sensors-raci" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-table" style="margin-right: 6px; color: blue;"></i> Wearable Sensors</span>
  <a class="anchor-link" href="#sensors-raci" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table">
<thead>
  <tr>
    <th style="width: 15%; text-align: center">Study Stage Step</th>
    <th style="width: 25%; text-align: center">Location</th>
    <th style="width: 20%; text-align: center">Responsible</th>
    <th style="background-color: #ff00088b; width: 20%; text-align: center">Accountable</th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>C</b><span class="tooltiptext">Consulted</span></span>/<span class="tooltip tooltip-left"><b>I</b><span class="tooltiptext">Informed</span></span></th>
  </tr>
</thead>
<tbody>
<tr>
  <td>Data Collection</td>
  <td>Site</td>
  <td></td>
  <td></td>
  <td></td>
</tr>
<tr>
  <td>Convert Axivity data to BIDS</td>
  <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
  <td>Cecile Madjar</td>
  <td>Cecile Madjar</td>
  <td>[<b>C</b>] Jinseok Oh<br>[<b>C</b>] Beth Smith<br>[<b>C</b>] Erik Lee</td>
</tr>
<tr>
  <td>Run Axtivity Pipeline</td>
  <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
  <td>Erik Lee</td>
  <td>Erik Lee</td>
  <td>[<b>C</b>] Jinseok Oh<br>[<b>C</b>] Beth Smith</td>
</tr>
<tr>
  <td>QC preprocessed data</td>
  <td></td>
  <td></td>
  <td></td>
  <td></td>
</tr>
</tbody>
</table>
</div>


## UMN De-Identification & Pipeline Processing

This documentation outlines how UMN processes imaging data after it has been curated by LORIS into BIDS format.  
The workflow consists of **eight interdependent components** that handle de-identification, pipeline processing, synchronization, and cleanup of imaging data.

### Workflow Summary

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

### Individual Workflows

<div id="1" class="table-banner" onclick="toggleCollapse(this)">
<span class="emoji"><i class="fa-solid fa-1"></i></span>
  <span class="text-with-link">
  <span class="table-text">Creation of Release Candidate IDs for Anonymization</span>
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
<span class="emoji"><i class="fa-solid fa-2"></i></span>
  <span class="text-with-link">
  <span class="table-text">Raw BIDS De-identification</span>
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
<span class="emoji"><i class="fa-solid fa-3"></i></span>
  <span class="text-with-link">
  <span class="table-text">Registration of Subjects from Raw BIDS Data into CBRAIN</span><a class="anchor-link" href="#3" title="Copy link"><i class="fa-solid fa-link"></i></a></span>
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
  <span class="emoji"><i class="fa-solid fa-4"></i></span>
  <span class="text-with-link">
  <span class="table-text">Pipeline processing of De-identified Data</span>
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
  <span class="emoji"><i class="fa-solid fa-5"></i></span>
  <span class="text-with-link">
  <span class="table-text">Saving stdout/stderr Logs for Failed CBRAIN Processing Tasks</span>
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
  <span class="emoji"><i class="fa-solid fa-6"></i></span>
  <span class="text-with-link">
  <span class="table-text">Cleanup for Out-of-Sync Raw BIDS Data (between LORIS & de-id buckets)</span>
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
<li>If session counts or <code>loris-versionid</code> mismatch, delete all associated derivatives, CBRAIN task records, and raw BIDS data. The next time the query scripts are run that look for new subjects to process, the processing will be re-initiated for these subjects.</li>
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
  <span class="emoji"><i class="fa-solid fa-7"></i></span>
  <span class="text-with-link">
  <span class="table-text">Re-identification of Derivatives (i.e. re-insertion of DCCIDs) for LORIS</span>
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
  <span class="emoji"><i class="fa-solid fa-8"></i></span>
  <span class="text-with-link">
  <span class="table-text">Cleanup for Out-of-Sync Derivatives in LORIS Bucket</span>
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