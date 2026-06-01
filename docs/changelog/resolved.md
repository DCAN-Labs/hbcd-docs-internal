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

# Resolved Issues & Updates Archive

!!! danger "Resolved Known Issues & Updates"
    **This page contains a running record of issues and updates verified as RESOLVED by Workgroups/SMEs** (from BR21.0; see prior release notes for earlier records). Until final sign off, items remain listed as ACTIVE in [Known Issues & Pending Updates](knownissues.md). Individual BR release notes may include *provisional* updates that are not yet verified.

<p style="font-size: 1.2em; color: #555; text-align: center;">
<i class="fas fa-bug" style="color: #f97316; font-size: 1em;"></i> = Resolved Known Issue &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-rotate" style="color: #199bd6; font-size: 1em;"></i> = Completed Pending Update &nbsp;&nbsp;&nbsp;
<i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.1em;"></i> = Final BR with Fix</i>
</p>

<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Domain</th>
<th>Table/Topic</th>
<th>Summary</th>
<th style='text-align: center;'>
  <i class="fa-solid fa-location-crosshairs" style="color: #489000; font-size: 1.3em;"></i>
</th></tr>
</tr>
</thead>
<tbody>

<!-- GENERAL -->
<tr>
<td>NA</td>
<td>Language</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>  Addition of language of administration across all instruments where applicable.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- ADMIN -->
<tr>
<td>ADM</td>
<td>Study Navigators</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Populate SUBSTANCE_USE and OTHER checkbox fields.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- BIOSPEC -->
<tr>
<td rowspan="4">BIO</td>
<td>Nails</td>
<td><i class="fas fa-bug icon-bug"></i>  Add unit (mg) for <code>nails_results_nail_weight</code> variable.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td>Urine</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>  Add creatinine results (<code>bio_creat_u</code>).</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td>Nails & Urine</td>
<td><i class="fas fa-bug icon-bug"></i>  Remove quotes from level values to prevent double quotes in downloaded data (e.g. 1=""positive"").</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>
<tr>
<td>Olink</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i>  Addition of Olink Explore 384 Inflammation 1 Panel, proteomics measure of maternal inflammation during pregnancy</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- DEMO -->
<tr>
<td rowspan="2">Demo</td>
<td>Visit Info</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> SU flags will include Nail toxicology results in addition to Urine.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>

<tr>
<td>.set files</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> 
Add <code>work_{002–004}_post</code> and <code>work_004__01</code> (adult table).
</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>

<!-- EEG -->
<tr>
<td rowspan="2">EEG</td>
<td>MADE</td>
<td><i class="fas fa-bug icon-bug"></i>  N=3 V04 session derivatives are missing corresponding tabulated data for FACE/MMN tasks</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td>.set files</td>
<td><i class="fas fa-bug icon-bug"></i>  Update EEG .set files to include subject release IDs.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- MH -->
<tr>
<td>MH</td>
<td>ERICA</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Add the ERICA instrument (<code>mh_cg_erica{_rel}_3_9m</code>); raw scores only</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- MRI -->
<tr>
<td rowspan="4">MRI</td>
<td>Summary Forms</td>
<td style='word-wrap: break-word; white-space: normal;'><i class="fa-solid fa-rotate icon-rotate"></i>  Add MRI Scan Session + Data Summary Forms (information from the MRI technician obtained on day of scan).</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td>BrainSwipes</td>
<td style='word-wrap: break-word; white-space: normal;'><i class="fa-solid fa-rotate icon-rotate"></i>   BrainSwipes QC results updated with latest results available in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>
<td>XCP-D</td>
<td style='word-wrap: break-word; white-space: normal;'><i class="fas fa-bug icon-bug"></i>  Metadata values for <code>sub_domain</code> were corrected to <code>Structural MRI</code> for tabulated XCP-D Myers-Labonte <code>*morph.tsv</code> files.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>
<tr>
<td>Raw BIDS</td>
<td style='word-wrap: break-word; white-space: normal;'><i class="fas fa-bug icon-bug"></i>  Resolved 2 corrupted bold runs in V02 raw BIDS (see filepaths in <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>).</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- NCL -->
<tr>
<td rowspan="3">NCL</td>
<td>Bayley-4</td>
<td><i class="fa-solid fa-rotate icon-rotate"></i> Add item-level scores.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>

<tr>
<td>MLDS</td>
<td style='word-wrap: break-word; white-space: normal;'><i class="fas fa-bug icon-bug"></i>  Correct Data Dictionary 'description' element to remove erroneous text that appears at end (e.g., "Â Â Â")</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>
<tr>
<td>Vineland</td>
<td><i class="fas fa-bug icon-bug"></i>  Correct subset of variables with typo in the spelling of "receptive."<br>
<i class="fa-solid fa-rotate icon-rotate"></i>   Addition of language field to <code>ncl_cg_vabs</code>.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- PH -->
<tr>
<td rowspan="1">PH</td>
<td>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'>
  <i class="fas fa-bug icon-bug"></i> Remove <code>ph_ch_anthro_002</code><br>
  <i class="fa-solid fa-rotate icon-rotate"></i>  Add age-based z-scores to <code>ph_ch_anthro</code> (see <a href="https://docs.hbcdstudy.org/latest/instruments/physhealth/growth/#warning">Z-Scores Excluded</a>).
</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>

<!-- SED -->

<tr><td rowspan="3">SED</td>
<td>C-PACEs</td>
<td><i class="fas fa-bug icon-bug"></i>  Summary scores are inaccurate; until corrected, users can compute scores following the provided scoring documentation.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<td>Demographics</td>
<td>
  <i class="fa-solid fa-rotate icon-rotate"></i>  Add variables on Other Biological Parent (adult table).
  <br>
  <i class="fa-solid fa-rotate icon-rotate"></i>  
Add V01 household income (<code>income_002</code>) (adult table)
<br>
<i class="fas fa-bug icon-bug"></i>  Remove descriptive fields (e.g. <code>roster_001__00</code>) <em>[BR data only]</em>.
</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td>Demographics</td>
<td><i class="fas fa-bug icon-bug"></i>  Add back <code>sed_bm_demo_residence_{001|002}</code> (present in prior release then missing).<br>
<i class="fa-solid fa-rotate icon-rotate"></i>  Child Demo: Household roster updated to clarify that counts exclude the main child.
</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

</tbody>
</table>
