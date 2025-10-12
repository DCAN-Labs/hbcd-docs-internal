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

This section outlines the full HBCD processing workflows for [tabulated data](tab-wf.md) and [file-based data](fb-data-proc-wf.md), detailing each step from data capture at study sites to final ingestion into Lasso (the NBDC Data Access Platform). Each subsection of the workflow diagram includes the name of the responsible organization in the lower left-hand corner. Clicking on an organization name directs you to its corresponding section on the [HDCC Structure & Organizational Charts](../orgcharts.md) page, where you can find more information about that organization's role in the HBCD Study and its team members. 

<div id="def-terms" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-book" style="margin-right: 6px; color: blue;"></i> Definition of Terms</span>
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
    <td>Tabulated data</td>
    <td style="word-wrap: break-word; white-space: normal;">In standardized HBCD table format, includes behavior & biology, demographics, visit data, and tabulated derivatives. See <a href="https://docs.hbcdstudy.org/latest/datacuration/overview/">Data Structure Overview</a> on the main Docs site for an overview of tabulated vs. file-based data.</td>
  </tr>
  <tr>
    <td>File-based data</td>
    <td style="word-wrap: break-word; white-space: normal;">In varied formats, includes raw BIDS and processed derivatives for MRI, MRS, EEG, and wearable sensor data. See <a href="https://docs.hbcdstudy.org/latest/datacuration/overview/">Data Structure Overview</a> on the main Docs site for an overview of tabulated vs. file-based data.</td>
  </tr>
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
    <td style="word-wrap: break-word; white-space: normal;">Additional ID used in LORIS and during data collection. This ID begins with a five character sequence where the first two characters indicate participant status and the last three characters indicate the recruitment site.</td>
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
    <tr>
    <td>Post-processing pipelines, BIDS Apps</td>
    <td style="word-wrap: break-word; white-space: normal;">Terms used to denote pipelines whose goal is to take imaging, eeg, or other data organized in BIDS and run numerical algorithms to create outputs that can be used for further processing or for statistical analyses. The outputs of these pipelines are referred to as derivatives or imaging-derived phenotypes depending on the context.</td>
    </tr>
    <tr>
    <td>derivatives</td>
    <td style="word-wrap: break-word; white-space: normal;">Any files produced by a post-processing pipeline. In other words, the outputs of containerized pipelines or BIDS Apps (such as Nibabies) that are run in CBRAIN.</td>
    </tr>
    <tr>
    <td>Imaging-derived phenotypes</td>
    <td style="word-wrap: break-word; white-space: normal;">Scalar values that are output from a pipeline (such as brain volume) that can be concatenated across subjects and used for statistical analyses</td>
    </tr>
    </tbody>
    </table>
</div>

### S3 Bucket Object Descriptions

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
  <td>
  <b>S3 Object:</b> <code>s3://midb-hbcd-main-pr/</code><br>
  <b>Diagram Key Name:</b> Main PR<br>
  <b>Description:</b> LORIS-curated BIDS data for the full HBCD study, see -<br>
  <ul>
    <li><code>s3://midb-hbcd-main-pr/assembly_bids</code>: Raw BIDS curated by LORIS (DCCIDs used for subject labels)</li>
    <li><code>s3://midb-hbcd-main-pr/derivatives/</code>: Re-identified derivatives</li>
    <li><code>s3://midb-hbcd-main-pr/reid_brainswipes/</code>: Re-identified BrainSwipes data</li>
  </ul>
  </td>
</tr>
<tr>
  <td>
  <b>S3 Object:</b> <code>s3://midb-hbcd-main-deid/</code><br>
  <b>Diagram Key Name:</b> De-ID<br>
  <b>Description:</b> De-identified/anonymized (Release Candidate IDs used for subject labels)  see -<br>
  <ul>
    <li><code>s3://midb-hbcd-main-deid/assembly_bids/</code>: Raw BIDS</li>
    <li><code>s3://midb-hbcd-main-deid/derivatives/</code>: Derivatives</li>
    <li><code>s3://midb-hbcd-main-deid/brainswipes/</code>: BrainSwipes data</li>
  </ul>
  </td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">
  <b>S3 Object:</b> <code>s3://midb-hbcd-main-pr-deidentification-list/release_identifiers_YYYYMMDD.csv</code><br>
  <b>Diagram Key Name:</b> De-Id-List<br>
  <b>Description:</b> ID mapping file, re-created daily, showing the relationship between the various types of IDs used in HBCD.
  </td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">
  <b>S3 Object:</b> <code>s3://midb-hbcd-lasso-hdcc-qc-br/br{BETA RELEASE#}/hbcd/</code><br>
  <b>Diagram Key Name:</b> Lasso Prerelease<br>
  <b>Description:</b> Release version-specific data, including participant list to be included in the release (<code>rawdata/participants.tsv</code>). This is the final repository after de-identification and prior to Lasso ingestion.
  </td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">
  <b>S3 Object:</b> <code>s3://midb-hbcd-lasso-hdcc-qc-ongoing-dccid/</code><br>
  <b>Diagram Key Name:</b> QC Env<br>
  <b>Description:</b> Lasso HDCC environment for ongoing QC (<a href="#lasso-hdcc-qc-environment">see details).
  </td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">
  <b>S3 Object:</b> <code>s3://midb-hbcd-ucsd-main-pr-dicoms/</code><br>
  <b>Diagram Key Name:</b> JCVI<br>
  <b>Description:</b> JCVI DICOMs and raw data QC results.
  </td>
</tr>
<tr>
  <td style="word-wrap: break-word; white-space: normal;">
  <b>S3 Object:</b> <code>s3://midb-hbcd-main-pr-mrs/</code><br>
  <b>Diagram Key Name:</b> MRS BIDS<br>
  <b>Description:</b> MRS data post-BIDS conversion.
  </td>
</tr>
</tbody>
</table>


<br>