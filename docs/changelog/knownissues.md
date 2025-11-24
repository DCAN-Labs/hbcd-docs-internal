
# Known Issues

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

<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
<th style="padding-top: 2px; padding-bottom: 2px">Table/Var</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fixed Issue/Update</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<!-- General -->
<tr><td colspan="4"><b>General</b></td></tr>
<tr>
<td>1</td>
<td>NA- Data Dictionary</td>
<td>'Instruction' metadata text may be incomplete/misaligned - <a href="https://docs.hbcdstudy.org/latest/changelog/knownissues/#instruction-metadata-read-carefully">see details</a></td>
<td>TBD</td>
</tr>
<tr>
<td>1</td>
<td>GA</td>
<td>Implausible gestational ages in multiple instruments - <a href="https://ucsd-actri.monday.com/boards/6045591843/pulses/18387442075">see details</a></td>
<td>TBD</td>
</tr>

<!-- BCGI -->
<tr><td colspan="4"><i class="fa fa-people-arrows"></i>&nbsp; <b>Behavior & Caregiver-Child Interaction</b></td></tr>
<tr>
<td>1</td>
<td>CHAOS</td>
<td><b>Scoring Correction:</b> implement scoring, including prorated scores</td>
<td>20.2</td>
</tr>
<tr>
<td>2</td>
<td>ECBQ (<code>mh_cg_ecbq</code>)</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Correction:</b> Change coding for "Does not apply" to 8 to be consistent with IBQR (currently noted on instrument page under <a href="https://docs.hbcdstudy.org/2.0/instruments/bcgi/ibqr/#scoring">Scoring Procedures</a>)</td>
<td>TBD</td>
</tr>
<tr>
<td>3</td>
<td>ECBQ &amp; IBQR</td>
<td><b>Remove Variables:</b> administration (all, partial, none) &amp; data_taken</td>
<td>TBD</td>
</tr>
<tr>
<td>4</td>
<td>ECBQ &amp; IBQR</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Error:</b> ~10 participants have both IBQR and ECBQ at V05 (should only have one or the other). Currently under LORIS review.</td>
<td>TBD</td>
</tr>
<!-- Biospec -->
<tr><td colspan="4"><i class="fa fa-vial"></i>&nbsp; <b>Biospecimen & Omics</b></td></tr>
<tr>
<td>1</td>
<td>Nails/Urine</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Request:</b> Add 'ANALYSIS DATE' for Biospec tables.</td>
<td>TBD</td>
</tr>
<tr>
<td>2</td>
<td>Nails/Urine</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Request:</b> Large gaps between collection and analysis dates - currently documented as a <a href="https://docs.hbcdstudy.org/latest/instruments/biospec/nails/#warning">Data Warning</a> on central HBCD Docs site. Currently under review by WG to determine next steps.</td>
<td>TBD</td>
</tr>

<!-- Neurocognition & Language -->
<tr><td colspan="4"><i class="fa-solid fa-puzzle-piece"></i>&nbsp; <b>Neurocognition & Language</b></td></tr>
<tr>
<td>1</td>
<td>CDI</td>
<td style="word-wrap: break-word; white-space: normal;">All percentile scores besides (`ncl_ch_cdiwgen_words_produced_percentile_both`) are incorrectly set to `type_data`=text, but should be integer.</td>
<td>20.1</td>
</tr>

<!-- Physical Health -->
<tr><td colspan="4"><i class="fa fa-heart-pulse"></i>&nbsp; <b>Physical Health</b></td></tr>
<tr>
<td>1</td>
<td>BISQ</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Add missing score fields</b>: infant_sleep_score, parent_behavior_score, parent_perception_score, total_score</td>
<td>20.2</td>
</tr>

<!-- PEX -->
<tr><td colspan="4"><i class="fa-solid fa-baby"></i>&nbsp; <b>Pregnancy & Exposure, Including Substance Use</b></td></tr>
<tr>
<td>1</td>
<td>TLFB (missing V02)</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Error:</b> TLFB missing for subset of participants at V02. Under LORIS review.</td>
<td>20.2</td>
</tr>
<tr>
<td>2</td>
<td>pex_bm_health</td>
<td><b>Data Correction:</b> Fix inconsistently provided ICD codes for Pregnancy/Infant Health</td>
<td>TBD (R3.X)</td>
</tr>

<!-- SED -->
<tr><td colspan="4"><i class="fas fa-city"></i>&nbsp; <b>Social & Environmental Determinants</b></td></tr>
<tr>
  <td>1</td>
  <td><code>sed_bm_ehits</code></td> 
  <td style="word-wrap: break-word; white-space: normal;"><code>total_score</code> and <code>score</code> both look like sum scores except former has inaccurate values - currently under review</td>
  <td>TBD</td>
</tr>

<!-- EEG & IMAGING-->
<tr><td colspan="4"><i class="fa fa-brain"></i>&nbsp; <b>EEG & Imaging</b></td></tr>
<tr>
<td>1</td>
<td>EEG</td>
<td>Missing EEG capping quality variables for V03 (<a href="https://ucsd-actri.monday.com/boards/6045591843/pulses/18386241252">monday.com</a>)</td>
<td>TBD</td>
</tr>
<tr>
<td>1</td>
<td>MR</td>
<td>Run ID Order Not Chronological - <a href="https://docs.hbcdstudy.org/latest/changelog/knownissues/#imaging-data">see details</a></td>
<td>TBD</td>
</tr>
</tbody>
</table>



