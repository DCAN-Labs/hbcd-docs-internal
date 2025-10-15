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

This section provides an overview of the complete HBCD processing workflows for both [tabulated data](tab-wf.md) and [file-based data](fb-data-proc-wf.md), detailing key processing steps, data storage locations (on S3 and other systems), and the responsible teams (see [HDCC Structure & Organizational Charts](../orgcharts.md)).

<p>
<div id="def-terms" class="table-banner" onclick="toggleCollapse(this)">
  <span class="emoji"><i class="fas fa-book"></i></span>
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
</p>

#### S3 Bucket Descriptions

<table class="compact-table" style="width:100%; border-collapse: collapse; table-layout: fixed; font-size: 14px;">
  <thead>
    <tr>
      <th style="width: 1%;">Diagram Key</th>
      <th style="width: 30%;">S3 Object <code>s3://midb-hbcd*</code></th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Main PR</td>
      <td><code>-main-pr/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">
        LORIS production bucket that receives all tabulated and file-based data for the full HBCD study prior to staging and Lasso ingestion, including:<br>
        <ul>
          <li><code>phenotype/</code>: Tabulated data</li>
          <li><code>assembly_bids/</code>: Raw BIDS curated by LORIS (DCCIDs used for subject labels)</li>
          <li><code>derivatives/</code>: Re-identified derivatives</li>
          <li><code>reid_brainswipes/</code>: Re-identified BrainSwipes data</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>De-ID</td>
      <td><code>-main-deid/</code></td>
      <td>
        De-identified/anonymized data (Release Candidate IDs used for subject labels), including:<br>
        <ul>
          <li><code>assembly_bids/</code>: Raw BIDS</li>
          <li><code>derivatives/</code>: Derivatives</li>
          <li><code>brainswipes/</code>: BrainSwipes data</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td>De-Id-List</td>
      <td><code>-main-pr-deidentification-list/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">ID mapping file <code>release_identifiers_YYYYMMDD.csv</code>, re-created daily, showing relationships between the various ID types used in HBCD (e.g. contains de-identified participant list information used for de-identification).
      </td>
    </tr>
    <tr>
      <td>Lasso Staging</td>
      <td><code>-staging/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">Where LORIS deposits tabulated data after running data release script for each BR</td>
    </tr>
    <tr>
      <td>Lasso PR*</td>
      <td><code>-lasso-hdcc-qc-br/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">Lasso Pre-Release contains release version-specific data (de-identified) housed under <code>br{BETA RELEASE#}/hbcd/</code> to be ingested into Lasso</td>
    </tr>
    <tr>
      <td>QC Env*</td>
      <td><code>-lasso-hdcc-qc-ongoing-dccid/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">
      Lasso HDCC environment for ongoing QC; mimics the structure of the release data deposits, but excludes the br{BETA RELEASE#} prefix. The data contains DCCIDs only and is updated with both release and non-release main study participant data regularly, including:<br>
      <ul>
        <li>Tabulated data provided by LORIS to Lasso</li>
        <li>Raw BIDS copied from s3://midb-hbcd-main-pr/assembly_bids</li>
        <li>Re-identified derivatives from s3://midb-hbcd-main-pr/reid_derivatives</li>
      </ul>
      </td>
    </tr>
    <tr>
      <td>JCVI</td>
      <td><code>-ucsd-main-pr-dicoms/</code></td>
      <td>JCVI DICOMs and raw data QC results.</td>
    </tr>
    <tr>
      <td>MRS BIDS</td>
      <td><code>-main-pr-mrs/</code></td>
      <td>MRS data post-BIDS conversion.</td>
    </tr>
    <tr>
      <td>Sandbox</td>
      <td><code>main-sb/</code></td>
      <td style="word-wrap: break-word; white-space: normal;">LORIS Bucket for non-production system to test data flows on pilot data</td>
    </tr>
  </tbody>
</table>
<tfoot>* <i>Lasso PR and QC Env S3 buckets collectively form the <b>Lasso HDCC QC environment</b></i></tfoot>


<br>