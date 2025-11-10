
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

## Instruction Metadata — Read Carefully

<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr>
    <th>KNOWN ISSUE - <span style="color: #f97316;">EXPECTED FIX TBD</span></th>
  </tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">
  Instruction text in each form’s metadata is automatically extracted from the most recent <code>instruction</code> field in the REDCap Data Dictionary (based on field order). Because this process is automated, it may produce the following issues:
  <ul>
    <li>If an instruction spans multiple fields, only the <b>last portion</b> will be captured.</li>
    <li>Some fields may display text intended for a <b>previous section</b>.</li>
  </ul>
  Manual review and correction of instruction metadata are planned for a future release (<b>expected fix date TBD</b>). For the most accurate and complete information, please refer to the original form.</td>
</tr>
</tbody>
</table>

## General

#### [1] Adjusted Age (<code>age_adjusted</code>) wrong for most instruments (Expected Fix: BR20.1)   
Caused by inaccurate calculation based on the LMP (EDD/EDC +280 days) instead of the EDD/EDC, which shifts the age upwards by ~40 weeks. Calculation will be corrected, after which outliers are likely caused by incorrectly entered 'Date of Administration'.     
**Impacted instrument examples (NON-EXHAUSTIVE LIST):** <code>adm_bm_screen</code>, <code>mh_cg_chaos</code>, <code>mh_cg_erica_fcm_adm_3_9m</code>, <code>mh_cg_erica_fcm_3_9m</code>, <code>mh_cg_fad</code>, <code>mh_cg_ibqr</code>, <code>sens_ch_setup</code>, <code>ncl_ch_mlds</code>, <code>ncl_cg_spm2_i_tod</code>, <code>nt_pa_gabi_rcpt</code> (<code>candidate_age</code> also inaccurate), <code>nt_ch_sens_i_qtn_2</code>, <code>ph_cg_pms_i_pags</code>, <code>ph_cg_inq</code>, <code>ph_cg_bisq</code> 

## <i class="fas fa-id-card"></i> Demographics
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr>
    <th style="width: 20%;">TABLE/DATA</th>
    <th style="width: 1%; text-align: center;">FIX</th>
    <th>KNOWN ISSUE</th>
  </tr>
</thead>
<tbody>
<tr>
  <td rowspan="3">Basic Demographics<br><code>sed_basic_demographics</code></td>
  <td><b>20.1</b></td> 
  <td><b>[1]</b> Mother Race (<code>screen_mother_race</code>) contains invalid response option 2 = <i>Hawaiian</i>.</td>
</tr>
<tr>
    <td><b>20.1</b></td> 
  <td style="word-wrap: break-word; white-space: normal;">
  <b>[2]</b> Child Multi-Race (<code>child_ethnoracial_acs_by_multi_race</code>) coding is a duplicate of Child Multi-Ethnicity (<code>child_ethnoracial_acs_by_multi_ethnicity</code>) and will be removed.
  </td>
</tr>
<tr>
<td><b>20.1</b></td> 
<td style="word-wrap: break-word; white-space: normal;">
<b>[3]</b> Child Multi-Race/Ethnicity V01 data will be removed. In the meantime, we do not recommend using V01 data for this variable in analyses.
</td>
</tr>
<tr>
<td rowspan="3">Visit Information<br><code>par_visit_data</code></td>
<td><b>20.1</b></td> 
<td style="word-wrap: break-word; white-space: normal;">
  <b>[1]</b> Participants who did <b>not</b> withdraw from the study (<code>participant_withdrawal</code> = “no”) are assigned a sentinel withdrawal date (<code>participant_withdrawal_date</code>) of <code>12/26/1999</code>. These values will be updated to null for clarity and consistency.
</td>
</tr>
<tr>
<td><b>20.1</b></td> 
<td style="word-wrap: break-word; white-space: normal;">
<b>[2]</b> Erroneous inclusion of Biospec substance use flags derived from USDTL urine toxicology</a> (<code>su_flag_bio_*</code>) for V02 (urine samples not collected at V02) - will be removed to FIX.
</td>
</tr>
<tr>
<td><b>20.2</b></td> 
<td style="word-wrap: break-word; white-space: normal;">
<b>[3]</b> The TLFB substance use flags (<code>su_flag_tlfb_*</code>) for participants who do not have a Visit 2 have incorrect values of 'no:' these will be corrected to 'null.'
</td>
</tr>
</tr>
</tbody>
</table>

## <i class="fa fa-people-arrows"></i> Behavior & Caregiver-Child Interaction
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr>
    <th>Type</th>
    <th>Fix</th>
    <th>Table/Var</th>
    <th>Issue/Update</th>
  </tr>
</thead>
<tbody>
<tr>
<td>Remove Var</td>
<td>TBD</td>
<td>ECBQ &amp; IBQR</td>
<td>Remove: administration (all, partial, none) &amp; data_taken</td>
</tr>
<tr>
<td>Data Correction</td>
<td>20.2</td>
<td>ECBQ</td>
<td>Change coding for "Does not apply" to 8 to be consistent with IBQR (currently = 0)</td>
</tr>
</tbody>
</table>

