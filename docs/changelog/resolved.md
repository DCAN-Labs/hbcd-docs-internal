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



<p style="font-size: 1em; color: #555; margin-bottom: 1em;">
<i class="fa-solid fa-rotate" style="color: #199bd6; font-size: 1em;"></i>&nbsp;= Completed Pending Update &nbsp;&nbsp;&nbsp;&nbsp;
<i class="fas fa-bug" style="color: #f97316; font-size: 1em;"></i>&nbsp;= Resolved Known Issue
</p>
<table class="compact-table-no-vertical-lines">
<thead>
<tr>
<th>Domain</th>
<th>Table/Topic</th>
<th>Summary</th>
<th style='text-align: center;'><span class="tooltip tooltip-left">BR<span class="tooltiptext">Final Beta Release</span></span></th>
</tr>
</thead>
<tbody>

<!-- GENERAL -->
<tr>
<td><i>NA/All</i></td>
<td>Language</td>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i> Addition of language of administration across all instruments where applicable.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- ADMIN -->
<tr>
<td><b>ADM</b></td>
<td>Study Navigators</td>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i> Populate SUBSTANCE_USE and OTHER checkbox fields.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- BIOSPEC -->
<tr>
<td rowspan="3"><b>BIO</b></td>
<td>Nails</td>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> Add unit (mg) for <code>nails_results_nail_weight</code> variable.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>

<tr>
<td>Nails & Urine</td>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> Remove quotes from level values to prevent double quotes in downloaded data (e.g. 1=""positive"").</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>
<tr>
<td>Olink</td>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i> Addition of Olink Explore 384 Inflammation 1 Panel, proteomics measure of maternal inflammation during pregnancy</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- DEMO -->
<tr>
<td><b>Demo</b></td>
<td>.set files</td>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i>
Add <code>work_{002–004}_post</code> and <code>work_004__01</code> (adult table).
</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>

<!-- EEG -->
<tr>
<td><b>EEG</b></td>
<td>.set files</td>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> Update EEG .set files to include subject release IDs.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- MH -->
<tr>
<td><b>MH</b></td>
<td>ERICA</td>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i> Addition of the ERICA instrument tables (<code>mh_cg_erica{_rel}_3_9m</code>); raw scores only</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- MRI -->
<tr>
<td rowspan="3"><b>MRI</b></td>
<td>BrainSwipes</td>
<td style='word-wrap: break-word; white-space: normal;'><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i>  BrainSwipes QC results updated with latest results available in the <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>
<td>XCP-D</td>
<td style='word-wrap: break-word; white-space: normal;'><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> Metadata values for <code>sub_domain</code> were corrected to <code>Structural MRI</code> for tabulated XCP-D Myers-Labonte <code>*morph.tsv</code> files.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>
<tr>
<td>Raw BIDS</td>
<td style='word-wrap: break-word; white-space: normal;'><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> Resolved 2 corrupted bold runs in V02 raw BIDS (see filepaths in <a href="https://hbcd-docs-private.lassoinformatics.com/#download">HBCD Private Release Notes</a>).</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- NCL -->
<tr>
<td rowspan="2"><b>NCL</b></td>
<td>MLDS</td>
<td style='word-wrap: break-word; white-space: normal;'><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> Correct Data Dictionary 'description' element to remove erroneous text that appears at end (e.g., "Â Â Â")</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>
<tr>
<td>Vineland</td>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> Correct subset of variables with typo in the spelling of "receptive."<br>
<i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i>  Addition of language field to <code>ncl_cg_vabs</code>.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- PH -->
<tr>
<td rowspan="1"><b>PH</b></td>
<td>Growth</td>
<td style='word-wrap: break-word; white-space: normal;'><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> 
Remove <code>ph_ch_anthro_002</code>
</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>

<!-- SED -->

<tr><td rowspan="2"><b>SED</b></td>
<td>Demographics</td>
<td><i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i> 
Add V01 household income (<code>income_002</code>) (adult table)
<br>
<i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> Remove descriptive fields (e.g. <code>roster_001__00</code>) <em>[BR data only]</em>.
</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>
<tr>
<td>Demographics</td>
<td><i class="fas fa-bug" style="color: #f97316; margin-right: 0.4em; font-size: 1em;"></i> Add back <code>sed_bm_demo_residence_{001|002}</code> (present in prior release then missing).<br>
<i class="fa-solid fa-rotate" style="color: #199bd6; margin-right: 0.4em; font-size: 1em;"></i> Child Demo: Household roster updated to clarify that counts exclude the main child.
</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>
</tbody>
</table>






<!-- <table class="compact-table-no-vertical-lines">
<thead>
<tr style="text-decoration: bold; font-size: 1.2em;">
<th>TABLE/TOPIC</th>
<th>SUMMARY</th>
<th style='text-align: center;'><span class="tooltip tooltip-left">BR<span class="tooltiptext">Final Beta Release</span></span></th>
</tr>
</thead>
<tbody>
<tr class="domain-row-pending"><td colspan="3"><strong>Biospecimens & Omics</strong></td></tr>
<tr>
<td class='table-cell'>Nails & Urine</td>
<td style='word-wrap: break-word; white-space: normal;'>Data dictionary level values have quotes around them, causing the downloaded to have double quotes (e.g. 1=""positive"").</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>
<tr class="domain-row-pending"><td colspan="3"><strong>MRI</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>XCP-D</td>
<td style='word-wrap: break-word; white-space: normal;'>Tabulated XCP-D <span class="tooltip">Myers-Labonte tables<span class="tooltiptext"><code>img_xcpd_hash-{X}_space-fsLR_seg-MyersLabonte_stat-mean_desc-_morph</code></span></span> metadata corrected to have a <code>sub_domain</code> value of <code>Structural MRI</code>.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>
<tr class="domain-row-pending"><td colspan="4"><strong>NEUROCOGNITION &amp; LANGUAGE</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>MLDS</td>
<td style='word-wrap: break-word; white-space: normal;'>Correct Data Dictionary 'description' element to remove erroneous text that appears at end (e.g., "√Ç √Ç √Ç √Ç ")</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Vineland</td>
<td style='word-wrap: break-word; white-space: normal;'>Subset of variables have a typo in the spelling of "receptive."</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>
<tr class="domain-row-pending"><td colspan="4"><strong>Social & Environmental Determinants</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Demographics</td>
<td style='word-wrap: break-word; white-space: normal;'>The variables <code>sed_bm_demo_residence_{001|002}</code>, present in the prior release, are missing in the current release and will be added back.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>
</tbody>
</table> -->