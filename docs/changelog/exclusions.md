# Release Notes & History: Overview

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
  
## Static Element Exclusions
Static elements are precisely identified hard-coded elements. Exclusions applied to static elements in the current release are as follows:

## Dynamic Element Exclusions

In contrast to static elements (e.g. participants, instruments, and instrument fields), which are fixed and consistently structured, dynamic elements refer to data that are programmatically derived, conditionally included, or vary based on participant behavior or system context. These elements may include calculated fields, system-generated metadata, or selectively captured measures such as biospecimens, geocoded data, and direct REDCap submissions. The following filters were applied to exclude specific dynamic elements from this release, based on participant status, visit timing, data completeness, and domain-specific conditions:
