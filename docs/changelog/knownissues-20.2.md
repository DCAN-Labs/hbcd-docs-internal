
# Known Issues

<div class="pill-center">
  <a href="../../#data-quality-checks" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip">
        <i class="fa-solid fa-clipboard-check" style="color: #6300d3;"></i>
        <span class="tooltiptext">Data quality checks<br><i>Click to learn more</i></span>
      </span>
    </span>
  </a>
  <a href="../../#transparency" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip">
        <i class="fa-solid fa-eye" style="color: #6300d3;"></i>
        <span class="tooltiptext">Transparency<br><i>Click to learn more</i></span>
      </span>
    </span>
  </a>
</div>

### General

<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
<th style="padding-top: 2px; padding-bottom: 2px">Table/Var</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fixed Issue/Update</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<!-- General -->
<tr>
<td>1</td>
<td>NA- Data Dictionary</td>
<td>'Instruction' metadata text may be incomplete/misaligned - <a href="https://docs.hbcdstudy.org/latest/changelog/knownissues/#instruction-metadata-read-carefully">see details</a></td>
<td>TBD</td>
</tr>
<tr>
<td>2</td>
<td>Gestational Age (GA)</td>
<td>Implausible gestational ages in multiple instruments - <a href="https://ucsd-actri.monday.com/boards/6045591843/pulses/18387442075">see details</a></td>
<td>TBD</td>
</tr>
</tbody>
</table>

### Behavior & Caregiver-Child Interaction

<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
<th style="padding-top: 2px; padding-bottom: 2px">Table/Var</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fixed Issue/Update</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<!-- BCGI -->
<tr>
<td>1</td>
<td>ECBQ (<code>mh_cg_ecbq</code>)</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Correction:</b> Change coding for "Does not apply" to 8 to be consistent with IBQR (currently noted on instrument page under <a href="https://docs.hbcdstudy.org/2.0/instruments/bcgi/ibqr/#scoring">Scoring Procedures</a>)</td>
<td>TBD</td>
</tbody>
</table>

### Biospecimen & Omics

<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
<th style="padding-top: 2px; padding-bottom: 2px">Table/Var</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fixed Issue/Update</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<!-- Biospec -->
<tr>
<td>1</td>
<td>Nails/Urine</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Request:</b> Add 'ANALYSIS DATE' for Biospec tables.</td>
<td>TBD</td>
</tr>
<tr>
<td>2</td>
<td>Nails/Urine</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Request:</b> Large gaps between collection and analysis dates - currently documented as a <a href="https://docs.hbcdstudy.org/latest/instruments/biospec/nails/#warning">Data Warning</a> on central HBCD Docs site. Currently under review by WG to determine next steps.</td>
<td>TBD</td>
</tr>
</tbody>
</table>

### Neurocognition & Language

<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
<th style="padding-top: 2px; padding-bottom: 2px">Table/Var</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fixed Issue/Update</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<!-- Neurocognition & Language -->
<tr>
<td>1</td>
<td>CDI</td>
<td style="word-wrap: break-word; white-space: normal;">All percentile scores besides (`ncl_ch_cdiwgen_words_produced_percentile_both`) are incorrectly set to `type_data`=text, but should be integer.</td>
<td>TBD (R2.1)</td>
</tr>
<tr>
<td>2</td>
<td>MLDS</td>
<td style="word-wrap: break-word; white-space: normal;">
Correct 'dictionary' Data Dictionary element to remove erroneous text that appears at end, e.g., "Are there other children being cared for at the same time with your child?Â Â Â Â Â Â." These are coming from the options as coded in REDCap, and will need to be removed. They are not visible on the displayed options, but the HTML leakage is found in LORIS.</td>
<td>TBD (R2.1)</td>
</tr>
</tbody>
</table>

### Physical Health

<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
<th style="padding-top: 2px; padding-bottom: 2px">Table/Var</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fixed Issue/Update</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>ecPROMIS - Physical Activity</td>
<td style="word-wrap: break-word; white-space: normal;">Add score fields that are to be excluded from release 2.0 due to incorrect data (documented as known issue on public HBCD Docs site with instructions for users to calculate fields themselves)</td>
<td>R2.1 patch</td>
</tr>
</tbody>
</table>

### Pregnancy & Exposure, Including Substance Use

<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
<th style="padding-top: 2px; padding-bottom: 2px">Table/Var</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fixed Issue/Update</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<!-- PEX -->
<tr>
<td>1</td>
<td>TLFB (missing V02)</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Error:</b> TLFB missing for subset of participants at V02. Under LORIS review.</td>
<td>TBD</td>
</tr>
<tr>
<td>2</td>
<td>pex_bm_health</td>
<td><b>Data Correction:</b> Fix inconsistently provided ICD codes for Pregnancy/Infant Health</td>
<td>TBD (R3.X)</td>
</tr>
</tbody>
</table>

### Imaging
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
<th style="padding-top: 2px; padding-bottom: 2px">Table/Var</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fixed Issue/Update</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<!-- EEG & IMAGING-->
<tr>
<td>1</td>
<td>MR</td>
<td>Run ID Order Not Chronological - <a href="https://docs.hbcdstudy.org/latest/changelog/knownissues/#imaging-data">see details</a></td>
<td>TBD</td>
</tr>
</tbody>
</table>



