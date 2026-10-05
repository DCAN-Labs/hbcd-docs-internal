<style>
.wy-nav-content {
    width: 90% !important;
    max-width: 90% !important;
    flex-grow: 1 !important;
}

/* Known issues filter controls */
.archive-controls {
  margin: 1.5rem 0 1rem;
  padding: 1rem 1.1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  background: #f8f9fa;
}

.archive-controls-row {
  display: flex;
  flex-wrap: wrap;
  gap: 0.6rem;
  align-items: center;
}

.archive-search {
  flex: 1 1 280px;
  min-width: 220px;
}

.archive-controls input,
.archive-controls select,
.archive-controls button {
  box-sizing: border-box;
  height: 38px;
  border: 1px solid #cfd4da;
  border-radius: 5px;
  background: white;
  padding: 0 0.75rem;
  font: inherit;
  font-size: 0.9rem;
}

.archive-controls input:focus,
.archive-controls select:focus,
.archive-controls button:focus {
  outline: 2px solid rgba(25, 155, 214, 0.25);
  border-color: #199bd6;
}

.archive-controls button {
  cursor: pointer;
  font-weight: 600;
}

.archive-controls button:hover {
  background: #f1f3f5;
}

.archive-status {
  margin-top: 0.65rem;
  font-size: 0.85rem;
  color: #666;
}

.archive-empty {
  display: none;
  padding: 2rem 1rem;
  text-align: center;
  color: #777;
  font-size: 0.95rem;
}

@media (max-width: 700px) {
  .archive-controls-row {
    align-items: stretch;
  }

  .archive-controls input,
  .archive-controls select,
  .archive-controls button {
    width: 100%;
  }

  .archive-search {
    flex-basis: 100%;
  }
}
</style>

# Known Issues & Pending Updates
!!! info "Resolved Issues Archive"
    See the [Resolved Issues Archive](resolved-archive.html) for a running list of all previously resolved issues and updates.

