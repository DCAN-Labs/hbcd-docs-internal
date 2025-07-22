# HBCD Data Processing Workflows

<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

This section outlines the full HBCD processing workflows for [tabulated data](#tabulated-data) and [file-based data](#file-based-data), detailing each step from data capture at study sites to final ingestion into Lasso. Each subsection of the workflow diagram includes the name of the responsible organization in the lower left-hand corner. Clicking on an organization name directs you to its corresponding section on the [Org Charts](../orgcharts.md) page, where you can find more information about that organization's role in the HBCD Study and its team members. 

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

<object type="image/svg+xml" data="../images/pre-CBRAIN.svg" style="width: 100%; height: auto;">
  Your browser does not support SVG
</object>

### CBRAIN Processing, Re-Identification, & Lasso Ingestion

<object type="image/svg+xml" data="../images/cbrain-release.svg" style="width: 100%; height: auto;">
  Your browser does not support SVG
</object>


<div id="record-query" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text">Record Query</span>
  <a class="anchor-link" href="#record-query" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>After CBRAIN processing, previous processing records are queried against the contents of s3://midb-hbcd-main-deid/assembly_bids to ensure that processing is still up-to-date with the current BIDS data. For any cases where the derivative data has become out of sync with the assembly_bids data, the impacted derivative data along with CBRAIN processing task objects are deleted. The next time the query scripts are run that look for new subjects to process, the processing will be re-initiated for these subjects.</p>
</div>

## Lasso Staging & Ingestion

<object type="image/svg+xml" data="../images/lasso-ingestion.svg" width="100%"></object>




