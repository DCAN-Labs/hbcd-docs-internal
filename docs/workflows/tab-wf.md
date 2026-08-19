# Tabulated Data Processing Workflow

Data collected from sites is transferred to the central **LORIS Production S3 bucket**, where it is **de-identified** and **staged for ingestion into Lasso (NBDC Data Access Platform)**. The diagram below outlines the tabulated data processing workflow, showing the steps for each data type and the HDCC group responsible for each stage: **capture**, **de-identification**, **staging**, and **ingestion**.     
*Note: Genetics data capture currently occurs via Sampled and BAH but will transition to Sampled only, as shown in the diagram.*

<object type="image/svg+xml" data="../images/tab-wf.svg" width="100%"></object>
<i><b>*</b> All tabulated data from the UMN SCE is also copied to a LORIS Sandbox (non-production) bucket.</i>

<div id="s3buckets-tab" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-key" style="margin-right: 6px; color: blue;"></i> S3 Bucket Key</span>
  <a class="anchor-link" href="#s3buckets-tab" title="Copy link">
    <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="table-no-vertical-lines">
    <thead>
      <tr>
        <th>Key Name in Diagram</th>
        <th>S3 URL</th>
      </tr>
    </thead>
    <tbody>
    <tr>
      <td>Main PR</td>
      <td><code>s3://midb-hbcd-main-pr/</code></td>
    </tr>
    <tr>
      <td>Sandbox</td>
      <td><code>s3://midb-hbcd-main-sb/</code></td>
    </tr>
    <tr>
      <td>De-ID</td>
      <td><code>s3://midb-hbcd-main-deid/</code></td>
    </tr>
    <tr>
      <td>De-ID-List</td>
      <td><code>s3://midb-hbcd-main-pr-deidentification-list/</code></td>
    </tr>
    <tr>
      <td>Lasso Staging</td>
      <td><code>s3://midb-hbcd-staging/</code></td>
    </tr>
    <tr>
      <td>Lasso PR</td>
      <td><code>s3://midb-hbcd-lasso-hdcc-qc-br/</code></td>
    </tr>
  </tbody>
  </table>
</div>

<div id="third-party" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-globe" style="margin-right: 6px; color: blue;"></i> Third Party Tools</span>
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
<td>Early Regulation in Context Assessment</td>
</tr>
<tr>
<td><b>CDI</b></td>
<td>The MacArthur-Bates Communicative Development Inventories, a widely used tool for assessing early language</td>
</tr>
<tr>
<td><b>Bayley</b></td>
<td>The Bayley Scales of Infant and Toddler Development (licensed via Pearson), used to assess cognitive, motor, and language development</td>
</tr>
<tr>
<td><b>Vineland</b></td>
<td>The Vineland Adaptive Behavior Scales (licensed via Pearson), used to measure adaptive behaviors and daily functioning</td>
</tr>
<tr>
<td><b>NIH BTB</b></td>
<td>NIH Baby Toolbox</td>
</tr>
<tr>
<td><b>BISQ-R</b></td>
<td>The Brief Infant Sleep Questionnaire - Revised, a validated parent-report sleep instrument</td>
</tr>
</tbody>
</table>
</div>

<div id="tab-raci" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-table" style="margin-right: 6px; color: blue;"></i> RACI for Tabulated Data</span>
  <a class="anchor-link" href="#tab-raci" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table">
<thead>
  <tr>
    <th>Study Stage</th>
    <th>Step</th>
    <th>Location</th>
    <th>Responsible</th>
    <th style="background-color: #ff00088b;">Accountable</th>
    <th>Consulted/Informed</th>
  </tr>
</thead>
<tbody>
<tr>
<td>Set Up</td>
<td>Testing and Validation of questions &amp; scoring</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#loris">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#lasso">Lasso</a></span></td>
<td>Santiago Torres, Jen Zink, WG Leads</td>
<td>Santiago Torres</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td>Data Conversion</td>
<td>Add missingness and shadow matrix</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#loris">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#lasso">Lasso</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#ripple">Ripple</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts">HCAC</a></span></td>
<td>Santiago Torres (LORIS), Jen Zink (Lasso), Sauren Ravencroft (Ripple), Stephanie Averill (HCAC)</td>
<td>Santiago Torres</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td>Data Conversion</td>
<td>Re-ID</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi">UMN MSI</a></span></td>
<td>Sriharshitha Anuganti, Tanya Pandhi</td>
<td>Sriharshitha Anuganti</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td>Data Readiness for transfer</td>
<td>Hot Sheet Population</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi">UMN MSI</a></span></td>
<td>Tanya Pandhi, Santiago Torres, Lucille Moore</td>
<td>Maren Macgregor-Hannah</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td>Data Ingestion/Transfer</td>
<td>Transfer release data to bucket for Lasso to pick up</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi">UMN MSI</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#lasso">Lasso</a></span></td>
<td>Sriharshitha Anuganti, Tanya Pandhi</td>
<td>Sriharshitha Anuganti</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td>Data Ingestion</td>
<td>Ingestion to Lasso</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#lasso">Lasso</a></span></td>
<td>Lasso Data Loading Team, Jen Zink, Leigh MacIntyre</td>
<td>Laetitia Fesselier</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td>Data QC</td>
<td>Review of data and corresponding shadow matrix</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#loris">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#lasso">Lasso</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#ripple">Ripple</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts">HCAC</a></span></td>
<td>WG Leads, Santiago Torres (LORIS), Jen Zink (Lasso), Sauren Ravencroft (Ripple), Stephanie Averill (HCAC)</td>
<td>Jen Zink</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
</tbody>
</table>
</div>

<br>