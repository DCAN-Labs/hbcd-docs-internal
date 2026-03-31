<style>
.wy-nav-content {
    width: 100% !important;
    max-width: 100% !important;
    flex-grow: 1 !important;
}
</style>

# Resolved Known Issues & Updates

<table class="compact-table-no-vertical-lines">
<thead>
<tr style="text-decoration: bold; font-size: 1.2em;">
<th>TABLE/TOPIC</th>
<th>SUMMARY</th>
<th style='text-align: center;'><span class="tooltip tooltip-left">BR<span class="tooltiptext">Final Beta Release</span></span></th>
</tr>
</thead>
<tbody>

<tr class="domain-row-pending"><td colspan="3"><strong>BIOSPECIMEN &amp; OMICS</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Nails &amp; Urine</td>
<td style='word-wrap: break-word; white-space: normal;'>Data dictionary level values have quotes around them, causing the downloaded to have double quotes (e.g. 1=""positive"").</td>
<td style='text-align: center;'><span class='br-pill br-210'>21.0</span></td>
</tr>

<tr class="domain-row-issue"><td colspan="4"><strong>DEMOGRAPHICS</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>Demographics</td>
<td style='word-wrap: break-word; white-space: normal;'>Variables on the Other Biological Parent are missing from <code>sed_bm_demo</code>.</td>
<td style='text-align: center;'><span class='br-pill br-211'>21.1</span></td>
</tr>

<tr class="domain-row-pending"><td colspan="3"><strong>MRI</strong></td></tr>
<tr>
<td class='table-cell' style='font-weight: bold;'>XCP-D</td>
<td style='word-wrap: break-word; white-space: normal;'>Tabulated XCP-D Myers-Labonte tables (<code>img_xcpd_hash-{X}_space-fsLR_seg-MyersLabonte_stat-mean_desc-_morph</code>) metadata corrected to have a <code>sub_domain</code> value of <code>Structural MRI</code> (currently <code>Resting State fMRI</code>).</td>
<td style='text-align: center;'>21.0</td>
</tr>

<tr class="domain-row-issue"><td colspan="4"><strong>NEUROCOGNITION &amp; LANGUAGE</strong></td></tr>
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
</tbody>
</table>