This page lists ACTIVE issues/pending updates either targeted for upcoming BRs or still pending final Workgroup/SME sign-off. Items are not considered resolved until final review and approval by Workgroup/SME. Note that items addressed in a BR are not reflected as resolved in the [public release documentation](https://docs.hbcdstudy.org/latest/changelog/issues-updates/) until the corresponding PR is released. For a list of resolved items, see [Resolved Issues & Updates Archive](resolved-archive.html).

---

<p style="font-size: 1.2em; color: #555; text-align: center; line-height: 2;">
<i class="fas fa-bug" style="color: #f97316; font-size: 1em;"></i> = Known Issue &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-rotate" style="color: #199bd6; font-size: 1em;"></i> = Pending Update
</p>

<div class="archive-controls" aria-label="Known issues filters">
  <div class="archive-controls-row">
    <input
      id="ki-search"
      class="archive-search"
      type="search"
      placeholder="Search table/topic or summary..."
      aria-label="Search known issues"
    >

    <select id="ki-domain" aria-label="Filter by domain">
      <option value="">All domains</option>
    </select>

    <select id="ki-target" aria-label="Filter by target release">
      <option value="">All targets</option>
    </select>

    <select id="ki-type" aria-label="Filter by type">
      <option value="">All types</option>
      <option value="issue">Known Issues</option>
      <option value="update">Pending Updates</option>
    </select>
    <button id="ki-reset" type="button">Clear filters</button>
  </div>
  <div id="ki-status" class="archive-status" aria-live="polite"></div>
</div>

<div id="ki-empty" class="archive-empty">No matching issues or updates found.</div>

<!-- BEGIN KNOWN_ISSUES_TABLE -->
### All Data / General

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Blank Fields for Siblings</td>
<td>Family-level (i.e., non-child-specific) instrument fields are currently populated only for the Main Child, not sibling records (e.g., HBCD Multiple Birth – Sibling). Until resolved, users should obtain family-level values for sibling participants from the corresponding Main Child record. See the participant ID mapping in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Incorrect JSONs</td>
<td>Metadata field values were corrected for several instruments, but are not yet corrected in the JSON files. IN PARTICULAR, PLEASE CHECK <code>type_data</code> CAREFULLY as an incorrect data type may impact analyses. Impacted instruments include: <strong>APA 1/2</strong>, <strong>Bayley-4</strong>, and <strong>EEG Form-2</strong>. See details in <a href="../release-notes/#data-warning">Release Notes</a>.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>FamilyID</td>
<td>A <code>FamilyID</code> field will be added to instruments to identify sibling relationships. Until then, sibling ID mapping (Main Child vs Sibling) is provided in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Implausible GA</td>
<td>A small subset of participants have implausible <code>gestational_age</code> (V01 only) values for one or more instrument. Until corrected, review GA distribution to exclude outliers from analysis (should be positive and generally &lt; 45 weeks).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Score text</td>
<td>Text inappropriately located in score fields where score is missing to be moved to corresponding 'notes' field (impacts ecPROMIS-PAGS; MAPS-TL; SPM-2).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Instruction</td>
<td>The 'instruction' data dictionary element is currently blank.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Sequence Field</td>
<td>The currently included Sequence field is blank across all instruments and will be removed.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


### Behavior &amp; Child-Caregiver Interaction

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>FAD</td>
<td>N=4 V06 participants with &lt;3 item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>MAPS-TL (&lt;1yr)</td>
<td>N=4 participants with no item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>ecPROMIS CC</td>
<td>N=12 V03 participants with &lt;3 item responses are incorrectly scored as <code>0</code> in <code>mh_cg_pms__cc__inf</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ERICA</td>
<td>A future release will include reliability codes integrated into the primary coding dataset. Until then, users must perform this integration manually: see the ERICA Data Warning for instructions. Instructions include cleaning the current files to exclude n=44 participants with incorrect code values (data entry/form errors), capping <code>b_raw</code> values at 3.0 (n=3 participants), and removing the “Locomotor Ability” field (<code>mh_cg_erica_3_9m_locomotor_ability</code>), which has errors, also to be corrected in the next release.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>MAPS-EASI</td>
<td>Addition of the MAPS-EASI- Toddler</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>MAPS-TL (Tod)</td>
<td>Pro-rated scoring for <code>mh_cg_mapdb__tod</code> not yet implemented; N=16 participants missing scores.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ERICA</td>
<td>Add all age and <code>date_taken</code> fields (currently excluded due to use of coding rather than visit dates).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>ECHO</td>
<td>Addition of the Early Child Care and Education</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


### Biospecimens &amp; Omics

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Blood</td>
<td>Inclusion of Blood Spot Card Results data from USDTL.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Nails</td>
<td>Nail type is <code>4</code> (Unknown) in the main results table (<code>*_nails_results</code>) and should be obtained from the specimen table (<code>*_nails_type</code>).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
</tbody></table>


### Demographics

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>TLFB</td>
<td>PNR data were incorrectly reported using TLFB versions 1/2 and will be updated to <a href="https://docs.hbcdstudy.org/latest/instruments/pregexp/su/tlfb/#v3">version 3 specific to PNR</a></td>
<td style='text-align: center;'><span class='pill'>R3.0</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Basic Demo</td>
<td>N=14 participants in <code>sed_basic_demographics</code> have a Maternal Age at V01 of 0; exclude these values from analyses until corrected.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Basic Demo</td>
<td>The <code>screen_race_multi__*</code> variables are almost entirely coded as '0' and should not be used for analysis. Users interested in race and ethnicity information should instead use the corresponding derived ACS race and ethnicity variable. Values will be corrected in a future release.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Visit Info</td>
<td>Harmonize participant status and withdrawal fields</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
</tbody></table>


### EEG

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Age fields</td>
<td>Chronological and adjusted age fall outside of 3-9 months in N=74 V03 sessions (site entry errors); exclude age values prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>R3.1</span></td>
</tr>
</tbody></table>


### MRI

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>QSIRecon</td>
<td>Tabulated data for QSIRecon (participant data combined across derivative files into single tidy table) will be provided in a future release.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Scanner info</td>
<td>Scanner metadata, currently available within the raw BIDS Scans TSV files, will be additionally provided within the tabulated data for ease of access (see <a href="#infobbox">Participant Derived</a> domain info on this page).</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td></td>
<td>All 0s for numeric values in tabulated XCP-D derivatives</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Cook&#x27;s Distance</td>
<td>Addition Cook's distance values computed for fMRI.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Postprocessing</td>
<td>Addition of individual functional network maps (generated with template matching) and <a href="https://modelarrayio.readthedocs.io/en/latest/">ModelArray</a> outputs for XCP-D for efficient voxel-wise statistical modeling.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>fmap QC</td>
<td>Additional QC fields added to the scans TSV files related to line artifacts in fmaps (<code>line2_*</code>)</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Run ID</td>
<td>The <code>run-{X}</code> field may not reflect chronological acquisition order. While this affects both <strong>raw BIDS and derivatives</strong>, data remain internally consistent (i.e. run IDs match between raw and processed datasets).</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>dMRI metadata</td>
<td><code>LargeDelta</code> and <code>SmallDelta</code> in the sidecars currently are set to vendor-specific values (which aren't always correct because the models have their own values) and will be updated to reflect accurate values.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Raw QC Metrics</td>
<td>Raw MR data QC metrics provided in the raw BIDS SCANS TSV files will be combined into a single table across participants/sessions.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


### Neurocognition &amp; Language

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>CDI</td>
<td>Percentiles incorrectly converted for N=36 cases, resulting in values &gt;100 ('Adjusted Percentile' incorrectly parsed from 'Total Produced' instead of 'Total Produced Percentile-sex (adjusted)')</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Bayley</td>
<td>Remove invalid scores of <code>-9999</code>; until resolved, users should remove this participant data prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Vineland</td>
<td>The Coping Skills, Domestic, and Written subscales are not administered at V05 because children are too young. However, for some participants, the missing reason is incorrectly coded as "Logic skipped" or "Unknown" in the shadow matrix. In addition, the age of one child is outside of the valid bounds for V05.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>MLDS</td>
<td>Total non-parental hours/week (<code>ncl_ch_mlds_arr_hr_wk</code>) includes implausible values due to data entry errors. Exclude values &gt;168 hours from analysis.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


### Physical Health

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Anthropometrics</td>
<td>Add sex-specific birth weight to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Sex-Specific Birthweight for GA</a>).</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Anthropometrics</td>
<td>Adjusted age contains N=303 "unknown missing" values that are also missing 'Date of Administration'.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Anthropometrics</td>
<td>Growth (<code>ph_ch_anthro</code>) filter ranges will be updated to be visit-specific, as current ranges allow biologically implausible values (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Range Checks</a>).</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Anthropometrics</td>
<td>The data dictionary element <code>type_data</code> for <code>average_bmi</code> will be corrected to <code>double</code> (currently=<code>character</code>).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>BISQ-SF</td>
<td>Add Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Vision Screener</td>
<td>Add more fields to <code>ph_ch_vs</code> (current release only includes completion status and overall screening results).</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


### Pregnancy &amp; Environmental Exposure

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>EPDS</td>
<td>Inconsistent scoring: (1) item responses present, but score is null (N=1); (2) all items null, but score is <code>0</code> (N≥3).</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>PEX Health</td>
<td>ICD codes for the <code>pex_bm_health*</code> tables are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <em>Health V1- Medications</em>, while the <em>Health V2- Pregnancy</em> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a></td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Healthv2 Preg</td>
<td>The field for the date when PNV was stopped (<code>pex_bm_healthv2_preg__exp__pnv_007__01</code>) is blank, despite participants having reported stopping.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Healthv2 Preg</td>
<td>Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


### Social &amp; Environmental Determinants

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Demo</td>
<td>Roster was inappropriately collected at V02/V03 for all cohorts and should have been restricted to V02 PNRs and alternate caregiver cohorts; to be excluded.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>eHITS</td>
<td>Participants missing all item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>GLED</td>
<td>Addition of Geocoded Linkage from Home and Work Addresses</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i></td>
<td>Demo</td>
<td>Relationship status was inappropriately collected at V02/V03 for all cohorts and should have been restricted to cases where there was a change in caregiver (i.e. only Alternative Caregiver cohorts should have this field populated). Data for non-ACG cohorts to be excluded.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>Demo</td>
<td>Add household roster fields capturing the sex of listed individuals (adult &amp; child tables).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i></td>
<td>TIC Questionnaire</td>
<td>Addition of TIC Questionnaire table</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
</tbody></table><!-- END KNOWN_ISSUES_TABLE -->


  <br>

<script>
document.addEventListener("DOMContentLoaded", function () {
  const container = document.querySelector(".wy-nav-content") || document.body;

  const searchInput = document.getElementById("ki-search");
  const domainSelect = document.getElementById("ki-domain");
  const targetSelect = document.getElementById("ki-target");
  const typeSelect = document.getElementById("ki-type");
  const resetButton = document.getElementById("ki-reset");
  const status = document.getElementById("ki-status");
  const emptyMessage = document.getElementById("ki-empty");

  if (!searchInput) return;

  // Each domain section is an <h3> heading immediately followed (in document
  // order) by its known-issues table.
  const sections = Array.from(container.querySelectorAll("h3"))
    .map(heading => {
      let table = heading.nextElementSibling;
      while (table && table.tagName !== "TABLE") {
        table = table.nextElementSibling;
      }
      const clone = heading.cloneNode(true);
      clone.querySelectorAll(".headerlink").forEach(link => link.remove());
      return { heading, table, domain: clone.textContent.trim() };
    })
    .filter(section => section.table && section.table.classList.contains("compact-table-no-vertical-lines"));

  sections.forEach(section => {
    domainSelect.add(new Option(section.domain, section.domain));
  });

  const targets = new Set();
  sections.forEach(section => {
    section.table.querySelectorAll("tbody tr").forEach(row => {
      const value = row.cells[3]?.textContent.trim();
      if (value) targets.add(value);
    });
  });

  Array.from(targets)
    .sort((a, b) => {
      const numA = parseFloat(a.replace(/^R/i, ""));
      const numB = parseFloat(b.replace(/^R/i, ""));
      if (!Number.isNaN(numA) && !Number.isNaN(numB) && a.toUpperCase() !== "TBD" && b.toUpperCase() !== "TBD") {
        return numA - numB;
      }
      return a.localeCompare(b, undefined, { numeric: true, sensitivity: "base" });
    })
    .forEach(value => targetSelect.add(new Option(value, value)));

  function normalize(value) {
    return value.toLowerCase().replace(/\s+/g, " ").trim();
  }

  function rowType(row) {
    return row.querySelector(".icon-bug") ? "issue" : "update";
  }

  function applyFilters() {
    const search = normalize(searchInput.value);
    const domain = domainSelect.value;
    const target = targetSelect.value;
    const type = typeSelect.value;

    let totalVisible = 0;
    let sectionsVisible = 0;

    sections.forEach(section => {
      if (domain && section.domain !== domain) {
        section.heading.style.display = "none";
        section.table.style.display = "none";
        return;
      }

      let visibleInSection = 0;

      section.table.querySelectorAll("tbody tr").forEach(row => {
        const topicValue = row.cells[1]?.textContent.trim() || "";
        const summaryValue = row.cells[2]?.textContent.trim() || "";
        const targetValue = row.cells[3]?.textContent.trim() || "";

        const matchesSearch =
          !search ||
          normalize(topicValue).includes(search) ||
          normalize(summaryValue).includes(search) ||
          normalize(section.domain).includes(search);

        const matchesTarget = !target || targetValue === target;
        const matchesType = !type || rowType(row) === type;

        const show = matchesSearch && matchesTarget && matchesType;
        row.style.display = show ? "" : "none";
        if (show) visibleInSection++;
      });

      const showSection = visibleInSection > 0;
      section.heading.style.display = showSection ? "" : "none";
      section.table.style.display = showSection ? "" : "none";

      if (showSection) sectionsVisible++;
      totalVisible += visibleInSection;
    });

    status.textContent =
      `Showing ${totalVisible} item${totalVisible === 1 ? "" : "s"} across ${sectionsVisible} domain${sectionsVisible === 1 ? "" : "s"}.`;
    emptyMessage.style.display = totalVisible === 0 ? "block" : "none";
  }

  [searchInput, domainSelect, targetSelect, typeSelect].forEach(control => {
    control.addEventListener("input", applyFilters);
    control.addEventListener("change", applyFilters);
  });

  resetButton.addEventListener("click", function () {
    searchInput.value = "";
    domainSelect.value = "";
    targetSelect.value = "";
    typeSelect.value = "";
    applyFilters();
  });

  applyFilters();
});
</script>

