<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

# Tabulated Data Processing Workflow

Data is collected from sites and ultimately transferred to the central LORIS Production S3 bucket, where it is subsequently de-identified and staged for ingestion into Lasso (NBDC Data Access Platform). The tabulated data processing workflow is outlined in the diagram below, showing the specific workflows for different data types and identifying the HDCC organization responsible for each processing step. These steps include data capture, de-identification, staging, and ingestion into Lasso.

<object type="image/svg+xml" data="../images/tab-wf.svg" width="100%"></object>
<small><b>NOTE</b>: <i>Genetics capture currently occurs via Sampled and BAH, but will be changed to only Sampled in the future.</i></small>

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
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
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
      <td><code>s3://midb-hbcd-lasso-staging/</code></td>
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
    <th style="width: 15%; text-align: center">Study Stage</th>
    <th style="width: 20%; text-align: center">Step</th>
    <th style="width: 25%; text-align: center">Location</th>
    <th style="width: 20%; text-align: center">Responsible</th>
    <th style="background-color: #ff00088b; width: 20%; text-align: center">Accountable</th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>C</b><span class="tooltiptext">Consulted</span></span>/<span class="tooltip tooltip-left"><b>I</b><span class="tooltiptext">Informed</span></span></th>
  </tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Set Up</td>
<td style="word-wrap: break-word; white-space: normal;">Testing and Validation of questions &amp; scoring</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#loris" target="_blank">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#lasso" target="_blank">Lasso</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Santiago Torres, Jen Zink, WG Leads</td>
<td style="word-wrap: break-word; white-space: normal;">Santiago Torres</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Conversion</td>
<td style="word-wrap: break-word; white-space: normal;">Add missingness and shadow matrix</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#loris" target="_blank">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#lasso" target="_blank">Lasso</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#ripple" target="_blank">Ripple</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts" target="_blank">HCAC</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Santiago Torres (LORIS), Jen Zink (Lasso), Sauren Ravencroft (Ripple), Stephanie Averill (HCAC)</td>
<td style="word-wrap: break-word; white-space: normal;">Santiago Torres</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Conversion</td>
<td style="word-wrap: break-word; white-space: normal;">Re-ID</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Sriharshitha Anuganti, Erik Lee</td>
<td style="word-wrap: break-word; white-space: normal;">Sriharshitha Anuganti</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Readiness for transfer</td>
<td style="word-wrap: break-word; white-space: normal;">Hot Sheet Population</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Erik Lee, Tim Hendrickson, Santiago Torres, Lucille Moore</td>
<td style="word-wrap: break-word; white-space: normal;">Maren Macgregor-Hannah</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Ingestion/Transfer</td>
<td style="word-wrap: break-word; white-space: normal;">Transfer release data to bucket for Lasso to pick up</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#lasso" target="_blank">Lasso</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Sriharshitha Anuganti, Erik Lee</td>
<td style="word-wrap: break-word; white-space: normal;">Sriharshitha Anuganti</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Ingestion</td>
<td style="word-wrap: break-word; white-space: normal;">Ingestion to Lasso</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#lasso" target="_blank">Lasso</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Lasso Data Loading Team, Jen Zink, Leigh MacIntyre</td>
<td style="word-wrap: break-word; white-space: normal;">Laetitia Fesselier</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC</td>
<td style="word-wrap: break-word; white-space: normal;">Review of data and corresponding shadow matrix</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#loris" target="_blank">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#lasso" target="_blank">Lasso</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#ripple" target="_blank">Ripple</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts" target="_blank">HCAC</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">WG Leads, Santiago Torres (LORIS), Jen Zink (Lasso), Sauren Ravencroft (Ripple), Stephanie Averill (HCAC)</td>
<td style="word-wrap: break-word; white-space: normal;">Jen Zink</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
</tbody>
</table>
</div>

<br>