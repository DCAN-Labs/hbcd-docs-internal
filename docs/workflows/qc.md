# HBCD Quality Control

![](images/qc-wf.png)


## MRI & MRS Data

These data include both file-based and tabulated data for the instruments listed on the HBCD Data Release Docs site [here](https://docs.hbcdstudy.org/latest/instruments/#mri).

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
<p>Validations performed during MRI & MRS data acquisition include:<br>
 • XXXX<br>
 • XXXX<br></p>
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
<p>As outlined in the <a href="../data-proc-wf">data processing workflow diagram</a>, raw data are sent via FIONA to UMN SCE/HST and HBCD Central/JCVI. Data are checked for protocal compliance and completion - see <a href="https://docs.hbcdstudy.org/latest/instruments/mri/qc/#automated-qc">HBCD Data Release Docs</a> for full details. In summary:</p> 
<p><b>Protocol compliance</b><br>
This is based on extraction of information from DICOM headers to identify common issues and protocol deviations (e.g.  missing files or incorrect patient orientation). Criteria include whether key imaging parameters, such as voxel size or repetition time, match the expected values for a given scanner.</p> 
<p><b>Completeness checks</b><br>
A complete imaging session consists of the following valid series:
<table class="table-no-vertical-lines" style="width: 100%; border-collapse: collapse; table-layout: fixed;">
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
<p><b>AUTOMATED QC</b> (see <a href="https://docs.hbcdstudy.org/latest/instruments/mri/qc/#automated-qc">HBCD Data Release Docs</a> for full details)</p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px">
<thead>
<tr>
    <th style="width: 20%; text-align: center;">Modality</th>
    <th style="width: 80%; text-align: center;">QC Procedures</th>
</tr>
</thead>
<tbody>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Structural (T1w, T2w, qMRI)</td>
<td style="word-wrap: break-word; white-space: normal;">• Deep learning model estimates motion artifacts<br />• Signal-to-noise ratio (SNR) computed</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">dMRI</td>
<td style="word-wrap: break-word; white-space: normal;">• Framewise displacement (FD) for head motion<br />• Head motion estimated via <span class="tooltip">registration to tensor-synthesized images<span class="tooltiptext">accounts for contrast differences across orientations</span></span> (<a href="https://doi.org/10.1002/hbm.20619">Hagler et al. 2009</a>)<br />• Identification of <span class="tooltip">dark slices<span class="tooltiptext">artifacts caused by abrupt head movements</span></span> via RMS difference between raw and tensor-fitted data<br />• Total slices and frames with motion artifacts calculated<br />• Metrics for line artifacts and field-of-view (FOV) cutoff</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">fMRI</td>
<td style="word-wrap: break-word; white-space: normal;">• FD for head motion (average FD and seconds with FD &lt; 0.2 mm, 0.3 mm, 0.4 mm) (<a href="https://doi.org/10.1016/j.neuroimage.2011.10.018">Power et al., 2012</a>)<br />• Metrics for line artifacts and FOV cutoff<br />• <span class="tooltip">FWHM<span class="tooltiptext">Full width half max () spatial smoothness</span></span> and <span class="tooltip">tSNR<span class="tooltiptext">temporal SNR</span></span> computed after motion correction (<a href="https://doi.org/10.1016/j.neuroimage.2005.01.007">Triantafyllou et al. 2005</a>)</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">Field Maps</td>
<td style="word-wrap: break-word; white-space: normal;">• Metrics for line artifacts and FOV cutoff</td>
</tr>
<tr>
<td style="word-wrap: break-word; white-space: normal;">All Modalities</td>
<td style="word-wrap: break-word; white-space: normal;">• SNR computed where applicable</td>
</tr>
</tbody>
</table>

<p><b>MANUAL QC</b> (see <a href="https://docs.hbcdstudy.org/latest/instruments/mri/qc/#manual-review">HBCD Data Release Docs</a> for full details)</p>
<table style="width: 100%; border-collapse: collapse; table-layout: fixed; font-size: 14px">
<thead>
<tr>
    <th style="width: 20%; text-align: center;">Modality</th>
    <th style="width: 80%; text-align: center;">QC Procedures</th>
</tr>
</thead>
<tbody>
<tr>
<td>T1w, T2w</td>
<td style="word-wrap: break-word; white-space: normal;"> • Scored for <strong>motion artifacts</strong> (e.g., ripples, blurring) on a 0-3 scale (0 = none, 3 = severe)<br> • Other documented issues include intensity inhomogeneity and <span class="tooltip">ghosting<span class="tooltiptext">faint displaced copy of anatomy due to slices outside FOV</span></span></td>
</tr>
<tr>
<td>qMRI</td>
<td style="word-wrap: break-word; white-space: normal;"> • Same artifact scoring as above (0 - 3)<br> • Inspection of derived data (parametric maps, ROI analysis, and quantitative comparisons for 3D-QALAS)</td>
</tr>
<tr>
<td>B1 field maps</td>
<td style="word-wrap: break-word; white-space: normal;"> • Visual inspection and overall QC only; used for bias field correction of qMRI scans.</td>
</tr>
<tr>
<td>SVS localizer scans (MRS)</td>
<td style="word-wrap: break-word; white-space: normal;"> • Visual inspection and overall QC only; used to define ROI for spectroscopy.</td>
</tr>
<tr>
<td>dMRI, fMRI, field maps</td>
<td style="word-wrap: break-word; white-space: normal;"> • Scored for susceptibility artifacts, FOV cutoff, and <span class="tooltip">line artifacts<span class="tooltiptext">horizontal lines present in the sagittal view, including dark slice-frame and interleaved sliced offset</span></span>.<br> • Susceptibility issues include <span class="tooltip">signal dropout<span class="tooltiptext">Consistent with prior infant fMRI using posterior-anterior (PA) acquisitions, signal dropout is commonly noted in the posterior occipital cortex</span></span>, signal bunching, and warping.</td>
</tr>
</tbody>
</table>
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
<p>QC is performed on processed MR data using BrainSwipes - please see full details <a href="https://docs.hbcdstudy.org/latest/instruments/mri/qc/#brainswipes">here</a>.</p>
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
<p>Prior to inclusion in the release data, the following checks are performed:</p>
<p> • Analysis of processed structural data based on tabulated data (<a href="https://docs.hbcdstudy.org/latest/datacuration/phenotypes/">see details</a>) derived from XCP-D file-based outputs: blah blah</p>
<p> • Analysis of processed functional data based on tabulated data (<a href="https://docs.hbcdstudy.org/latest/datacuration/phenotypes/">see details</a>) derived from XCP-D file-based outputs: blah blah</p>
<p> • Diffusion derivatives from QSIPrep: analysis of automated QC metric distributions</p>

<p>See <a href="https://docs.hbcdstudy.org/latest/instruments/mri/qc/#qc-summary-statistics">QC Summary Statistics</a> on the HBCD Data Release Docs for some findings from these analysis shared with users.</p>
</div>

## EEG Data




