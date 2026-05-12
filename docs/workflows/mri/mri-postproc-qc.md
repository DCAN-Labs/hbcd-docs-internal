# MRI Post-Processing QC

## BME-X 

We evaluate image enhancement effects and association between BME-X QI and manual QC ratings. Manual visual QC is performed for all T1/T2 structural data pre- and post-BME-X enhancement to evaluate:

- If the manual QC ratings improve post- BME-X enhancement (**paired one-sided t-test** of manual QC ratings pre- vs post-enhancement)
- Association between BME-X QI scores and manual QC ratings before and after image enhancement, including:
    - **Spearman correlations** between BME-X QI scores and manual QC scores pre- vs post-enhancement
    - **linear regression models** testing whether BME-X QI scores predicts enhanced and/or original manual QC ratings

**Code:** [bmex_qc_analysis.r](https://github.com/DCAN-Labs/NBDC-MRI-Post-Processing-QC/blob/main/scripts/bmex_qc_analysis.r)       
**README:** [BME-X QC Analysis](https://github.com/DCAN-Labs/NBDC-MRI-Post-Processing-QC/blob/main/docs/bmex_qc_analysis.md)

---

## HBCD QC-FC Summary Analysis

We evaluate whether scan quality, as quantified by BrainSwipes QC summary score, meaningfully changes functional connectivity (FC) estimates in HBCD resting-state fMRI data. The script loads BrainSwipes QC scores and Gordon FC matrices (`.pconn.nii`) for a selected session, then evaluates how functional connectivity differs between high- and low-quality runs across multiple QC thresholds (0.9–0.1). Summary measures include within-network FC, between-network FC, and network distinctness (within-network FC - between-network FC). 

Outputs include:

- Run-level QC + FC summary tables
- QC-vs-FC scatter plots
- High-QC vs Low-QC comparison tables
- Cutoff-based summary plots

**Code:** [hbcd_qc_fc_analysis.r](https://github.com/DCAN-Labs/NBDC-MRI-Post-Processing-QC/blob/main/scripts/hbcd_qc_fc_analysis.r)       
**README:** [HBCD QC-FC Analysis](https://github.com/DCAN-Labs/NBDC-MRI-Post-Processing-QC/blob/main/docs/hbcd_qc_fc_analysis.md)

---

## Per-Network QC Impact Analysis

We also evaluate the association between scan quality (BrainSwipes QC scores) and *network-level* FC metrics (including network distinctness and within-network mean FC) to identify networks most affected by scan quality. The script evaluates the relationship between QC and FC metrics per-network, ranks the networks by effect size, and flags those that display FDR-significant QC effects. The scriopt computes and plots the following for each metric:

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
