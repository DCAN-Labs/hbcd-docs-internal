
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
<td style="word-wrap: break-word; white-space: normal;"><b>Correct Adjusted Age (<code>age_adjusted</code>) variable across instruments:</b>  inaccurately calculated based on the LMP (EDD +280 days) instead of the EDD (shifts age upwards by ~40 weeks).</td>
<td>20.1</td>
</tr>
<tr>
<td>2</td>
<td><b>'Instruction' metadata text may be incomplete/misaligned</b> - <a href="https://docs.hbcdstudy.org/latest/changelog/knownissues/#instruction-metadata-read-carefully">see details</a></td>
<td>TBD</td>
</tr>
<tr>
<td>3</td>
<td><b><i class="fa fa-brain"></i> Imaging: Run ID Order Not Chronological</b> - <a href="https://docs.hbcdstudy.org/latest/changelog/knownissues/#imaging-data">see details</a></td>
<td>TBD</td>
</tr>
</tbody>
</table>

#### <i class="fas fa-id-card"></i>&nbsp; Demographics 

<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
<tr>
<th style="padding-top: 2px; padding-bottom: 2px">#</th>
  <th style="padding-top: 2px; padding-bottom: 2px">Table/Variable</th>
  <th style="padding-top: 2px; padding-bottom: 2px">Issue/Update</th>
  <th style="padding-top: 2px; padding-bottom: 2px">Fix</th>
