<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

# Data Release Workflows & SOPs

This document outlines the staged workflow for selecting, releasing, and validating data for public dissemination. Key stakeholders include the HCAC Project Manager (PM), HBCD Data Coordinating Center (HDCC), Oversight Group (OG), Workgroups (WGs), and Lasso.

## Release Timeline

<div class="pill-center">
  </a>
    <a href="../../#clear-objectives-and-scope" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip"><i class="fa-solid fa-bullseye" style="color: #6300d3;"></i><span class="tooltiptext">Clear objectives & scope<br><i>Click to learn more</i></span></span>
    </span>
  </a>
  <a href="../../#timeliness-planning" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip">
        <i class="fa-solid fa-clock" style="color: #6300d3;"></i>
        <span class="tooltiptext">Timeliness planning<br><i>Click to learn more</i></span>
      </span>
    </span>
</div>
<br>

<div class="notification-banner static-banner">
  <span class="emoji"><i class="fa-regular fa-lightbulb"></i></span>
  <span class="text">
    See timeline in PDF format to access embedded links - <a href="../images/timeline.pdf" target="_blank" rel="noopener noreferrer">CLICK HERE</a>
  </span>
</div>

<object type="image/svg+xml" data="../images/timeline.svg" width="100%"></object>

## Stages of the Release Workflow

### Stage 1: Determine Measures to Include in Release

<div class="pill-center">
  <a href="../../#clear-objectives-and-scope" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip"><i class="fa-solid fa-bullseye" style="color: #6300d3;"></i><span class="tooltiptext">Clear objectives & scope<br><i>Click to learn more</i></span></span>
    </span>
  </a>
  <a href="../#project-management" target="_blank" class="pill-link-wrapper">
      <span class="pill-link">
        <span class="tooltip">
          <i class="fa-solid fa-diagram-project" style="color: #6300d3;"></i>
          <span class="tooltiptext">Project Management<br><i>Click to learn more</i></span>
        </span>
      </span>
  </a>
  <a href="../../#timeliness-planning" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip">
        <i class="fa-solid fa-clock" style="color: #6300d3;"></i>
        <span class="tooltiptext">Timeliness planning<br><i>Click to learn more</i></span>
      </span>
    </span>
  </a>
</div>

