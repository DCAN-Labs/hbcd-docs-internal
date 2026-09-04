# MRI Pre-Release QC Details

The following [Pre-release QC](../qc.md#pre-release-mri) procedures are performed by the **MRI Post-Processing QC team** (at [CDNI](../../orgcharts.md#center-for-developmental-neuroimaging)) for processed MRI data included in the release pool. Any major results of interest are summarized in the data release notes - see the [fMRI QC Summary Statistics on HBCD Docs](https://docs.hbcdstudy.org/latest/instruments/mri/fmri/#quality-control-summary-statistics) for details. Scripts used to perform post-processing QC are all housed within the [NBDC-MRI-Post-Processing-QC](https://github.com/DCAN-Labs/NBDC-MRI-Post-Processing-QC/) GitHub repository.

## Quick Reference - S3 Buckets & Data Sources for QC

!!! warning "Confirm that data required is available before download"
    Please slack Tanya P. in the `#hbcd` CDNI slack channel prior to downloading data to confirm that the data that you need is available. Remember to specify exactly what data you are looking for, e.g. "deidentified BR 30.0 raw BIDS/derivatives/tabulated data."

Currently, the post-processing MRI QC group sources de-identified data directly from the Lasso PR bucket containing deidentified data that are directly sourced to include in the public release: `s3://midb-hbcd-lasso-hdcc-qc-br/`.       
*In the future, workflows will be developed to instead work on reidentified data maintained by LORIS for data QC.*

**Raw BIDS Data**       
*Includes: fieldmaps, scans TSV files with raw MR QC metrics provided by JCVI (located within [session folders](https://docs.hbcdstudy.org/latest/datacuration/file-based-data/#raw-bids)), etc.*       
Bucket path: `s3://midb-hbcd-lasso-hdcc-qc-br/frozen_files/rawdata/`

**Derivatives**     
*Includes: processed pipelines outputs, e.g. XCP-D derivatives*             
Bucket path: `s3://midb-hbcd-lasso-hdcc-qc-br/br{BETA RELEASE#}/hbcd/derivatives/`

**Phenotypic/tabulated data**      
*Includes: tabulated MRI pipeline derivatives, demographics, behavioral data, etc.*           
Bucket path: `s3://midb-hbcd-lasso-hdcc-qc-br/br{BETA RELEASE#}/hbcd/rawdata/phenotype/` *(download entire folder)* 

---

## Internal Protocol for Release Sign-Off 

1. The post-proc QC team runs automated analyses (described below) and review the results 
1. Results (figures and statistics) are emailed to the MRI Workgroup for review and discussed/reviewed at a subsequent MRI Workgroup meeting as needed to obtain SME signoff 
1. The team meets with relevant SMEs as needed if there are concerns/issues with the data that need to be addressed prior to sign off (note that our team is not as well-equipped to review modalities such as MRS, so feedback from certain subgroups is particularly important)
1. Documentation is revised as needed
1. Post-proc QC team provides official sign-off on QC to Lasso

---

## Analyses Performed 

### Outlier Detection

A QMD file is used to read in tabulated data:

- QSIRecon (Diffusion)
- OSPREY (MRS)
- XCP-D (Structural/Functional)
- BIBSNet (Structural)

The QMD file identifies outliers, or null values, flags subject IDs/sessions, and writes them to an output file.

### XCP-D
#### Structural Checks
Tabulated XCP-D pipeline derivatives are analyzed using R-based scripts. ROI-level measures include:

- Cortical metrics (Gordon parcellation, 333 ROIs): cortical thickness, surface area, and curvature
- Subcortical metrics (Freesurfer segmentation, 19 ROIs): volume

BrainSwipes visual QC outputs are used to assess data quality and its impact on the underlying distributions. We also evaluate associations with demographic variables. Over 90% of data passed BrainSwipes QC, indicating high overall quality. No significant effects of data quality or associations with demographic factors have been detected, suggesting either minimal confounding or limited statistical power to detect such effects in the current sample.

#### Functional Checks
From the **tabulated XCP-D derivatives**, we analyze ALFF and ReHo measures from the Gordon cortical parcellation and Freesurfer subcortical segmentation, covering a total of 352 ROIs. BrainSwipes visual QC is used to assess the proportion of rs-fMRI data meeting quality thresholds and evaluate its impact on distributional characteristics. The QC metric exhibited a linear trend, supporting its interpretation as a continuous measure. Examining effects of data quality, we find that data quality effects are most minimized when the pass rate for BrainSwipes QC exceeds 70%.

We also analyze mean ROI-to-ROI functional connectivity maps from the same parcellations (Gordon cortical and Freesurfer subcortical, 352 ROIs) in the **file-based data**. As with tabulated data, BrainSwipes QC outputs were used to assess data quality and its influence on connectivity estimates. A similar linear relationship was observed, and QC effects were minimized when only data with at least a 70% pass rate were included.

### BME-X 

We evaluate image enhancement effects and association between BME-X QI and manual QC ratings. Manual visual QC is performed for all T1/T2 structural data pre- and post-BME-X enhancement to evaluate:

- If the manual QC ratings improve post- BME-X enhancement (**paired one-sided t-test** of manual QC ratings pre- vs post-enhancement)
- Association between BME-X QI scores and manual QC ratings before and after image enhancement, including:
    - **Spearman correlations** between BME-X QI scores and manual QC scores pre- vs post-enhancement
    - **linear regression models** testing whether BME-X QI scores predicts enhanced and/or original manual QC ratings

**Code:** [bmex_qc_analysis.r](https://github.com/DCAN-Labs/NBDC-MRI-Post-Processing-QC/blob/main/scripts/bmex_qc_analysis.r)       
**README:** [BME-X QC Analysis](https://github.com/DCAN-Labs/NBDC-MRI-Post-Processing-QC/blob/main/docs/bmex_qc_analysis.md)

---

### HBCD QC-FC Summary Analysis

We evaluate whether scan quality, as quantified by BrainSwipes QC summary score, meaningfully changes functional connectivity (FC) estimates in HBCD resting-state fMRI data. The script loads BrainSwipes QC scores and Gordon FC matrices (`.pconn.nii`) for a selected session, then evaluates how functional connectivity differs between high- and low-quality runs across multiple QC thresholds (0.9–0.1). Summary measures include within-network FC, between-network FC, and network distinctness (within-network FC - between-network FC). 

Outputs include:

- Run-level QC + FC summary tables
- QC-vs-FC scatter plots
- High-QC vs Low-QC comparison tables
- Cutoff-based summary plots

**Code:** [hbcd_qc_fc_analysis.r](https://github.com/DCAN-Labs/NBDC-MRI-Post-Processing-QC/blob/main/scripts/hbcd_qc_fc_analysis.r)       
**README:** [HBCD QC-FC Analysis](https://github.com/DCAN-Labs/NBDC-MRI-Post-Processing-QC/blob/main/docs/hbcd_qc_fc_analysis.md)

**Results from Release 1.0 data are currently provided in the HBCD Data Release Docs site [here](https://docs.hbcdstudy.org/latest/instruments/mri/fmri/#quality-control-summary-statistics).**

---

### Per-Network QC Impact Analysis

We also evaluate the association between scan quality (BrainSwipes QC scores) and *network-level* FC metrics (including network distinctness and within-network mean FC) to identify networks most affected by scan quality. The script evaluates the relationship between QC and FC metrics per-network, ranks the networks by effect size, and flags those that display FDR-significant QC effects. The script computes and plots the following for each metric:

- **LM slope**: estimated association between QC and the FC metric
- **Pearson correlation (r)** between QC and the FC metric across runs
- Also outputs both raw and FDR-corrected p-values (correction applied separately within each metric)

**Code:** [per_network_qc_impact_analysis.r](https://github.com/DCAN-Labs/NBDC-MRI-Post-Processing-QC/blob/main/scripts/per_network_qc_impact_analysis.r)      
**README:** [Per-Network QC Impact Analysis](https://github.com/DCAN-Labs/NBDC-MRI-Post-Processing-QC/blob/main/docs/per_network_qc_impact_analysis.md)




<!-- ### Input data

The script reads a BMEX QC Excel file and uses the following key variables:

- `Enhanced_Image_Score_v2` (or matching equivalent) = manual QC rating after enhancement
- `QU_motion` = manual QC rating for the original image
- `QI_from_BMEX` = automatic continuous quality metric
-  Optional columns, if present, may also be used:
    - `Visit` or similar visit/session variable
    - `Vendor` or similar scanner/vendor variable

## QC scoring

Manual QC ratings are coded as follows, where lower values indicate better image quality:

- `Excellent = 0`
- `Good = 1`
- `Questionable = 2`
- `Unusable = 3`

`QI_from_BMEX` is treated as a continuous variable. Invalid or missing QI values (`-1` or `NA`) are excluded. Rows with missing original QC, enhanced QC, or QI values are removed before analysis.

### Statistical analyses

- **Paired one-sided t-test** to test whether enhanced QC scores are lower than original QC scores
- **Spearman correlations** between `QI_from_BMEX` and (1) enhanced manual QC and (2) original manual QC
- **linear regression models** testing whether `QI_from_BMEX` predicts enhanced and/or original manual QC

### Output files

The script writes outputs including:

- Short text report summarizing the analysis
- Cleaned data, summary results, and regression output tables
- QC category percentage table
- Visualizations:
    - QC category percentage proportion plot: grouped bar plot showing QC category percentages for original and enhanced images
    - QC distribution violin plot: violin/boxplot showing the distribution of manual QC ratings before and after enhancement
    - `QI_from_BMEX` versus manual QC comparison plot: side-by-side scatter plots of `QI_from_BMEX` versus manual QC, with fitted linear trend lines
    - Optional visit- and/or vendor-based QC distribution plots: violin plot by Visit or Vendor, if a visit/session or vendor/scanner column is detected, respectively -->
