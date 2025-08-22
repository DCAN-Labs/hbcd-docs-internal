# Software & Analytic Standards

<div class="pill-center">
  <a href="../../#data-quality-checks" target="_blank" class="pill-link-wrapper">
      <span class="pill-link">
        <span class="tooltip">
          <i class="fa-solid fa-clipboard-check" style="color: #6300d3;"></i>
          <span class="tooltiptext">Data quality checks<br><i>Click to learn more</i></span>
        </span>
      </span>
  </a>
  <a href="../../#reproducibility" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip">
        <i class="fa-solid fa-code-compare" style="color: #6300d3;"></i>
        <span class="tooltiptext">Reproducibility<br><i>Click to learn more</i></span>
      </span>
    </span>
  </a>
  <a href="../../#clear-objectives-and-scope" target="_blank" class="pill-link-wrapper">
    <span class="pill-link">
      <span class="tooltip"><i class="fa-solid fa-bullseye" style="color: #6300d3;"></i><span class="tooltiptext">Clear objectives & scope<br><i>Click to learn more</i></span></span>
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

The following procedures are performed to support transparency, reproducibility, and standard environments for our databases and systems controls:

## Processing & Analytic Standards

See the full details on the HBCD Data Release Docs site [here](https://docs.hbcdstudy.org/latest/instruments/#processing-analytic-standards). This includes the use of standardized processing pipelines for MRI, EEG, and other modalities, as well as the use of standardized analytic approaches across sites. Independent code review is performed for all processing pipelines via the NMIND Coding Standards Checklist, with a focus on ensuring that the code is well-documented, reproducible, and follows best practices in software development. This includes version control of all internal and public-facing code bases, including the documentation websites.

## New Pipeline Integration

<p style="text-align: center; font-size: 1.5em;">🚧 <i>UNDER CONSTRUCTION</i> 🚧 </p>

Integrating new pipelines into HBCD’s file-based data processing workflow involves three main phases:

- **Approval**: Review and sign-off to begin integration testing
- **Integration & Testing**: Implementation and evaluation against [HBCD Pipeline & Analytic Standards](https://docs.hbcdstudy.org/latest/instruments/processing/standards/)
- **Final Review**: Workgroup subject matter experts (SMEs) and leads provide consultation and sign-off

<div class="notification-banner static-banner">
  <span class="emoji"><i class="fa-solid fa-circle-info"></i></span>
  <span class="text">Integration Status Tracker: View the latest pipeline integration steps and status in the <a href="https://docs.google.com/spreadsheets/d/17jad-Majiveg0vngXDQEpkSrQ7TC08Z_yaGnIr5BN_o/edit?usp=sharing">H-PIP Spreadsheet</a></span>
</div>
<br>

#### HBCD Pipeline Integration Proposal (H-PIP) Stages 

<table class="compact-table-no-vertical-lines">
<thead>
  <th>Stage</th>
  <th>Description/Actions</th>
  <th>Responsible Group(s)</th>
  <th>Requirements</th>
</thead>
<tbody>
    <tr>
        <td>1. Approval</td>
        <td style="word-wrap: break-word; white-space: normal;">Senior stakeholder approves H-PIP testing via MRI WG consensus. Define scope and request initial timeline.</td>
        <td>Senior stakeholder &amp; MRI WG</td>
        <td>&mdash;</td>
    </tr>
    <tr>
        <td>2. Scoping</td>
        <td style="word-wrap: break-word; white-space: normal;">Refine proposed timeline and scope for integration.</td>
        <td>Informatics Core &amp; Developers</td>
        <td>&mdash;</td>
    </tr>
    <tr>
        <td>3. Integration</td>
        <td style="word-wrap: break-word; white-space: normal;">Pipeline integrated within Informatics Core.</td>
        <td style="word-wrap: break-word; white-space: normal;">Erik Lee, Tim Hendrickson, Sriharshitha Anuganti, pipeline developers</td>
        <td>• Containerized<br>• BIDSified<br>• Independent per-session processing<br>• NMIND bronze certified</td>
    </tr>
    <tr>
        <td>4. Testing</td>
        <td style="word-wrap: break-word; white-space: normal;">Pipeline tested</td>
        <td style="word-wrap: break-word; white-space: normal;"><span class="tooltip">FAB (Eric Feczko's Lab)</i><span class="tooltiptext">Eric Feczko (PI), Begim Fayzullobekova, rae McCollum, Jacob Lundquist, Michael Anderson</span></span></td>
        <td>• Validity<br>• Reliability<br>• Analytic reproducibility</td>
    </tr>
    <tr>
        <td>5. Review</td>
        <td style="word-wrap: break-word; white-space: normal;">Findings presented to MRI WG for sign-off.</td>
        <td>MRI WG</td>
        <td>&mdash;</td>
    </tr>
    <tr>
    <td>6. SME Consult</td>
    <td style="word-wrap: break-word; white-space: normal;">Findings presented to SME WG for additional consultation and final approval.</td>
    <td>SME WG</td>
    <td>&mdash;</td>
    </tr>
</tbody>
</table>

## Data Storage and Backup

 - Large data files are stored in MSI's Tier 2 Ceph storage system, while the LORIS systems operate off of the storage in MSI's OpenStack cloud environment.
 - Research data is encrypted and backed up to AWS Deep Glacier on a nightly basis.
 - The LORIS systems (prod, sandbox, and staging) have their database backed up on a nightly basis to MSI Tier 2 storage.
 - Currently all data is held, although we are in the final phases of determining a system for retiring some nightly backups after six months, reducing to retaining weekly backups for another three months and then monthly after nine total months.

## Code Versioning
All code, both LORIS customizations and Puppet orchestration code, are maintained in the University of Minnesota's local Enterprise GitHub. These code bases are kept in separate internal GitHub organizations with different memberships and access controls. The orchestration code is also subject to our Internal Change Control process that requires a change to get a separate approval and verification from someone other than the implementer to ensure safety and reliability.

## Access Controls
Data access is modified through the same Internal Change Control process governing orchestration changes. All change requests must be signed off on by a senior staff manner and are vetted by data stewards or managers of the projects.
