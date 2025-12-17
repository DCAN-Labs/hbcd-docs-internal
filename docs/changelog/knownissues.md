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

See issues documented on the beta 2.0 version of the HBCD Docs site [here](https://docs.hbcdstudy.org/2.0/changelog/knownissues/#general).

### Demographics

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
<td>Visit Level Data</td>
<td style="word-wrap: break-word; white-space: normal;"><code>par_visit_data_visit_missed_date</code> variable data is incorrect: dates are inaccurate (e.g. year of 1999 for some) and also cases where a date is provided when a visit was not missed</td>
<td>R2.1</td>
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
<td style="word-wrap: break-word; white-space: normal;"><b>Data Request:</b> Large gaps between collection and analysis dates - currently documented as a <a href="https://docs.hbcdstudy.org/latest/instruments/biospec/nails/#warning">Data Warning</a> on central HBCD Docs site. Currently under review by WG to determine next steps.</td>
<td>TBD</td>
</tr>
<tr>
<td>2</td>
  <td>Urinary Creatinine</td>
  <td style="word-wrap: break-word; white-space: normal;">
  Address out-of-range values in creatinine results (<code>bio_bm_biosample_urine_results_bio_creat_u</code>)
  </td>
    <td><b>R2.1</b></td> 
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
  <td>Bayley</td>
  <td style="word-wrap: break-word; white-space: normal;">13 Bayley administrations that do not have valid scores for all sub-tests (<code>-9999</code>)</td>
<td>TBD (R2.1)</td>
  </td>
</tr>
<tr>
<td>3</td>
<td>MLDS</td>
<td style="word-wrap: break-word; white-space: normal;">
Correct 'dictionary' Data Dictionary element to remove erroneous text that appears at end, e.g., "Are there other children being cared for at the same time with your child?Â Â Â Â Â Â." These are coming from the options as coded in REDCap, and will need to be removed. They are not visible on the displayed options, but the HTML leakage is found in LORIS.</td>
<td>TBD (R2.1)</td>
</tr>
<tr>
<td>4</td>
  <td>MLDS</td>
  <td style="word-wrap: break-word; white-space: normal;">
  The variable "total hours per week of non parental hours" (<code>ncl_ch_mlds_arr_hr_wk</code>) contains implausible values due to data entry errors. The max plausible value for this variable is 168 hours.
  </td>
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
<tr>
  <td>2</td>
  <td>Growth<br><code>ph_ch_anthro</code></td>
  <td style="word-wrap: break-word; white-space: normal;">Ranges used to filter out-of-range growth measurements are not age-specific, leading to values that are within the valid range, but biologically implausible for the visit age. Filtering methods need to be re-evaluated.</td>
  <td>R2.1 patch</td>
</tr>
<tr>
  <td>3</td>
  <td>BISQ-SF</td>
  <td style="word-wrap: break-word; white-space: normal;">Missing Infant Sleep (IS) sub-scale score</td>
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
<td>TLFB</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Error:</b> TLFB missing for subset of V02 participants. Under LORIS review (see <a href="https://ucsd-actri.monday.com/boards/6045591843/pulses/9389624562">monday.com</a>)</td>
<td>TBD</td>
</tr>
<tr>
<td>2</td>
<td>pex_bm_health</td>
<td><b>Data Correction:</b> Fix inconsistently provided ICD codes for Pregnancy/Infant Health</td>
<td>TBD (R3.X)</td>
</tr>
<tr>
<td>3</td>
<td>TLFB</td>
<td>PNR cohort reported TLFB on the wrong weeks (versions 1 or 2 instead of 3)</td>
<td>R2.1 patch</td>
</tr>
<tr>
<td>4</td>
<td>pex_bm_health_preg</td>
<td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_health_preg__healthhx_002__01</code> is blank - remove from R2.0 if not able to resolve (currently under LORIS review)</td>
<td>TBD</td>
</tr>
<tr>
<td>5</td>
<td>pex_bm_health_preg</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Error:</b> <code>pex_bm_health_preg__illness_003__12</code> is blank. This is the highest temperature for the third illness. Participants would have needed to report on a first and second illness before seeing this item due to branching logic, but these are not in the dataset (currently under LORIS review).</td>
<td>TBD</td>
</tr>
<tr>
<td>6</td>
<td>pex_bm_health_preg</td>
<td style="word-wrap: break-word; white-space: normal;"><code>pex_bm_healthv2_preg__exp__pnv_007__01</code> is entirely blank, which shouldn't be the case for participants who reported that they stopped PNV (currently under LORIS review).</td>
<td>TBD</td>
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



