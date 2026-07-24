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
  background-color: #e6f0ff; 
  color: #1a4fb3;
}
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
.tbd-pill {
  display: inline-block;
  padding: 2px 8px;
  font-size: 0.75em;
  font-weight: 600;
  border-radius: 999px;
  line-height: 1.4;
  white-space: nowrap;
  background-color: #f1f3f5; 
  color: #666; 
  font-style: italic;
}
</style>

<div class="pill-center">
<a href="../../#data-quality-checks" target="_blank" class="pill-link-wrapper">
<span class="pill-link"><span class="tooltip"><i class="fa-solid fa-clipboard-check" style="color: #6300d3;"></i><span class="tooltiptext">Data quality checks<br><i>Click to learn more</i></span></span></span></a>
<a href="../../#transparency" target="_blank" class="pill-link-wrapper">
<span class="pill-link"><span class="tooltip"><i class="fa-solid fa-eye" style="color: #6300d3;"></i><span class="tooltiptext">Transparency<br><i>Click to learn more</i></span></span></span></a>
</div>

# Known Issues & Pending Updates

!!! danger "Active Items Only"
    This page lists ACTIVE issues/pending updates either targeted for upcoming BRs or still pending final Workgroup/SME sign-off. Items are not considered resolved until final review and approval by Workgroup/SME. Note that items addressed in a BR are not reflected as resolved in the [public release documentation](https://docs.hbcdstudy.org/latest/changelog/issues-updates/) until the corresponding PR is released.

    <b>FOR A LIST OF RESOLVED ITEMS, SEE</b> <a href="../resolved-archive.html" target="_blank"><b>Resolved Issues & Updates Archive</b></a>   

---

<p style="font-size: 1.2em; color: #555; text-align: center; line-height: 2;">
<i class="fas fa-bug" style="color: #f97316; font-size: 1em;"></i> = Known Issue &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-rotate" style="color: #199bd6; font-size: 1em;"></i> = Pending Update &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.1em;"></i> = Target Fix <i>(BR if known, otherwise public R#/TBD)</i>
</p>
    
<!-- BEGIN KNOWN_ISSUES_TABLE -->
### Behavior &amp; Child-Caregiver Interaction

!!! info "Resolved items are archived to [Resolved Issues & Updates Archive](resolved-archive.html) (domain MH)"

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
<td><i class="fas fa-bug icon-bug"></i></td>
<td>FAD</td>
<td>N=4 V06 participants with &lt;3 item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>MAPS-TL (&lt;1yr)</td>
<td>N=4 participants with no item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>ecPROMIS CC</td>
<td>N=12 V03 participants with &lt;3 item responses are incorrectly scored as <code>0</code> in <code>mh_cg_pms__cc__inf</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ECHO</td>
<td>Addition of the Early Child Care and Education</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ERICA</td>
<td>A future release will include reliability codes integrated into the primary coding dataset. Until then, users must perform this integration manually: <strong>see the ERICA <a href="../../instruments/bcgi/erica/#warning">Data Warning</a> for instructions.</strong><br />
Instructions include cleaning the current files to exclude n=44 participants with incorrect code values (data entry/form errors) and capping <code>b_raw</code> values at 3.0 (n=3 participants). These issues will also be corrected in future release data.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ERICA</td>
<td>Add all age and <code>date_taken</code> fields (currently excluded due to use of coding rather than visit dates).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ERICA</td>
<td>Remove <code>locomotor_ability</code> fields from both tables</td>
<td style='text-align: center;'><span class='br-pill'>30</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>MAPS-EASI</td>
<td>Addition of the MAPS-EASI- Toddler</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>MAPS-TL (Tod)</td>
<td>Pro-rated scoring for <code>mh_cg_mapdb__tod</code> not yet implemented; N=16 participants missing scores.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>MCHAT</td>
<td>Addition of the Modified Checklist for Autism in Toddlers</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
</tbody></table>


### Biospecimens &amp; Omics

!!! info "Resolved items are archived to [Resolved Issues & Updates Archive](resolved-archive.html) (domain BIO)"

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
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Nails</td>
<td>Nail type is <code>4</code> (Unknown) in the main results table (<code>*_nails_results</code>) and should be obtained from the specimen table (<code>*_nails_type</code>).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Blood</td>
<td>Inclusion of Blood Spot Card Results data from USDTL.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
</tbody></table>


### Demographics

!!! info "Resolved items are archived to [Resolved Issues & Updates Archive](resolved-archive.html) (domain Demo)"

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
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Basic Demo</td>
<td>N=14 participants in <code>sed_basic_demographics</code> have a Maternal Age at V01 of 0; exclude these values from analyses until corrected.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>TLFB</td>
<td>PNR data were incorrectly reported using TLFB versions 1/2 and will be updated to <a href="https://docs.hbcdstudy.org/latest/instruments/pregexp/su/tlfb/#v3">version 3 specific to PNR</a></td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>RESTRUCTURE</td>
<td>The Demographics domain includes 2 tables with derived information grouped into visit-specific data (<a href="https://docs.hbcdstudy.org/latest/instruments/demo/visitinfo/">Visit Info</a>) and general demographics (<a href="https://docs.hbcdstudy.org/latest/instruments/demo/basicdemo/">Basic Demographics</a>). In a future release, these tables will be restructured to instead organize variables as either longitudinal (dynamic measures that change over time) or global (static measures, such as sex assigned at birth and race/ethnicity).</td>
<td style='text-align: center;'><span class='br-pill'>30</span></td>
</tr>
</tbody></table>


### EEG

!!! info "Resolved items are archived to [Resolved Issues & Updates Archive](resolved-archive.html) (domain EEG)"

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
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Age fields</td>
<td>Chronological and adjusted age fall outside of 3-9 months in N=74 V03 sessions (site entry errors); exclude age values prior to analysis.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>MADE v1.7.0</td>
<td>HBCD-MADE derivatives processed through updated version v1.7.0</td>
<td style='text-align: center;'><span class='br-pill'>30</span></td>
</tr>
</tbody></table>


### General

!!! info "Resolved items are archived to [Resolved Issues & Updates Archive](resolved-archive.html) (domain NA)"

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
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Implausible GA</td>
<td>A small subset of participants have implausible <code>gestational_age</code> (V01 only) values  for one or more instrument. Until corrected, review GA distribution to exclude outliers from analysis (should be positive and generally &lt; 45 weeks).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Instruction</td>
<td>The 'instruction' data dictionary element is currently blank.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Score text</td>
<td>Text inappropriately located in score fields where score is missing to be moved to corresponding 'notes' field (impacts ecPROMIS-PAGS; MAPS-TL; SPM-2).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Multibirth Cohorts</td>
<td>Missing instrument fields for Sibling cohorts will be populated and <em>FamilyID</em> will be added to help identify siblings - <a href="https://docs.hbcdstudy.org/latest/instruments/demo/visitinfo/#warning">see details</a>.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Sequence Field</td>
<td>The currently included Sequence field is blank across all instruments and will be removed.</td>
<td style='text-align: center;'><span class='tbd-pill'>TBD</span></td>
</tr>
</tbody></table>


### MRI

!!! info "Resolved items are archived to [Resolved Issues & Updates Archive](resolved-archive.html) (domain MRI)"

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
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Run ID</td>
<td>The <code>run-{X}</code> field may not reflect chronological acquisition order. While this affects both <strong>raw BIDS and derivatives</strong>, data remain internally consistent (i.e. run IDs match between raw and processed datasets).</td>
<td style='text-align: center;'><span class='tbd-pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Cook&#x27;s Distance</td>
<td>Addition Cook's distance values computed for fMRI.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>QSIRecon</td>
<td>Tabulated data for QSIRecon (participant data combined across derivative files into single tidy table) will be provided in a future release.</td>
<td style='text-align: center;'><span class='tbd-pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Source DICOMs</td>
<td>Add source DICOMs for all imaging modalities.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
</tbody></table>


### Neurocognition &amp; Language

!!! info "Resolved items are archived to [Resolved Issues & Updates Archive](resolved-archive.html) (domain NCL)"

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
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Bayley</td>
<td>Remove invalid scores of <code>-9999</code>; until resolved, users should remove this participant data prior to analysis.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>MLDS</td>
<td>Total non-parental hours/week (<code>ncl_ch_mlds_arr_hr_wk</code>) includes implausible values due to data entry errors. Exclude values &gt;168 hours from analysis.</td>
<td style='text-align: center;'><span class='tbd-pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>CDI-2</td>
<td>Addition of the MacArthur-Bates CDI-2 Language</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Vineland</td>
<td>The Coping Skills, Domestic, and Written subscales are not administered at V05 because children are too young. However, for some participants, the missing reason is incorrectly coded as "Logic skipped" or "Unknown" in the shadow matrix.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>

</tbody></table>


### Novel Tech &amp; Wearable Sensors

!!! info "Resolved items are archived to [Resolved Issues & Updates Archive](resolved-archive.html) (domain NT)"

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
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>GABI</td>
<td>Addition of raw BIDS data for GABI (infant heart rate).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
</tbody></table>


### Physical Health

!!! info "Resolved items are archived to [Resolved Issues & Updates Archive](resolved-archive.html) (domain PH)"

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
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Growth</td>
<td>Adjusted age contains N=303 "unknown missing" values that are also missing 'Date of Administration'.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Growth</td>
<td>The data dictionary element <code>type_data</code> for <code>average_bmi</code> will be corrected to <code>double</code> (currently=<code>character</code>).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Growth</td>
<td>Growth (<code>ph_ch_anthro</code>) filter ranges will be updated to be visit-specific, as current ranges allow biologically implausible values (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Range Checks</a>).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>BISQ-SF</td>
<td>Add Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>.</td>
<td style='text-align: center;'><span class='tbd-pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Child Nutrition</td>
<td>Addition of the Child Nutrition Questionnaire.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Growth</td>
<td>Add sex-specific birth weight to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Sex-Specific Birthweight for GA</a>).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>PEDsQL</td>
<td>Addition of the PEDsQL</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Vision Screener</td>
<td>Add more fields to <code>ph_ch_vs</code> (current release only includes completion status and overall screening results).</td>
<td style='text-align: center;'><span class='tbd-pill'>TBD</span></td>
</tr>

