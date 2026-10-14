<style>
.wy-nav-content {
    width: 100% !important;
    max-width:100% !important;
    flex-grow: 1 !important;
}
.compact-table-no-vertical-lines td:first-child,
.compact-table-no-vertical-lines th:first-child,
.compact-table-no-vertical-lines td:nth-child(2),
.compact-table-no-vertical-lines th:nth-child(2) {
    white-space: nowrap !important;
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
<td><i class="fas fa-bug icon-bug"></i> ID-83</td>
<td>Incorrect JSONs</td>
<td>Metadata field values were corrected for several instruments, but are not yet corrected in the JSON files. IN PARTICULAR, PLEASE CHECK <code>type_data</code> CAREFULLY as an incorrect data type may impact analyses. Impacted instruments include: <strong>APA 1/2</strong>, <strong>Bayley-4</strong>, and <strong>EEG Form-2</strong>. See details in <a href="../release-notes/#data-warning">Release Notes</a>.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-36</td>
<td>Score text</td>
<td>Text inappropriately located in score fields where score is missing to be moved to corresponding 'notes' field (impacts ecPROMIS-PAGS; MAPS-TL; SPM-2).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-692</td>
<td>Concatenation</td>
<td>MRI, EEG and Axtivity derivative concatenation run directly on the de-ID bucket instead of the re-ID bucket</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-32</td>
<td>Implausible GA</td>
<td>A small subset of participants have implausible <code>gestational_age</code> (V01 only) values for one or more instrument. Until corrected, review GA distribution to exclude outliers from analysis (should be positive and generally &lt; 45 weeks).</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-84</td>
<td>FamilyID</td>
<td>A <code>FamilyID</code> field will be added to instruments to identify sibling relationships. Until then, sibling ID mapping (Main Child vs Sibling) is provided in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-121</td>
<td>Instruction</td>
<td>Instruction text in each form's metadata is automatically extracted from the most recent <code>instruction</code> field in the REDCap Data Dictionary (based on field order). Because this process is automated, it may produce the following issues: (1) If an instruction spans multiple fields, only the last portion will be captured and/or (2) Some fields may display text intended for a previous section. Until this is corrected, please refer to original forms for accurate instruction text.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-142</td>
<td>Instruction</td>
<td>The 'instruction' data dictionary element is currently blank.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-110</td>
<td>Sequence Field</td>
<td>The currently included Sequence field is blank across all instruments and will be removed.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-22</td>
<td>Blank Fields for Siblings</td>
<td>Family-level (i.e., non-child-specific) instrument fields are currently populated only for the Main Child, not sibling records (e.g., HBCD Multiple Birth – Sibling). Until resolved, users should obtain family-level values for sibling participants from the corresponding Main Child record. See the participant ID mapping in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
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
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-69</td>
<td>MCHAT</td>
<td>Addition of the Modified Checklist for Autism in Toddlers</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-24</td>
<td>FAD</td>
<td>N=4 V06 participants with &lt;3 item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-27</td>
<td>ecPROMIS CC</td>
<td>N=12 V03 participants with &lt;3 item responses are incorrectly scored as <code>0</code> in <code>mh_cg_pms__cc__inf</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-68</td>
<td>MAPS-EASI</td>
<td>Addition of the MAPS-EASI- Toddler</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-100</td>
<td>CHAOS</td>
<td>Shift item values to start with value of 1 instead of 0 for normalization.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-101</td>
<td>IBQ-R &amp; ECBQ</td>
<td>Shift item values to start with value of 1 instead of 0 for normalization.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-21</td>
<td>ERICA</td>
<td>Reliability codes integrated into the primary coding dataset and no longer requires manual user generation (see <a href="https://docs.hbcdstudy.org/r2.1/instruments/bcgi/erica/#data-warning">2.1 data warning</a> for details).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-26</td>
<td>MAPS-TL (Tod)</td>
<td>Pro-rated scoring for <code>mh_cg_mapdb__tod</code> not yet implemented; N=16 participants missing scores.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-45</td>
<td>ERICA</td>
<td>Add all age and <code>date_taken</code> fields (currently excluded due to use of coding rather than visit dates).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-89</td>
<td>FAD</td>
<td>Shift item values to start with value of 1 instead of 0 for normalization.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-92</td>
<td>MAPS-TL, ecPROMIS</td>
<td>Shift item values to start with value of 1 instead of 0 for normalization.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-30</td>
<td>MAPS-TL (&lt;1yr)</td>
<td>N=4 participants with no item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-52</td>
<td>MAPS-EASI</td>
<td>Merge <code>total_score</code> and <code>prorated_score</code> fields into a new <code>summary_score</code> field and remove.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-686</td>
<td>V03 age &gt;1.5y</td>
<td>Resolve age for small number of V03 participants in MAPS-TL and ecPROMIS over 1.5 years old.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-146</td>
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
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-44</td>
<td>Blood</td>
<td>Inclusion of Blood Spot Card Results data from USDTL.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-42</td>
<td>Nails</td>
<td>Nail type is <code>4</code> (Unknown) in the main results table (<code>*_nails_results</code>) and should be obtained from the specimen table (<code>*_nails_type</code>).</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-693</td>
<td>USDTL Blood</td>
<td>Convert values of 999 to null. Users must do this manually until resolved prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-687</td>
<td>BAP</td>
<td>Biospecimen timestamps for BAP data flow.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
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
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-655</td>
<td>MADE v1.7.0</td>
<td>HBCD-MADE derivatives processed through updated version v1.7.0</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-55</td>
<td>Age fields</td>
<td>Chronological and adjusted age fall outside of 3-9 months in N=74 V03 sessions (site entry errors); exclude age values prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
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
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-657</td>
<td>Source DICOMs</td>
<td>Add source DICOMs for all imaging modalities.</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-108</td>
<td>Scanner info</td>
<td>Scanner metadata, currently available within the raw BIDS Scans TSV files, will be additionally provided within the tabulated data for ease of access (see <a href="#infobbox">Participant Derived</a> domain info on this page).</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-86</td>
<td>QSIRecon</td>
<td>Tabulated data for QSIRecon (participant data combined across derivative files into single tidy table) will be provided in a future release.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-667</td>
<td>Tabulated XCP-D</td>
<td>Resolved tabulation error resulting in all 0s for tabulated XCP-D numeric fields.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-73</td>
<td>Summary Forms</td>
<td>Fixed Sequence numbering in <code>mri_ra_chkl_data</code> to increment for <code>start_time</code> fields.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-28</td>
<td>Cook&#x27;s Distance</td>
<td>Addition Cook's distance values computed for fMRI.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-59</td>
<td>fmap QC</td>
<td>Frames containing line artifacts are removed from functional raw BIDS fmap files (in cases where the fmap file passes QC and is therefore used for data processing). Removed frames are documented in the scans TSV metadata files (see fields containing <code>line2_*</code>).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-680</td>
<td>ModelArray</td>
<td>Addition of <a href="https://modelarrayio.readthedocs.io/en/latest/">ModelArray</a> outputs derived from XCP-D and QSIRecon.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-685</td>
<td>XCP-D</td>
<td>New XCP-D pipeline outputs (processed with version 26.2.0) and updated hashes as a result.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-128</td>
<td>Run ID</td>
<td>The <code>run-{X}</code> field may not reflect chronological acquisition order. While this affects both <strong>raw BIDS and derivatives</strong>, data remain internally consistent (i.e. run IDs match between raw and processed datasets).</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-154</td>
<td>dMRI metadata</td>
<td><code>LargeDelta</code> and <code>SmallDelta</code> in the sidecars currently are set to vendor-specific values (which aren't always correct because the models have their own values) and will be updated to reflect accurate values.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-155</td>
<td>Raw QC Metrics</td>
<td>Raw MR data QC metrics provided in the raw BIDS SCANS TSV files will be combined into a single table across participants/sessions.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-681</td>
<td>ReproTM</td>
<td>Addition of individual functional network maps generated with template matching via ReproTM pipeline.</td>
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
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-63</td>
<td>Deferred Imitation</td>
<td>Addition of instrument: Deferred Imitation Task: Gong and Berry-Go-Round</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-661</td>
<td>CDI-2</td>
<td>Addition of the MacArthur-Bates CDI-2 Language</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-78</td>
<td>CDI</td>
<td>Percentiles incorrectly converted for N=36 cases, resulting in values &gt;100 ('Adjusted Percentile' incorrectly parsed from 'Total Produced' instead of 'Total Produced Percentile-sex (adjusted)')</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-93</td>
<td>CDI</td>
<td>Exclude open text fields.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-95</td>
<td>CDI</td>
<td>Include <code>total_produced_percentile_both</code> and <code>total_produced_percentile_both_adjusted</code>.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-80</td>
<td>Vineland</td>
<td>The Coping Skills, Domestic, and Written subscales are not administered at V05 because children are too young. However, for some participants, the missing reason is incorrectly coded as "Logic skipped" or "Unknown" in the shadow matrix. In addition, the age of one child is outside of the valid bounds for V05.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-119</td>
<td>MLDS</td>
<td>Total non-parental hours/week (<code>ncl_ch_mlds_arr_hr_wk</code>) includes implausible values due to data entry errors. Exclude values &gt;168 hours from analysis.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-54</td>
<td>Bayley</td>
<td>Remove invalid scores of <code>-9999</code>; until resolved, users should remove this participant data prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>


### Novel Tech &amp; Wearable Sensors

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-654</td>
<td>GABI</td>
<td>Addition of raw BIDS data for GABI (infant heart rate).</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-58</td>
<td>Axivity</td>
<td>Addition of concatenated Axivity table.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-691</td>
<td>GABI</td>
<td>Exclusion of <code>setup_004_status</code> from <code>nt_pa_gabi</code> instrument (GABI setup)</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
</tbody></table>


### Participant Derived

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-81</td>
<td>Static table</td>
<td>The <code>screen_race_multi__*</code> variables are almost entirely coded as '0' and should not be used for analysis. Users interested in race and ethnicity information should instead use the corresponding derived ACS race and ethnicity variable. Values will be corrected in a future release.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-106</td>
<td>All tables</td>
<td><ul>
<li>Static &amp; Dynamic: updated Domain &amp; Source </li>
<li>Dynamic: addition of visit missed and visit missed reason to <code>par_gd_dyn</code></li>
<li>Static table: [1] Resolve inconsistent use of 'Unknown' in the derived ACS variables, [2] Exclude non valid recruitment sites</li>
</ul></td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-669</td>
<td>Cannabis flag</td>
<td>Fixed description of Rolled up cannabis flag.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-678</td>
<td>Static table</td>
<td>Resolve inaccurate no response values for <code>par_gd_stc_acs_child_race_multi___0</code> (“Child race [multi-select] White”).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-34</td>
<td>Static table</td>
<td>N=14 participants have a Maternal Age at V01 of 0; exclude these values from analyses until corrected.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-676</td>
<td>MAD</td>
<td>Correct static maternal age at delivery.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-677</td>
<td>GAD</td>
<td>Correct static gestational age at delivery.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-671</td>
<td>SU flags</td>
<td>Make substance use flags in dynamic table cumulative.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-688</td>
<td>ACGs SU flag</td>
<td>Remove substance use survey for ACGs.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-37</td>
<td>TLFB</td>
<td>PNR data were incorrectly reported using TLFB versions 1/2 and will be updated to <a href="https://docs.hbcdstudy.org/latest/instruments/pregexp/su/tlfb/#v3">version 3 specific to PNR</a></td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-675</td>
<td>ADI</td>
<td>ADI in Static table (<code>par_gd_stc_adi_national_prcn</code>) is present, but completely unpopulated.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-679</td>
<td>Static table</td>
<td>AOU race checkbox/constructed-variable inconsistency.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-79</td>
<td>Visit Info</td>
<td>Harmonize participant status and withdrawal fields</td>
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
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-62</td>
<td>Child Nutrition</td>
<td>Addition of the Child Nutrition Questionnaire.</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-662</td>
<td>Med History V1</td>
<td>Addition of V06</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-70</td>
<td>PEDsQL</td>
<td>Addition of the PEDsQL</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-19</td>
<td>Medical History</td>
<td>Remove <code>ecls</code> string in the <code>ph_cg__medhist</code> instrument table name.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-47</td>
<td>Anthropometrics</td>
<td>Inclusion of <code>average_bmi</code>, <code>bmi_for_length_girls_z_score</code>, and <code>bmi_for_length_boys_z_score</code> fields.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-48</td>
<td>Anthropometrics</td>
<td>Growth (<code>ph_ch_anthro</code>) filter ranges will be updated to be visit-specific, as current ranges allow biologically implausible values (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Range Checks</a>).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-673</td>
<td>Anthropometrics</td>
<td>Convert implausible z scores outside of range +/-4 to null.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-33</td>
<td>Anthropometrics</td>
<td>Adjusted age contains N=303 "unknown missing" values that are also missing 'Date of Administration'.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-20</td>
<td>Anthropometrics</td>
<td>Add sex-specific birth weight to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Sex-Specific Birthweight for GA</a>).</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-109</td>
<td>Vision Screener</td>
<td>Add more fields to <code>ph_ch_vs</code> (current release only includes completion status and overall screening results).</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-134</td>
<td>BISQ-SF</td>
<td>Add Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>.</td>
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
<td><i class="fas fa-bug icon-bug"></i> ID-46</td>
<td>EPDS</td>
<td>Inconsistent scoring: (1) item responses present, but score is null (N=1); (2) all items null, but score is <code>0</code> (N≥3).</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-684</td>
<td>TLFB</td>
<td>Remove emails present in <code>user_completion</code> field.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-689</td>
<td>ACG SU data</td>
<td>Remove ACG substance use survey data.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-137</td>
<td>Healthv2 Preg</td>
<td>The field for the date when PNV was stopped (<code>pex_bm_healthv2_preg__exp__pnv_007__01</code>) is blank, despite participants having reported stopping.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-138</td>
<td>Healthv2 Preg</td>
<td>Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-144</td>
<td>TLFB</td>
<td>Select participants (N=8) were recruited postnatally, but not administered the V1 portion of the TLFB. When this was recognized, the participants were administered the TLFB at the next in-person visit, resulting in a longer recall period than specified in the protocol.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-683</td>
<td>TLFB</td>
<td>Source for TLFB should be Biological Mother, not Child.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-43</td>
<td>PEX Health</td>
<td>ICD codes for the <code>pex_bm_health*</code> tables are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <em>Health V1- Medications</em>, while the <em>Health V2- Pregnancy</em> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a></td>
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
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-64</td>
<td>Demo</td>
<td>Addition of V6 Adult and V6 Child Demographics</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-67</td>
<td>Incarceration</td>
<td>Addition of the Incarceration Questionnaire</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-38</td>
<td>eHITS</td>
<td>Participants missing all item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-60</td>
<td>Demo</td>
<td>Roster was inappropriately collected at V02/V03 for all cohorts and should have been restricted to V02 PNRs and alternate caregiver cohorts; to be excluded.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-71</td>
<td>TIC Questionnaire</td>
<td>Addition of TIC Questionnaire table</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-53</td>
<td>Demo</td>
<td>Relationship status was inappropriately collected at V02/V03 for all cohorts and should have been restricted to cases where there was a change in caregiver (i.e. only Alternative Caregiver cohorts should have this field populated). Data for non-ACG cohorts to be excluded.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-668</td>
<td>Incarceration</td>
<td>Remove Incarceration Questionnaire (sample sizes currently too small, sensititive info included, etc.)</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-50</td>
<td>Demo</td>
<td>Add household roster fields capturing the sex of listed individuals (adult &amp; child tables).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-99</td>
<td>HOME-21</td>
<td>Shift item values to start with value of 1 instead of 0 for normalization.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-666</td>
<td>HOME-21</td>
<td>Emotional support subscale not calculated for V04 and V06.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-694</td>
<td>TIC</td>
<td>Add Transition in Care flags.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr>
<td><i class="fas fa-bug icon-bug"></i> ID-670</td>
<td>eHITS</td>
<td>Sum score of null instead of 25 in cases where all items have score of 5.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr>
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-66</td>
<td>GLED</td>
<td>Addition of Geocoded Linkage from Home and Work Addresses</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
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

