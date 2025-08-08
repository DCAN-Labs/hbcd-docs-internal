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