</tr>
</thead>
<tbody>
<tr><td colspan="3" style="padding: 2px 8px;"><b>Basic Demographics (<code>sed_basic_demographics</code>)</b></td></tr>
<tr>
<td>1</td>
<td>Child Multi-Ethnicity</td>
<td><b>Remove:</b> child_ethnoracial_acs_by_multi_ethnicity V01 data</td>
<td>20.1</td>
</tr>
<tr>
<td>2</td>
<td>Child Multi-Race</td>
<td><b>Remove:</b> child_ethnoracial_acs_by_multi_race (duplicate coding of Child Multi-Ethnicity)</td>
<td>20.1</td>
</tr>
<tr>
<td>3</td>
<td>screen_mother_race</td>
<td><b>Data Error:</b> Remove invalid response option 2 = <i>Hawaiian</i></td>
<td>20.1</td>
</tr>
<tr><td colspan="3"></td></tr>
<tr><td colspan="3" style="padding: 2px 8px;"><b>Visit Information (<code>par_visit_data</code>)</b></td></tr>
<tr>
<td>1</td>
<td>participant_withdrawal_date</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Error:</b> Change sentinel value for withdrawal date of participants who did NOT withdraw (<code>12/26/1999</code>) to null</td>
<td>20.1</td>
</tr>
<tr>
<td>2</td>
<td>su_flag_bio_*</td>
<td><b>Remove:</b> SU flags derived from USDTL urine toxicology for V02 (not collected)</td>
<td>20.1</td>
</tr>
<tr>
<td>3</td>
<td>su_flag_tlfb_*</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Error:</b> Correct erroneous positive TLFB SU flags (e.g. nicotine use reported only weeks 3 & 4, but V01 & V02 'self_report_nicotine'=1)</td>
<td>20.1</td>
</tr>
<tr>
<td>4</td>
<td>su_flag_tlfb_*</td>
<td><b>Data Error:</b> Change TLFB SU flags for participants without a V02 from 'no' to 'null'</td>
<td>20.2</td>
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
<td>20.1</td>
</tr>
<tr>
<td>2</td>
<td>ecPROMIS Peer Relationships</td>
<td><b>Correct prorated scoring</b></td>
<td>20.1</td>
</tr>
<tr>
<td>3</td>
<td>ecPROMIS Self-Reg/Flex</td>
<td><b>Correct prorated scoring</b></td>
<td>20.1</td>
</tr>
<tr>
<td>4</td>
<td>ecPROMIS Ch-CG Rel</td>
<td><b>Correct prorated scoring</b> (for both versions: &lt;1 yr & 1-5 yr)</td>
<td>20.1</td>
</tr>
<tr>
<td>5</td>
<td>MAPS-TL/PROMIS</td>
<td><b>Workgroup validate prorated scoring</b></td>
<td>20.1</td>
</tr>
<tr>
<td>6</td>
<td>ECBQ (<code>mh_cg_ecbq</code>)</td>
<td><b>Data Correction:</b> Change coding for "Does not apply" to 8 to be consistent with IBQR</td>
<td>20.2</td>
</tr>
<tr>
<td>7</td>
<td>ECBQ (<code>mh_cg_ecbq</code>)</td>
<td><b>Data Error:</b> Add missing score fields (currently under LORIS review)</td>
<td>TBD</td>
</tr>
<tr>
<td>8</td>
<td>IBQR (<code>mh_cg_ibqr</code>)</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Shadow Matrix Error:</b> Missingness reason showing as LOGIC SKIPPED, but missingess is not caused by branching logic. Currently under LORIS review.</td>
<td>TBD</td>
</tr>
<tr>
<td>9</td>
<td>ECBQ &amp; IBQR</td>
<td><b>Remove Variables:</b> administration (all, partial, none) &amp; data_taken</td>
<td>TBD</td>
</tr>
<tr>
<td>10</td>
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
<td>Urine</td>
<td><b>Data Error:</b> Missing values for urinary cotinine (<code>bio_c_cot_u</code>) were erroneously set to <code>0</code> (N = 18) and will be restored in a future release.</td>
<td>20.1</td>
</tr>
<tr>
<td>2</td>
<td>Nails/Urine</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Request:</b> Large gaps between collection and analysis dates (e.g., over 100–300 days, compared to the 30-day limit specified by internal SOPs) for a large number of samples. Next steps: determine whether this reflects a data entry or site-level issue.</td>
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
<td><b>Add missing status scores</b> that are currently missing for all but one subscale</td>
<td>20.1</td>
</tr>
<tr>
<td>2</td>
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
<td>BFH</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Add variables:</b> add remaining variables flagged for inclusion (currently only 2 of the 17 present)</td>
<td>20.1</td>
</tr>
<tr>
<td>2</td>
<td>BISQ</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Add missing score fields</b>: infant_sleep_score, parent_behavior_score, parent_perception_score, total_score</td>
<td>20.1</td>
</tr>
<tr>
<td>3</td>
<td>Growth (<code>ph_ch_anthro</code>)</td>
<td><b>Data Request:</b> recalculate z-score based on actual DOB</td>
<td>20.1</td>
</tr>
<tr>
<td>4</td>
<td>ecPROMIS PA/Greenspace (<code>ph_cg_pms__pags</code>)</td>
<td><b>Data Error:</b> Add missing score fields (currently under LORIS review)</td>
<td>TBD</td>
</tr>
<tr>
<td>5</td>
<td>ecPROMIS Sleep (<code>ph_cg_pms__sleep</code>)</td>
<td><b>Data Error:</b> Add missing score fields (currently under LORIS review)</td>
<td>TBD</td>
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
<td>pex_bm_apa</td>
<td><b>Data Request:</b> Remove Level 2 data for participants not meeting Level 1 threshold</td>
<td>20.1</td>
</tr>
<tr>
<td>2</td>
<td>pex_bm_apa_apa2_*</td>
<td><b>Data Correction:</b> Add missing APA Level 2 scores (<i>all are currently blank</i>)</td>
<td>20.1</td>
</tr>
<tr>
<td>3</td>
<td>TLFB</td>
<td><b>Add Variables:</b> Add all age variable fields</td>
<td>20.1</td>
</tr>
<tr>
<td>4</td>
<td>TLFB</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Request:</b> Detailed variable breakdown (e.g. create new subcategories to separate out 'nicotine' from 'cigarettes, e-cigarettes, cigars etc.' & extract frequency for each)</td>
<td>20.1</td>
</tr>
<tr>
<td>5</td>
<td>TLFB (PNR)</td>
<td><b>Data Error:</b> Postnatal Recruits reported in v1 or v2, but should be v3</td>
<td>20.2</td>
</tr>
<tr>
<td>6</td>
<td>TLFB (missing V02)</td>
<td style="word-wrap: break-word; white-space: normal;"><b>Data Error:</b> TLFB missing for subset of participants at V02. Solution/fix currently unclear.</td>
<td>20.2</td>
</tr>
<tr>
<td>7</td>
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
<td>sed_bm_demo (Adult)</td>
<td><b>SME Request:</b> Remove Roster Gender fields (<i>based on internal list</i>)</td>
<td>20.1</td>
</tr>
<tr>
<td>2</td>
<td>sed_bm_demo_child</td>
<td><b>SME Request:</b> Remove Roster Gender AND Sex fields (<i>based on internal list</i>)</td>
<td>20.1</td>
</tr>
<tr>
<td>3</td>
<td>sed_bm_demo_child</td>
<td><b>SME Request:</b> Remove Roster '_table' fields (eg <i>roster_table_13</i>)</td>
<td>20.1</td>
</tr>
<tr>
<td>4</td>
<td>sed_bm_demo_child__roster_001__01</td>
<td><b>Remove variable</b> (<i>SED request - duplicate of roster_001</i>)</td>
<td>20.1</td>
</tr>
<tr>
<td>5</td>
<td>sed_bm_demo_transp_001</td>
<td><b>Add Variables</b>: transportation</td>
<td>20.1</td>
</tr>
<tr>
<td>6</td>
<td>sed_bm_demo_disab_*</td>
<td><b>Add Variables</b>: disability</td>
<td>20.1</td>
</tr>
<tr>
<td>7</td>
<td>sed_cg_employ_002</td>
<td><b>DD Update:</b> Change type_level to 'Ordinal'</td>
<td>20.1</td>
</tr>
<tr>
<td>8</td>
<td>sed_cg_hce_007 & sed_cg_hce_008_i_0</td>
<td><b>DD Update:</b> Change type_level to 'Ordinal'</td>
<td>20.1</td>
</tr>
<tr>
<td>9</td>
<td>sed_cg_hce_002</td>
<td><b>DD Update:</b> Change type_level to 'Nominal'</td>
<td>20.1</td>
</tr>
<tr>
<td>10</td>
<td>sed_cg_employ_101*</td>
 <td style="word-wrap: break-word; white-space: normal;"><b>DD Update:</b> use "spouse/partner" in 'Description': “Do you have a partner?”</td>
<td>20.1</td>
</tr>
<tr>
<td>11</td>
<td>sed_*_{ace/car_sf/pedals}_sensitive</td>
<td><b>Remove 'sensitive' variables across SED tables</b></td>
<td>20.1</td>
</tr>
<tr>
<td>12</td>
<td>sed_cg_nsc (Experiences w/ Police)</td>
<td><b>Remove instrument</b></td>
<td>TBD</td>
</tr>
<tr>
<td>13</td>
<td>HOME-21 (<code>sed_cg_home_it</code>)</td>
<td><b>Data Error:</b> Add missing score fields (currently under LORIS review)</td>
<td>TBD</td>
</tr>
<tr>
<td>14</td>
<td>PACES &lt;18 (<code>sed_cg_paces</code>)</td>
<td><b>Data Error:</b> Add missing score fields (currently under LORIS review)</td>
<td>TBD</td>
</tr>
</tbody>
</table>
