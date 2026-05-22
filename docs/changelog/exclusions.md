# Release 2.0 Exclusion Criteria & Filters

<table class="compact-table-no-vertical-lines" style="font-size: 16px;">
<thead>
<tr>
  <th colspan="2"><i>Items listed below are filtered/excluded from release data unless stated otherwise</i></th>
</tr>
</thead>
<tbody>
<tr>
  <td><b>Participants</b></td>
  <td>
  <ul>
<li>DCC participants excluded</li>
<li>Only CH Profiles included - Exclusion by PSCID prefix (PI, QI, XI, YI)</li>
<li>Only 'Active' participants included</li>
<li>Only selected 'Multiple Birth' profiles are included (based on clean-up procedures)</li>
<li>Only selected 'Postnatal Recruitment' profiles are included (based on clean-up procedures)</li>
<li>No sites excluded as of 2.0 </li>
<li>Participant exclusion if 'Brain Rating' is 'Abnormal'</li>
<li>Participant excluded due to 'Examiner' not 'REDCap' on REDCap surveys (possible modification of data between REDCap and LORIS, or data entered directly into LORIS) </li>
</ul>
  </td>
</tr>
<tr>
  <td><b>Visits</b></td>
  <td>
   <ul>
    <li>Only data from visits whose status is set to ‘LaunchPad Complete’ up to '2025-07-01' for 2.0 release and '2026-07-01' for 3.0 release (YYYY-MM-DD)</li>
    <li>Forced insertion/exclusion of participants (based on 'LaunchPad Complete' date after July 1, 2024 exceptions granted for 1.0 release only)</li>
    </ul>
  </td>
</tr>
<tr>
<td><b>Instruments</b></td>
<td>
    <ul>
    <li>ERICA — <code>mh_cg_erica_{fcm_adm_}{3_7m|7_9m}</code></li>
    <li>GABI Setup/Receipt — <code>nt_pa_gabi_{setup|rcpt}</code></li>
    <li>MRI Data &amp; Scan Summary — <code>mri_ra_chkl_{data|scan}</code></li>
    <li>NIH Baby Toolbox — <code>ncl_ch_nbtb</code></li>
    <li>Participant &amp; RA Feedback — <code>adm_cg_fb</code> / <code>adm_ra_fb</code></li>
    <li>Urgent Events &amp; Participant Alerts — <code>adm_fd_urgent</code> / <code>admin_alert</code></li>
    </ul>
</td>
</tr>

<tr>
<td><b>Variables</b></td>
<td>
    <ul>
    <li>Informant (<code>informant</code>), Validity (<code>validity</code>), Duration (<code>duration</code>), and Window Difference (<code>window_difference</code>)</li>
    <li>Open text, descriptive, and line variables</li>
    <li>Impossible or selected Extreme/Outlier values filtered out</li>
    <li>Select Item/Score-level fields (hardcoded per instrument)</li>
    </ul>
</td>
</tr>
</tbody>
</table>


<!-- 

## General Rules Applied to All Data

<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
    <td><strong>Exclusions applied to all data</strong></td>
    <td>Inactive participants/sessions excluded</td>
</tr>
<tr>
  <td><strong>Field Conversions</strong></td>
  <td>• Empty fields are replaced with 'n/a'<br>
      • Sex is set to 'Other' for participants with only one active Visit 1 (V01) visit<br>
      • 'Candidate_Age' values are replaced with 'n/a' for Visit 1 (V01)
  </td>
</tr>
</tbody>
</table>

## Exclusion Criteria & Filters
  
### Static Element Exclusions
Static elements are precisely identified hard-coded elements, including **participants**, **instruments**, **instrument fields**, etc.

### Dynamic Element Exclusions

In contrast to static elements, which are fixed and consistently structured, dynamic elements refer to data that are programmatically derived, conditionally included, or vary based on participant behavior or system context. These elements may include calculated fields, system-generated metadata, or selectively captured measures such as biospecimens, geocoded data, and direct REDCap submissions. 

Examples of dynamic filters applied to former releases include filters based on **participant status**, **visit timing**, **data completeness**, and **domain-specific conditions**. -->