## <i class="fa fa-vial"></i> Biospecimen & Omics
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr>
    <th>Type</th>
    <th>Fix</th>
    <th>Table/Var</th>
    <th>Issue/Update</th>
  </tr>
</thead>
<tbody>
<tr>
<td>Data Error</td>
<td>20.1</td>
<td>Urine</td>
<td>Missing values for urinary cotinine (<code>bio_c_cot_u</code>) were erroneously set to <code>0</code> (N = 18) and will be restored in a future release.</td>
</tr>
</tbody>
</table>

## <i class="fa-solid fa-puzzle-piece"></i> Neurocognition & Language

<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr>
    <th>Type</th>
    <th>Fix</th>
    <th>Table/Var</th>
    <th>Issue/Update</th>
  </tr>
</thead>
<tbody>
<tr>
<td>Add Var</td>
<td>TBD (20.X)</td>
<td>SPM-2</td>
<td style="word-wrap: break-word; white-space: normal;">Add age fields</td>
</tr>
<tr>
<td>Add Var</td>
<td>20.1</td>
<td>SPM-2</td>
<td style="word-wrap: break-word; white-space: normal;">Add missing status scores (missing for all but one subscale)</td>
</tr>
</tbody>
</table>

## <i class="fa fa-heart-pulse"></i> Physical Health
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr>
    <th>Type</th>
    <th>Fix</th>
    <th>Table/Var</th>
    <th>Issue/Update</th>
  </tr>
</thead>
<tbody>
<tr>
<td>Add Var</td>
<td>20.1</td>
<td>BFH</td>
<td style="word-wrap: break-word; white-space: normal;">Add remaining variables flagged for inclusion (currently only 2 of the 17 present)</td>
</tr>
<tr>
<td>Data Error</td>
<td>20.1</td>
<td>BISQ</td>
<td style="word-wrap: break-word; white-space: normal;">Add missing score fields: infant_sleep_score, parent_behavior_score, parent_perception_score, total_score</td>
</tr>
</tbody>
</table>

## <i class="fa-solid fa-baby"></i> Pregnancy & Exposure, Including Substance Use
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr>
    <th>Type</th>
    <th>Fix</th>
    <th>Table/Var</th>
    <th>Issue/Update</th>
  </tr>
</thead>
<tbody>
<tr>
<td>Data Correction</td>
<td>TBD (R2.1)</td>
<td>pex_bm_health</td>
<td>Fix inconsistently provided ICD codes for Pregnancy/Infant Health</td>
</tr>
<tr>
<td>Data Correction</td>
<td>20.1</td>
<td>pex_bm_apa_anger_*</td>
<td>Add missing T-scores and total scores to APA 1/2 Anger subscale</td>
</tr>
<tr>
<td>Add Var</td>
<td>20.1</td>
<td>TLFB</td>
<td>Add all age variable fields</td>
</tr>
<tr>
<td>Data Error</td>
<td>20.1</td>
<td>TLFB flags</td>
<td>Correct self-report flags for visits</td>
</tr>
</tbody>
</table>

## <i class="fas fa-city"></i> Social & Environmental Determinants
<table class="compact-table-no-vertical-lines">
<thead style="background-color: #ff8a42cc; color: #695541ff;">
  <tr>
    <th>Type</th>
    <th>Fix</th>
    <th>Table/Var</th>
    <th>Issue/Update</th>
  </tr>
</thead>
<tbody>
<tr>
<td>SME Request</td>
<td>20.1</td>
<td>sed_bm_demo/demo_child</td>
<td>Sex/Gender fields to be removed</td>
</tr>
<tr>
<td>SME Request</td>
<td>20.1</td>
<td>sed_bm_demo/demo_child</td>
<td>Remove roster variables (eg child_roster_table_13)</td>
</tr>
<tr>
<td>Add Var</td>
<td>20.1</td>
<td>sed_bm_demo_{transp_001/disab_*}</td>
<td>Add transportation and disability variables</td>
</tr>
<tr>
<td rowspan="3">DD Update</td>
<td rowspan="3">20.1</td>
<td>sed_cg_{employ_002/hce_007/hce_008_i_0}</td>
<td>Change type_level to 'Ordinal'</td>
</tr>
<tr>
<td>sed_cg_hce_002</td>
<td>Change type_level to 'Nominal'</td>
</tr>
<tr>
<td>sed_cg_employ_101*</td>
 <td style="word-wrap: break-word; white-space: normal;">Change 'Description': “Do you have a partner?” to “Do you have a spouse/partner?”</td>
</tr>
</tbody>
</table>

## <a href="https://docs.hbcdstudy.org/latest/instruments/#mri" target="_blank"><i class="fa fa-brain"></i></a> Imaging Data

#### [1] Run ID Order Not Chronological (Expected Fix: TBD)   
For HBCD imaging data with multiple runs, the <code>run-{X}</code> field may not reflect chronological acquisition order.  
This affects both <b>raw BIDS and derivatives</b> as well as <b>derivative files converted to HBCD tabulated data</b> (<a href="https://docs.hbcdstudy.org/latest/datacuration/overview/">see file type details</a>). Despite this, data remain internally consistent — e.g., run IDs match between raw and processed datasets.