</tbody></table>


### Pregnancy &amp; Environmental Exposure

!!! info "Resolved items are archived to [Resolved Issues & Updates Archive](resolved-archive.html) (domain PEX)"

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
<td><i class="fas fa-bug icon-bug"></i></td>
<td>EPDS</td>
<td>Inconsistent scoring: (1) item responses present, but score is null (N=1); (2) all items null, but score is <code>0</code> (N≥3).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Healthv2 Preg</td>
<td>The field for the date when PNV was stopped (<code>pex_bm_healthv2_preg__exp__pnv_007__01</code>) is blank, despite participants having reported stopping.</td>
<td style='text-align: center;'><span class='tbd-pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Healthv2 Preg</td>
<td>Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank.</td>
<td style='text-align: center;'><span class='tbd-pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>PEX Health</td>
<td>ICD codes for the <code>pex_bm_health*</code>  tables are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <em>Health V1- Medications</em>, while the <em>Health V2- Pregnancy</em> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a></td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
</tbody></table>


### Social &amp; Environmental Determinants

!!! info "Resolved items are archived to [Resolved Issues & Updates Archive](resolved-archive.html) (domain SED)"

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
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Demo</td>
<td>Relationship status was inappropriately collected at V02/V03 for all cohorts and should have been restricted to cases where there was a change in caregiver (i.e. only Alternative Caregiver cohorts should have this field populated). Data for non-ACG cohorts to be excluded.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Demo</td>
<td>Roster was inappropriately collected at V02/V03 for all cohorts and should have been restricted to V02 PNRs and alternate caregiver cohorts; to be excluded.</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>eHITS</td>
<td>Participants missing all item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='tbd-pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Demo</td>
<td>Add household roster fields capturing the sex of listed individuals (adult &amp; child tables).</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Demo</td>
<td>Addition of V6 Adult</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Demo</td>
<td>Addition of V6 Child</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>GLED</td>
<td>Addition of Geocoded Linkage from Home and Work Addresses</td>
<td style='text-align: center;'><span class='br-pill'>30</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Incarceration</td>
<td>Addition of the Incarceration Questionnaire</td>
<td style='text-align: center;'><span class='pr-pill'>R3</span></td>
</tr>
</tbody></table><!-- END KNOWN_ISSUES_TABLE -->


  <br>

