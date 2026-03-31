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

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="text-decoration: bold; font-size: 1.2em;">
<th>TABLE/TOPIC</th>
<th>SUMMARY</th>
<th style='text-align: center;'><span class="tooltip tooltip-left">BR<span class="tooltiptext">Final Beta Release</span></span></th>
</tr>
</thead>
<tbody>

<!-- BIOSPEC -->
<tr class="domain-row-pending"><td colspan="3"><strong>Biospecimens & Omics</strong></td></tr>
<tr>
<td class='table-cell'>Nails & Urine</td>
<td style='word-wrap: break-word; white-space: normal;'>Data dictionary level values have quotes around them, causing the downloaded to have double quotes (e.g. 1=""positive"").</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- MRI -->
<tr class="domain-row-pending"><td colspan="3"><strong>MRI</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>XCP-D</td>
<td style='word-wrap: break-word; white-space: normal;'>Tabulated XCP-D <span class="tooltip">Myers-Labonte tables<span class="tooltiptext"><code>img_xcpd_hash-{X}_space-fsLR_seg-MyersLabonte_stat-mean_desc-_morph</code></span></span> metadata corrected to have a <code>sub_domain</code> value of <code>Structural MRI</code>.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<!-- NCL -->
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

<!-- SED -->
<tr class="domain-row-pending"><td colspan="4"><strong>Social & Environmental Determinants</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Demographics</td>
<td style='word-wrap: break-word; white-space: normal;'>The variables <code>sed_bm_demo_residence_{001|002}</code>, present in the prior release, are missing in the current release and will be added back.</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>
</tbody>
</table>