The HCAC PM (Stephanie Averill) collaborates with the HDCC to generate a comprehensive list of potential measures for the upcoming data release.

 - Leadership, the Oversight Group (OG), and Workgroups review and approve the proposed measures.
 - The full list is circulated to all Workgroups and subject matter experts (SMEs), who mark each variable as INCLUDE or NOT INCLUDED in the following form: [Measure Inclusion Form (Google Sheet)](https://docs.google.com/spreadsheets/d/171oj0PLLtVgp5OSReBD5J6Ir4U56QQrWEwu92ZwttrM/edit?usp=sharing)

### Stage 2: Integrate Planned Measures in Beta Releases

<div class="pill-center">
  <a href="../../#clear-objectives-and-scope" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip"><i class="fa-solid fa-bullseye" style="color: #6300d3;"></i><span class="tooltiptext">Clear objectives & scope<br><i>Click to learn more</i></span></span>
    </span>
  </a>
  <a href="../../#data-quality-checks" target="_blank" class="pill-link-wrapper">
      <span class="pill-link">
        <span class="tooltip">
          <i class="fa-solid fa-clipboard-check" style="color: #6300d3;"></i>
          <span class="tooltiptext">Data quality checks<br><i>Click to learn more</i></span>
        </span>
      </span>
  </a>
  <a href="../#project-management" target="_blank" class="pill-link-wrapper">
      <span class="pill-link">
        <span class="tooltip">
          <i class="fa-solid fa-diagram-project" style="color: #6300d3;"></i>
          <span class="tooltiptext">Project Management<br><i>Click to learn more</i></span>
        </span>
      </span>
  </a>
  </a>
  <a href="../../#timeliness-planning" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip">
        <i class="fa-solid fa-clock" style="color: #6300d3;"></i>
        <span class="tooltiptext">Timeliness planning<br><i>Click to learn more</i></span>
      </span>
    </span>
  </a>
</div>

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
  <td style="word-wrap: break-word; white-space: normal;">Specifies when BRX is ready and identifies the single point of contact.</td>
</tr>
<tr>
  <td><i class="fa fa-check" style="margin-right: 6px; color: blue;"></i><b>Compliance Checklist</b></td>
  <td style="word-wrap: break-word; white-space: normal;">Highlights potential issues that could make the data non-compliant (e.g., missing participants in `participant.tsv`) or disrupt loading or downloading.</td>
</tr>
<tr>
  <td><i class="fa fa-check" style="margin-right: 6px; color: blue;"></i><b>Sign-Off and Documentation</b></td>
  <td style="word-wrap: break-word; white-space: normal;">Responsible parties provide a clear/thoughtful review and sign off on the release contents. This includes confirmation that the BR Release Notes are documented under Change Logs in the internal Docs site.</td>
</tr>
</tbody>
</table>

#### Lasso Ingestion

Once the BR Hot Sheet is finalized, the HDCC sends it to Lasso to initiate BR ingestion, which includes [Lasso ingestion QA](qc.md#pre-release-pheno). After ingestion is complete, the HDCC liaison (Jen Zink) notifies WGs that data are available in Lasso and requests they complete Quality Control (QC) reviews.
  
### Stage 3: Data Quality Issue Identification, Reporting, and Handling  

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

<div class="pill-center">
  <a href="../../#clear-objectives-and-scope" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip"><i class="fa-solid fa-bullseye" style="color: #6300d3;"></i><span class="tooltiptext">Clear objectives & scope<br><i>Click to learn more</i></span></span>
    </span>
  </a>
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

When the the second-to-last BR prior to Public Release is loaded in Lasso, the HDCC liaison (Jen Zink) schedules one-on-one sign-off meetings with all WG chairs/SMEs who have measures in the planned release for final QC/review in Lasso. Prior to these meetings, WG chairs/SMEs have pre-QC’ed their data in the latest BR. During these meetings, Jen reviews:

1. Past QC items that have been identified and corrected in previous BRs
2. Any further QC action-items to be addressed prior to public release (if applicable) based on WG/SME review of the latest BR and items identified by Jen 

During the one-on-one sign-off meetings, if no further action-items are found by either the WG/SMEs or Jen, the WGs/SMEs sign off on their measures via this [sign-off sheet template](https://docs.google.com/spreadsheets/d/1zPfNGb7ejFlVelfGWNJZSlaslsv3yHQjjiZJgt0BiyU/edit?gid=615569410#gid=615569410). 

If further QC action-items are found in the second-to-last BR during the one-on-one sign-off meetings, the WG/SMEs do NOT sign off on their measures.  Jen communicates the data issues back to the HDCC via the centralized Monday Board, so the remaining items can be prioritized for the final BR prior to public release. 

When the final BR prior to public release is loaded into Lasso, Jen schedules one-on-one sign-off meetings with the remaining WGs/SMEs who were awaiting corrections to their data prior to sign off. During these meetings, Jen reviews the list of items that were identified in the last round of QC with the WGs/SMEs to ensure the correction is implemented as expected in the Lasso; the WGs/SMEs then sign off on their measures via the same google form above. 

In the event that data issues remain, or new issues are identified in QC of the final BR during the one-on-one sign-off meetings, Jen collaborates with the WGs/SMEs and Luci Moore to document these as ‘Known Issues’ for the Data Release Documentation site. Jen reports the known issues on the HDCC centralized Monday Board so they can be prioritized for the Patch Release.

## Patch Releases

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

<table class="compact-table-no-vertical-lines" style="margin: 0 auto;">
<thead>
  <tr>
    <th></th>
    <th>Meaning</th>
    <th>Definition</th>
  </tr>
</thead>
<tbody>
<tr>
<td><b>R</b></td><td>Responsible</td><td style="word-wrap: break-word; white-space: normal;">Individual doing a piece of the work to complete this task.</td>
</tr>
<tr><td><b>A</b></td><td>Accountable</td><td style="word-wrap: break-word; white-space: normal;">1 person only who is ultimately answerable for the correct and thorough completion of the deliverable or task.</td>
</tr>
<tr>
<td><b>C</b></td><td>Consulted</td><td style="word-wrap: break-word; white-space: normal;">People who provide input or advice before the work is done.</td>
</tr>
<tr><td><b>I</b></td><td>Informed</td><td style="word-wrap: break-word; white-space: normal;">People who need to be kept updated on progress or decisions, but do not need to be consulted or perform tasks.</td>
</tr>
</tbody>
</table>


<div id="tab-raci" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-table" style="margin-right: 6px; color: blue;"></i> Tabulated Data</span>
  <a class="anchor-link" href="#tab-raci" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table">
<thead>
  <tr>
    <th style="width: 15%; text-align: center">Study Stage</th>
    <th style="width: 20%; text-align: center">Step</th>
    <th style="width: 25%; text-align: center">Location</th>
    <th style="width: 20%; text-align: center"><span class="tooltip tooltip-left"><b>R</b><span class="tooltiptext">Responsible</span></span></th>
    <th style="width: 20%; text-align: center"><span class="tooltip tooltip-left"><b>A</b><span class="tooltiptext">Accountable</span></span></th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>C</b><span class="tooltiptext">Consulted</span></span>/<span class="tooltip tooltip-left"><b>I</b><span class="tooltiptext">Informed</span></span></th>
  </tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Set Up</td>
<td style="word-wrap: break-word; white-space: normal;">Testing and Validation of questions &amp; scoring</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#loris" target="_blank">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#lasso" target="_blank">Lasso</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Santiago Torres<br>Jen Zink</td>
<td style="word-wrap: break-word; white-space: normal;">WG Leads</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC</td>
<td style="word-wrap: break-word; white-space: normal;">Review of Dashboards and Completeness</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#loris" target="_blank">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#lasso" target="_blank">Lasso</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#ripple" target="_blank">Ripple</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts" target="_blank">HCAC</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Santiago Torres (LORIS)<br>Jen Zink (Lasso)<br>Sauren Ravencroft (Ripple)<br>Stephanie Averill (HCAC)</td>
<td style="word-wrap: break-word; white-space: normal;">WG Leads</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Conversion</td>
<td style="word-wrap: break-word; white-space: normal;">Add missingness and shadow matrix</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#loris" target="_blank">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#lasso" target="_blank">Lasso</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#ripple" target="_blank">Ripple</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts" target="_blank">HCAC</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Santiago Torres (LORIS)<br>Jen Zink (Lasso)<br>Sauren Ravencroft (Ripple)<br>Stephanie Averill (HCAC)</td>
<td style="word-wrap: break-word; white-space: normal;">Santiago Torres</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Conversion</td>
<td style="word-wrap: break-word; white-space: normal;">Re-ID</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Sriharshitha Anuganti</td>
<td style="word-wrap: break-word; white-space: normal;">Sriharshitha Anuganti</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Readiness for transfer</td>
<td style="word-wrap: break-word; white-space: normal;">Hot Sheet Population</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Erik Lee<br>Tim Hendrickson<br>Santiago Torres<br>Lucille Moore</td>
<td style="word-wrap: break-word; white-space: normal;">Maren Macgregor-Hannah</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Ingestion/Transfer</td>
<td style="word-wrap: break-word; white-space: normal;">Transfer release data to bucket for Lasso to pick up</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#lasso" target="_blank">Lasso</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Sriharshitha Anuganti</td>
<td style="word-wrap: break-word; white-space: normal;">Sriharshitha Anuganti</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Ingestion</td>
<td style="word-wrap: break-word; white-space: normal;">Ingestion to Lasso</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#lasso" target="_blank">Lasso</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Lasso Data Loading Team<br>Jen Zink<br>Leigh MacIntyre</td>
<td style="word-wrap: break-word; white-space: normal;">Laetitia Fesselier</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC</td>
<td style="word-wrap: break-word; white-space: normal;">Review of data and corresponding shadow matrix</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#loris" target="_blank">LORIS</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#lasso" target="_blank">Lasso</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#ripple" target="_blank">Ripple</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts" target="_blank">HCAC</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Santiago (LORIS)<br>Jen Zink (Lasso)<br>Sauren Ravencroft (Ripple)<br>Stephanie Averill (HCAC)</td>
<td style="word-wrap: break-word; white-space: normal;">WG Leads</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Pre-Release</td>
<td style="word-wrap: break-word; white-space: normal;">Sign Off on Release Candidate</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#lasso" target="_blank">Lasso</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Jen Zink<br>WG Leads</td>
<td style="word-wrap: break-word; white-space: normal;">Damien Fair</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
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
<table class="compact-table">
<thead>
  <tr>
    <th style="width: 15%; text-align: center">Study Stage</th>
    <th style="width: 25%; text-align: center">Step</th>
    <th style="width: 20%; text-align: center">Location</th>
    <th style="width: 15%; text-align: center"><span class="tooltip tooltip-left"><b>R</b><span class="tooltiptext">Responsible</span></span></th>
    <th style="width: 15%; text-align: center"><span class="tooltip tooltip-left"><b>A</b><span class="tooltiptext">Accountable</span></span></th>
    <th style="width: 15%; text-align: center"><span class="tooltip tooltip-left"><b>C</b><span class="tooltiptext">Consulted</span></span>/<span class="tooltip tooltip-left"><b>I</b><span class="tooltiptext">Informed</span></span></th>
  </tr>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Pre-Release Prep</td>
<td style="word-wrap: break-word; white-space: normal;">Determine Release Candidate and Process with Sign Off</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#washu" target="_blank">WashU</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Chris Smyser</td>
<td style="word-wrap: break-word; white-space: normal;">Chris Smyser</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Collection</td>
<td style="word-wrap: break-word; white-space: normal;">Participant Source Data Acquisition: DCMs, eCRF population (MRI Acquisition Form)</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#fiona" target="_blank">FIONA</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#loris" target="_blank">LORIS</a></span></td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff<br>(Varies by site)</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">QC at Source Data Acquisition: eCRF populated properly, DCM header checks, naming convention checks</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#fiona" target="_blank">FIONA</a></span></td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff<br>(Varies by site)</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">QC at Source: Check acquisition/protocol adherence</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#j-craig-venter-institute" target="_blank">JCVI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Josh Kuperman</td>
<td style="word-wrap: break-word; white-space: normal;">Anders Dale</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">Transfer acquisition/protocol adherence (both DCM acquisition and MRI Acquisition Form) to DCC</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#j-craig-venter-institute" target="_blank">JCVI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Process</td>
<td style="word-wrap: break-word; white-space: normal;">Scan De-Identification send confirmation to DCC</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">Validate metadata, de-id, and scan completeness: send confirmation to DCC</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#fiona" target="_blank">FIONA</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">MRI QC Workgroup</td>
<td style="word-wrap: break-word; white-space: normal;">Don Hagler</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Collection</td>
<td style="word-wrap: break-word; white-space: normal;">Convert DICOMs to BIDS/NIfTI</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Cecile Madjar</td>
<td style="word-wrap: break-word; white-space: normal;">Cecile Madjar</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">QC of the DCM ot BIDs Conversion: Correct BIDS errors</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Cecile Madjar</td>
<td style="word-wrap: break-word; white-space: normal;">Cecile Madjar</td>
<td style="word-wrap: break-word; white-space: normal;">[<b>C</b>] Lucille Moore<br>[<b>C</b>] Timothy Hendrickson</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">Check for protocol deviations (based on BIDS)</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#j-craig-venter-institute" target="_blank">JCVI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">MRI QC Workgroup</td>
<td style="word-wrap: break-word; white-space: normal;">Don Hagler</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Ingestion</td>
<td style="word-wrap: break-word; white-space: normal;">Ingestion and catalogue DICOMs in Lasso</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">QC of ingestion</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#j-craig-venter-institute" target="_blank">JCVI</a></span><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#health-sciences-technology" target="_blank">HST</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">Initial QC raw data (e.g. manual, automated)</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#j-craig-venter-institute" target="_blank">JCVI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">MRI QC Workgroup</td>
<td style="word-wrap: break-word; white-space: normal;">Don Hagler</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">Dashboard Inspection of QC Pipeline Output and site notification</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#j-craig-venter-institute" target="_blank">JCVI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">MRI QC Workgroup</td>
<td style="word-wrap: break-word; white-space: normal;">Don Hagler</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Process</td>
<td style="word-wrap: break-word; white-space: normal;">Run anatomical pipelines (freesurfer, qsiprep, qsirecon, mcribs)</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Erik Lee</td>
<td style="word-wrap: break-word; white-space: normal;">Erik Lee</td>
<td style="word-wrap: break-word; white-space: normal;">[<b>C</b>] Timothy Hendrickson<br>[<b>C</b>] Lucille Moore<br>[<b>C</b>] Eric Feczko</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">Post-processing QC (manual, automated)</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#center-for-developmental-neuroimaging" target="_blank">CDNI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Michael Anderson</td>
<td style="word-wrap: break-word; white-space: normal;">Eric Feczko</td>
<td style="word-wrap: break-word; white-space: normal;">[<b>C</b>] Lucille Moore<br>[<b>I</b>] Damien Fair</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Process</td>
<td style="word-wrap: break-word; white-space: normal;">Index source BIDS to platform</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Erik Lee</td>
<td style="word-wrap: break-word; white-space: normal;">Erik Lee</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Process</td>
<td style="word-wrap: break-word; white-space: normal;">Index raw BIDS to platform</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Erik Lee</td>
<td style="word-wrap: break-word; white-space: normal;">Erik Lee</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data Process</td>
<td style="word-wrap: break-word; white-space: normal;">Index derivatives BIDS to platform</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Erik Lee</td>
<td style="word-wrap: break-word; white-space: normal;">Erik Lee</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
<td style="word-wrap: break-word; white-space: normal;">SMEs review data</td>
<td style="word-wrap: break-word; white-space: normal;">Various</td>
<td style="word-wrap: break-word; white-space: normal;">MRI Workgroup SMEs</td>
<td style="word-wrap: break-word; white-space: normal;">MRI Workgroup Leads</td>
<td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Data QC + Action</td>
    <td style="word-wrap: break-word; white-space: normal;">Data corrections</td>
    <td style="word-wrap: break-word; white-space: normal;">Various</td>
    <td style="word-wrap: break-word; white-space: normal;">MRI Workgroup SMEs, HDCC</td>
    <td style="word-wrap: break-word; white-space: normal;">MRI Workgroup Leads</td>
    <td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Documentation of Processes</td>
    <td style="word-wrap: break-word; white-space: normal;">Documentation of processes, known issues, etc.</td>
    <td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#center-for-developmental-neuroimaging" target="_blank">CDNI</a></span></td>
    <td style="word-wrap: break-word; white-space: normal;">MRI Workgroup SMEs, HDCC</td>
    <td style="word-wrap: break-word; white-space: normal;">Lucille Moore</td>
    <td style="text-align: center; word-wrap: break-word; white-space: normal;">-/-</td>
</tr>
<tr>
    <td style="word-wrap: break-word; white-space: normal;">Sign Off</td>
    <td style="word-wrap: break-word; white-space: normal;">SMEs sign off on data</td>
    <td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#lasso" target="_blank">Lasso</a></span></td>
    <td style="word-wrap: break-word; white-space: normal;">Jen Zink</td>
    <td style="word-wrap: break-word; white-space: normal;">MRI Workgroup Leads</td>
    <td style="word-wrap: break-word; white-space: normal;">[<b>C</b>] Eric Feczko</td>
</tr>
</tbody>
</table>
</div>


<div id="sensors-raci" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-table" style="margin-right: 6px; color: blue;"></i> Wearable Sensors</span>
  <a class="anchor-link" href="#sensors-raci" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table">
<thead>
  <tr>
    <th style="width: 20%; text-align: center">Study Stage</th>
    <th style="text-align: center">Step</th>
    <th style="text-align: center">Location</th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>R</b><span class="tooltiptext">Responsible</span></span></th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>A</b><span class="tooltiptext">Accountable</span></span></th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>C</b><span class="tooltiptext">Consulted</span></span></th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>I</b><span class="tooltiptext">Informed</span></span></th>
  </tr>
<tbody>
</tbody>
</table>
</div>

<div id="biospec-raci" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-table" style="margin-right: 6px; color: blue;"></i> Biospecimens</span>
  <a class="anchor-link" href="#biospec-raci" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table">
<thead>
  <tr>
    <th style="text-align: center">Step</th>
    <th style="text-align: center">Location</th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>R</b><span class="tooltiptext">Responsible</span></span></th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>A</b><span class="tooltiptext">Accountable</span></span></th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>C</b><span class="tooltiptext">Consulted</span></span></th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>I</b><span class="tooltiptext">Informed</span></span></th>
  </tr>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Pre-Release Prep: Determine Release Candidate and Process with Sign Off</td>
<td></td>
<td>&nbsp;</td>
<td></td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Acquisition of sample</td>
<td>Site</td>
<td>&nbsp;</td>
<td>Site Staff</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Population of meta data form</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#loris" target="_blank">LORIS</a></span></td>
<td>&nbsp;</td>
<td>Site Coordinator</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>QC of form population</td>
<td></td>
<td>WG Co-Chairs</td>
<td>Elinor Sullivan (Co-Chair)</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Shipment of sample</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>Site Staff</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>QC: Ensuring sample was received</td>
<td>&nbsp;</td>
<td>Charles Hevi</td>
<td>Charles Hevi</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>QC: deviation code of sample at Sampled</td>
<td>&nbsp;</td>
<td>Charles Hevi</td>
<td>Charles Hevi</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>QC: deviation code of sample at USDTL</td>
<td>&nbsp;</td>
<td>Priti Soni</td>
<td>Priti Soni</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Analysis of sample at Sampled</td>
<td>&nbsp;</td>
<td>Charles Hevi</td>
<td>Charles Hevi</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>Analysis of sample at USDTL</td>
<td>&nbsp;</td>
<td>Priti Soni</td>
<td>Priti Soni</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>QC of analysis of sample</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>Gretchen Bandoli</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>QC of data acquisition</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>Elinor Sullivan (Co-Chair)</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
<tr>
<td>QC of analysis</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
<td>Gretchen Bandoli</td>
<td>&nbsp;</td>
<td>&nbsp;</td>
</tr>
</tbody>
</table>
</div>


<div id="eeg-raci" class="table-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="table-text"><i class="fas fa-table" style="margin-right: 6px; color: blue;"></i> EEG</span>
  <a class="anchor-link" href="#eeg-raci" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="table-collapsible-content">
<table class="compact-table">
<thead>
  <tr>
    <th style="width: 20%; text-align: center">Study Stage</th>
    <th style="text-align: center">Location</th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>R</b><span class="tooltiptext">Responsible</span></span></th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>A</b><span class="tooltiptext">Accountable</span></span></th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>C</b><span class="tooltiptext">Consulted</span></span></th>
    <th style="text-align: center"><span class="tooltip tooltip-left"><b>I</b><span class="tooltiptext">Informed</span></span></th>
  </tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Pre-Release Prep: Determine Release Candidate and Process with Sign Off</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#university-of-maryland" target="_blank">UMD EEG Core</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Nathan Fox</td>
<td style="word-wrap: break-word; white-space: normal;">Nathan Fox</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">Program</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Monthly Net Inventory/Equipment QC</td>
<td style="word-wrap: break-word; white-space: normal;">Site</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site), EEG Core, HDCC, LORIS</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site)</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">EEG Acquisition</td>
<td style="word-wrap: break-word; white-space: normal;">Site</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site), EEG Core, HDCC, LORIS</td>
<td style="word-wrap: break-word; white-space: normal;">Trisha Maheswari, Elise Harris</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Populate EEG Acquisition Form</td>
<td style="word-wrap: break-word; white-space: normal;">Site</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site), EEG Core, HDCC, LORIS</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site)</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">QC Acquisition form population</td>
<td style="word-wrap: break-word; white-space: normal;">Site</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site), EEG Core, HDCC, LORIS</td>
<td style="word-wrap: break-word; white-space: normal;">Trisha Maheswari, Elise Harris</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">De-Identification &amp; Flags (pre-LORIS)</td>
<td style="word-wrap: break-word; white-space: normal;">Site</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site), EEG Core, HDCC, LORIS</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site)</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">BIDs Wizard Population and Execution</td>
<td style="word-wrap: break-word; white-space: normal;"><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#loris" target="_blank">LORIS</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site), EEG Core, HDCC, LORIS</td>
<td style="word-wrap: break-word; white-space: normal;">Site Staff (Varies Per Site)</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">QC pre-processed EEG</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#university-of-maryland" target="_blank">UMD EEG Core</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Santiago Morales, Kira Ashton, Dylan Gilbreath, Trisha Maheswari, Elise Harris</td>
<td style="word-wrap: break-word; white-space: normal;">Nathan Fox</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Run MADE Pipeline</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#midb-informatics-hub-msi" target="_blank">UMN MSI</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Erik Lee</td>
<td style="word-wrap: break-word; white-space: normal;">Erik Lee</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">QC Pre-release data</td>
<td><span style="display: inline-block; background-color: #f0f8ff; color: #333; border-radius: 12px; padding: 1px 5px; font-size: 1em; border: 1px solid #d0e7ff;"><i class="fas fa-users" style="margin-right: 6px; color: blue;"></i><a href="../../orgcharts/#university-of-maryland" target="_blank">UMD EEG Core</a></span></td>
<td style="word-wrap: break-word; white-space: normal;">Santiago Morales</td>
<td style="word-wrap: break-word; white-space: normal;">Nathan Fox</td>
<td style="word-wrap: break-word; white-space: normal;">&nbsp;</td>
<td style="word-wrap: break-word; white-space: normal;">Program</td>
</tr>
</tbody>
</table>
</div>

<br>