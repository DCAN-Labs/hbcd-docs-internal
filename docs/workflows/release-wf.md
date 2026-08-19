# Data Release Workflows & SOPs

This document outlines the staged workflow for selecting, releasing, and validating data for public dissemination. Key stakeholders include the HCAC Project Manager (PM), HBCD Data Coordinating Center (HDCC), Oversight Group (OG), Workgroups (WGs), and Lasso.

## Release Timeline

The release timeline for determination of variables to include in the release, study instrument documentation (or "READMEs" - [see details](../internal/readmes.md)), final QC of data as available via the [Lasso Pre-Release System](https://hbcd-hdcc-qc.lassoinformatics.com/), etc. is as follows:

#### Release 3.0 Timeline
<img src="../images/3.0-timeline.png" alt="Release timeline" width="100%" height="auto" class="center">

***Useful Links***

<ul>
  <li><a href="https://docs.google.com/spreadsheets/d/171oj0PLLtVgp5OSReBD5J6Ir4U56QQrWEwu92ZwttrM/edit?gid=0#gid=0">Measure Inclusion Form</a> tracking the list of variables to be included in upcoming release</li>
  <li><a href="https://docs.google.com/spreadsheets/d/1YkBeu8PpY2hTDq4_2X2SmI6vYaD6ib9mA-s3h4jALq0/edit?usp=sharing">Release Timeline Sign-Off Form</a></li>
</ul> 

### Process for Determination of Release Timeline

The release timeline is determined as follows:

1. HDCC proposes a timeline 
2. HCAC leadership approves proposed timeline
3. Program approves proposed timeline
4. Feedback is acquired from Workgroups

## Stages of the Release Workflow

### Stage 1: Determine Variables to Include & Data Filters for Release

#### Variable Inclusion Sign-Off

The HCAC PM (Stephanie Averill) collaborates with the HDCC WG Liaison (Jen Zink)  to generate a comprehensive list of potential variables for the upcoming data release.

 - The full list is circulated to all Workgroups and subject matter experts (SMEs), who mark each variable as INCLUDE or NOT INCLUDED in the  [Variable Inclusion Form](https://docs.google.com/spreadsheets/d/171oj0PLLtVgp5OSReBD5J6Ir4U56QQrWEwu92ZwttrM/edit?usp=sharing).
 - From this list, a [Variable Inclusion Sign-Off Form](https://docs.google.com/spreadsheets/d/1ABh8u6s4R3jUKUcfj2xA_nRyO1r1kQRVfwDDJRWwVq0/edit?usp=sharing) is generated for HDCC/HCAC Leadership to review the proposed measures to be included/excluded from public release.
 - Proposed public release measures are then brought to the Steering Committee for final sign-off. 

**Release measure inclusion sign off [RACI](#responsibility-assignment-matrices):**

<img src="../images/release-stage1-raci.png" alt="lasso" width="60%" height="auto">

#### Data Filters Sign-Off

In addition to deciding which variables to include in the release, the HDCC, HCAC, and Workgroups collaborate to determine general administrative inclusion/exclusion filters (*as opposed to specific variable filters, which are tracked elsewhere*) to be applied to the data release. This includes, but is not limited to:

 - Site exclusions (e.g., Florida)
 - Cell size per site
 - Cohort (e.g., post-natal recruitment)
 - Outlier or "impossible value" removal (yes/no) 
 - etc.

Data filters applied to Release 1.0 are described in detail on the R1.0 Release Notes under [Exclusion Criteria & Filters](https://docs.hbcdstudy.org/latest/changelog/versions/R1/#exclusion-criteria-filters).
 
**Status Tracker:** View the latest status of filter sign-offs in the [Data Filters Sign Off Form](https://docs.google.com/spreadsheets/d/1M_QuEVgUoVAOdzXlY8FMTZvgLRtGUx2ykevUo8iUnr8/edit?usp=sharing).

### Stage 2: Integrate Planned Measures in Beta Releases

The HDCC implements the measures marked as INCLUDE and begins the first versioned Beta Release (BR) approximately 1–2 months after the data freeze. *Note: An updated SOP is under development to address scenarios where a measure is marked as “INCLUDE,” but cannot be implemented during the current release.*

#### Beta Release (BR) Sprint Cycle 

1. Known issues and new features are prioritized for the sprint.
2. Versioned BRs are released on the 4th Friday of every month.
3. Each BR is accompanied by a BR Hot Sheet completed by HDCC to guide Lasso ingestion - see [Hot Sheet template](https://docs.google.com/document/d/1qwfD_lccV89u205KPdq_5dZCx_w4pu8BFWI31wLDH8Q/edit?usp=sharing).

<p style="margin-bottom: 2px; font-weight: bold;"><i>BR Hot Sheet - Key Areas</i></p>
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
<tbody>
<tr>
  <td><i class="fa fa-check" style="margin-right: 6px; color: blue;"></i><b>Date/Time Confirmation </b></td>
  <td>Specifies when BRX is ready and identifies the single point of contact.</td>
</tr>
<tr>
  <td><i class="fa fa-check" style="margin-right: 6px; color: blue;"></i><b>Compliance Checklist</b></td>
  <td>Highlights potential issues that could make the data non-compliant (e.g., missing participants in `participant.tsv`) or disrupt loading or downloading.</td>
</tr>
<tr>
  <td><i class="fa fa-check" style="margin-right: 6px; color: blue;"></i><b>Sign-Off and Documentation</b></td>
  <td>Responsible parties provide a clear/thoughtful review and sign off on the release contents. This includes confirmation that the BR Release Notes are documented under Change Logs in the internal Docs site.</td>
</tr>
</tbody>
</table>

#### Lasso Ingestion

Once the BR Hot Sheet is finalized, the HDCC sends it to Lasso to initiate BR ingestion, which includes [Lasso ingestion QA](qc.md#pre-release-pheno). After ingestion is complete, the HDCC liaison (Jen Zink) notifies WGs that data are available in Lasso and requests they complete Quality Control (QC) reviews. Lasso obtains final sign-off from Workgroups on datasets in their release-ready form, with <a href="https://docs.hbcdstudy.org/latest/changelog/versions/R1/#exclusion-criteria-filters">applied filters</a>, via the <a href="https://hbcd-hdcc-qc.lassoinformatics.com/">Lasso Pre-Release System</a>.
  
### Stage 3: Data Quality Issue Identification, Reporting, and Handling  

There are 2 bins of issues with separate pipelines for reporting/handling:

##### Bin 1: Internal Findings

- Identified during [Lasso ingestion QA](qc.md#pre-release-pheno)
- Tracked by HDCC on the internal Monday board for resolution

##### Bin 2: Workgroup Findings

Issues identified by WGs, analysts, or via LORIS, reported in collaboration with the HDCC liaison (Jen Zink). These issues are logged in a structured format for BR sprint planning and resolution by HDCC. Once Bin 2 issues are added to an upcoming BR sprint and the corrections appear in a versioned BR in Lasso, Jen communicates to original reporter that the known issue is addressed and verifies the correction is implemented as expected in the Lasso system.

###### WG Template for Reporting Issues

<table class="table-no-vertical-lines">
  <tbody>
    <tr>
      <td><strong>Issue Category</strong></td>
      <td><em>Data Error, Data Improvement, Data Dictionary Request</em></td>
    </tr>
    <tr>
      <td><strong>Data Element/Instrument Affected</strong></td>
      <td><em>Element/instrument name</em></td>
    </tr>
    <tr>
      <td><strong>Description</strong></td>
      <td><em>Explanation of issue</em></td>
    </tr>
    <tr>
      <td><strong>Proposed Fix</strong></td>
      <td><em>Description of fix</em></td>
    </tr>
    <tr>
      <td><strong>Reporter</strong></td>
      <td><em>SME/analyst name and contact info</em></td>
    </tr>
  </tbody>
</table>

### Stage 4: Data Sign-off and Public Release

When the the second-to-last BR prior to Public Release is loaded in Lasso, the HDCC liaison (Jen Zink) schedules one-on-one sign-off meetings with all WG chairs/SMEs who have measures in the planned release for final QC/review in Lasso. Prior to these meetings, WG chairs/SMEs have pre-QC’ed their data in the latest BR. During these meetings, Jen reviews:

1. Past QC items that have been identified and corrected in previous BRs
2. Any further QC action-items to be addressed prior to public release (if applicable) based on WG/SME review of the latest BR and items identified by Jen 

During the one-on-one sign-off meetings, if no further action-items are found by either the WG/SMEs or Jen, the WGs/SMEs sign off on their measures via this [sign-off sheet template](https://docs.google.com/spreadsheets/d/1zPfNGb7ejFlVelfGWNJZSlaslsv3yHQjjiZJgt0BiyU/edit?gid=615569410#gid=615569410). 

If further QC action-items are found in the second-to-last BR during the one-on-one sign-off meetings, the WG/SMEs do NOT sign off on their measures.  Jen communicates the data issues back to the HDCC via the centralized Monday Board, so the remaining items can be prioritized for the final BR prior to public release. 

When the final BR prior to public release is loaded into Lasso, Jen schedules one-on-one sign-off meetings with the remaining WGs/SMEs who were awaiting corrections to their data prior to sign off. During these meetings, Jen reviews the list of items that were identified in the last round of QC with the WGs/SMEs to ensure the correction is implemented as expected in the Lasso; the WGs/SMEs then sign off on their measures via the same google form above. 

In the event that data issues remain, or new issues are identified in QC of the final BR during the one-on-one sign-off meetings, Jen collaborates with the WGs/SMEs and Luci Moore to document these as ‘Known Issues’ for the Data Release Documentation site. Jen reports the known issues on the HDCC centralized Monday Board so they can be prioritized for the Patch Release.

## Patch Releases

<!-- ***See the procedures for patch release BR15.1, including timelines and responsible parties, [here](https://docs.google.com/document/d/1rVvzBA7eu_ZuTpD9Mbp_Hg8sTzAYT9R6cp3AGtHNhYg/edit?tab=t.0).*** -->

Patch releases occur only to address “Known Issues” in the current public data release; they are not intended for releasing additional sessions/visits, protocol elements, or participants. Known issues are either identified via the HDCC, WGs/SMEs, or the scientific community (users of the public release data via the Lasso ticketing system). Once they are identified and reported to HDCC, they are then placed on the centralized Monday Board for prioritization. 

When known issues are addressed, HDCC sends samples of the corrected data to the respective WGs/SMEs for their confirmation. Once the data fixes are confirmed by SMEs, the corrected data elements are then ingested into the Lasso QC environment (where the BRs are QCed). Jen further QC’s the data in the Lasso environment to ensure all fixes are implemented appropriately and schedules one-on-one sign-off meetings with each WG with a measure in the patch release. 

During these sign off meetings, the following is covered:

1. The WG confirmation the data issues are addressed (in Lasso)  
2. Jen confirmation the data issues are addressed (in Lasso)  
3. WG sign-off (via google form) 

## Approved Updates to Future Releases

See the approved updates to release 2.0 in the Release Notes on the HBCD Data Release Docs site: [Release 2.0 (Release Date TBA)](https://docs.hbcdstudy.org/latest/changelog/pending/#release-20-release-date-tba).

## Responsibility Assignment Matrices

Below we outline the individuals responsible for various stages of the release across data modalities via RACI matrices, which outline the following:

**Note that items outlined below pertain specifically to the data release stage. Responsibility matrices for general processing and quality control stages can be found on under Data Processing Workflows.**

<div id="tab-raci" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-table" style="margin-right: 6px; color: blue;"></i>Tabulated Data</span>
  <a class="anchor-link" href="#tab-raci" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
<thead>
  <tr>
    <th>Study Stage</th>
    <th>Step</th>
    <th>Location</th>
    <th>Responsible</th>
    <th>Accountable</th>
    <th>Consulted/<br>Informed</th>
  </tr>
</thead>
<tbody>
<tr>
  <td>Pre-Release Prep</td>
  <td>Generate Release Candidate IDs for Public Release</td>
  <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#health-sciences-technology">UMN HST</a></span></td>
  <td>Reed McEwan</td>
  <td>Reed McEwan</td>
  <td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td>Data QC</td>
<td>Review of Dashboards and Completeness</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#loris">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#lasso">Lasso</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#ripple">Ripple</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts">HCAC</a></span></td>
<td>Santiago Torres (LORIS), Jen Zink (Lasso), Sauren Ravencroft (Ripple), Stephanie Averill (HCAC)</td>
<td>WG Leads</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td>Pre-Release</td>
<td>Sign Off on Release Candidate</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#lasso">Lasso</a></span></td>
<td>Jen Zink, WG Leads</td>
<td>Damien Fair</td>
<td style="text-align: center;">-/-</td>
</tr>
</tbody>
</table>
</div>

<div id="img-raci" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-table" style="margin-right: 6px; color: blue;"></i> Imaging Data</span>
  <a class="anchor-link" href="#img-raci" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
<thead>
  <tr>
    <th>Study Stage</th>
    <th>Step</th>
    <th>Location</th>
    <th>Responsible</th>
    <th>Accountable</th>
    <th>Consulted/<br>Informed</th>
  </tr>
</thead>
<tbody>
<tr>
  <td>Pre-Release Prep</td>
  <td>Determine Release Candidate and Process with Sign Off</td>
  <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#washu">WashU</a></span></td>
  <td>MRI WGs, Eric Feczko, Jen Zink</td>
  <td>Chris Smyser</td>
  <td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td>Data Process</td>
<td>De-identification of BIDS data</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi">UMN MSI</a></span></td>
<td>Sriharshitha Anuganti</td>
<td>Sriharshitha Anuganti	</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td>Data Process</td>
<td>Run <a href="https://docs.hbcdstudy.org/latest/instruments/processing/#overview">processing pipelines</a></td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi">UMN MSI</a></span></td>
<td>CBRAIN</td>
<td>Tanya Pandhi</td>
<td>[<b>C</b>] SMEs</td>
</tr>
<tr>
<td>Data Process</td>
<td>Transfer derivatives to LORIS, re-inserting DCCIDs</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi">UMN MSI</a></span></td>
<td>Harshitha Anuganti, Tanya Pandhi, Jesse Erdmann</td>
<td>Harshitha Anuganti</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td>Data Process</td>
<td>Ingest derivatives into LORIS and create tabulated imaging files</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi">UMN MSI</a></span></td>
<td>Cecile Madjar, Santiago Torres, Samir Das</td>
<td>Cecile Madjar</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td>Data QC + Action</td>
<td>Post-processing QC (Manual & Automated)</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#center-for-developmental-neuroimaging">CDNI (UMN)</a></span></td>
<td>Michael Anderson</td>
<td>Eric Feczko</td>
<td>[<b>C</b>] Lucille Moore<br>[<b>I</b>] Damien Fair</td>
</tr>
<tr>
<td>Data Process</td>
<td>Move source BIDS to platform</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi">UMN MSI</a></span></td>
<td>Tanya Pandhi, Data Loading Team (Lasso)</td>
<td>Tanya Pandhi</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td>Data Process</td>
<td>Move BIDS phenotype files to platform</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi">UMN MSI</a></span></td>
<td>Harshitha Anuganti, Tanya Pandhi, Jesse Erdmann, Data Loading Team (Lasso)</td>
<td>Harshitha Anuganti</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td>Data Process</td>
<td>Move raw BIDS and derivatives to platform</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi">UMN MSI</a></span></td>
<td>Tanya Pandhi</td>
<td>Tanya Pandhi</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td>Data QC + Action</td>
<td>SMEs review data</td>
<td>Various</td>
<td>MRI SMEs, Jen Zink</td>
<td>Eric Feczko</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
    <td>Data QC + Action</td>
    <td>Data corrections</td>
    <td>Various</td>
    <td>Erik Feczko, Jen Zink, Tanya Pandhi</td>
    <td>Tanya Pandhi</td>
    <td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
    <td>Documentation of Processes</td>
    <td>Documentation of processes, known issues, etc.</td>
    <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi">UMN MSI</a></span><br><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#center-for-developmental-neuroimaging">CDNI</a></span></td>
    <td>MRI SMEs, HDCC</td>
    <td>Lucille Moore</td>
    <td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
    <td>Sign Off</td>
    <td>SMEs sign off on data</td>
    <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#lasso">Lasso</a></span></td>
    <td>Jen Zink, Eric Feczko</td>
    <td>Jen Zink</td>
    <td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
</tbody>
</table>
</div>

<div id="eeg-raci" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-table" style="margin-right: 3px; color: blue;"></i> EEG</span>
  <a class="anchor-link" href="#eeg-raci" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table-no-vertical-lines">
<thead>
  <tr>
    <th>Study Stage</th>
    <th>Step</th>
    <th>Location</th>
    <th>Responsible</th>
    <th>Accountable</th>
    <th>Consulted/<br>Informed</th>
  </tr>
</thead>
<tbody>
<tr>
  <td>Pre-Release Prep: Determine Release Candidate and Process with Sign Off</td>
  <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#university-of-maryland">UMD EEG Core</a></span></td>
  <td>Santiago Morales, EEG WG</td>
  <td>Nathan Fox</td>
  <td>[<b>I</b>] Program</td>
</tr>
<tr>
<td>QC Pre-release data</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 3px; color: blue;"></i><a href="../../orgcharts/#university-of-maryland">UMD EEG Core</a></span></td>
<td>Santiago Morales</td>
<td>Nathan Fox</td>
<td>[<b>I</b>] Program</td>
</tr>
</tbody>
</table>
</div>

## Release Management & Utilities

### Data Management & Release Meetings

There are several regular calls where release action items are discussed and tracked:

<table class="compact-table-no-vertical-lines" style="margin: 0 auto;">
<thead>
  <th>Meeting (<i>agenda/notes linked</i>)</th>
  <th>Meeting Facilitator</th>
  <th>Stakeholders</th>
</thead>
<tbody>
<tr>
  <td><a href="https://docs.google.com/document/d/1CQNtqezeXOiTg_13XIFn0v7u4aymY40JyKAXI4QU4Hk/edit?pli=1&tab=t.0">HDCC Data Release WG</a><br><i>Mondays 11 AM CT</i></td>
  <td>Maren Macgregor-Hannah</td>
  <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#university-of-minnesota">UMN</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#loris">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#lasso">Lasso</a></td>
</tr>
<tr>
  <td>HBCD Workgroup calls<br>(action items track on<a href="https://ucsd-actri.monday.com/boards/6045591843">Monday.com</a>)<br><i>Time/day varies</i></td>
  <td>First 10 min of WG calls are dedicated to discussing QC and data releases, facilitated by Jen Zink</td>
  <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#hbcd-workgroups">HBCD Workgroups</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#lasso">Lasso</a></span></td>
</tr>
<tr>
  <td>MRI QC<br><i>Wednesdays 4 PM CT (biweekly)</i></td>
  <td>Don Hagler</td>
  <td>
    <span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px;
      font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#loris">LORIS</a></span>
    <span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px;
      font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#j-craig-venter-institute">JCVI</a></span>
    <span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px;
      font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#health-sciences-technology">HST</a></span>
    <span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px;
      font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#midb-informatics-hub-msi">MIDB</a></span>
  </td>
</tr>
<tr>
  <td>ABCD-HBCD Release<br><i>Tuesdays 10 AM CT</i></td>
  <td>Deanna Barch</td>
  <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#j-craig-venter-institute">ABCD team (JCVI)</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#university-of-minnesota">UMN</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#loris">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#lasso">Lasso</a></span></td>
</tr>
<tr>
  <td>ABCD-HBCD Sync<br><i>Thursday 2 PM CT (Biweekly)</i></td>
  <td>Janosch Linkersdoerfer</td>
  <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#j-craig-venter-institute">ABCD team (JCVI)</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#university-of-minnesota">UMN</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#loris">LORIS</a></span></td>
</tr>
<tr>
  <td><a href="https://docs.google.com/document/d/1kFCWVpvdSXFVzBajmfffIVk-LhGtFF8KP0Ifv4mJwQg/edit?tab=t.0">HDCC Architecture & Implementation</a><br><i>Tuesdays 3:30 PM CT</i></td>
  <td>Maren Macgregor-Hannah</td>
  <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#university-of-minnesota">UMN</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#loris">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#lasso">Lasso</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#washu">WashU</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#j-craig-venter-institute">JCVI</a></span></td>
</tr>
<tr>
  <td><a href="https://docs.google.com/document/d/1e9sutOlHjfevRgCBVjyl-hy-PxnS5Ee8IVDn8TPyirY/edit?tab=t.0">HBCD LORIS Implementation</a><br><i>Wednesdays 1:30 PM CT</i></td>
  <td>Maren Macgregor-Hannah</td>
  <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#university-of-minnesota">UMN</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#loris">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#lasso">Lasso</a></span></td>
</tr>
<tr>
  <td><a href="https://docs.google.com/document/d/1_GMbyzbhkEeS1mFHdClFOWjo6V_XC7QHtzTiIT6GUfw/edit?tab=t.0">HDCC IT Workgroup Call</a> (EEG, Biospecimens, and other WGs)<br><i>Fridays 3 PM CT</i></td>
  <td>Maren Macgregor-Hannah</td>
  <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#lasso">Lasso</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#loris">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#j-craig-venter-institute">JCVI</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#university-of-maryland">UMD</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#libr">LIBR</a></span></td>
</tr>
<tr>
  <td><a href="https://docs.google.com/document/d/1jGtWPspUv5fJGooBrCUSBMgt91BW40YIMzaa3zO1BQ0/edit?tab=t.0">HDCC/HCAC Biweekly Calls</a><br><i>Friday 2 PM CT (biweekly)</i></td>
  <td>Site monitors</td>
  <td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;">HCAC</span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#university-of-minnesota">UMN</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#washu">WashU</a></span></td>
</tr>
<tr>
  <td>EMR<br><i>Mondays 4 PM CT (biweekly)</i></td>
  <td>Nicole Venteris</td>
  <td>
    <span style="display: inline-block; background-color: #f0f8ff; color: #333;
      border-radius: 12px; padding: 1px 5px; font-size: 1em;
      border: 1px solid #d0e7ff;"><a href="../../orgcharts/#health-sciences-technology">HST</a></span>
    <span style="display: inline-block; background-color: #f0f8ff; color: #333;
      border-radius: 12px; padding: 1px 5px; font-size: 1em;
      border: 1px solid #d0e7ff;"><a href="../../orgcharts/#hbcd-workgroups">HBCD Workgroup</a></span>
    <span style="display: inline-block; background-color: #f0f8ff; color: #333;
      border-radius: 12px; padding: 1px 5px; font-size: 1em;
      border: 1px solid #d0e7ff;"><a href="../../orgcharts/#libr">LIBR</a></span>
  </td>
</tr>
<tr>
  <td>NIH-BTB<br><i>Wednesday 11 AM CT (monthly)</i></td>
  <td>Maren Macgregor-Hannah</td>
  <td>
    <span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px;
      font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#loris">LORIS</a></span>
    <span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px;
      font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#health-sciences-technology">HST</a></span>
    <span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px;
      font-size: 1em; border: 1px solid #d0e7ff;"><a href="../../orgcharts/#hbcd-workgroups">HBCD Workgroup</a></span>
    <span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px;
      font-size: 1em; border: 1px solid #d0e7ff;">App Devs</span>
  </td>
</tr>
</tbody>
</table>

### Project Management Utilities

<table class="table-no-vertical-lines" style="margin: 0 auto;">
<thead>
  <th>Platform</th>
  <th>Use Case(s)</th>
</thead>
<tbody>
<tr>
  <td><a href="https://ucsd-actri.monday.com/boards/6045591843">Monday.com board</a></td>
  <td>Tracking release actions items</td>
</tr>
<tr>
  <td><a href="https://hbcdstudy.atlassian.net/wiki/x/kYB4">Confluence</a></td>
  <td>Storage of all internal documentation and protocols</td>
</tr>
<tr>
  <td><a href="../../orgcharts/#airtable">AirTable</a></td>
  <td>Document current protocol, change requests (REDCap or Responsible Conduct request modifications), IRB approvals, initial list of included measures in data releases, QC pages, SC approval, etc. Also used to keep track of staff member item-level access to different working platforms and related required paperworks.</td>
</tr>
<tr>
  <td>Slack</td>
  <td>Team and topic-specific communication/coordination</td>
</tr>
<tr>
  <td><a href="https://hbcd-docs-internal.readthedocs.io/">HBCD DCC Internal Docs</a> (<i>this site</i>)</td>
  <td>Organized, curated, and centralized internal documentation</td>
</tr>
<tr>
  <td>Google Docs</td>
  <td>Meeting agendas/notes; holds historical documentation of workflows, context of decision-making, etc.</td>
</tr>
</tbody>
</table>


<br>