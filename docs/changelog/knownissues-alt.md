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
.br-210 {
  background-color: #e6f0ff;
  color: #1a4fb3;
}
.br-211 {
  background-color: #e9f7ef;
  color: #1e7e34;
}
/* TBD */
.br-tbd {
  background-color: #f1f3f5;
  color: #666;
  font-style: italic;
}
</style>

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

# Known Issues & Pending Updates-ALT (UNDER CONSTRUCTION)

!!! danger "Active Items Only"
    **This page lists ACTIVE issues/updates targeted for upcoming BRs, or included in the current BR pending final Workgroup/SME sign-off.** Items are not considered resolved until final review is complete. A running record of verified items is archived to [Resolved Issues & Updates](resolved.md) (from BR21.0; see prior release notes for earlier records). See the [HBCD Data Release Docs](https://docs.hbcdstudy.org/latest/changelog/issues-updates/) for corresponding public releases (PR) <span class="tooltip"> <i class="fa-solid fa-circle-info"></i><span class="tooltiptext">Items addressed in a BR are not reflected as resolved publicly until the corresponding PR is released</span></span>.


## BEHAVIOR &amp; CAREGIVER-CHILD INTERACTION

<table class="compact-table-no-vertical-lines">
<thead><tr><th>Table/Topic</th><th>Description</th><th><span class="tooltip tooltip-left">BR<span class="tooltiptext">Target Beta Release</span></span></th></tr></thead>
<tbody>
<tr>
<td rowspan="3">ERICA</td>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i>Remove date taken, age, and language fields as specified by WG.</td>
<td><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr><td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> Recalculate all <code>age</code> and <code>date_taken</code> fields using <i>visit date</i> instead of <i>date coded</i>; currently to be excluded from PR2.1.</td>
<td><span class='br-pill br-tbd'>TBD</span></td>
</tr>
<tr><td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i>Remove 2 data points specified by WG from the ERICA Codes (3-9M) table.</td><td><span class='br-pill br-tbd'>TBD</span></td></tr>
<tr>
<td>MAPS-TL</td><td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i>Notes appear in the score field in both versions (Infant/Toddlerhood) and will be moved to a separate field.</td><td><span class='br-pill br-tbd'>TBD</span></td>
</tr>
<tr><td>MAPS-TL (&lt;1yr)</td><td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i>N=4 participants in <code>mh_cg_mapdb__inf</code> had no responses, but were scored 0; until resolved, set to null before analysis.</td><td><span class='br-pill br-tbd'>TBD</span></td>
</tr>
<tr><td>MAPS-TL (Tod)</td><td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i>Pro-rated scoring is not yet applied for missing responses in the <code>mh_cg_mapdb__tod</code>, resulting in N=16 participants missing scores.</td>
<td><span class='br-pill br-tbd'>TBD</span></td>
</tr>
<tr>
<td>ECBQ</td>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i> Change coding for "Does not apply" to 8 to match the IBQ-R.</td>
<td><span class='br-pill br-tbd'>TBD</span></td>
</tr>
</tbody></table>

### BIOSPECIMEN &amp; OMICS

<table class="compact-table-no-vertical-lines">
<thead><tr><th>Table/Topic</th><th>Description</th><th><span class="tooltip tooltip-left">BR<span class="tooltiptext">Target Beta Release</span></span></th></tr></thead>
<tbody>
<tr>
<td>Nails</td>
<td>Add unit (mg) for <code>nails_results_nail_weight</code> variable.</td>
<td><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td>Nails</td>
<td>Use <code>bio_bm_biosample_nails_typ_collection_nail_type</code> <em>specimen type</em> table for nail type (<em>results</em> table values are all 4 (Unknown)).</td>
<td><span class='br-pill br-211'>21.1</span></td>
</tr> 
<tr>




