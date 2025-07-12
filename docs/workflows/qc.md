# HBCD Quality Control

![](images/qc-wf.png)


## File-Based MRI Data

<div id="source" class="source-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Source QC</span>
  <a class="anchor-link" href="#source" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>ADD CONTENT</p>
</div>

<div id="ingestion" class="ingestion-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Ingestion QC</span>
  <a class="anchor-link" href="#ingestion" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p>ADD CONTENT</p>
</div>

<div id="preproc" class="preproc-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Pre-Processing QC</span>
  <a class="anchor-link" href="#preproc" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
<p><b>Automated QC</b></p>

<p><i><b>Protocol compliance</b></i><br>
Extraction of information from DICOM headers to identify common issues and protocol deviations (e.g.  missing files or incorrect patient orientation). Criteria include whether key imaging parameters, such as voxel size or repetition time, match the expected values for a given scanner. Out-of-compliance series are reviewed and sites are contacted if corrective action is required.</p> 

<p><i><b>Completeness checks</b></i><br>
A complete imaging session consists of the following valid series:
<table style="width: 100%; border-collapse: collapse; table-layout: fixed;">
    <tbody>
    <tr>
        <td>Structural T1 Block:</td>
        <td>T1</td>
    </tr>
    <tr>
        <td>Structural T2 Block:</td>
        <td>T2</td>
    </tr>
    <tr>
        <td>Diffusion (dMRI) Block:</td>
        <td>dMRI AP; dMRI PA</td>
    </tr>
    <tr>
        <td>Resting state (rsfMRI) Block:</td>
        <td>fMRI field map AP; fMRI field map PA; rsfMRI (run 1); rsfMRI (run 2)</td>
    </tr>
    <tr>
        <td>MRS Block</td>
        <td>SVS localizer; MRS</td>
    </tr>
    <tr>
        <td>Quantitative (qMRI) Block</td>
        <td>B1 Map; 3DMagic/QALAS</td>
    </tr>
</tbody>
</table>
</p>

<p>See <a href="https://docs.hbcdstudy.org/latest/instruments/mri/qc/#automated-qc">HBCD Data Release Docs</a> for full details.</p>
</div>

<div id="proc" class="proc-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Processed Data QC</span>
  <a class="anchor-link" href="#proc" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
ADD CONTENT
</div>

<div id="pre-release" class="pre-release-banner" onclick="toggleCollapse(this)">
  <span class="text-with-link">
  <span class="text">Pre-Release/Analysis QC</span>
  <a class="anchor-link" href="#pre-release" title="Copy link">
  <i class="fa-solid fa-link"></i>
  </a>
  </span>
  <span class="arrow">▸</span>
</div>
<div class="collapsible-content">
ADD CONTENT
</div>


