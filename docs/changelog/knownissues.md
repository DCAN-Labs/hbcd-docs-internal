<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
.br-pill {
  display: inline-block;
  padding: 2px 8px;
  font-size: 0.75em;
  font-weight: 600;
  border-radius: 999px;
  line-height: 1.4;
  white-space: nowrap;
}
/* Version-specific styling */
.br-212 {background-color: #e6f0ff; color: #1a4fb3;}
.br-211 {background-color: #e9f7ef; color: #1e7e34;}
.br-tbd {background-color: #f1f3f5; color: #666; font-style: italic;}

.pr-pill {
  display: inline-block;
  padding: 2px 8px;
  font-size: 0.75em;
  font-weight: 600;
  border-radius: 999px;
  line-height: 1.4;
  white-space: nowrap;
  background-color: #f89781af;
}
</style>

<div class="pill-center">
<a href="../../#data-quality-checks" target="_blank" class="pill-link-wrapper">
<span class="pill-link"><span class="tooltip"><i class="fa-solid fa-clipboard-check" style="color: #6300d3;"></i><span class="tooltiptext">Data quality checks<br><i>Click to learn more</i></span></span></span></a>
<a href="../../#transparency" target="_blank" class="pill-link-wrapper">
<span class="pill-link"><span class="tooltip"><i class="fa-solid fa-eye" style="color: #6300d3;"></i><span class="tooltiptext">Transparency<br><i>Click to learn more</i></span></span></span></a>
</div>

<!-- <i>[BR data only]</i> = this means that the issue is not present in public release data, so will not be documented in the HBCD Docs site -->

# Known Issues & Pending Updates

!!! danger "Active Items Only"
    **This page lists ACTIVE issues/updates targeted for upcoming BRs, or included in the current BR pending final Workgroup/SME sign-off.** Items are not considered resolved until final review is complete. A running record of verified items is archived to [Resolved Issues & Updates](resolved.md) (from BR21.0; see prior release notes for earlier records). See the [HBCD Data Release Docs](https://docs.hbcdstudy.org/latest/changelog/issues-updates/) for corresponding public releases (PR) <span class="tooltip"> <i class="fa-solid fa-circle-info"></i><span class="tooltiptext">Items addressed in a BR are not reflected as resolved publicly until the corresponding PR is released</span></span>.

---

<p style="font-size: 1.2em; color: #555; text-align: center; line-height: 2;">
<i class="fas fa-bug" style="color: #f97316; font-size: 1em;"></i> = Known Issue &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-rotate" style="color: #199bd6; font-size: 1em;"></i> = Pending Update<br>
<i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.1em;"></i> = Target Fix <i>(BR if known, otherwise public R#/TBD)</i>
</p>
    
<!-- BEGIN KNOWN_ISSUES_TABLE -->

### General
<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Implausible GA</td>
<td style='word-wrap: break-word; white-space: normal;'>A small subset of participants have implausible <code>gestational_age</code> (V01 only) values  for one or more instrument. Until corrected, review GA distribution to exclude outliers from analysis (should be positive and generally &lt; 45 weeks).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Instruction</td>
<td style='word-wrap: break-word; white-space: normal;'>The 'instruction' Data Dictionary element is currently blank.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Multibirth Cohorts</td>
<td style='word-wrap: break-word; white-space: normal;'>Missing instrument fields for Sibling cohorts will be populated and <em>FamilyID</em> will be incorporated to help identify siblings - <a href="https://docs.hbcdstudy.org/latest/instruments/demo/visitinfo/#warning">see details</a>.</td>
<td style='text-align: center;'><span class='br-pill br-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Sequence Field</td>
<td style='word-wrap: break-word; white-space: normal;'>The currently included Sequence field is blank across all instruments and will be removed.</td>
<td style='text-align: center;'><span class='br-pill br-tbd'>TBD</span></td>
</tr>
</tbody></table>


### Behavior & Child-Caregiver Interaction
<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>ERICA</td>
<td style='word-wrap: break-word; white-space: normal;'>Remove date taken, age, and language fields (computed based on <em>date coded</em>) to exclude from patch 2.1 <em>[BR data only]</em>.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>ERICA</td>
<td style='word-wrap: break-word; white-space: normal;'>For a subset of participants, ERICA Codes (N=17) or Reliability (N=2) form scores are inaccurate; corrected scores are available to DUC-authorized users via the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>. Users should further exclude participants with values of 0 across all scores (N=23 Codes, 12 Reliability) prior to analysis.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>FAD</td>
<td style='word-wrap: break-word; white-space: normal;'>N=4 V06 participants with &lt;3 item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>MAPS-TL</td>
<td style='word-wrap: break-word; white-space: normal;'>Notes appear in the score field in both versions (Infant/Toddlerhood) and will be moved to a separate field.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>MAPS-TL (&lt;1yr)</td>
<td style='word-wrap: break-word; white-space: normal;'>N=4 participants with no item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='br-pill br-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>ecPROMIS CC</td>
<td style='word-wrap: break-word; white-space: normal;'>N=12 V03 participants with &lt;3 item responses are incorrectly scored as <code>0</code> in <code>mh_cg_pms__cc__inf</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='br-pill br-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>ECBQ</td>
<td style='word-wrap: break-word; white-space: normal;'>Change coding for "Does not apply" to 8 to match the IBQ-R.</td>
<td style='text-align: center;'><span class='pr-pill'>R2.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>MAPS-TL (Tod)</td>
<td style='word-wrap: break-word; white-space: normal;'>Pro-rated scoring for <code>mh_cg_mapdb__tod</code> not yet implemented; N=16 participants missing scores.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
</tbody></table>


### Biospecimens & Omics

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Nails</td>
<td style='word-wrap: break-word; white-space: normal;'>Add unit (mg) for <code>nails_results_nail_weight</code> variable.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Nails</td>
<td style='word-wrap: break-word; white-space: normal;'>Nail type is <code>4</code> (Unknown) in the main results table (<code>*_nails_results</code>) and should be obtained from the specimen table (<code>*_nails_type</code>).</td>
<td style='text-align: center;'><span class='br-pill br-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Urine</td>
<td style='word-wrap: break-word; white-space: normal;'>Add creatinine results (<code>bio_creat_u</code>).</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
</tbody></table>


### Demographics

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Basic Demo</td>
<td style='word-wrap: break-word; white-space: normal;'>N=14 participants in <code>sed_basic_demographics</code> have a Maternal Age at V01 of 0; exclude these values from analyses until corrected.</td>
<td style='text-align: center;'><span class='br-pill br-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>RESTRUCTURE</td>
<td style='word-wrap: break-word; white-space: normal;'>The Demographics domain includes 2 tables with derived information grouped into visit-specific data (<a href="https://docs.hbcdstudy.org/latest/instruments/demo/visitinfo/">Visit Info</a>) and general demographics (<a href="https://docs.hbcdstudy.org/latest/instruments/demo/basicdemo/">Basic Demographics</a>). In a future release, these tables will be restructured to instead organize variables as either longitudinal (dynamic measures that change over time) or global (static measures, such as sex assigned at birth and race/ethnicity).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>SU Flags</td>
<td style='word-wrap: break-word; white-space: normal;'>A derived/rolled up substance use flag for Stimulants will be added based on positive instrument-specific Stimulant results.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Visit Info</td>
<td style='word-wrap: break-word; white-space: normal;'>SU flags will include Nail toxicology results in addition to Urine.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Visit Info</td>
<td style='word-wrap: break-word; white-space: normal;'>Date of missed visit (<code>visit_missed_date</code>) is currently excluded from the release due to inaccuracies and will be added once corrected.</td>
<td style='text-align: center;'><span class='br-pill br-tbd'>TBD</span></td>
</tr>
</tbody></table>


### EEG
<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Age fields</td>
<td style='word-wrap: break-word; white-space: normal;'>Chronological and adjusted age fall outside of 3-9 months in N=74 V03 sessions; exclude age values prior to analysis.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>MADE</td>
<td style='word-wrap: break-word; white-space: normal;'>N=3 V04 session derivatives are missing corresponding tabulated data for FACE/MMN tasks. See <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a> for impacted participant IDs.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
</tbody></table>


### MRI

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Run ID</td>
<td style='word-wrap: break-word; white-space: normal;'>The <code>run-{X}</code> field may not reflect chronological acquisition order. While this affects both <strong>raw BIDS and derivatives</strong>, data remain internally consistent (i.e. run IDs match between raw and processed datasets).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Scanner Info</td>
<td style='word-wrap: break-word; white-space: normal;'>Scanner information must currently be parsed from raw BIDS data (specifically the scans .tsv files), as described <a href="https://docs.hbcdstudy.org/latest/help/faq/#faq-scanner-info">here</a>. Future releases will include a dedicated 'MRI Info' table that summarizes scanner information across participants, similar to the ABCD study (<a href="https://docs.abcdstudy.org/latest/documentation/imaging/admin.html#mr_y_adm__info">see details</a>).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Source DICOMs</td>
<td style='word-wrap: break-word; white-space: normal;'>Add source DICOMs for all imaging modalities.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Summary Forms</td>
<td style='word-wrap: break-word; white-space: normal;'>Add MRI Scan Session + Data Summary Forms (information from the MRI technician obtained on day of scan).</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Var name length</td>
<td style='word-wrap: break-word; white-space: normal;'>Variable names for tabulated MRI data (particularly XCP-D outputs) can be upwards of 167 characters, which may exceed variable name limits in some software and lead to truncation or import errors.</td>
<td style='text-align: center;'><span class='br-pill br-tbd'>TBD</span></td>
</tr>
</tbody></table>


### Neurocognition & Language 
<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Data Type</td>
<td style='word-wrap: break-word; white-space: normal;'>Summary score variables in the Bayley and CDI are misclassified as text in the metadata, which may cause formatting issues in some tools.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>MLDS</td>
<td style='word-wrap: break-word; white-space: normal;'>Total non-parental hours/week (<code>ncl_ch_mlds_arr_hr_wk</code>) includes implausible values due to data entry errors. Exclude values &gt;168 hours from analysis.</td>
<td style='text-align: center;'><span class='br-pill br-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Bayley-4</td>
<td style='word-wrap: break-word; white-space: normal;'>Add item-level scores.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<!-- <tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>CDI</td>
<td style='word-wrap: break-word; white-space: normal;'>Set percentile scores in <code>ncl_ch_cdiwgen</code> (with the exception of <code>percentile_both</code>) to data type=integer.</td>
<td style='text-align: center;'><span class='br-pill br-tbd'>TBD</span></td>
</tr> -->
</tbody></table>


### Physical Health

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'>Confirm that negative <code>ph_ch_anthro_adjusted_age</code>  data point is accurate.</td>
<td style='text-align: center;'><span class='br-pill br-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'>Remove <code>ph_ch_anthro_002</code>.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'>The Data Dictionary element <code>type_data</code> for <code>average_bmi</code> will be corrected to <code>double</code> (currently=<code>character</code>).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'>Growth (<code>ph_ch_anthro</code>) filter ranges will be updated to be visit-specific, as current ranges allow biologically implausible values (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Range Checks</a>).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>BISQ-SF</td>
<td style='word-wrap: break-word; white-space: normal;'>Add Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>.</td>
<td style='text-align: center;'><span class='br-pill br-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'>Add age-based z-scores to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Z-Scores Excluded</a>).</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'>Add sex-specific birth weight to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Sex-Specific Birthweight for GA</a>).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Vision Screener</td>
<td style='word-wrap: break-word; white-space: normal;'>Add more fields to <code>ph_ch_vs</code> (current release only includes completion status and overall screening results).</td>
<td style='text-align: center;'><span class='br-pill br-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>ecPROMIS- Sleep</td>
<td style='word-wrap: break-word; white-space: normal;'>Add <code>ph_cg_pms__sleep</code>  summary scores</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>ecPROMIS-PAG</td>
<td style='word-wrap: break-word; white-space: normal;'>Add scores to <code>ph_cg_pms__pags</code>. Until added, scores can be calculated by following the <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/ecpromis-pags/#scoring">Scoring Procedures</a> documentation.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
</tbody></table>


### Pregnancy & Exposure
<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>APA 1/2</td>
<td style='word-wrap: break-word; white-space: normal;'>APA Level 2 was sometimes administered despite unmet gating criteria (e.g., missing Level 1 responses). These cases are not scored (“No additional inquiry required”) even when Level 2 responses are present. Level 2 item data will be removed to avoid confusion.</td>
<td style='text-align: center;'><span class='br-pill br-212'>21.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>EPDS</td>
<td style='word-wrap: break-word; white-space: normal;'>Inconsistent scoring: (1) item responses present, but score is null (N=1); (2) all items null, but score is <code>0</code> (N≥3).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Healthv2 Preg</td>
<td style='word-wrap: break-word; white-space: normal;'>The field for the date when PNV was stopped (<code>pex_bm_healthv2_preg__exp__pnv_007__01</code>) is blank, despite participants having reported stopping.</td>
<td style='text-align: center;'><span class='br-pill br-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Healthv2 Preg</td>
<td style='word-wrap: break-word; white-space: normal;'>Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank.</td>
<td style='text-align: center;'><span class='br-pill br-tbd'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>TLFB</td>
<td style='word-wrap: break-word; white-space: normal;'>PNR data were incorrectly reported using TLFB versions 1/2 and will be updated to <a href="https://docs.hbcdstudy.org/latest/instruments/pregexp/su/tlfb/#v3">version 3 specific to PNR</a>.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>PEX Health</td>
<td style='word-wrap: break-word; white-space: normal;'>ICD codes for the <code>pex_bm_health*</code> instrument tables are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <em>Health V1- Medications</em>, while the <em>Health V2- Pregnancy</em> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a></td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
</tbody></table>


### Social & Environmental Determinants
<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>C-PACEs</td>
<td style='word-wrap: break-word; white-space: normal;'>Summary scores are inaccurate; until corrected, users can compute scores following the provided scoring documentation.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Demo</td>
<td style='word-wrap: break-word; white-space: normal;'>Remove descriptive fields (e.g. <code>roster_001__00</code>) <em>[BR data only]</em>.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>eHITS</td>
<td style='word-wrap: break-word; white-space: normal;'>Participants missing all item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='br-pill br-212'>21.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Demo</td>
<td style='word-wrap: break-word; white-space: normal;'>Add <code>work_{002–004}_post</code> (worked for pay/≥20/≥35 hours while pregnant) and <code>work_004__01</code> (job held ≥1 month since V01) (adult table).</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Demo</td>
<td style='word-wrap: break-word; white-space: normal;'>Add V01 household income (<code>income_002</code>) (adult table).</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Demo</td>
<td style='word-wrap: break-word; white-space: normal;'>Add variables on Other Biological Parent (adult table).</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i></td>
<td>Demo</td>
<td style='word-wrap: break-word; white-space: normal;'>Add household roster fields capturing the sex of listed individuals (adult &amp; child tables).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
</tbody></table><!-- END KNOWN_ISSUES_TABLE -->


  <br>

