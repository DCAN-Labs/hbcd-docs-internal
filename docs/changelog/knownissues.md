
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

### Demographics - *Visit Information*

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
<td><code>par_visit_data</code></td>
<td>Remove 'protocol_exception' field (3 cases with 'IRB Deviation')</td>
<td>20.2</td>
</tr>
<tr>
<td>2</td>
<td><code>par_visit_data</code></td>
<td>Remove open text fields</td>
<td>20.2</td>
</tr>
<tr>
<td>3</td>
<td><code>par_visit_data</code></td>
<td>Remove 'participant_withdrawal' and 'participant_withdrawal_reason' fields</td>
<td>20.2</td>
</tr>
<tr>
<td>4</td>
<td><code>par_visit_data</code></td>
<td>Remove incorrect 'lol' test entry for 'Reason visit missed'</td>
<td>20.2</td>
</tr>
<tr>
<td>5</td>
<td><code>par_visit_data</code></td>
<td>Set 'source' to 'General' across all items and set 'description' to 'Biological Mother' for all SU flag fields</td>
<td>20.2</td>
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
<td>CHAOS</td>
<td><b>Scoring Correction:</b> implement scoring, including prorated scores</td>
<td>20.2</td>
</tr>
<tr>
<td>2</td>
<td>ECBQ (<code>mh_cg_ecbq</code>)</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Correction:</b> Change coding for "Does not apply" to 8 to be consistent with IBQR (currently noted on instrument page under <a href="https://docs.hbcdstudy.org/2.0/instruments/bcgi/ibqr/#scoring">Scoring Procedures</a>)</td>
<td>TBD</td>
</tr>
<tr>
<td>3</td>
<td>ECBQ &amp; IBQR</td>
<td><b>Remove Variables:</b> administration (all, partial, none) &amp; data_taken</td>
<td>TBD</td>
</tr>
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
<tr>
<td>3</td>
<td>Urine</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Remove Variables:</b> Remove <code>bio_c_mep_u</code>; <code>bio_c_mep_u_cat</code>; <code>bio_c_mep_unit_u</code> (only keep nmep[normeperidine]).</td>
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
<td>20.2</td>
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
<td>BISQ</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Add missing score fields</b>: infant_sleep_score, parent_behavior_score, parent_perception_score, total_score</td>
<td>20.2</td>
</tr>
<tr>
<td>2</td>
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
<td>20.2</td>
</tr>
<tr>
<td>2</td>
<td>pex_bm_health</td>
<td><b>Data Correction:</b> Fix inconsistently provided ICD codes for Pregnancy/Infant Health</td>
<td>TBD (R3.X)</td>
</tr>
<tr>
<td>3</td>
<td>ASSIST V1</td>
<td style="word-wrap: break-word; white-space: normal;"><b>SME Request:</b> (1) Order variables in the order of the survey and (2) Remove <i>adjusted age</i>, <i>candidate age</i>, and <i>sequence</i> fields</td>
<td>20.2</td>
</tr>
</tbody>
</table>

Assist V2
1- Please remove sequence field
2- Please order variables in the order of the survey
3- pex_bm_assistv2_candidate_age has blanks, and also has two outliers (.47, .55) 

### Social & Environmental Determinants
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
<!-- SED -->
<tr>
  <td>1</td>
  <td><code>sed_bm_ehits</code></td> 
  <td style="word-wrap: break-word; white-space: normal;"><code>total_score</code> and <code>score</code> both look like sum scores except former has inaccurate values - currently under review</td>
  <td>TBD</td>
</tr>
</tbody>
</table>

### EEG & Imaging
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
<td>EEG</td>
<td>Missing EEG capping quality variables for V03 (<a href="https://ucsd-actri.monday.com/boards/6045591843/pulses/18386241252">monday.com</a>)</td>
<td>TBD</td>
</tr>
<tr>
<td>1</td>
<td>MR</td>
<td>Run ID Order Not Chronological - <a href="https://docs.hbcdstudy.org/latest/changelog/knownissues/#imaging-data">see details</a></td>
<td>TBD</td>
</tr>
</tbody>
</table>



