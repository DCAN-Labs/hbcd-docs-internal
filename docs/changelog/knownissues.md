
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

#### General

<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
  <th style="padding-top: 2px; padding-bottom: 2px">Issue/Update</th>
  <th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td><b>'Instruction' metadata text may be incomplete/misaligned</b> - <a href="https://docs.hbcdstudy.org/latest/changelog/knownissues/#instruction-metadata-read-carefully">see details</a></td>
<td>TBD</td>
</tr>
<tr>
<td>2</td>
<td><b><i class="fa fa-brain"></i> Imaging: Run ID Order Not Chronological</b> - <a href="https://docs.hbcdstudy.org/latest/changelog/knownissues/#imaging-data">see details</a></td>
<td>TBD</td>
</tr>
</tbody>
</table>

#### <i class="fa fa-people-arrows"></i>&nbsp; Behavior & Caregiver-Child Interaction
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
<th style="padding-top: 2px; padding-bottom: 2px">Table/Var</th>
<th style="padding-top: 2px; padding-bottom: 2px">Issue/Update</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>CHAOS</td>
<td><b>Scoring Correction:</b> implement scoring, including prorated scores</td>
<td>20.2</td>
</tr>
<tr>
<td>2</td>
<td>ECBQ (<code>mh_cg_ecbq</code>)</td>
<td><b>Data Correction:</b> Change coding for "Does not apply" to 8 to be consistent with IBQR</td>
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
</tbody>
</table>

#### <i class="fa fa-vial"></i>&nbsp; Biospecimen & Omics
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
<th style="padding-top: 2px; padding-bottom: 2px">Table/Var</th>
<th style="padding-top: 2px; padding-bottom: 2px">Issue/Update</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>Nails/Urine</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Request:</b> Add 'ANALYSIS DATE' for Biospec tables.</td>
<td>TBD</td>
</tr>
</tbody>
</table>

#### <i class="fa-solid fa-puzzle-piece"></i>&nbsp; Neurocognition & Language

<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
<th style="padding-top: 2px; padding-bottom: 2px">Table/Var</th>
<th style="padding-top: 2px; padding-bottom: 2px">Issue/Update</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>SPM-2 Infant (<code>ncl_cg_spm2__inf</code>)</td>
<td><b>Add Variables:</b> age fields</td>
<td>TBD (20.X)</td>
</tr>
</tbody>
</table>

#### <i class="fa fa-heart-pulse"></i>&nbsp; Physical Health
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
<th style="padding-top: 2px; padding-bottom: 2px">Table/Var</th>
<th style="padding-top: 2px; padding-bottom: 2px">Issue/Update</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>BISQ</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Add missing score fields</b>: infant_sleep_score, parent_behavior_score, parent_perception_score, total_score</td>
<td>20.2</td>
</tr>
</tbody>
</table>

#### <i class="fa-solid fa-baby"></i>&nbsp; Pregnancy & Exposure, Including Substance Use
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
<th style="padding-top: 2px; padding-bottom: 2px">Table/Var</th>
<th style="padding-top: 2px; padding-bottom: 2px">Issue/Update</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>TLFB (missing V02)</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Error:</b> TLFB missing for subset of participants at V02. Solution/fix currently unclear.</td>
<td>20.2</td>
</tr>
<tr>
<td>2</td>
<td>pex_bm_health</td>
<td><b>Data Correction:</b> Fix inconsistently provided ICD codes for Pregnancy/Infant Health</td>
<td>TBD (R3.X)</td>
</tr>
</tbody>
</table>

#### <i class="fas fa-city"></i>&nbsp; Social & Environmental Determinants
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
<th style="padding-top: 2px; padding-bottom: 2px">Table/Var</th>
<th style="padding-top: 2px; padding-bottom: 2px">Issue/Update</th>
<th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<tr>
<td>1</td>
<td>PACES &lt;18 (<code>sed_cg_paces</code>)</td>
<td><b>Data Error:</b> Add missing score fields (currently under LORIS review)</td>
<td>TBD</td>
</tr>
</tbody>
</table>
