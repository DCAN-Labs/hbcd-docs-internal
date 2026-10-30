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

/* Sortable column headers */
.known-issues th[data-sort-col] {
  cursor: pointer;
  user-select: none;
  white-space: nowrap;
}
.known-issues th[data-sort-col]:hover {
  background: #f1f3f5;
}
.known-issues th[data-sort-col]::after {
  content: " \2195";
  color: #aaa;
  font-size: 0.85em;
}
.known-issues th[data-sort-dir="asc"]::after {
  content: " \25B2";
  color: #199bd6;
}
.known-issues th[data-sort-dir="desc"]::after {
  content: " \25BC";
  color: #199bd6;
}

[data-known-issue-row][hidden],
[data-known-issue-domain][hidden] {
  display: none !important;
}
</style>

# Known Issues & Updates

This page documents issues associated with the next public data release, including open known issues and pending updates, and resolved issues/updates. Items are not marked as resolved until final review and approval by Workgroups/SMEs. Items relevant to currently available release data are also documented in the public-facing [HBCD Data Release Docs](https://docs.hbcdstudy.org/latest/changelog/issues-updates/). See the [Resolved Issues Archive](resolved-archive.html) for a running list of items associated with prior releases.

!!! danger "Issue Status "Pending""
    Items labeled with "Pending" have been resolved by the HDCC and require final review and sign-off from Workgroups/SMEs to confirm successful implementation. Final sign-off is required prior to inclusion in the public release, so please review these ASAP.

---

<div class="archive-controls">
  <div class="archive-controls-row">
    <input
      id="ki-search"
      class="archive-search"
      type="search"
      placeholder="Search table/topic or summary..."
    >
    <select id="ki-status-filter" aria-label="Filter by status">
      <option value="">Status</option>
      <option value="open">Open</option>
      <option value="pending">Pending</option>
      <option value="resolved">Resolved</option>
    </select>
    <select id="ki-domain">
      <option value="">Domain</option>
    </select>
    <select id="ki-target">
      <option value="">Target</option>
    </select>
    <button id="ki-reset" type="button">Clear filters</button>
  </div>
  <div id="ki-status" class="archive-status"></div>
</div>

<div id="ki-empty" class="archive-empty">No matching issues or updates found.</div>

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

<p data-known-issues-empty role="status">No issues or updates match the current filter.</p>

<div data-known-issue-domain markdown="1" hidden>

### All Data / General

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th>Status</th><th>Table/Topic</th><th>Summary</th>
<th>BR</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Sequence Field</td>
<td>The currently included Sequence field is blank across all instruments and will be removed. (<b>ID-110</b>)</td>
<td style='text-align: center;'><span class=pill>R4.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Sibling cohort</td>
<td>Family-level (i.e., non-child-specific) instrument fields are currently populated only for the Main Child, not sibling records (e.g., HBCD Multiple Birth – Sibling). Until resolved, users should obtain family-level values for sibling participants from the corresponding Main Child record. See the participant ID mapping in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>. (<b>ID-115</b>)</td>
<td style='text-align: center;'><span class=pill>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Instruction</td>
<td>The 'instruction' data dictionary element is currently blank. (<b>ID-142</b>)</td>
<td style='text-align: center;'><span class=pill>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Implausible GA</td>
<td>A small subset of participants have implausible <code>gestational_age</code> (V01 only) values for one or more instrument. Until corrected, review GA distribution to exclude outliers from analysis (should be positive and generally &lt; 45 weeks). (<b>ID-32</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill pending'>Pending</span></td>
<td>Incorrect JSONs</td>
<td>Metadata field values were corrected for several instruments, but are not yet corrected in the JSON files. IN PARTICULAR, PLEASE CHECK <code>type_data</code> CAREFULLY as an incorrect data type may impact analyses. Impacted instruments include: <strong>APA 1/2</strong>, <strong>Bayley-4</strong>, and <strong>EEG Form-2</strong>. See details in <a href="../release-notes/#data-warning">Release Notes</a>. (<b>ID-83</b>)</td>
<td style='text-align: center;'><span class=pill>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>FamilyID</td>
<td>A <code>FamilyID</code> field will be added to instruments to identify sibling relationships. Until then, sibling ID mapping (Main Child vs Sibling) is provided in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>. (<b>ID-84</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>Score text</td>
<td>Text inappropriately located in score fields where score is missing to be moved to corresponding 'notes' field (impacts ecPROMIS-PAGS; MAPS-TL; SPM-2). (<b>ID-36</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>Concatenation</td>
<td>MRI, EEG and Axtivity derivative concatenation run directly on the de-ID bucket instead of the re-ID bucket (<b>ID-692</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1" hidden>

### Behavior &amp; Child-Caregiver Interaction

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th>Status</th><th>Table/Topic</th><th>Summary</th>
<th>BR</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>ECHO</td>
<td>Addition of the Early Child Care and Education (<b>ID-146</b>)</td>
<td style='text-align: center;'><span class=pill>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill pending'>Pending</span></td>
<td>ERICA</td>
<td>Reliability codes integrated into the primary coding dataset and no longer requires manual user generation (see <a href="https://docs.hbcdstudy.org/r2.1/instruments/bcgi/erica/#data-warning">2.1 data warning</a> for details). (<b>ID-21</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>MAPS-TL (Tod)</td>
<td>Pro-rated scoring for <code>mh_cg_mapdb__tod</code> not yet implemented; N=16 participants missing scores. (<b>ID-26</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>MAPS-TL (&lt;1yr)</td>
<td>N=4 participants with no item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis. (<b>ID-30</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>MAPS-EASI</td>
<td>Merge <code>total_score</code> and <code>prorated_score</code> fields into a new <code>summary_score</code> field and remove. (<b>ID-52</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>V03 age &gt;1.5y</td>
<td>Resolve age for small number of V03 participants in MAPS-TL and ecPROMIS over 1.5 years old. (<b>ID-686</b>)</td>
<td style='text-align: center;'><span class=pill>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>CHAOS</td>
<td>Shift item values to start with value of 1 instead of 0 for normalization. (<b>ID-100</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>IBQ-R &amp; ECBQ</td>
<td>Shift item values to start with value of 1 instead of 0 for normalization. (<b>ID-101</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>FAD</td>
<td>N=4 V06 participants with &lt;3 item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis. (<b>ID-24</b>)</td>
<td style='text-align: center;'><span class=pill>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>ecPROMIS CC</td>
<td>N=12 V03 participants with &lt;3 item responses are incorrectly scored as <code>0</code> in <code>mh_cg_pms__cc__inf</code>; set values to null prior to analysis. (<b>ID-27</b>)</td>
<td style='text-align: center;'><span class=pill>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>ERICA</td>
<td>Add all age and <code>date_taken</code> fields (currently excluded due to use of coding rather than visit dates). (<b>ID-45</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>MAPS-EASI</td>
<td>Addition of the MAPS-EASI- Toddler (<b>ID-68</b>)</td>
<td style='text-align: center;'><span class=pill>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>MCHAT</td>
<td>Addition of the Modified Checklist for Autism in Toddlers (<b>ID-69</b>)</td>
<td style='text-align: center;'><span class=pill>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>FAD</td>
<td>Shift item values to start with value of 1 instead of 0 for normalization. (<b>ID-89</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>MAPS-TL, ecPROMIS</td>
<td>Shift item values to start with value of 1 instead of 0 for normalization. (<b>ID-92</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1" hidden>

### Biospecimens &amp; Omics

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th>Status</th><th>Table/Topic</th><th>Summary</th>
<th>BR</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Nails</td>
<td>Nail type is <code>4</code> (Unknown) in the main results table (<code>*_nails_results</code>) and should be obtained from the specimen table (<code>*_nails_type</code>). (<b>ID-42</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Blood PEth</td>
<td>Address issue of incorrect cleaning practices at sites that affect test results PEth. (<b>ID-44</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>BAP</td>
<td>Biospecimen timestamps for BAP data flow. (<b>ID-687</b>)</td>
<td style='text-align: center;'><span class=pill>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Blood PEth</td>
<td>Convert values of 999 to null. Users must do this manually until resolved prior to analysis. (<b>ID-693</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill'>TO DO</span></td>
<td>Nails</td>
<td> (<b>ID-700</b>)</td>
<td style='text-align: center;'><span class=pill>TBD</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1" hidden>

### EEG

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th>Status</th><th>Table/Topic</th><th>Summary</th>
<th>BR</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Age fields</td>
<td>Chronological and adjusted age fall outside of 3-9 months in N=74 V03 sessions (site entry errors); exclude age values prior to analysis. (<b>ID-55</b>)</td>
<td style='text-align: center;'><span class=pill>R3.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>MADE v1.7.0</td>
<td>HBCD-MADE derivatives processed through updated version v1.7.0 (<b>ID-655</b>)</td>
<td style='text-align: center;'><span class=pill>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>HBCD ECG</td>
<td>Inaugural inclusion of ECG data processed through <a href="https://github.com/DCAN-Labs/HBCD_ECG_pipeline">HBCD ECG pipeline</a>. (<b>ID-75</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1" hidden>

### HBCD General

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th>Status</th><th>Table/Topic</th><th>Summary</th>
<th>BR</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Static table</td>
<td>N=14 participants have a Maternal Age at V01 of 0; exclude these values from analyses until corrected. (<b>ID-34</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>TLFB</td>
<td>PNR data were incorrectly reported using TLFB versions 1/2 and will be updated to <a href="https://docs.hbcdstudy.org/latest/instruments/pregexp/su/tlfb/#v3">version 3 specific to PNR</a> (<b>ID-37</b>)</td>
<td style='text-align: center;'><span class=pill>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Cannabis flag</td>
<td>Fixed description of Rolled up cannabis flag. (<b>ID-669</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>SU flags</td>
<td>Make substance use flags in dynamic table cumulative. (<b>ID-671</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>ADI</td>
<td>ADI in Static table (<code>par_gd_stc_adi_national_prcn</code>) is present, but completely unpopulated. (<b>ID-675</b>)</td>
<td style='text-align: center;'><span class=pill>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>MAD</td>
<td>Correct static maternal age at delivery. (<b>ID-676</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>GAD</td>
<td>Correct static gestational age at delivery. (<b>ID-677</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Static table</td>
<td>AOU race checkbox/constructed-variable inconsistency. (<b>ID-679</b>)</td>
<td style='text-align: center;'><span class=pill>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Visit Info</td>
<td>Harmonize participant status and withdrawal fields (<b>ID-79</b>)</td>
<td style='text-align: center;'><span class=pill>R3.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>All tables</td>
<td>Update Domain &amp; Source; Add visit missed and reason to Dynamic table (<code>par_gd_dyn</code>); Resolve inconsistent use of “Unknown” in derived ACS variables and exclude non-valid recruitment sites for Static table (<code>par_gd_stc</code>). (<b>ID-106</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>Static table</td>
<td>The <code>screen_race_multi__*</code> variables are almost entirely coded as '0' and should not be used for analysis. Users interested in race and ethnicity information should instead use the corresponding derived ACS race and ethnicity variable. Values will be corrected in a future release. (<b>ID-81</b>)</td>
<td style='text-align: center;'><span class=pill>30.1</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1" hidden>

### MRI

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th>Status</th><th>Table/Topic</th><th>Summary</th>
<th>BR</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Run ID</td>
<td>The <code>run-{X}</code> field may not reflect chronological acquisition order. While this affects both <strong>raw BIDS and derivatives</strong>, data remain internally consistent (i.e. run IDs match between raw and processed datasets). (<b>ID-128</b>)</td>
<td style='text-align: center;'><span class=pill>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>dMRI metadata</td>
<td><code>LargeDelta</code> and <code>SmallDelta</code> in the sidecars currently are set to vendor-specific values (which aren't always correct because the models have their own values) and will be updated to reflect accurate values. (<b>ID-154</b>)</td>
<td style='text-align: center;'><span class=pill>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Raw QC Metrics</td>
<td>Raw MR data QC metrics provided in the raw BIDS SCANS TSV files will be combined into a single table across participants/sessions. (<b>ID-155</b>)</td>
<td style='text-align: center;'><span class=pill>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Cook&#x27;s Distance</td>
<td>Addition Cook's distance values computed for fMRI. (<b>ID-28</b>)</td>
<td style='text-align: center;'><span class=pill>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill pending'>Pending</span></td>
<td>ModelArray</td>
<td>Addition of <a href="https://modelarrayio.readthedocs.io/en/latest/">ModelArray</a> outputs derived from XCP-D and QSIRecon. (<b>ID-680</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>ReproTM</td>
<td>Addition of individual functional network maps generated with template matching via ReproTM pipeline. (<b>ID-681</b>)</td>
<td style='text-align: center;'><span class=pill>R3.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Summary Forms</td>
<td>Fixed Sequence numbering in <code>mri_ra_chkl_data</code> to increment for <code>start_time</code> fields. (<b>ID-73</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>Scanner info</td>
<td>Add a table with scanner metadata extracted from raw BIDS JSON files for easier access. (<b>ID-108</b>)</td>
<td style='text-align: center;'><span class=pill>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>fmap QC</td>
<td>Frames containing line artifacts are removed from functional raw BIDS fmap files (in cases where the fmap file passes QC and is therefore used for data processing). Removed frames are documented in the relevant field map sidecar JSONs for which frame removal occurred. Three additional raw data QC fields used to identify frames to remove are now documented in the scans TSV metadata files (see fields containing <code>line2_*</code>). Finally, impacted sessions have been reprocessed post-frame removal. (<b>ID-59</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>Source DICOMs</td>
<td>Add source DICOMs for all imaging modalities. (<b>ID-657</b>)</td>
<td style='text-align: center;'><span class=pill>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>Tabulated XCP-D</td>
<td>Resolved tabulation error resulting in all 0s for tabulated XCP-D numeric fields. (<b>ID-667</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>XCP-D</td>
<td>New XCP-D pipeline outputs (processed with version 26.2.0) and updated hashes as a result. (<b>ID-685</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>QSIRecon</td>
<td>Provide tabulated QSIRecon derivatives. (<b>ID-86</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1" hidden>

### Neurocognition &amp; Language

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th>Status</th><th>Table/Topic</th><th>Summary</th>
<th>BR</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>MLDS</td>
<td>Total non-parental hours/week (<code>ncl_ch_mlds_arr_hr_wk</code>) includes implausible values due to data entry errors. Exclude values &gt;168 hours from analysis. (<b>ID-119</b>)</td>
<td style='text-align: center;'><span class=pill>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Bayley</td>
<td>Remove invalid scores of <code>-9999</code>; until resolved, users should remove this participant data prior to analysis. (<b>ID-54</b>)</td>
<td style='text-align: center;'><span class=pill>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Vineland</td>
<td>The Coping Skills, Domestic, and Written subscales are not administered at V05 because children are too young. However, for some participants, the missing reason is incorrectly coded as "Logic skipped" or "Unknown" in the shadow matrix. In addition, the age of one child is outside of the valid bounds for V05. (<b>ID-80</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>Deferred Imitation</td>
<td>Addition of instrument: Deferred Imitation Task: Gong and Berry-Go-Round (<b>ID-63</b>)</td>
<td style='text-align: center;'><span class=pill>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>CDI-2</td>
<td>Addition of the MacArthur-Bates CDI-2 Language (<b>ID-661</b>)</td>
<td style='text-align: center;'><span class=pill>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>CDI</td>
<td>Percentiles incorrectly converted for N=36 cases, resulting in values &gt;100 ('Adjusted Percentile' incorrectly parsed from 'Total Produced' instead of 'Total Produced Percentile-sex (adjusted)') (<b>ID-78</b>)</td>
<td style='text-align: center;'><span class=pill>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>CDI</td>
<td>Exclude open text fields. (<b>ID-93</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>CDI</td>
<td>Include <code>total_produced_percentile_both</code> and <code>total_produced_percentile_both_adjusted</code>. (<b>ID-95</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1" hidden>

### Novel Tech &amp; Wearable Sensors

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th>Status</th><th>Table/Topic</th><th>Summary</th>
<th>BR</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>Axivity</td>
<td>Addition of concatenated Axivity table. (<b>ID-58</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>GABI</td>
<td>Addition of raw BIDS data for GABI (infant heart rate). (<b>ID-654</b>)</td>
<td style='text-align: center;'><span class=pill>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>GABI</td>
<td>Exclusion of <code>setup_004_status</code> from <code>nt_pa_gabi</code> instrument (GABI setup) (<b>ID-691</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1" hidden>

### Physical Health

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th>Status</th><th>Table/Topic</th><th>Summary</th>
<th>BR</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Vision Screener</td>
<td>Add more fields to <code>ph_ch_vs</code> (current release only includes completion status and overall screening results). (<b>ID-109</b>)</td>
<td style='text-align: center;'><span class=pill>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>BISQ-SF</td>
<td>Add Infant Sleep (IS) sub-scale score to <code>ph_cg_bisq</code>. (<b>ID-134</b>)</td>
<td style='text-align: center;'><span class=pill>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Medical History</td>
<td>Remove <code>ecls</code> string in the <code>ph_cg__medhist</code> instrument table name. (<b>ID-19</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Anthropometrics</td>
<td>Add sex-specific birth weight to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Sex-Specific Birthweight for GA</a>). (<b>ID-20</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Anthropometrics</td>
<td>Adjusted age contains N=303 "unknown missing" values that are also missing 'Date of Administration'. (<b>ID-33</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Anthropometrics</td>
<td>Inclusion of <code>average_bmi</code>, <code>bmi_for_length_girls_z_score</code>, and <code>bmi_for_length_boys_z_score</code> fields. (<b>ID-47</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill pending'>Pending</span></td>
<td>Anthropometrics</td>
<td>Filter ranges will be updated to be visit-specific as current ranges allow biologically implausible values (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Range Checks</a>). (<b>ID-48</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill pending'>Pending</span></td>
<td>Anthropometrics</td>
<td>Convert implausible z scores outside of range +/-4 to null. (<b>ID-673</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>Child Nutrition</td>
<td>Addition of the Child Nutrition Questionnaire. (<b>ID-62</b>)</td>
<td style='text-align: center;'><span class=pill>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>Med History V1</td>
<td>Addition of V06 (<b>ID-662</b>)</td>
<td style='text-align: center;'><span class=pill>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>PEDsQL</td>
<td>Addition of the PEDsQL (<b>ID-70</b>)</td>
<td style='text-align: center;'><span class=pill>30.0</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1" hidden>

### Pregnancy &amp; Environmental Exposure

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th>Status</th><th>Table/Topic</th><th>Summary</th>
<th>BR</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Healthv2 Preg</td>
<td>The field for the date when PNV was stopped (<code>pex_bm_healthv2_preg__exp__pnv_007__01</code>) is blank, despite participants having reported stopping. (<b>ID-137</b>)</td>
<td style='text-align: center;'><span class=pill>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Healthv2 Preg</td>
<td>Note that items about aspirin use (<code>pex_bm_healthv2_preg__exp__pnv_{011|012}</code>) are largely blank. (<b>ID-138</b>)</td>
<td style='text-align: center;'><span class=pill>TBD</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>PEX Health</td>
<td>ICD codes for the <code>pex_bm_health*</code> tables are inconsistently provided, sometimes missing corresponding names/labels. For example, medication names are present for the <em>Health V1- Medications</em>, while the <em>Health V2- Pregnancy</em> instrument only has medication codes without corresponding labels. Until resolved, users can use external packages to merge ICD labels if needed: <a href="https://www.stata.com/features/overview/icd/">Stata</a>, <a href="https://hcup-us.ahrq.gov/toolssoftware/ccsr/dxccsr.jsp">SAS</a>, <a href="https://www.rdocumentation.org/packages/icd/versions/3.3">R</a> (<b>ID-43</b>)</td>
<td style='text-align: center;'><span class=pill>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>TLFB</td>
<td>Source for TLFB should be Biological Mother, not Child. (<b>ID-683</b>)</td>
<td style='text-align: center;'><span class=pill>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>TLFB</td>
<td>Remove emails present in <code>user_completion</code> field. (<b>ID-684</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>ACG SU data</td>
<td>Remove ACG substance use survey data. (<b>ID-689</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>EPDS</td>
<td>Inconsistent scoring: (1) item responses present, but score is null (N=1); (2) all items null, but score is <code>0</code> (N≥3). (<b>ID-46</b>)</td>
<td style='text-align: center;'><span class=pill>30.1</span></td>
</tr>
</tbody></table>

</div>

<div data-known-issue-domain markdown="1" hidden>

### Social &amp; Environmental Determinants

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="font-size: 1.1em;">
<th>Status</th><th>Table/Topic</th><th>Summary</th>
<th>BR</th></tr>
</thead>
<tbody>

<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Demo</td>
<td>Add household roster fields capturing the sex of listed individuals (adult &amp; child tables). (<b>ID-50</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>Demo</td>
<td>Relationship status was inappropriately collected at V02/V03 for all cohorts and should have been restricted to cases where there was a change in caregiver (i.e. only Alternative Caregiver cohorts should have this field populated). Data for non-ACG cohorts to be excluded. (<b>ID-53</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>GLED</td>
<td>Addition of Geocoded Linkage from Home and Work Addresses (<b>ID-66</b>)</td>
<td style='text-align: center;'><span class=pill>R3.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>HOME-21</td>
<td>Emotional support subscale not calculated for V04 and V06. (<b>ID-666</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="false">
<td><span class='pill open'>Open</span></td>
<td>TIC</td>
<td>Add Transition in Care flags. (<b>ID-694</b>)</td>
<td style='text-align: center;'><span class=pill>30.3</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>eHITS</td>
<td>Participants missing all item responses are incorrectly scored as <code>0</code>; set values to null prior to analysis. (<b>ID-38</b>)</td>
<td style='text-align: center;'><span class=pill>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>Demo</td>
<td>Roster was inappropriately collected at V02/V03 for all cohorts and should have been restricted to V02 PNRs and alternate caregiver cohorts; to be excluded. (<b>ID-60</b>)</td>
<td style='text-align: center;'><span class=pill>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>Demo</td>
<td>Addition of V6 Adult and V6 Child Demographics (<b>ID-64</b>)</td>
<td style='text-align: center;'><span class=pill>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>Incarceration</td>
<td>Remove Incarceration Questionnaire (sample sizes currently too small, sensititive info included, etc.) (<b>ID-668</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>Incarceration</td>
<td>Addition of the Incarceration Questionnaire (<b>ID-67</b>)</td>
<td style='text-align: center;'><span class=pill>30.0</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>eHITS</td>
<td>Sum score of null instead of 25 in cases where all items have score of 5. (<b>ID-670</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>TIC Questionnaire</td>
<td>Addition of TIC Questionnaire table (<b>ID-71</b>)</td>
<td style='text-align: center;'><span class=pill>30.1</span></td>
</tr>
<tr data-known-issue-row data-resolved="true" hidden>
<td><span class='pill resolved'>Resolved</span></td>
<td>HOME-21</td>
<td>Shift item values to start with value of 1 instead of 0 for normalization. (<b>ID-99</b>)</td>
<td style='text-align: center;'><span class=pill>30.2</span></td>
</tr>
</tbody></table>

</div>

</div><!-- END KNOWN_ISSUES_TABLE -->


<script>
(function () {
  function initializeKnownIssuesFilters() {
    const search = document.getElementById("ki-search");
    const domain = document.getElementById("ki-domain");
    const target = document.getElementById("ki-target");
    const statusFilter = document.getElementById("ki-status-filter");
    const reset = document.getElementById("ki-reset");
    const countMessage = document.getElementById("ki-status");
    const empty = document.getElementById("ki-empty");
    const container = document.querySelector("[data-known-issues]");

    if (
      !search ||
      !domain ||
      !target ||
      !statusFilter ||
      !reset ||
      !container
    ) return;

    if (search.dataset.filtersInitialized === "true") return;
    search.dataset.filtersInitialized = "true";

    // Remove the separate checkbox generated by Python.
    container.querySelectorAll('input[type="checkbox"][onchange]')
      .forEach(function (checkbox) {
        const paragraph = checkbox.closest("p");

        if (
          paragraph &&
          /Show resolved (issues|items)/.test(paragraph.textContent)
        ) {
          paragraph.remove();
        }
      });

    // Use the filter box's empty message instead of Python's message.
    container.querySelectorAll("[data-known-issues-empty]")
      .forEach(function (message) {
        message.remove();
      });

    function normalize(value) {
      return String(value || "").trim().toLowerCase();
    }

    function getText(element) {
      return element
        ? element.textContent.replace(/\s+/g, " ").trim()
        : "";
    }

    function getDomainName(section) {
      const heading = section.querySelector("h3");

      if (!heading) return "";

      // Exclude permalink anchors added by MkDocs.
      const copy = heading.cloneNode(true);
      copy.querySelectorAll(".headerlink").forEach(function (anchor) {
        anchor.remove();
      });

      return getText(copy).replace(/\s*🔗$/, "");
    }

    // Natural number ordering: 30.2 sorts before 30.10.
    const collator = new Intl.Collator("en", {
      numeric: true,
      sensitivity: "base"
    });

    const sections = Array.from(
      container.querySelectorAll("[data-known-issue-domain]")
    );

    // Sort domain sections alphabetically.
    sections.sort(function (a, b) {
      return collator.compare(getDomainName(a), getDomainName(b));
    });

    sections.forEach(function (section) {
      container.appendChild(section);

      // Include hidden rows so resolved items are also sorted.
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

    // Read Status from the first column, including its pill badge text.
    const records = Array.from(
      container.querySelectorAll("[data-known-issue-row]")
    ).map(function (row) {
      const section = row.closest("[data-known-issue-domain]");

      return {
        row: row,
        domain: section ? getDomainName(section) : "",
        target: getText(row.cells[3]),
        status: normalize(getText(row.cells[0])),
        searchText: normalize(
          getText(row.cells[1]) + " " + getText(row.cells[2])
        )
      };
    });

    // Click a column header (Status, Table/Topic, Target) to sort every
    // table by that column; click again to reverse.
    const statusRank = { open: 0, pending: 1, resolved: 2 };
    const sortColumns = { 0: "status", 1: "topic", 3: "target" };
    const allHeaders = [];

    function sortKey(row, col) {
      const text = getText(row.cells[col]);

      return col === 0
        ? (statusRank[normalize(text)] !== undefined
            ? statusRank[normalize(text)]
            : 99)
        : text;
    }

    function compareRows(a, b, col, direction) {
      const first = sortKey(a, col);
      const second = sortKey(b, col);

      let result = typeof first === "number"
        ? first - second
        : collator.compare(first, second);

      // Tie-breakers keep the order stable and sensible.
      if (result === 0 && col !== 3) {
        result = collator.compare(getText(a.cells[3]), getText(b.cells[3]));
      }
      if (result === 0 && col !== 1) {
        result = collator.compare(getText(a.cells[1]), getText(b.cells[1]));
      }

      return direction * result;
    }

    sections.forEach(function (section) {
      section.querySelectorAll("table").forEach(function (table) {
        const headerRow = table.tHead && table.tHead.rows[0];

        if (!headerRow) return;

        Object.keys(sortColumns).forEach(function (index) {
          const th = headerRow.cells[index];

          if (!th) return;

          th.setAttribute("data-sort-col", sortColumns[index]);
          th.setAttribute("role", "button");
          th.setAttribute("tabindex", "0");
          allHeaders.push(th);

          function sortBy() {
            const col = Number(index);
            const direction = th.getAttribute("data-sort-dir") === "asc"
              ? -1
              : 1;

            // Sort all tables together so the view stays consistent.
            sections.forEach(function (other) {
              other.querySelectorAll("table").forEach(function (t) {
                Array.from(t.tBodies).forEach(function (tbody) {
                  Array.from(tbody.rows)
                    .filter(function (row) {
                      return row.matches("[data-known-issue-row]");
                    })
                    .sort(function (a, b) {
                      return compareRows(a, b, col, direction);
                    })
                    .forEach(function (row) {
                      tbody.appendChild(row);
                    });
                });
              });
            });

            allHeaders.forEach(function (header) {
              header.removeAttribute("data-sort-dir");
            });

            // Mark the matching header in every table.
            allHeaders.forEach(function (header) {
              if (header.getAttribute("data-sort-col") === sortColumns[index]) {
                header.setAttribute(
                  "data-sort-dir",
                  direction === 1 ? "asc" : "desc"
                );
              }
            });
          }

          th.addEventListener("click", sortBy);
          th.addEventListener("keydown", function (event) {
            if (event.key === "Enter" || event.key === " ") {
              event.preventDefault();
              sortBy();
            }
          });
        });
      });
    });

    function populateOptions(select, values, firstLabel) {
      const selected = select.value;

      select.replaceChildren(new Option(firstLabel, ""));

      Array.from(new Set(values.filter(Boolean)))
        .sort(collator.compare)
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
      records.map(function (record) {
        return record.domain;
      }),
      "Domain"
    );

    populateOptions(
      target,
      records.map(function (record) {
        return record.target;
      }),
      "Target"
    );

    function applyFilters() {
      const query = normalize(search.value);
      const selectedDomain = domain.value;
      const selectedTarget = target.value;
      const selectedStatus = normalize(statusFilter.value);

      let visibleCount = 0;

      records.forEach(function (record) {
        const matchesSearch =
          !query || record.searchText.includes(query);

        const matchesDomain =
          !selectedDomain || record.domain === selectedDomain;

        const matchesTarget =
          !selectedTarget || record.target === selectedTarget;

        const matchesStatus =
          !selectedStatus || record.status === selectedStatus;

        const visible =
          matchesSearch &&
          matchesDomain &&
          matchesTarget &&
          matchesStatus;

        record.row.hidden = !visible;

        if (visible) visibleCount++;
      });

      // Hide domain sections with no matching rows.
      sections.forEach(function (section) {
        section.hidden = !section.querySelector(
          "[data-known-issue-row]:not([hidden])"
        );
      });

      if (countMessage) {
        countMessage.textContent =
          "Showing " + visibleCount + " matching item" +
          (visibleCount === 1 ? "" : "s") + ".";
      }

      if (empty) {
        empty.style.display = visibleCount === 0 ? "block" : "none";
      }
    }

    search.addEventListener("input", applyFilters);

    [domain, target, statusFilter].forEach(function (control) {
      control.addEventListener("change", applyFilters);
    });

    reset.addEventListener("click", function () {
      search.value = "";
      domain.value = "";
      target.value = "";
      statusFilter.value = "";

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

  // Reinitialize after MkDocs Material instant navigation.
  if (typeof document$ !== "undefined") {
    document$.subscribe(initializeKnownIssuesFilters);
  }
})();
</script>
