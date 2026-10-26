<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
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
.archive-checks {
  display: flex;
  flex-wrap: wrap;
  gap: 0.9rem;
  align-items: center;
  min-height: 38px;
  padding: 0 0.25rem;
  font-size: 0.9rem;
}
.archive-checks label {
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  cursor: pointer;
  user-select: none;
}
.archive-controls .archive-checks input[type="checkbox"] {
  width: 1rem;
  height: 1rem;
  padding: 0;
  margin: 0;
  cursor: pointer;
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

[data-known-issue-row][hidden],
[data-known-issue-domain][hidden] {
  display: none !important;
}
</style>

# Known Issues & Pending Updates

This page documents issues associated with the next public data release, including open known issues and pending updates, and resolved issues/updates. Items are not marked as resolved until final review and approval by Workgroups/SMEs. Items relevant to currently available release data are also documented in the public-facing [HBCD Data Release Docs](https://docs.hbcdstudy.org/latest/changelog/issues-updates/). 


See the [Resolved Issues Archive](resolved-archive.html) for a running list of items associated with prior releases.

---

<div class="archive-controls">
  <div class="archive-controls-row">
    <input
      id="ki-search"
      class="archive-search"
      type="search"
      placeholder="Search table/topic or summary..."
    >
    <select id="ki-domain">
      <option value="">Domain</option>
    </select>
    <select id="ki-target">
      <option value="">Target</option>
    </select>
    <div class="archive-checks">
      <label><input id="ki-show-resolved" type="checkbox"> Show resolved items</label>
    </div>
    <button id="ki-reset" type="button">Clear filters</button>
  </div>
  <div id="ki-status" class="archive-status"></div>
</div>

<div id="ki-empty" class="archive-empty">No matching issues or updates found.</div>

<!-- ICON LEGEND -->

<p style="font-size: 1.2em; color: #555; text-align: center; line-height: 2;">
  <i class="fas fa-bug" style="color: #f97316;"></i> = Known Issue &nbsp;&nbsp;&nbsp;
  <i class="fa-solid fa-rotate" style="color: #199bd6;"></i> = Pending Update &nbsp;&nbsp;&nbsp;
  <i class="fa-solid fa-circle-check" style="color: #24AE70;"></i> = Resolved
</p>


<!-- BEGIN KNOWN_ISSUES_TABLE --><div class="known-issues" data-known-issues markdown="1">

<style>.known-issues [hidden] { display: none !important; }</style>

<p><label><input type="checkbox" autocomplete="off" onchange="const container = this.closest(&#x27;[data-known-issues]&#x27;);
container.querySelectorAll(&#x27;[data-known-issue-row][data-resolved=&quot;true&quot;]&#x27;).forEach(row =&gt; {
    row.hidden = !this.checked;
});
container.querySelectorAll(&#x27;[data-known-issue-domain]&#x27;).forEach(section =&gt; {
    section.hidden = !section.querySelector(&#x27;[data-known-issue-row]:not([hidden])&#x27;);
});
container.querySelector(&#x27;[data-known-issues-empty]&#x27;).hidden =
    !!container.querySelector(&#x27;[data-known-issue-row]:not([hidden])&#x27;);"> Show resolved issues</label></p>

<p data-known-issues-empty role="status" hidden>No issues or pending updates match the current filter.</p>

<div data-known-issue-domain markdown="1">

### All Data / General

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-110</td>
<td>Sequence Field</td>
<td>The currently included Sequence field is blank across all instruments and will be removed.</td>
<td style='text-align: center;'><span class='pill'>R4.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-83</td>
<td>Incorrect JSONs</td>
<td>Metadata field values were corrected for several instruments, but are not yet corrected in the JSON files. IN PARTICULAR, PLEASE CHECK <code>type_data</code> CAREFULLY as an incorrect data type may impact analyses. Impacted instruments include: <strong>APA 1/2</strong>, <strong>Bayley-4</strong>, and <strong>EEG Form-2</strong>. See details in <a href="../release-notes/#data-warning">Release Notes</a>.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-36</td>
<td>Score text</td>
<td>Text inappropriately located in score fields where score is missing to be moved to corresponding 'notes' field (impacts ecPROMIS-PAGS; MAPS-TL; SPM-2).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-692</td>
<td>Concatenation</td>
<td>MRI, EEG and Axtivity derivative concatenation run directly on the de-ID bucket instead of the re-ID bucket</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-32</td>
<td>Implausible GA</td>
<td>A small subset of participants have implausible <code>gestational_age</code> (V01 only) values for one or more instrument. Until corrected, review GA distribution to exclude outliers from analysis (should be positive and generally &lt; 45 weeks).</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-84</td>
<td>FamilyID</td>
<td>A <code>FamilyID</code> field will be added to instruments to identify sibling relationships. Until then, sibling ID mapping (Main Child vs Sibling) is provided in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-142</td>
<td>Instruction</td>
<td>The 'instruction' data dictionary element is currently blank.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-115</td>
<td>Sibling cohort</td>
<td>Family-level (i.e., non-child-specific) instrument fields are currently populated only for the Main Child, not sibling records (e.g., HBCD Multiple Birth – Sibling). Until resolved, users should obtain family-level values for sibling participants from the corresponding Main Child record. See the participant ID mapping in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1">

### Behavior &amp; Child-Caregiver Interaction

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-686</td>
<td>V03 age &gt;1.5y</td>
<td>Resolve age for small number of V03 participants in MAPS-TL and ecPROMIS over 1.5 years old.</td>
<td style='text-align: center;'><span class='pill'>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-69</td>
<td>MCHAT</td>
<td>Addition of the Modified Checklist for Autism in Toddlers</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-24</td>
<td>FAD</td>
<td>N=4 V06 participants with &lt;3 item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-27</td>
<td>ecPROMIS CC</td>
<td>N=12 V03 participants with &lt;3 item responses are incorrectly scored as <code>0</code> in <code>mh_cg_pms__cc__inf</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-68</td>
<td>MAPS-EASI</td>
<td>Addition of the MAPS-EASI- Toddler</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-101</td>
<td>IBQ-R &amp; ECBQ</td>
<td>Shift item values to start with value of 1 instead of 0 for normalization.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-21</td>
<td>ERICA</td>
<td>Reliability codes integrated into the primary coding dataset and no longer requires manual user generation (see <a href="https://docs.hbcdstudy.org/r2.1/instruments/bcgi/erica/#data-warning">2.1 data warning</a> for details).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-92</td>
<td>MAPS-TL, ecPROMIS</td>
<td>Shift item values to start with value of 1 instead of 0 for normalization.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-100</td>
<td>CHAOS</td>
<td>Shift item values to start with value of 1 instead of 0 for normalization.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-45</td>
<td>ERICA</td>
<td>Add all age and <code>date_taken</code> fields (currently excluded due to use of coding rather than visit dates).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-89</td>
<td>FAD</td>
<td>Shift item values to start with value of 1 instead of 0 for normalization.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-30</td>
<td>MAPS-TL (&lt;1yr)</td>
<td>N=4 participants with no item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-26</td>
<td>MAPS-TL (Tod)</td>
<td>Pro-rated scoring for <code>mh_cg_mapdb__tod</code> not yet implemented; N=16 participants missing scores.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-52</td>
<td>MAPS-EASI</td>
<td>Merge <code>total_score</code> and <code>prorated_score</code> fields into a new <code>summary_score</code> field and remove.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-146</td>
<td>ECHO</td>
<td>Addition of the Early Child Care and Education</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1">

### Biospecimens &amp; Omics

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-44</td>
<td>Blood PEth</td>
<td>Address issue of incorrect cleaning practices at sites that affect test results PEth.</td>
<td style='text-align: center;'><span class='pill'>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-687</td>
<td>BAP</td>
<td>Biospecimen timestamps for BAP data flow.</td>
<td style='text-align: center;'><span class='pill'>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-42</td>
<td>Nails</td>
<td>Nail type is <code>4</code> (Unknown) in the main results table (<code>*_nails_results</code>) and should be obtained from the specimen table (<code>*_nails_type</code>).</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-693</td>
<td>Blood PEth</td>
<td>Convert values of 999 to null. Users must do this manually until resolved prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1">

### EEG

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-55</td>
<td>Age fields</td>
<td>Chronological and adjusted age fall outside of 3-9 months in N=74 V03 sessions (site entry errors); exclude age values prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>R3.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-655</td>
<td>MADE v1.7.0</td>
<td>HBCD-MADE derivatives processed through updated version v1.7.0</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1">

### MRI

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-681</td>
<td>ReproTM</td>
<td>Addition of individual functional network maps generated with template matching via ReproTM pipeline.</td>
<td style='text-align: center;'><span class='pill'>R3.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-657</td>
<td>Source DICOMs</td>
<td>Add source DICOMs for all imaging modalities.</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-108</td>
<td>Scanner info</td>
<td>Scanner metadata, currently available within the raw BIDS Scans TSV files, will be additionally provided within the tabulated data for ease of access (see <a href="#infobbox">Participant Derived</a> domain info on this page).</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-86</td>
<td>QSIRecon</td>
<td>Provide tabulated QSIRecon derivatives.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-667</td>
<td>Tabulated XCP-D</td>
<td>Resolved tabulation error resulting in all 0s for tabulated XCP-D numeric fields.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-59</td>
<td>fmap QC</td>
<td>Frames containing line artifacts are removed from functional raw BIDS fmap files (in cases where the fmap file passes QC and is therefore used for data processing). Removed frames are documented in the relevant field map sidecar JSONs for which frame removal occurred. Three additional raw data QC fields used to identify frames to remove are now documented in the scans TSV metadata files (see fields containing <code>line2_*</code>). Finally, impacted sessions have been reprocessed post-frame removal.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-680</td>
<td>ModelArray</td>
<td>Addition of <a href="https://modelarrayio.readthedocs.io/en/latest/">ModelArray</a> outputs derived from XCP-D and QSIRecon.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-685</td>
<td>XCP-D</td>
<td>New XCP-D pipeline outputs (processed with version 26.2.0) and updated hashes as a result.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-73</td>
<td>Summary Forms</td>
<td>Fixed Sequence numbering in <code>mri_ra_chkl_data</code> to increment for <code>start_time</code> fields.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-128</td>
<td>Run ID</td>
<td>The <code>run-{X}</code> field may not reflect chronological acquisition order. While this affects both <strong>raw BIDS and derivatives</strong>, data remain internally consistent (i.e. run IDs match between raw and processed datasets).</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-154</td>
<td>dMRI metadata</td>
<td><code>LargeDelta</code> and <code>SmallDelta</code> in the sidecars currently are set to vendor-specific values (which aren't always correct because the models have their own values) and will be updated to reflect accurate values.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-155</td>
<td>Raw QC Metrics</td>
<td>Raw MR data QC metrics provided in the raw BIDS SCANS TSV files will be combined into a single table across participants/sessions.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-28</td>
<td>Cook&#x27;s Distance</td>
<td>Addition Cook's distance values computed for fMRI.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1">

### Neurocognition &amp; Language

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-54</td>
<td>Bayley</td>
<td>Remove invalid scores of <code>-9999</code>; until resolved, users should remove this participant data prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-63</td>
<td>Deferred Imitation</td>
<td>Addition of instrument: Deferred Imitation Task: Gong and Berry-Go-Round</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-661</td>
<td>CDI-2</td>
<td>Addition of the MacArthur-Bates CDI-2 Language</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-78</td>
<td>CDI</td>
<td>Percentiles incorrectly converted for N=36 cases, resulting in values &gt;100 ('Adjusted Percentile' incorrectly parsed from 'Total Produced' instead of 'Total Produced Percentile-sex (adjusted)')</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-95</td>
<td>CDI</td>
<td>Include <code>total_produced_percentile_both</code> and <code>total_produced_percentile_both_adjusted</code>.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-93</td>
<td>CDI</td>
<td>Exclude open text fields.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-80</td>
<td>Vineland</td>
<td>The Coping Skills, Domestic, and Written subscales are not administered at V05 because children are too young. However, for some participants, the missing reason is incorrectly coded as "Logic skipped" or "Unknown" in the shadow matrix. In addition, the age of one child is outside of the valid bounds for V05.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-119</td>
<td>MLDS</td>
<td>Total non-parental hours/week (<code>ncl_ch_mlds_arr_hr_wk</code>) includes implausible values due to data entry errors. Exclude values &gt;168 hours from analysis.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1">

### Novel Tech &amp; Wearable Sensors

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-654</td>
<td>GABI</td>
<td>Addition of raw BIDS data for GABI (infant heart rate).</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-691</td>
<td>GABI</td>
<td>Exclusion of <code>setup_004_status</code> from <code>nt_pa_gabi</code> instrument (GABI setup)</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-58</td>
<td>Axivity</td>
<td>Addition of concatenated Axivity table.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1">

### Participant Derived

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-37</td>
<td>TLFB</td>
<td>PNR data were incorrectly reported using TLFB versions 1/2 and will be updated to <a href="https://docs.hbcdstudy.org/latest/instruments/pregexp/su/tlfb/#v3">version 3 specific to PNR</a></td>
<td style='text-align: center;'><span class='pill'>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-675</td>
<td>ADI</td>
<td>ADI in Static table (<code>par_gd_stc_adi_national_prcn</code>) is present, but completely unpopulated.</td>
<td style='text-align: center;'><span class='pill'>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-679</td>
<td>Static table</td>
<td>AOU race checkbox/constructed-variable inconsistency.</td>
<td style='text-align: center;'><span class='pill'>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-79</td>
<td>Visit Info</td>
<td>Harmonize participant status and withdrawal fields</td>
<td style='text-align: center;'><span class='pill'>R3.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-81</td>
<td>Static table</td>
<td>The <code>screen_race_multi__*</code> variables are almost entirely coded as '0' and should not be used for analysis. Users interested in race and ethnicity information should instead use the corresponding derived ACS race and ethnicity variable. Values will be corrected in a future release.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-106</td>
<td>All tables</td>
<td><ul>
<li>Updated Domain &amp; Source </li>
<li>Addition of visit missed and visit missed reason to Dynamic table <code>par_gd_dyn</code></li>
<li>Static table: Resolve inconsistent use of 'Unknown' in derived ACS variables and exclude non-valid recruitment sites</li>
</ul></td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-34</td>
<td>Static table</td>
<td>N=14 participants have a Maternal Age at V01 of 0; exclude these values from analyses until corrected.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-669</td>
<td>Cannabis flag</td>
<td>Fixed description of Rolled up cannabis flag.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-676</td>
<td>MAD</td>
<td>Correct static maternal age at delivery.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-677</td>
<td>GAD</td>
<td>Correct static gestational age at delivery.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-671</td>
<td>SU flags</td>
<td>Make substance use flags in dynamic table cumulative.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-688</td>
<td>ACGs SU flag</td>
<td>Remove substance use survey for ACGs.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1">

### Physical Health

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-62</td>
<td>Child Nutrition</td>
<td>Addition of the Child Nutrition Questionnaire.</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-662</td>
<td>Med History V1</td>
<td>Addition of V06</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-70</td>
<td>PEDsQL</td>
<td>Addition of the PEDsQL</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-48</td>
<td>Anthropometrics</td>
<td>Growth (<code>ph_ch_anthro</code>) filter ranges will be updated to be visit-specific, as current ranges allow biologically implausible values (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Range Checks</a>).</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-673</td>
<td>Anthropometrics</td>
<td>Convert implausible z scores outside of range +/-4 to null.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-19</td>
<td>Medical History</td>
<td>Remove <code>ecls</code> string in the <code>ph_cg__medhist</code> instrument table name.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-33</td>
<td>Anthropometrics</td>
<td>Adjusted age contains N=303 "unknown missing" values that are also missing 'Date of Administration'.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-47</td>
<td>Anthropometrics</td>
<td>Inclusion of <code>average_bmi</code>, <code>bmi_for_length_girls_z_score</code>, and <code>bmi_for_length_boys_z_score</code> fields.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-20</td>
<td>Anthropometrics</td>
<td>Add sex-specific birth weight to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Sex-Specific Birthweight for GA</a>).</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-109</td>
<td>Vision Screener</td>
<td>Add more fields to <code>ph_ch_vs</code> (current release only includes completion status and overall screening results).</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-134</td>
<td>BISQ-SF</td>
<td>Add Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1">

### Pregnancy &amp; Environmental Exposure

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-683</td>
<td>TLFB</td>
<td>Source for TLFB should be Biological Mother, not Child.</td>
<td style='text-align: center;'><span class='pill'>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-43</td>
<td>PEX Health</td>
<td>ICD codes for the <code>pex_bm_health*</code> tables are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <em>Health V1- Medications</em>, while the <em>Health V2- Pregnancy</em> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a></td>
<td style='text-align: center;'><span class='pill'>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-46</td>
<td>EPDS</td>
<td>Inconsistent scoring: (1) item responses present, but score is null (N=1); (2) all items null, but score is <code>0</code> (N≥3).</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-684</td>
<td>TLFB</td>
<td>Remove emails present in <code>user_completion</code> field.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-689</td>
<td>ACG SU data</td>
<td>Remove ACG substance use survey data.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-137</td>
<td>Healthv2 Preg</td>
<td>The field for the date when PNV was stopped (<code>pex_bm_healthv2_preg__exp__pnv_007__01</code>) is blank, despite participants having reported stopping.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-138</td>
<td>Healthv2 Preg</td>
<td>Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank.</td>
<td style='text-align: center;'><span class='pill'>TBD</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1">

### Social &amp; Environmental Determinants

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th></th><th>Table/Topic</th><th>Summary</th>
<th>Target</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-66</td>
<td>GLED</td>
<td>Addition of Geocoded Linkage from Home and Work Addresses</td>
<td style='text-align: center;'><span class='pill'>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-64</td>
<td>Demo</td>
<td>Addition of V6 Adult and V6 Child Demographics</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-67</td>
<td>Incarceration</td>
<td>Addition of the Incarceration Questionnaire</td>
<td style='text-align: center;'><span class='pill'>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-71</td>
<td>TIC Questionnaire</td>
<td>Addition of TIC Questionnaire table</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-38</td>
<td>eHITS</td>
<td>Participants missing all item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-60</td>
<td>Demo</td>
<td>Roster was inappropriately collected at V02/V03 for all cohorts and should have been restricted to V02 PNRs and alternate caregiver cohorts; to be excluded.</td>
<td style='text-align: center;'><span class='pill'>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-670</td>
<td>eHITS</td>
<td>Sum score of null instead of 25 in cases where all items have score of 5.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><i class="fa-solid fa-circle-check icon-resolved"></i> ID-99</td>
<td>HOME-21</td>
<td>Shift item values to start with value of 1 instead of 0 for normalization.</td>
<td style='text-align: center;'><span class='pill'>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-53</td>
<td>Demo</td>
<td>Relationship status was inappropriately collected at V02/V03 for all cohorts and should have been restricted to cases where there was a change in caregiver (i.e. only Alternative Caregiver cohorts should have this field populated). Data for non-ACG cohorts to be excluded.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-666</td>
<td>HOME-21</td>
<td>Emotional support subscale not calculated for V04 and V06.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fas fa-bug icon-bug"></i> ID-668</td>
<td>Incarceration</td>
<td>Remove Incarceration Questionnaire (sample sizes currently too small, sensititive info included, etc.)</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-50</td>
<td>Demo</td>
<td>Add household roster fields capturing the sex of listed individuals (adult &amp; child tables).</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><i class="fa-solid fa-rotate icon-rotate"></i> ID-694</td>
<td>TIC</td>
<td>Add Transition in Care flags.</td>
<td style='text-align: center;'><span class='pill'>30.3</span></td>
</tr>
</tbody></table>

</div>

</div><!-- END KNOWN_ISSUES_TABLE -->


  <br>

<script>
(function () {
  function initializeKnownIssuesFilters() {
    const search = document.getElementById("ki-search");
    const domain = document.getElementById("ki-domain");
    const target = document.getElementById("ki-target");
    const showResolved = document.getElementById("ki-show-resolved");
    const reset = document.getElementById("ki-reset");
    const status = document.getElementById("ki-status");
    const empty = document.getElementById("ki-empty");

    if (!search || !domain || !target || !showResolved || !reset) return;
    if (search.dataset.filtersInitialized === "true") return;

    search.dataset.filtersInitialized = "true";

    const container = document.querySelector("[data-known-issues]");
    if (!container) return;

    // Remove the separate checkbox and empty message generated by Python.
    // All filtering is handled together below.
    container.querySelectorAll('input[type="checkbox"][onchange]')
      .forEach(function (checkbox) {
        const paragraph = checkbox.closest("p");
        if (
          paragraph &&
          paragraph.textContent.includes("Show resolved issues")
        ) {
          paragraph.remove();
        }
      });

    container.querySelectorAll("[data-known-issues-empty]")
      .forEach(function (message) {
        message.remove();
      });

    // Ensure theme styles cannot override hidden rows or sections.
    if (!document.getElementById("ki-hidden-styles")) {
      const style = document.createElement("style");
      style.id = "ki-hidden-styles";
      style.textContent = `
        [data-known-issue-row][hidden],
        [data-known-issue-domain][hidden] {
          display: none !important;
        }
      `;
      document.head.appendChild(style);
    }

    function normalize(value) {
      return String(value || "").trim().toLowerCase();
    }

    const sections = Array.from(
      container.querySelectorAll("[data-known-issue-domain]")
    );

    // Compare text alphabetically, ignoring case, with natural number ordering.
// For example, 30.2 sorts before 30.10.
const collator = new Intl.Collator("en", {
  numeric: true,
  sensitivity: "base"
});

function getText(element) {
  return element
    ? element.textContent.replace(/\s+/g, " ").trim()
    : "";
}

// Sort the domain sections alphabetically by heading.
sections.sort(function (a, b) {
  return collator.compare(
    getText(a.querySelector("h3")),
    getText(b.querySelector("h3"))
  );
});

sections.forEach(function (section) {
  container.appendChild(section);

  // Sort each table independently, including hidden resolved rows.
  section.querySelectorAll("table").forEach(function (table) {
    Array.from(table.tBodies).forEach(function (tbody) {
      const rows = Array.from(tbody.rows).filter(function (row) {
        return row.matches("[data-known-issue-row]");
      });

      rows.sort(function (a, b) {
        // Primary sort: Target (fourth column).
        const targetComparison = collator.compare(
          getText(a.cells[3]),
          getText(b.cells[3])
        );

        if (targetComparison !== 0) return targetComparison;

        // Secondary sort: Table/Topic (second column).
        return collator.compare(
          getText(a.cells[1]),
          getText(b.cells[1])
        );
      });

      rows.forEach(function (row) {
        tbody.appendChild(row);
      });
    });
  });
});

    // Include hidden rows so resolved items can be revealed.
    const records = Array.from(
      container.querySelectorAll("[data-known-issue-row]")
    ).map(function (row) {
      const cells = row.querySelectorAll("td");
      const section = row.closest("[data-known-issue-domain]");
      const heading = section ? section.querySelector("h3") : null;

      // Exclude the 🔗 permalink anchor that MkDocs appends inside headings.
      const domainName = heading ? getText(heading).replace(/\s*🔗$/, "") : "";
      const targetName = cells[3] ? cells[3].textContent.trim() : "";

      // Support explicit type metadata if the generator provides it.
      let issueType = normalize(row.dataset.issueType);

      if (issueType === "pending update") issueType = "update";

      if (row.dataset.resolved === "true") {
        issueType = "resolved";
      } else if (!issueType) {
        if (row.querySelector(".fa-bug, .icon-bug")) {
          issueType = "issue";
        } else if (row.querySelector(".fa-rotate, .icon-rotate")) {
          issueType = "update";
        }
      }

      return {
        row: row,
        section: section,
        domain: domainName,
        target: targetName,
        type: issueType,
        resolved: row.dataset.resolved === "true",
        searchText: normalize(
          (cells[1] ? cells[1].textContent : "") + " " +
          (cells[2] ? cells[2].textContent : "")
        )
      };
    });

    function populateOptions(select, values, firstLabel) {
      const selected = select.value;

      select.replaceChildren(new Option(firstLabel, ""));

      Array.from(new Set(values.filter(Boolean)))
        .sort(function (a, b) {
          return a.localeCompare(b, undefined, {
            numeric: true,
            sensitivity: "base"
          });
        })
        .forEach(function (value) {
          select.add(new Option(value, value));
        });

      if (
        Array.from(select.options).some(function (option) {
          return option.value === selected;
        })
      ) {
        select.value = selected;
      }
    }

    populateOptions(
      domain,
      records.map(function (record) { return record.domain; }),
      "Domain"
    );

    populateOptions(
      target,
      records.map(function (record) { return record.target; }),
      "Target"
    );

    function applyFilters() {
      const query = normalize(search.value);
      const selectedDomain = domain.value;
      const selectedTarget = target.value;
      const showResolvedItems = showResolved.checked;

      let visibleCount = 0;

      records.forEach(function (record) {
        const matchesSearch =
          !query || record.searchText.includes(query);

        const matchesDomain =
          !selectedDomain || record.domain === selectedDomain;

        const matchesTarget =
          !selectedTarget || record.target === selectedTarget;

        const matchesResolved = showResolvedItems || !record.resolved;

        const visible =
          matchesSearch &&
          matchesDomain &&
          matchesTarget &&
          matchesResolved;

        record.row.hidden = !visible;

        if (visible) visibleCount++;
      });

      // Hide domain headings and tables with no matching rows.
      sections.forEach(function (section) {
        section.hidden = !section.querySelector(
          "[data-known-issue-row]:not([hidden])"
        );
      });

      if (status) {
        status.textContent =
          "Showing " + visibleCount + " matching item" +
          (visibleCount === 1 ? "" : "s") + ".";
      }

      if (empty) {
        empty.style.display = visibleCount === 0 ? "block" : "none";
      }
    }

    search.addEventListener("input", applyFilters);

    [domain, target, showResolved].forEach(function (control) {
      control.addEventListener("change", applyFilters);
    });

    reset.addEventListener("click", function () {
      search.value = "";
      domain.value = "";
      target.value = "";
      showResolved.checked = false;

      applyFilters();
    });

    applyFilters();
  }

  if (document.readyState === "loading") {
    document.addEventListener(
      "DOMContentLoaded",
      initializeKnownIssuesFilters,
      { once: true }
    );
  } else {
    initializeKnownIssuesFilters();
  }
})();
</script>
