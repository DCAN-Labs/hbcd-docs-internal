# Known Issues

## Lasso Interface
### ⚠️ Help Center Down for Maintenance
The Help Center is down for maintenance until next week - please email Aarushi Chaudhry (achaudhry@lassoinformatics.com) if you run into issues.

### ⚠️ Query Tool: No Rows Displayed on Toggling Between File-Based and Tabular Data Tabs
On toggling between file-based and tabular data tabs in the Dictionary Query Tool, users can expect to see an error where no rows are displayed. Please reload the page to populate the tabular data. We will fix this very soon.

---------------

## BR15 Target Release for Fix
### ⚠️ BioSpecimens: Transform '-999' 
The -999 code needs to be transformed to a note in shadow matrices. Relevant shadow matrices include: `bio_biosample_nails_results`, `bio_biosample_nails_type`, and `bio_biosample_urine`.

### ⚠️ Duplicate Rows for BioSpecimens
Flagged cases have two visits (V01 & V02). Flagged duplicates are labeled as 'ses-V02'. Team will need to verify with MSI on de-identified files to confirm if both visits are incorrectly labeled as 'ses-V02' during de-identification.

### ⚠️ Height/Weight/Head Circumference missing 'Date of Administration' (~6 cases)













